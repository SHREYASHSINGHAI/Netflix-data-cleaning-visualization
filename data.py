import pandas as pd
import numpy as np
import matplotlib.pyplot as mt

#odf = original dataframe
#reading the csv file
odf=pd.read_csv(r"D:\college\Netflix\archive (2)\netflix1.csv")
print("************************************************************************************************")
print("BEFORE OPERATIONS")
print("INFO : ")
print(odf.info())
print("COLUMNS : ")
print(odf.columns)
print("UNIQUE VALUES : ")
print(odf.nunique())

#counting the number of countries involved in making movies and uploading on netflix
#and calculating their contributions
print("  ")
country_count=odf['country'].nunique()       #total number of countries
print("Number of country's movies on netflix : ",country_count)
countries=odf['country'].value_counts()      #counting each contry's contribution
print("countries and their contributions : ",countries)
print("The year in which most films are released : ",odf["release_year"].value_counts().idxmax())
print("Number of films released in this year : ",odf["release_year"].value_counts().max())


#counting the number of different directors 
directorcnt=odf['director'].nunique()

print("------------------------------------------------------------------------------------------------")
#$$$$$$$$$$$ OPERATIONS $$$$$$$$$$$$$$$
df1=odf
#converting date_time from sting to proper date_time
df1['date_added']=pd.to_datetime(df1['date_added'])

#replacing the Not Given value with nan 

df1=df1.replace("Not Given",np.nan)

#Droping all null values 
df1=df1.dropna()

print("________________________________________________________________________________________________")
print("AFTER OPERATION")
print(' ')


#counting the number of countries involved in making movies and uploading on netflix
#and calculating their contributions
country_count=df1['country'].nunique()       #total number of countries
print("Number of country's movies on netflix : ",country_count)
countries=df1['country'].value_counts()      #counting each contry's contribution
print("countries and their contributions : ",countries)

#Getting the year in which most movies,series are released
print("The year in which most films are released : ",df1["release_year"].value_counts().idxmax())
print("Number of films released in this year : ",df1["release_year"].value_counts().max())
df1.to_csv(r"D:\college\Netflix\archive (2)\NoNull.csv")

#$$$$$$$$$$$ VISUALIZATION$$$$$$$$$$$$$
df1.groupby(df1['date_added'].dt.year)['show_id'].count().plot(kind="bar",color='r')
mt.title("Movies/series released with compolete details in year")
mt.legend()

mt.show()

# print("number of directors involved : ",directorcnt)
# print(df.groupby('country').value_counts())