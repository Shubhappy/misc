import pandas as pd 
import numpy as np

df=pd.read_csv('C:\\Users\\USER\Desktop\Shubham\Madhya Pradesh Population Data.csv')

# print(df["Sex Ratio"].mean())
# print(df["Sex Ratio"].sum())
# print(df["Sex Ratio"].median())
# print(df["Sex Ratio"].count())
# print(df["Sex Ratio"].mode())
# print(df["Sex Ratio"].rank()) #Ranking of values in ascending order
# print(df.loc[49]) #Get/set value of particular index by name(if set as index) or by index no.
# print(df.loc[49,'Sex Ratio']) #Get/set value of particular cell using index(row) and column by name(if set as index) or by index no.
# print(df.describe()) #Calculate count, mean, standard deviation, minimum value, 25%, 50% ,75% (percentile) and maximum value of the series
# print(df["Sex Ratio"].rank(ascending=False)) #Change the rank order in ascending or descending
# print(df.filter(items=['Sex Ratio'])) #To get particular column from dataframe
# print(df.filter(like='49',axis=0)) #Filter the row, if first column is not assingned as index
# print(df.get(["Persons","Sex Ratio"])) #returns the specified column(s) from the DataFrame.
# print(df.head(10)) #Return first n rows
# print(df.iat[49,1]) #Get/set value of particular cell using index(row) and column no.
# print(df.iloc[[49],[6]]) #get value using row and column no. only
# print (df.set_index('State/City')) #Set first column as index column
# print (df.insert(column no.,column name as string, list of series under column))
#print (df.pop('Males')) #Drop/remove particular column from dataframe

'''df=pd.read_csv('C:\\Users\\USER\Desktop\Shubham\supermarket_sales.csv')
#create pivot table with different aggfunc as per output requirement 
print (df.pivot_table(index='Product line',aggfunc="sum"))'''

'''
#Function to read text files
file=open("mytxtfile.txt","r") # r is reading mode
printf(file.read()) #This method reads the entire file and returns a single string containing all the contents of the file .

printf(file.readline()) #This method reads a single line from the file and returns it as string.

printf(file.readlines()) #This method reads a single line from the file and returns it as string.
'''

#print (df.set_index('Persons') #set one or more columns as index
#print (df.shape) #Give shape(Row, column) of dataframe in form of tuple
#print (df.size) #return no. of rows, if it is a series and return total no. of element(row*columns) if it is a daraframe
#print (df.sort_index()) #sort the index(row) as per requirement
#print (df.stack()) #one items details in all column can be seen horizontally in form of stack, please check dropdown of dataframe for more clarity
#print (df.unstack()) # To unstack the pivoted data
#print (df.style) #for styling of dataframe
#print (df.add_suffix('-column')) #Add suffix in row level in case of series and coulumn level in case of dataframe
#print (df.select_dtypes(include='float,int64,bool',exclude='float, int64,bool')) #print specific type of column float/int/bool
#print (df.value_counts()) #count rows of unique item values, use "normalize" property to create pie chart
#print (df.transpose()) #Transpose the dataframe
#print (df.to_excel_writer()) #write date to excel file
#print (df.to_dict() #convert dataframe into dictionary
print (df.t)