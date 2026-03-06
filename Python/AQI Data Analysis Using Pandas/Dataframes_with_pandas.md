<h1>Explore AQI data with pandas</h1>

## Introduction

Your work as a data professional for the U.S. Environmental Protection Agency (EPA) requires you to analyze air quality index data collected from the United States and Mexico.

The air quality index (AQI) is a number that runs from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health concern. For example, an AQI value of 50 or below represents good air quality, while an AQI value over 300 represents hazardous air quality. Refer to this guide from [AirNow.gov](https://www.airnow.gov/aqi/aqi-basics/) for more information.

In order to complete the project, load a dataframe, examine its metadata and summary statistics, and explore it using iloc indexing and sorting. Furthermore, practice also Boolean masking, grouping, and concatenating data.

![AQI Levels](https://github.com/PoojaSolanki2017/Portfolio_Project/blob/main/Input_Datasets/AQI_levels.JPG)")

## Task 1: Read data from csv file into a pandas dataframe

You are given two files of data. Begin with the first file, which contains the three states with the most observations (rows): California, Texas, and Pennsylvania.


```python
#import pandas
import pandas as pd
```

### 1b: Read in the first csv file


```python
#link to input dataset
input_dataset = "https://raw.githubusercontent.com/PoojaSolanki2017/Portfolio_Project/refs/heads/main/Python_Project/c2_epa_air_quality.csv"

#read data from csv as a pandas object
df_states = pd.read_csv(input_dataset)

#print data frame data
print(df_states.head(10))

```

       state_code  state_name  county_code  county_name   aqi  state_code_int  \
    0           4     Arizona           13     Maricopa  18.0               4   
    1           4     Arizona           13     Maricopa   9.0               4   
    2           4     Arizona           19         Pima  20.0               4   
    3           6  California            1      Alameda  11.0               6   
    4           6  California            7        Butte   6.0               6   
    5           6  California           19       Fresno  11.0               6   
    6           6  California           29         Kern   7.0               6   
    7           6  California           29         Kern   3.0               6   
    8           6  California           29         Kern   7.0               6   
    9           6  California           37  Los Angeles  13.0               6   
    
       county_code_int  
    0               13  
    1               13  
    2               19  
    3                1  
    4                7  
    5               19  
    6               29  
    7               29  
    8               29  
    9               37  


<details>
  <summary><h4><strong>Hint</strong></h4></summary>

Because the file is already in your working directory, you can simply pass the file name to the `pd.read_csv()` function as a string.

</details>

## Task 2: Summary information

### 2a: Metadata
Examine the number of rows and columns, the column names, the data type contained in each column, the number of non-null values in each column, and the amount of memory the dataframe uses.


```python
#### print data frame information
print("**********************************")
print("Data frame dimentions")
print("**********************************")
print(df_states.shape,"\n")

print("**********************************")
print("Data frame column names")
print("**********************************")
print(df_states.columns,"\n")

print("**********************************")
print("Data frame row names")
print("**********************************")
print(df_states.index,"\n")

print("**********************************")
print("Data frame column data types")
print("**********************************")
print(df_states.dtypes,"\n")

print("**********************************")
print("Data frame information")
print("**********************************")
print(df_states.info(),"\n")

```

    **********************************
    Data frame dimentions
    **********************************
    (1725, 7) 
    
    **********************************
    Data frame column names
    **********************************
    Index(['state_code', 'state_name', 'county_code', 'county_name', 'aqi',
           'state_code_int', 'county_code_int'],
          dtype='object') 
    
    **********************************
    Data frame row names
    **********************************
    RangeIndex(start=0, stop=1725, step=1) 
    
    **********************************
    Data frame column data types
    **********************************
    state_code           int64
    state_name          object
    county_code          int64
    county_name         object
    aqi                float64
    state_code_int       int64
    county_code_int      int64
    dtype: object 
    
    **********************************
    Data frame information
    **********************************
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1725 entries, 0 to 1724
    Data columns (total 7 columns):
     #   Column           Non-Null Count  Dtype  
    ---  ------           --------------  -----  
     0   state_code       1725 non-null   int64  
     1   state_name       1725 non-null   object 
     2   county_code      1725 non-null   int64  
     3   county_name      1725 non-null   object 
     4   aqi              1725 non-null   float64
     5   state_code_int   1725 non-null   int64  
     6   county_code_int  1725 non-null   int64  
    dtypes: float64(1), int64(4), object(2)
    memory usage: 94.5+ KB
    None 
    


<details>
  <summary><h4><strong>Hint</strong></h4></summary>

The `info()` method returns a dataframe's metadata.

</details>

### 2b: Summary statistics
Examine the summary statistics of the dataframe's numeric columns. The output should be a table that includes row count, mean, standard deviation, min, max, and quartile values.


```python
print("**********************************")
print("Data frame summary statistics")
print("**********************************")
print(df_states.describe(),"\n")
```

    **********************************
    Data frame summary statistics
    **********************************
            state_code  county_code          aqi  state_code_int  county_code_int
    count  1725.000000  1725.000000  1725.000000     1725.000000      1725.000000
    mean     26.595942    83.939130    11.034783       26.595942        83.939130
    std      18.702416   118.027324    10.385993       18.702416       118.027324
    min       1.000000     1.000000     0.000000        1.000000         1.000000
    25%       6.000000    20.000000     5.000000        6.000000        20.000000
    50%      26.000000    55.000000     8.000000       26.000000        55.000000
    75%      42.000000   101.000000    15.000000       42.000000       101.000000
    max      80.000000   810.000000    93.000000       80.000000       810.000000 
    


## Task 3: Explore and transform data

### 3a: Rows per state

Calculate total states from `state_name` column using `value_counts()` method to check how many rows there are for each state in the dataframe.


```python
#calculate count for each states
number_of_states = df_states['state_name'].nunique()
state_counts = df_states['state_name'].value_counts()

print("**********************************")
print("Total states in data frame")
print("**********************************")
print(number_of_states,"\n")

print("**********************************")
print("Value count for each states")
print("**********************************")
print(state_counts)

```

    **********************************
    Total states in data frame
    **********************************
    42 
    
    **********************************
    Value count for each states
    **********************************
    California              342
    Texas                   104
    Pennsylvania            100
    Florida                  81
    Arizona                  72
    Colorado                 66
    Nevada                   65
    Ohio                     63
    Virginia                 51
    New York                 51
    New Jersey               45
    Illinois                 37
    Washington               36
    North Carolina           34
    Missouri                 33
    Massachusetts            33
    Michigan                 31
    New Mexico               30
    Minnesota                29
    Country Of Mexico        28
    Tennessee                27
    Indiana                  27
    Utah                     26
    Kentucky                 24
    Oklahoma                 22
    Alabama                  22
    Connecticut              21
    Wisconsin                20
    Montana                  20
    Puerto Rico              19
    Oregon                   17
    Hawaii                   16
    West Virginia            15
    Kansas                   15
    Maryland                 15
    Georgia                  14
    Alaska                   14
    Nebraska                 13
    Iowa                     12
    District Of Columbia     12
    Louisiana                12
    Vermont                  11
    Name: state_name, dtype: int64


### 3b: Sort data frame by AQI values

Create a new dataframe called by using the `sort_values()` method and the new dataframe should contain the data sorted by AQI, beginning with the rows with the highest AQI values.



```python
#sort dat frame by AQI column
sorted_AQI_df = df_states.sort_values(by = 'aqi', ascending = False)

print("****************************************")
print("Top 10 Sstates with highest AQI values")
print("****************************************")

#print top10 AQI rows
print(sorted_AQI_df.head(10))

```

    ****************************************
    Top 10 Sstates with highest AQI values
    ****************************************
          state_code         state_name  county_code            county_name   aqi  \
    253            6         California           37            Los Angeles  93.0   
    1324          80  Country Of Mexico            2  BAJA CALIFORNIA NORTE  79.0   
    116           53         Washington           61              Snohomish  76.0   
    107           47          Tennessee          157                 Shelby  74.0   
    123            4            Arizona           13               Maricopa  66.0   
    607            4            Arizona           13               Maricopa  66.0   
    787            9        Connecticut            3               Hartford  61.0   
    980           80  Country Of Mexico            2  BAJA CALIFORNIA NORTE  60.0   
    125            4            Arizona           13               Maricopa  60.0   
    472            6         California           37            Los Angeles  59.0   
    
          state_code_int  county_code_int  
    253                6               37  
    1324              80                2  
    116               53               61  
    107               47              157  
    123                4               13  
    607                4               13  
    787                9                3  
    980               80                2  
    125                4               13  
    472                6               37  


### 3c: Use `iloc` to select rows

Use `iloc` to select the two rows at indices 10 and 11 of the `top3_sorted` dataframe.


```python
### print row indices 10 and 11
print(sorted_AQI_df.iloc[[10,11],:])
```

         state_code  state_name  county_code county_name   aqi  state_code_int  \
    173          53  Washington           77      Yakima  58.0              53   
    174          53  Washington           77      Yakima  57.0              53   
    
         county_code_int  
    173               77  
    174               77  


## Task 4: Examine California state's data

The previous results shows that California represents the highest AQI, so let's examine the data for just the state of California.

### 4a: Basic Boolean masking

1. Create a Boolean mask that selects only the observations of the dataframe that are from California.

2. Apply the Boolean mask to the the dataframe and assign the result to a new variable.

3. Print the first five rows of the new california data frame.


```python
# create boolean masking where state_name is California
ca_df_boolean_mask = (sorted_AQI_df['state_name'] == 'California')

#apply boolean mask to sorted AQI df
california_df = sorted_AQI_df[ca_df_boolean_mask]

print("****************************************")
print("California AQI data")
print("****************************************")

#print only California data from sorted AQI df
print(california_df)



```

    ****************************************
    California AQI data
    ****************************************
          state_code  state_name  county_code    county_name   aqi  \
    253            6  California           37    Los Angeles  93.0   
    472            6  California           37    Los Angeles  59.0   
    615            6  California           59         Orange  47.0   
    135            6  California           83  Santa Barbara  47.0   
    403            6  California           59         Orange  47.0   
    ...          ...         ...          ...            ...   ...   
    1353           6  California           59         Orange   0.0   
    74             6  California           99     Stanislaus   0.0   
    1276           6  California           25       Imperial   0.0   
    136            6  California           83  Santa Barbara   0.0   
    189            6  California           45      Mendocino   0.0   
    
          state_code_int  county_code_int  
    253                6               37  
    472                6               37  
    615                6               59  
    135                6               83  
    403                6               59  
    ...              ...              ...  
    1353               6               59  
    74                 6               99  
    1276               6               25  
    136                6               83  
    189                6               45  
    
    [342 rows x 7 columns]


### 4b: Validate CA data

Inspect the shape of the new `california_df` dataframe. Does its row count match the number of California rows determined in Task 3a?


```python
print(california_df.shape)
```

    (342, 7)


### 4c: Rows per CA county

Examine a list of the number of times each county is represented in the California data.


```python
#3count number of county for califormania
county_counts_CA = california_df['county_name'].value_counts()


print("**********************************")
print("County counts for California")
print("**********************************")
print(county_counts_CA)

```

    **********************************
    County counts for California
    **********************************
    Los Angeles        55
    Santa Barbara      26
    San Bernardino     21
    San Diego          19
    Orange             19
    Sacramento         17
    Alameda            17
    Fresno             16
    Riverside          14
    Contra Costa       13
    Imperial           13
    San Francisco       8
    Monterey            8
    Humboldt            8
    El Dorado           7
    Santa Clara         7
    Placer              6
    Butte               6
    Mendocino           6
    Kern                6
    Tulare              5
    Ventura             5
    San Joaquin         5
    Solano              5
    Sutter              4
    San Mateo           4
    Marin               3
    Stanislaus          3
    Sonoma              3
    Napa                2
    Santa Cruz          2
    San Luis Obispo     2
    Calaveras           2
    Shasta              1
    Inyo                1
    Yolo                1
    Tuolumne            1
    Mono                1
    Name: county_name, dtype: int64


### 4d: Calculate mean AQI for Los Angeles county

It seems that Los Angeles county has more than twice the number of rows of the next-most-represented county in California, so let's learn more about it.

*  Calculate the mean AQI for LA county.


```python
#create a boolean mask for Los Angeles
la_boolean_mask = california_df['county_name'] == 'Los Angeles'

la_df = california_df[la_boolean_mask]

groupby_county = california_df.query(" county_name == 'Los Angeles' ").groupby(['county_name']).agg(mean_aqi = ('aqi','mean'))

print("**********************************")
print("Mean AQI for Los Angeles")
print("**********************************")

print(groupby_county)

```

    **********************************
    Mean AQI for Los Angeles
    **********************************
                 mean_aqi
    county_name          
    Los Angeles      13.4


## Task 5: Use Groupby method

Group the original dataframe by state and calculate the mean AQI for each state.


```python
##group original df by state and calculate mean values for aqi
groupby_states = df_states.groupby(['state_name'])[['aqi']].mean()

print("**********************************")
print("Mean AQI for each states")
print("**********************************")
print(groupby_states)
```

    **********************************
    Mean AQI for each states
    **********************************
                                aqi
    state_name                     
    Alabama                7.500000
    Alaska                15.714286
    Arizona               16.597222
    California             9.412281
    Colorado              12.136364
    Connecticut           12.619048
    Country Of Mexico     19.071429
    District Of Columbia  15.916667
    Florida               11.654321
    Georgia                7.071429
    Hawaii                 7.687500
    Illinois              11.864865
    Indiana               11.148148
    Iowa                   8.000000
    Kansas                 6.400000
    Kentucky               8.625000
    Louisiana             14.833333
    Maryland               9.400000
    Massachusetts          9.454545
    Michigan               7.322581
    Minnesota              8.896552
    Missouri               7.060606
    Montana               10.600000
    Nebraska              15.153846
    Nevada                10.323077
    New Jersey            14.222222
    New Mexico            12.833333
    New York               9.235294
    North Carolina        13.470588
    Ohio                   9.682540
    Oklahoma               9.681818
    Oregon                22.411765
    Pennsylvania           6.690000
    Puerto Rico           15.947368
    Tennessee             15.000000
    Texas                  9.375000
    Utah                  18.192308
    Vermont               11.818182
    Virginia               8.588235
    Washington            24.972222
    West Virginia          6.600000
    Wisconsin              8.100000


## Task 6: Add more data by concatenating two data frames

Add more state data from your the second file.

### 6a: Read in the second file

1. Read in the data for the remaining territories. 

2. TO examine the data, print the first five rows.


```python
# read the second csv file
input_dataset2 = ("https://raw.githubusercontent.com/PoojaSolanki2017/Portfolio_Project/refs/heads/main/Python_Project/epa_others.csv")

#concat two df with pandas
df_other_states = pd.read_csv(input_dataset2)

print(df_other_states.head(5))
```

       state_code state_name  county_code county_name   aqi
    0           4    Arizona           13    Maricopa  18.0
    1           4    Arizona           13    Maricopa   9.0
    2           4    Arizona           19        Pima  20.0
    3           8   Colorado           41     El Paso   9.0
    4          12    Florida           31       Duval  15.0


### 6b: Concatenate the data

The data from `df_other_states` has the same format as the data from `df_states`. It has the same columns in the same order.

Add the data from `df_other_states` as new rows beneath the data from `df_states`. Assign the result to a new dataframe called `combined_df`.

Verify that the length of `combined_df` is equal to the sum of the lengths of `df_states` and `df_other_states`.


```python
#merge state and other_states df as combined_df

combined_df = pd.concat([df_states,df_other_states])

print("**********************************")
print("Few rows of combined data frame")
print("**********************************")

print(combined_df,"\n")
# calculate length of states and other states df and of combined_df

print("**********************************")
print("Length of states data frame")
print("**********************************")

print(len(df_states),"\n")

print("**********************************")
print("Length of other states data frame")
print("**********************************")

print(len(df_other_states),"\n")

print("**********************************")
print("Length of the new combined data frame")
print("**********************************")

print(len(combined_df),"\n")
print("Total length of df_states + df_other_states combined df:",(len(df_states) + len(df_other_states)))
print("Total length of combined df:",len(combined_df))
# 2. ### YOUR CODE HERE ###

```

    **********************************
    Few rows of combined data frame
    **********************************
          state_code  state_name  county_code     county_name   aqi  \
    0              4     Arizona           13        Maricopa  18.0   
    1              4     Arizona           13        Maricopa   9.0   
    2              4     Arizona           19            Pima  20.0   
    3              6  California            1         Alameda  11.0   
    4              6  California            7           Butte   6.0   
    ...          ...         ...          ...             ...   ...   
    1174          31    Nebraska           55         Douglas   2.0   
    1175           1     Alabama           73       Jefferson   3.0   
    1176          36    New York            5           Bronx   7.0   
    1177          29    Missouri          510  St. Louis City   5.0   
    1178          36    New York           29            Erie   0.0   
    
          state_code_int  county_code_int  
    0                4.0             13.0  
    1                4.0             13.0  
    2                4.0             19.0  
    3                6.0              1.0  
    4                6.0              7.0  
    ...              ...              ...  
    1174             NaN              NaN  
    1175             NaN              NaN  
    1176             NaN              NaN  
    1177             NaN              NaN  
    1178             NaN              NaN  
    
    [2904 rows x 7 columns] 
    
    **********************************
    Length of states data frame
    **********************************
    1725 
    
    **********************************
    Length of other states data frame
    **********************************
    1179 
    
    **********************************
    Length of the new combined data frame
    **********************************
    2904 
    
    Total length of df_states + df_other_states combined df: 2904
    Total length of combined df: 2904


## Task 7: Complex Boolean masking

According to the EPA, AQI values of 51-100 are considered of "Moderate" concern. 

*  Use Boolean masking to return the rows that represent data from the state of Washington with AQI values of 51+.


```python
#create boolean mask where state name is 'Washington' and aqi is more than 50
was_bool_mask = ((combined_df['state_name'] == 'Washington') & (combined_df['aqi'] > 51 ))

#apply boolean mask to combined data frame
washington_df = combined_df[was_bool_mask]

print(washington_df)


```

         state_code  state_name  county_code county_name   aqi  state_code_int  \
    57           53  Washington           33        King  55.0            53.0   
    116          53  Washington           61   Snohomish  76.0            53.0   
    173          53  Washington           77      Yakima  58.0            53.0   
    174          53  Washington           77      Yakima  57.0            53.0   
    40           53  Washington           33        King  55.0             NaN   
    82           53  Washington           61   Snohomish  76.0             NaN   
    121          53  Washington           77      Yakima  58.0             NaN   
    122          53  Washington           77      Yakima  57.0             NaN   
    
         county_code_int  
    57              33.0  
    116             61.0  
    173             77.0  
    174             77.0  
    40               NaN  
    82               NaN  
    121              NaN  
    122              NaN  



```python
#create a query to check all the states which has Moderate AQI level and highest AQI values
high_aqi_df = combined_df.query("aqi > 51").groupby(['state_name'])[['county_name','aqi']].max()

#create a query to check all the states which has Good AQI level and lowest AQI value
low_aqi_df = combined_df.query("aqi < 51").groupby(['state_name'])[['county_name','aqi']].min()

# define function to define aqi level from aqi values
def aqi_levels(aqi_level) :
    if aqi_level in range(0,50) :
        return "Good"
    elif aqi_level in range(51,101) :
        return "Moderate"
    elif aqi_level in range(101,151) :
        return "Unhealthy for Sensitive Groups"
    elif aqi_level in range(151,201) :
        return "Unhealthy"
    elif aqi_level in range(201,301) :
        return "Very Unhealthy"
    elif aqi_level >= 301 :
        return "Hazardous"
    

#map values by applying function 
high_aqi_df['aqi_levels'] = high_aqi_df['aqi'].map(aqi_levels)
low_aqi_df['aqi_levels'] = low_aqi_df['aqi'].map(aqi_levels)

print("**********************************")
print("States with highest AQI values")
print("**********************************")

print(high_aqi_df.sort_values(by = 'aqi', ascending=False),"\n")

print("**********************************")
print("States with lowest AQI values")
print("**********************************")
print(low_aqi_df.sort_values(by = 'aqi'))
```

    **********************************
    States with highest AQI values
    **********************************
                                 county_name   aqi aqi_levels
    state_name                                               
    California                   Los Angeles  93.0   Moderate
    Country Of Mexico  BAJA CALIFORNIA NORTE  79.0   Moderate
    Washington                        Yakima  76.0   Moderate
    Tennessee                         Shelby  74.0   Moderate
    Arizona                         Maricopa  66.0   Moderate
    Connecticut                     Hartford  61.0   Moderate
    New Mexico                    Bernalillo  54.0   Moderate
    Nevada                            Washoe  52.0   Moderate 
    
    **********************************
    States with lowest AQI values
    **********************************
                                    county_name  aqi aqi_levels
    state_name                                                 
    Alabama                           Jefferson  0.0       Good
    Virginia                    Alexandria City  0.0       Good
    Utah                                  Davis  0.0       Good
    Texas                                 Bexar  0.0       Good
    Pennsylvania                          Adams  0.0       Good
    New York                             Albany  0.0       Good
    Nevada                          Carson City  0.0       Good
    Kentucky                               Bell  0.0       Good
    Kansas                                 Linn  0.0       Good
    Minnesota                             Anoka  0.0       Good
    Country Of Mexico     BAJA CALIFORNIA NORTE  0.0       Good
    Arizona                            Maricopa  0.0       Good
    California                          Alameda  0.0       Good
    New Jersey                         Atlantic  1.0       Good
    Ohio                                Belmont  1.0       Good
    Montana                             Cascade  1.0       Good
    Colorado                              Adams  1.0       Good
    Michigan                          Kalamazoo  1.0       Good
    Connecticut                       Fairfield  1.0       Good
    Florida                             Broward  1.0       Good
    Iowa                                   Linn  1.0       Good
    Illinois                               Cook  1.0       Good
    New Mexico                       Bernalillo  1.0       Good
    Vermont                          Chittenden  2.0       Good
    Oregon                            Deschutes  2.0       Good
    Oklahoma                              Adair  2.0       Good
    Alaska                           Anchorage   2.0       Good
    Tennessee                            Blount  2.0       Good
    Hawaii                             Honolulu  2.0       Good
    Georgia                              DeKalb  2.0       Good
    Nebraska                            Douglas  2.0       Good
    Missouri                               Clay  2.0       Good
    West Virginia                        Brooke  2.0       Good
    Massachusetts                         Essex  2.0       Good
    Maryland                           Allegany  2.0       Good
    Louisiana                  East Baton Rouge  2.0       Good
    Indiana                               Allen  2.0       Good
    North Carolina                      Chatham  2.0       Good
    Wisconsin                             Dodge  2.0       Good
    Washington                            Clark  3.0       Good
    Puerto Rico                         Bayamon  5.0       Good
    District Of Columbia   District of Columbia  5.0       Good


# Conclusion

From the overall analysis, it can be predicted that the air quality level is good in many states such as Alabama, Virginia, Utah, Texas and Pennsylvania. However, it is "Moderate" in California, Country Of Mexico, Washington, Tennessee, Arizona, Connecticut, New Mexico and Nevada.

It is good that no state has Unhealthy or Hazardous air quality. 


[Double-click here to record your response.]


