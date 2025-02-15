import pandas as pd
import numpy as np
import matplotlib.pyplot as mt

#odf = original dataframe
#reading the csv file
odf=pd.read_csv(r"D:\college\Netflix\Netflix-data-cleaning-visualization\netflix1.csv")
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
year=df1["release_year"].value_counts().idxmax()
produced=df1["release_year"].value_counts().max()
print(f"The year in which most movies/shows are released is {year} with {produced} productions.")
df1.to_csv(r"D:\college\Netflix\Netflix-data-cleaning-visualization\NoNull.csv")

#Getting the director who made most movies/series
dir_name=df1["director"].value_counts().idxmax()
dir_val=df1["director"].value_counts().max()
print(f"The director with most movies is {dir_name} with {dir_val} movies.")

#$$$$$$$$$$$ VISUALIZATION$$$$$$$$$$$$$
df1_axis=df1.groupby(df1['date_added'].dt.year)['show_id'].count()
odf_axis=odf.groupby(odf['date_added'].dt.year)['show_id'].count()
yrs=sorted(set(df1_axis.index).union(set(odf_axis.index)))#matching the years
x=range(len(yrs))
width=0.4
mt.bar([pos - width/2 for pos in x],df1_axis,color="green",label="with full details",width=width)
mt.bar([pos + width/2 for pos in x],odf_axis,color="red",label="unfiltered",width=width)
mt.title("Movies/series released with compolete details in year")
mt.xticks(x,yrs,rotation=30)
mt.legend()

mt.show()

# print("number of directors involved : ",directorcnt)
# print(df.groupby('country').value_counts())