#CURRENCY EXCHANGE CONVERTER APP

#Aishlin Brown 23203276
#Lim Adilah Binte Adam 23201565
#Sara Cantero Izquierdo 23201887

#import necessary libraries
import streamlit as st
import csv
import pandas as pd

# Streamlit app title
st.title("Currency Converter App")

# Animation
st.markdown('<iframe src="https://lottie.host/?file=3f435f79-27c3-40f4-b215-798f9b441c8d/pIGRVJZTtt.json"></iframe>', unsafe_allow_html=True)
st.markdown('<style> body{text-align:center;} <style>', unsafe_allow_html=True)

st.subheader("Welcome to our real-time currency exchange converter!")
st.write('\n\n')

#create lists
currency = []
rates =[]

#open csv file ("eurofxref-2.csv") to read the data
with open("eurofxref-2.csv") as file:
    reader = csv.reader(file)
    rows = list(reader)

    # To know the structure of the data
    print("-----------This is the structure of the data---------- \n",rows)
    currency = rows[0]
    rates =rows[1]

    #to print the lists created
    print("\n-----------These are the lists created-----------")
    print("Currencies: ",currency,"\n")
    print("Rates: ", rates)

#create dictionary to assign the flags to each currency
flag = {
    'USD': '🇺🇸',
    'JPY': '🇯🇵',
    'BGN': '🇧🇬',
    'CZK': '🇨🇿',
    'DKK': '🇩🇰',
    'GBP': '🇬🇧',
    'HUF': '🇭🇺',
    'PLN': '🇵🇱',
    'RON': '🇷🇴',
    'SEK': '🇸🇪',
    'CHF': '🇨🇭',
    'ISK': '🇮🇸',
    'NOK': '🇳🇴',
    'TRY': '🇹🇷',
    'AUD': '🇦🇺',
    'BRL': '🇧🇷',
    'CAD': '🇨🇦',
    'CNY': '🇨🇳',
    'HKD': '🇭🇰',
    'IDR': '🇮🇩',
    'ILS': '🇮🇱',
    'INR': '🇮🇳',
    'KRW': '🇰🇷',
    'MXN': '🇲🇽',
    'MYR': '🇲🇾',
    'NZD': '🇳🇿',
    'PHP': '🇵🇭',
    'SGD': '🇸🇬',
    'THB': '🇹🇭',
    'ZAR': '🇿🇦',
    'EUR': '🇪🇺'
}


# To convert string items into float numbers and add EUR rate and currency
for i in range(len(rates)):
    currency[i]=currency[i].strip()
    rates[i]= rates[i].strip()
    rates[i]=float(rates[i])
rates.append(1.0)
currency.append('EUR')

#create list with currency symbols
currency_symbols = ['$', '¥', 'лв', 'Kč', 'kr', '£', 'Ft', 'zł', 'lei', 'kr', 'Fr.', 'kr', 'kr', '₺', '$', 'R$', '$', '¥', 'HK$', 'Rp', '₪', '₹', '₩', '$', 'RM', '$', '₱', '$', '฿', 'R', '€']


# create the first 3 columns
col1, col2, col3 = st.columns(3)

# Dropdown selection widget
# from_currency is the currency users want to convert from 
with col1:
    from_currency = st.selectbox('From Currency:', currency)
# to_currency is the currency users want to convert to
with col2:
    to_currency = st.selectbox('To Currency:', currency)
with col3:
    amount = st.number_input('Amount: ', min_value = 0.01)  
st.write('\n\n')

#fuction that converts the from_currency to to_currency
def converter(from_currency, to_currency, amount):
    
    """This function converts one currency that the user selects to another currency and returns the result.
    Arguments:
    from_currency -- the first currency they select
    to_currency -- the second currency they select and the one they wish to convert to
    amount -- the amount they want to convert

    Returns:
    The converted amount from from_currency to to_currency
    """
    #define variables needed for the conversion
    conversion1 = 0
    conversion2 = 0
    symbols = ''
    i = 0
    j = len(currency) - 1

    #enter the loop if the index is lower than the length of the currency list. i moves up the list
    while i < len(currency):
        #if the from_currency is on the list, then perform conversion 1: from currency selected to EUR
        if currency[i] == from_currency:
            conversion1 = amount / rates[i]
            #enter the loop until it reaches the first index of the list. j moves down the list 
            while j >= 0:
                #if j is lower or greater than i and to_currency is on the list, then convert from EUR to the selected currency and stop the loop
                if (j > i or j <= i) and currency[j] == to_currency:
                    conversion2 = conversion1 * rates[j]
                    symbols = currency_symbols[j]
                    break 
                else:
                    j = j - 1 #if to_currency has not been found in the list then subtract 1 from j
            break
        else:
            i = i + 1 #if from_currency has not been found in the list then add 1 to i
    
    #if-statement that returns the converted amount rounded to 2 or 5 decimal places
    if conversion2 > 0.01:
        return(symbols + ' '+ str(round(conversion2, 2)))
    else:
        return(symbols + ' '+ str(round(conversion2, 5)))


