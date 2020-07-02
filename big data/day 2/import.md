# Lab: Importing RDBMS Data into HDFS
## Steps
step 1-> Create an Amazon RDS database.<br />
step 2-> Creat a cluster-> go to advanced options -> select sqoop 1.4.7<br />
step 3-> Connect this database with MySQL Workbench
      -> RDS -> endpoint(copy) -> hostname(paste)

step 4 -> labs ->Lab3.1 -> salaries.sql(open)
          mysql -> create new database
          
          -> create table salaries (
            gender varchar(1),
            age int,
            salary double,
            zipcode int);
            
            -> copy this create table query in your connected workbench and run.
            
            -> Run this query
            
            ->load data local infile '/C:\Users\ADMIN\Downloads\labs\labs\Lab3.1/salaries.txt' into table salaries fields terminated by ',';
            
            -> mysql -> close connection ->right clk on your connection -> edit connetion -> advanced ->others ->
               OPT_LOCAL_INFILE=1(Paste) -> test connection ->OK
               
            -> mysql -> tables -> salaries -> rigth clk -> show rows-> you will see your data is loaded.
            
##  1)Enter the following Sqoop command (all on a single line), which imports the salaries table in the test database into HDFS:          
                          
![impo 1](https://user-images.githubusercontent.com/63596484/86345543-48ffa680-bc79-11ea-8db3-3477612d50e8.PNG)
 note -> op= 50 records retreived.


## 2) Verify the Import
## View the contents of your HDFS folder:

![impo 2](https://user-images.githubusercontent.com/63596484/86345559-4e5cf100-bc79-11ea-8d76-ba38873eaa98.PNG)

note ->Due to -m 1 , it shows only one part


## 3)Use the cat command to view the contents of the files.

![imppo 2 1](https://user-images.githubusercontent.com/63596484/86345618-62a0ee00-bc79-11ea-8dac-d2195ef955f2.PNG)

note -> You can use the -cat command to view text files in HDFS. Enter the following command to view the contents of data.txt:


## 4) Specify Columns to Import
Using the ‐‐columns argument, write a Sqoop command that imports the salary and age columns (in that order) of the salaries table into a directory in HDFS 
named salaries2. In addition, set the ‐m argument to 1 so that the result is a single file.

![impo 3 1](https://user-images.githubusercontent.com/63596484/86345565-50bf4b00-bc79-11ea-8145-5fee6cd7c9e9.PNG)

note -> op= retreived 50 records


## 5) After the import, verify you only have one part‐m file in salaries2:

![impo 3 2](https://user-images.githubusercontent.com/63596484/86345576-53ba3b80-bc79-11ea-9c71-e116d3d66476.PNG)


## 6) Verify that the contents of part‐m‐00000 are only the two columns you specified

![impo 4](https://user-images.githubusercontent.com/63596484/86345586-561c9580-bc79-11ea-9b9b-79b72589f5e5.PNG)


## 7) Importing from a Query
Write a Sqoop import command that imports the rows from salaries in MySQL whose
salary column is greater than 90,000.00.
a. Use gender as the --split-by value, specify only two mappers, and import the data into the salaries3 folder in HDFS.
## Tip
The Sqoop command will look similar to the ones you have been using throughout this lab, except you will use --query instead of --table. Recall that when you use
a --query command you must also define a --split-by column, or define -m to be 1. Also, do not forget to add $CONDITIONS to the WHERE clause of your query, as
demonstrated earlier in this unit.

![impo 5](https://user-images.githubusercontent.com/63596484/86345592-59178600-bc79-11ea-9625-e08489cbe1e7.PNG)


## 8)To verify the result, view the contents of the files in salaries3. You should have only two output files.
## View the contents of part‐m‐00000 and part‐m‐00001
![impo 6](https://user-images.githubusercontent.com/63596484/86345640-6cc2ec80-bc79-11ea-86ed-ad05c3e92b37.PNG)

## Result
You have imported the data from MySQL to HDFS using the entire table, specific columns, and
also using the result of a query.
