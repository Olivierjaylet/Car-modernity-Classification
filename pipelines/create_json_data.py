# packages

# sql
import sqlite3

import json

import pandas as pd

import re
import os


conn = sqlite3.connect(r'C:\Users\Olivier\Documents\GitHub\DVM_car.db')

query = "SELECT * FROM autosWithNames"
df_autosWithNames = pd.read_sql_query(query, conn)

query2 = "SELECT * FROM `Ad_table (extra)`"
df_Ad_table = pd.read_sql_query(query2, conn)

query3 = "SELECT * FROM Image_table"
df_Images = pd.read_sql_query(query3, conn)

# close the connection to database
conn.close()



df_Ad_table['image_link'] = df_Ad_table['Maker']  +'**'+df_Ad_table[' Genmodel'] +'**'+df_Ad_table['Adv_year'].astype(str)+'**'+df_Ad_table['Color']+'**' +df_Ad_table['Adv_ID']  

# Drop everything after the last '*'
df_Images['image_link'] = df_Images['Image_name'].str.rsplit('**', n=1).str[0]

merged_df = pd.merge(df_Images, df_Ad_table, on='image_link', how='inner')

data_dict = {}

for index, row in merged_df.iterrows():
    # Extract image_link
    image_link = row['image_link']
    image_link = image_link.replace('**', '$$')
    
    
    row_data = {}
    for column in merged_df.columns:
        if column != 'image_link':
            value=row[column]
            
            # Check if the value is NaN and handle accordingly
            if pd.notnull(row[column]):
                if type(value)==str:
                    value = value.replace('**', '$$')
                else :
                    pass
            else:
                value = None
            row_data[column] = value
            
    
    # Assign the row data to the image_link key in data_dict
    data_dict[image_link] = row_data


json_string = json.dumps(data_dict, indent=4)

# Save the JSON string to a file
with open('data/data.json', 'w') as json_file:
    json_file.write(json_string)
