import mysql.connector as connector
import pandas as pd
mydatabase=connector.connect(host="localhost", username="root",password="Vedant@123",database="hospital")

cursor=mydatabase.cursor()

#Extarct data from india table and create pipe seperated file
df=pd.read_sql("select * from ind",con=mydatabase)
df.to_csv("output_data.txt",sep="|")
mydatabase.commit()


