**Importing RDBMS Data into HDFS**
## step 1) create RDS and connect with the MYSQL <br/>
           create cluster with sqoop 
## step 2) open salaries.sql file in the labs/Lab3.1 <br/>
           with the queries in it create database and table <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/1.PNG)
## step 3)right clk on table ->table import wizard -> browse ->salect salaries.csv file(if doesn't exits rename it with csv extension)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/2.PNG)
## step 4) right clk on table and check data is available in table or not.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/3.PNG)
## step 5) Now import the data from DB into hdfs with command ->
           sqoop import --connect jdbc:mysql://(dns endpoint)/(name of DB) --username root --password 12345678 --table salaries(source) --target-dir(destination) s3a://pritam(name of bucket)/data(created directory in bucket)/
           sqoop import --connect jdbc:mysql://database-1.chbg97eakeaq.us-east-1.rds.amazonaws.com/test1 --username root --password 12345678 --table salaries --target-dir s3a://pritam/data/
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/5.PNG)           
## step 6) List the contents in the bucket <br/>
           List the contents in the data <br/>
           default mapper is 4,so data is divided in 4 parts.
           (-cat)view the contents in parts.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/6.PNG)
## step 7) import only two columns salary and age with mapper 1.<br/>
           sqoop import --connect jdbc:mysql://database-1.chbg97eakeaq.us-east-1.rds.amazonaws.com/test1 --username root --password 12345678 --table salaries --columns salary,age -m 1 --target-dir s3a://pritam/data/            
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/7.PNG)
## step 8) shows only two imported columns.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/8.PNG)
## step 9) alter table salaries with following changes.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/9.PNG)
## step 10) Split by command with mapper 2
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/10.PNG)
## step 11) shows two parts splited ganderwise.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.1/11.PNG)
