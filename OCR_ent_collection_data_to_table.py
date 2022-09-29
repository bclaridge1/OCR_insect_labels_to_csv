#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 06:03:36 2022

@author: bclaridge
"""


##____________________________ PREP STEPS____________________________________
import re
import pandas as pd


 ## SET UP FUNCTION THAT TRANSFORMS COMMON COLLECTION DATE FORMATS
 ## TO MACHINE READABLE
def convert_dates(dataframe_col): 
    
    ## CONVERT INPUT COLUMN WHICH IS A SERIES TO A PD DATAFRAME
    dataframe_col = pd.DataFrame(dataframe_col)
    
    ## CONVERT COLUMN ['columnname'] into a list which is easier to deal with
    column_name = dataframe_col.columns.values.tolist()
    empty = ""
    column_name = empty.join(column_name)
    
    ## SET UP NEEDED VARIABLES
    month_RR = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii',
            'ix', 'x', 'xi', 'xii']
    month_CAPS= ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 
              'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    month_lower = [x.lower() for x in month_CAPS]
    month_Cap = [x.capitalize() for x in month_lower]

    ##CONVERT ODD MONTHS IN RR
    dataframe_col[column_name].replace(regex=month_CAPS, value=month_RR, inplace=True)
    dataframe_col[column_name].replace(regex=month_lower, value=month_RR, inplace=True)
    dataframe_col[column_name].replace(regex=month_Cap, value=month_RR, inplace=True)
    
    ## TURN - into | before other dashes are added
    dataframe_col[column_name].replace(regex="-", value="/", inplace=True)
    ## REPLACE WHITESPACE WITH DOTS
    dataframe_col[column_name].replace(regex=" ", value=".", inplace=True)
 
   
    ## Split DATE into day, month, year
    day = []
    month = []
    year = []
    for index, row in dataframe_col.iterrows():
    ### NEED TO ADD MORE TO REGEX
        match = re.search("[0-9][0-9]\.|[0-9]\.|[0-9]*/[0-9][0-9]", row[column_name])
        if match != None:
            day.append(match.group())
        else:
            day.append(None)
    
    for index, row in dataframe_col.iterrows():
        ## NEED TO ADD MORE REGEX
        match = re.search("[a-zA-Z][a-zA-Z]*", row[column_name])
        if match != None:
            month.append(match.group())
        else:
            month.append(None)

        
    for index, row in dataframe_col.iterrows():
            
        match = re.search("[0-9][0-9][0-9][0-9]*", row[column_name])
        if match != None:
            year.append(match.group())
        else:
            year.append(None)
    
    dataframe_col['Day'] = day
    dataframe_col['Month'] = month
    dataframe_col['Year'] = year
    
    
    dataframe_col['Day'].replace(regex="\.", value="", inplace=True)
    dataframe_col['Month'].replace(regex="\.", value="", inplace=True)
    dataframe_col['Year'].replace(regex="\.", value="", inplace=True)
    
    dataframe_col['eventDate'] = dataframe_col['Year'] + "-" + dataframe_col['Month'] + "-" + dataframe_col['Day']

    dataframe_col['eventDate'].replace(regex="xii", value="12", inplace=True)
    dataframe_col['eventDate'].replace(regex="xi", value="11", inplace=True)
    dataframe_col['eventDate'].replace(regex="ix", value="09", inplace=True)
    dataframe_col['eventDate'].replace(regex="x", value="10", inplace=True)
    dataframe_col['eventDate'].replace(regex="ix", value="09", inplace=True)
    dataframe_col['eventDate'].replace(regex="vii", value="07", inplace=True)
    dataframe_col['eventDate'].replace(regex="vi", value="06", inplace=True)
    dataframe_col['eventDate'].replace(regex="iv", value="04", inplace=True)
    dataframe_col['eventDate'].replace(regex="v", value="05", inplace=True)
    dataframe_col['eventDate'].replace(regex="iii", value="03", inplace=True)
    dataframe_col['eventDate'].replace(regex="ii", value="02", inplace=True)
    dataframe_col['eventDate'].replace(regex="i", value="01", inplace=True)
    
    return dataframe_col['eventDate']



## SHOW ALL THE COLUMNS INSTEAD OF THE FEW BY DEFAULT
pd.set_option('display.max_columns', 30)

## READ THE TEXT FILE
f = open('OCR_example.txt', 'r+')
OCR1 = f.read()
OCR1
## SPLIT THE TEXT FILE INTO SEPARATE LIST ELEMENTS BASED ON A COMPLETE NEW LINE
OCR_2 = OCR1.split("\n\n")
OCR_2

## GET RID OF ANY EMPTY LIST ELEMENTS
OCR_2 = [i for i in OCR_2 if i != []]
OCR_2 = [i for i in OCR_2 if i !="\n"]
OCR_2

## SET UP LISTS WITH THINGS TO SEARCH FOR
## WORKS FOR US, CANADA AND MEXICO
STATES = ["AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY",
          "Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California",  
          "Connecticut",
          "Delaware",          
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New Hampshire",
          "New Jersey",
          "New Mexico",
          "New York",
          "North Carolina",
          "North Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West Virginia",
          "Wisconsin",
          "Wyoming",
          "Alberta",
          "British Columbia",
          "Ontario",
          "Quebec",
          "Nova Scotia",
          "New Brunswick",
          "Manitoba",
          "Prince Edward Island",
          "Saskatchewan",
          "Newfoundland and Labrador",
          "Northwest Territories",
          "Yukon",
          "Nunavut",
          "Aguascalientes",
          "Baja California",
          "Baja California Sur",
          "Campeche",
          "Chiapas",
          "Chihuahua",
          "Coahuila",
          "Colima",
          "Durango",
          "Guanajuato",
          "Guerrero",
          "Hidalgo",
          "Jalisco",
          "México",
          "Michoacán",
          "Morelos",
          "Nayarit",
          "Nuevo León",
          "Oaxaca",
          "Puebla",
          "Querétaro",
          "Quintana Roo",
          "San Luis Potosí",
          "Sinaloa",
          "Sonora",
          "Tabasco",
          "Tamaulipas",
          "Tlaxcala",
          "Veracruz",
          "Yucatán",
          "Zacatecas"]

## SET UP COUNTRY LISTS AS A REGEX SEARCH
COUNTRIES = ["Canada", 
             "CANADA",
             "U.S.A",
             "USA",
             "Colombia",
             "Costa Rica",
             "Cuba",
             "Ecuador",             
             "Italy",
             "Nicaragua",
             "MEXICO",
             "Mexico",
             "Panama",
             "Peru",             
             "Spain",
             ]

# NEEDED TO CONVERT BETWEEN ACRONYM AND FULL NAME
state_Acronymes = [
          "AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY"]

state_Full = [
          "Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California", 
          "Colorado",
          "Connecticut",
          "Delaware",          
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New Hampshire",
          "New Jersey",
          "New Mexico",
          "New York",
          "North Carolina",
          "North Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West Virginia",
          "Wisconsin",
          "Wyoming"]

## MAKE THE COUNTRIES HAVE THE OR _SEPARATOR AT END
COUNTRIES_string1 = []
for i in COUNTRIES:
    i = i+"|"
    print(i)
    COUNTRIES_string1.append(i)

## SET UP PATTERN TO USE IN re.search()
COUNTRIES_pattern = ""
for i in COUNTRIES_string1:
    COUNTRIES_pattern += i


## SAME THING AS IMMEDIATELY ABOVE EXCEPT WITH STATES
STATES_list_modified = []
for i in STATES: 
    i = i+"|"
    STATES_list_modified.append(i)
STATES_list_modified
STATES_pattern = ""
for i in STATES_list_modified:
    STATES_pattern += i
# REMOVE TRAILING \ it messes up the pattern recognition
STATES_pattern = re.sub("\|$", "", STATES_pattern)


    
##_________________________GET DATES______________________________

## USE REGEX TO EXTRACT DATES and also delete dates if found
## SET UP AN EMPTY COLUMN 
DATE_column = []
# FOR LOOP THROUGH MAIN OCR TEXT BLOCK
OCR_3 = []
for i in OCR_2:
    # REMOVED ANY LINE BREAKS
    i = i.strip("\n")
    """
    ASSIGN ANY MATCHES TO REGEX FIND FROM I TO "MATCH"
    REGEX PATTERN WORKS FOR FORMATS: ROMAN NUMERAL, 
    12 SEP 1999, 12SEP1999, 10-15.vi.1990, 10-15.vii.99
    #!!!!!!!!!!!!!!!!!!!!!!!!!!DOES NOT WORK FOR
    10-15.vi.1990
    14OCT1992    
    """
    match = re.search("[0-9][0-9][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9]|[0-9][0-9]\.[a-z]*\.[0-9]*|[0-9]* \w\w\w \w\w*|[0-9][0-9][A-Z][A-Z][A-Z][0-9]|[0-9]*\-[0-9]*\.[a-z]*\.[0-9]*",
                      i)
    # IF THERE IS SOMETHING IN MATCH THEN APPEND IT TO DATE COLUMN
    if match != None:
        DATE_column.append(match.group())
        i = i.replace(match.group(), "")
        OCR_3.append(i)
        
    # IF THERE ISN'T A MATCH TO THAT DATE FORMAT THEN APPEND A NONE
    else:
        DATE_column.append(None)
        OCR_3.append(i)

## TURN THEN LIST INTO A PANDAS COLUMN
zipped= list(zip(DATE_column, OCR_3))
df1 = pd.DataFrame(zipped, columns=["Date", "Rest"])
df1

##_____________________GET COUNTRY, STATE, COUNTY, AND COORDINATES_______


# FIND COUNTRY IN DATA AND MAKE A LIST WITH FINDS AND NANS
COUNTRY_column = []
for index, row in df1.iterrows():
    match = re.search(COUNTRIES_pattern, row['Rest'])
    if match != None:
        COUNTRY_column.append(match.group())
    else:
        COUNTRY_column.append(None)
        
        
df1['Country'] = COUNTRY_column
for index, row in df1.iterrows():
    if row['Country'] != None:
        row['Rest'] = re.sub(row["Country"], "", row['Rest'])
df1['Rest']
 

## FIND STATE AND MAKE COLUMN
STATE_column = []
for index, row in df1.iterrows():
    match = re.search(STATES_pattern, row['Rest'])
    if match != None:
        STATE_column.append(match.group())
    else:
        STATE_column.append(None)
df1['State'] = STATE_column
for index, row in df1.iterrows():
    if row['State'] != None:
        row['Rest'] = re.sub(row["State"], "", row['Rest'])


## DELETE ANY FOUND STATES
for index, row in df1.iterrows():
    if row['State'] != None:
        row['Rest'] = re.sub(row["State"], "", row['Rest'])
    row['Rest'] = re.sub("^\W ", "", row['Rest']) 
    row['Rest'] = re.sub("^\W ", "", row['Rest'])
df1['Rest']
         


## FIND COUNTIES AND MAKE COLUMN
COUNTIES_column = []
for index, row in df1.iterrows():
    match = re.search("\w* Co\W", row['Rest'])
    if match != None:
        COUNTIES_column.append(match.group())
    else:
        COUNTIES_column.append(None)
df1['County'] = COUNTIES_column

## DELETE FOUND COUNTIES AND EXTRA STUFF AT THE FRONT
for index, row in df1.iterrows():
    if row['County'] != None:
        row['Rest'] = re.sub(row["County"], "", row['Rest'])
    row['Rest'] = re.sub("^\W ", "", row['Rest']) 
    row['Rest'] = re.sub("\n", ";", row['Rest'])
    row['Rest'] = re.sub("^\W ", "", row['Rest']) 
    

## FIND ELEVATION AND MAKE COLUMN
ELEVATION_column = []
for index, row in df1.iterrows():
    match = re.search(" [0-9]*m\W| [0-9]* m\W| [0-9]* ft\W| [0-9]*ft\W| [0-9],[0-9]*ft\W", row['Rest'])
    if match !=None:
        ELEVATION_column.append(match.group())
    else:
        ELEVATION_column.append(None)
df1['Elevation'] = ELEVATION_column

## DELETE FOUND ELEVATION
for index, row in df1.iterrows():
    if row['Elevation'] != None:
        row['Rest'] = re.sub(row["Elevation"], "", row ['Rest'])
    row['Rest'] = re.sub("^\W", "", row['Rest'])
    row['Rest'] = re.sub("^\W", "", row['Rest'])
        
    
#FIND COORDINATES **BETA**
## NEEDS TO INCLUDE MORE FORMATS
## u00b0 = degree symbol
LATITUDE_pattern = "[0-9][0-9]\.[0-9]*|[0-9][0-9]\u00b0[0-9][0-9]\"[0-9][0-9]\WN|[0-9][0-9]\u00b0[0-9][0-9]\"[0-9][0-9]\WS"
LATITUDE_column = []
for index, row in df1.iterrows():
    match = re.search(LATITUDE_pattern, row['Rest'])
    if match != None:
        LATITUDE_column.append(match.group())
    else:
        LATITUDE_column.append(None)
df1['Latitude'] = LATITUDE_column
LATITUDE_column    


## DELETE FOUND LATITUDE
for index, row in df1.iterrows():
    if row['Latitude'] != None:
        row['Rest'] = re.sub(row['Latitude'], "", row['Rest'])
    row['Rest'] = re.sub('^\W', "", row['Rest'])
     
    
## NEEDS TO INCLUDE MORE FORMATS
## SUPPORTED FORMATS: -112.5010, 23degreesymbol13"12'
LONGITUDE_pattern = "\-[0-9]*\.[0-9]*|[0-9]*\.[0-9]|[0-9]*\u00b0[0-9][0-9]\"[0-9][0-9]\WE|[0-9]*\u00b0[0-9][0-9]\"[0-9][0-9]\WW"
LONGITUDE_column = []
for index, row in df1.iterrows():
    match = re.search(LONGITUDE_pattern, row['Rest'])
    if match != None:
        LONGITUDE_column.append(match.group())
    else:
        LONGITUDE_column.append(None)
df1['Longitude'] = LONGITUDE_column


## DELETE FOUND LONGITUDE
for index, row in df1.iterrows():
    if row['Longitude'] != None:
        row['Rest'] = re.sub(row['Longitude'], "", row['Rest'])
    row['Rest'] = re.sub('^\W', "", row['Rest'])


## THIS NEEDS MAJOR WORK. MAYBE TAKE OUT COORDINATES FIRST
LOCALITY_column = []
for index, row in df1.iterrows():
    match = re.search("(?m)^[^\r\n;]+",  row['Rest'])
    if match != None:
        LOCALITY_column.append(match.group())
    else:
        LOCALITY_column.append(None)
df1['Locality'] = LOCALITY_column
df1['Locality']
df1['Rest']


## DELETE FOUND LOCALITY
for index, row in df1.iterrows():
    if row['Locality'] != None:
        row['Rest'] = re.sub(row["Locality"], "", row ['Rest'])
    row['Rest'] = re.sub("^\W", "", row['Rest'])
    row['Rest'] = re.sub("^;", "", row['Rest'])
    
        
## FIND UNIQUE IDENTIFIER
occurrenceID = []
for index, row in df1.iterrows():
    match = re.search("EMUSENT[0-9]*", row['Rest'])
    if match != None:
        occurrenceID.append(match.group())
    else:
        occurrenceID.append(None)
df1['occurrenceID'] = occurrenceID


## DELETE UNIQUE IDENTIFIER
for index, row in df1.iterrows():
    if row['occurrenceID'] != None:
        row['Rest'] = re.sub(row['occurrenceID'], "", row['Rest'])
    
    
## COMPLETE THE FOLLOWING .replace FUNCTION 5 TIMES TO GET RID 
## OF EXTRA COMMAS AND SEMICOLONS AND SPACES
for i in range(5):
    df1.replace(regex=r';$|,$|, $|^,|^ ,| ,|^ ;', value = "", inplace=True)
df1
df1.replace(state_Acronymes, state_Full)


    
## REORDER DATAFRAM TO STANDARD 
df1['eventDate'] = convert_dates(df1['Date'])

new_cols = ['Country', 'State', 'County', 'Latitude', 'Longitude', 'Elevation',
            'eventDate', 'Date', 'Rest']


df1 = df1[new_cols]
df1



# CRITICAL PIECE OF CODE #
## IF THERE IS A DAY IN eventDate that is a single digit, then add a 0
## in front
for index, row in df1.iterrows():
    if type(row['eventDate']) == str:
        # REGEX finds any dash that is to the immediate left of
        # a number that is at the end without actually matching
        # the number too. The power is in the (?=)
       row['eventDate'] = re.sub("-(?=\d$)", "-0", row['eventDate'])
        


## USE TO EXPORT RESULTS TO A CSV
#df1.to_csv("OCR_CSV.csv", sep="\t")
        


## _______________________WORKING GREAT UNTIL HERE________________







## PRINTS OUT DATAFRAME IN A MORE READABLE DICTIONARY FORMAT
for index, row in df1.iterrows():
    print(row)
    print("\n")

  

    
 
    






# PRINTS OUT THE OCR LINES ALL PRETTY
#for i in OCR_2:
#    print(i)
 #   print("\n")