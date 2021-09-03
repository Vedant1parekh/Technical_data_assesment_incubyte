import mysql.connector as c
import pandas as pd
import csv
from datetime import datetime


#Hospital database is already created manually via create_table.sql
 
#Connecting to database using  mysql.connector
mydb=c.connect(host="localhost", username="root",password="Vedant@123",database="hospital")

#initialize cursor object
cursor=mydb.cursor()


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
#check if country table exits
def check_country_table(name):
    statement="select exists(select * from information_schema.tables where table_name='"+name+"')"
    cursor.execute(statement)
    ans=cursor.fetchone()[0]
    return ans

#Create Country table
def create_country_table(name):
    statement='''create table '''+name+'''(
    `Cust_ID` varchar(18) NOT NULL,
    `Customer_Name` varchar(255) NOT NULL,
    `Open_date` date NOT NULL,
    `Consult_Dt` date NOT NULL,
    `Vacc_type` char(5) NOT NULL,
    `Dr_Consulted` char(255) DEFAULT NULL,
    `State` char(5) DEFAULT NULL,
    `DOB` date DEFAULT NULL,
    `Active_customer` char(1) NOT NULL,
    PRIMARY KEY (`Cust_ID`)
    )'''
    cursor.execute(statement)


#check if data is already added or not
def check_data(id,entry):
    s="select Exists(select * from " + entry+ " where Cust_id ="  + id + " )"
    cursor.execute(s)
    ans=cursor.fetchone()[0] 
    return ans

#crete new data
def add_data(data,name):
    sql="INSERT INTO " + (name) + "(Cust_id,Customer_Name,Open_date,Consult_Dt,Vacc_type,Dr_Consulted,State,DOB,Active_customer)values('" + data[1][3] + "','" + data[1][2] + "','" + data[1][4] + "','" + data[1][5] + "','"+ data[1][6] + "','" + data[1][7] + "','" + data[1][8] + "','" + data[1][11] + "','" + data[1][12] + "')"
    cursor.execute(sql)
    
    

#open file and add data to each country table
with open("patients.txt","r") as f:
    data=csv.reader(f,delimiter="|")
    for each_data in enumerate(data):
        if(each_data[1][1]=='H' or each_data[1][1]=='T'):
            continue
        each_data[1][11]=datetime.strptime(each_data[1][11], '%m%d%Y').strftime('%Y-%m-%d')
        if (each_data[1][9]=="IND"):
            b=check_country_table(each_data[1][9].lower())
            if not b:
                create_country_table(each_data[1][9].lower())
            entry=check_data(each_data[1][3],each_data[1][9].lower())
            if not entry:
                add_data(each_data,each_data[1][9].lower())
mydb.commit() 
mydb.close()


        
