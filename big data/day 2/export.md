## Lab: Exporting HDFS Data to an RDBMS

steps :
## create salaries2 table in mysql 
    -> Lab3.2 -> salarydata.sql ->create table query(copy) -> connected workbench (paste)
    -> u will get an empty table.

## 1)Download lab file in AWS EMR using below command
wget https://dbda-labs.s3.amazonaws.com/labs.zip

## Unzip the downloaded zip file
unzip labs.zip .

![expo1](https://user-images.githubusercontent.com/63596484/86388663-ceec1380-bcb2-11ea-9299-e97a80dd35bc.PNG)

## 2) set CD to the Lab 3.2
Create the new directory salarydata
Put the salarydata.txt file in the salarydata
Check the file in salarydata directory

![expo 1](https://user-images.githubusercontent.com/63596484/86388644-c85d9c00-bcb2-11ea-99ce-b31ad7a49d1d.PNG)

## 2) show the contents of HDFS folder

![expo 2](https://user-images.githubusercontent.com/63596484/86388676-d27f9a80-bcb2-11ea-8add-5157b58366b3.PNG)

## 3) Run the sqoop command to export salartdata.txt file to salaries2 table in the workbench.

![expo 3](https://user-images.githubusercontent.com/63596484/86388683-d4e1f480-bcb2-11ea-9d80-8523fe24fe10.PNG)

## 4)Specify sequence of columns at the end of query.

![expo 4](https://user-images.githubusercontent.com/63596484/86388690-d7444e80-bcb2-11ea-9233-b20e881cd2ee.PNG)

## 5)Viewing the contents of salarydata.txt in the salaries2 table.

![expo 5](https://user-images.githubusercontent.com/63596484/86388692-d7dce500-bcb2-11ea-8296-817505897d93.PNG)

## Result
You have now used Sqoop to export data from HDFS into a database table in MySQL.