#create an empty container that updates the converted amount each time the user presses the button
with st.empty():
    if st.button("Convert"):
        converted_amount = converter(from_currency, to_currency, amount) #calling the function to get the converted amount
        flag_country = flag.get(to_currency) #retrieve the flag that is associated to to_currency in the dictionary flag
        st.write(
            f"<span style='font-size: 20px;'>Your converted amount is:</span> "
            f"<span style='font-size: 20px;'>{converted_amount} {flag_country}</span>",
            unsafe_allow_html=True
        ) #to modify the font size and print the result on the screen


st.write('\n\n\n\n\n\n\n\n')

#creating tabs to display information and visuals related to the selected to_currency
tabs = st.tabs(['Trends','Info', 'Map'])

#add content to Trends tab
with tabs[0]:
    #import the necessary library
    import plotly.express as px
    st.subheader("Trends over the past months")
    st.write('The data is based on EUR.')
    #print the message in the screen if the EUR currency is selected. Filter DataFrame based on selected currency
    if to_currency == 'EUR':
        st.write(' Please select a different currency besides EUR to view trends. ')
    # Add content for the first tab as needed
    else:
        # Read the data from the CSV file: 'Coding_Graph_Data - Sheet1.csv'
        df = pd.read_csv('Coding_Graph_Data - Sheet1.csv')
        # Create a line chart using Plotly Express
        fig = px.line(df, x='Dates', y=to_currency, title='Currency Line Chart')
        # Display the chart using Streamlit
        st.plotly_chart(fig)


#add content to Info tab
with tabs[1]:
    st.subheader(to_currency, "Relevant Information")
    # Load data from the CSV file: 'Coding_Graph_Data - Sheet1.csv'
    df1 = pd.read_csv('Coding_Graph_Data - Sheet1.csv')
    # Filter DataFrame based on selected currency
    if to_currency == 'EUR':
        st.write('Please select another currency that is not EUR')
    else:
        #filtering the dataframe based on the selected columns
        df_filter1 = df1[['Dates',to_currency]]
        #assigning the first and last elements of date and currency column to variables
        last_item = float(df_filter1.iloc[-1][to_currency])
        first_item = float(df_filter1.iloc[0][to_currency])
        first_date = df_filter1.iloc[0]['Dates']
        last_date = df_filter1.iloc[-1]['Dates']
        
        #assign a variable to to_currency
        col = [to_currency]

        #create first row of columns in the tab
        col1, col2 =st.columns(2)
        #add content to col1
        with col1:
            if first_item < last_item: #show the % if the currency has increased
                st.subheader('Increased by:')
                increase = (first_item - last_item) / last_item *100
                st.write(str(round(abs(increase), 2)),'% ','from ', first_date, 'to',last_date)
            elif first_item > last_item: #show the % if the currency has decreased
                st.subheader('Decreased by:')
                decrease = (first_item - last_item) / last_item *100
                st.write(to_currency, 'has decreased by',str(round(abs(decrease), 2)),'% ','from ', first_date, 'to',last_date)
            elif first_item == last_item: #if it is the same, then it has not increased/decreased
                st.subheader('Not changed')
                st.write('It has not increased/decreased from', first_date, 'to',last_date)
        #add content to col2
        with col2:
            st.subheader('Average rate')
            average = float(df_filter1[col].mean())
            st.write(to_currency, 'has an average rate of', str(round(average,2)))
        
        #create second row of columns in the tab
        col1, col2 =st.columns(2)
        with col1:
            st.subheader('Maximum')
            maximum = float(df_filter1[col].max()) #show the maximum rate attained of to_currency
            st.write(str(maximum),'is the maximum rate reached')
        with col2:
            st.subheader('Minimum')
            minimum = float(df_filter1[col].min())
            st.write(str(minimum),'is the minimum rate reached') #show the minimum rate attained of to_currency

#add content to Map tab
with tabs[2]:
    #import necessary library
    import folium
    from streamlit_folium import st_folium
    st.subheader('Countries with the selected currency \n')
    st.write('Zoom in/out when necessary \n')

    # Load  data from the CSV file: 'Currency_locations - Sheet1.csv'
    df = pd.read_csv('Currency_locations - Sheet1.csv')
    # Filter DataFrame based on selected currency
    df_filter = df[df['Currency'] == to_currency]
    # Create the folium map
    map = folium.Map(zoom_start=100, scrollWheelZoom=False)
    
    # Add Markers to highlight the countries that use the to_currency
    for i, row in df_filter.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Country'], 
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(map)

    # Adjust the map bounds to fit all markers
    map.fit_bounds(map.get_bounds())
    
    # Display the map
    st_folium(map, width=700, height=450)