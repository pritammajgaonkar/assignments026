**Exporting HDFS Data to an RDBMS**
## step 1) As we are going to export data in DB,DB requires a table to store the data.<br/>
           open labs/Lab3.2/salaries2.sql and ctreate an empty table in the MYSQL.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.2/1.PNG)
## step 2) Write a command to export a data from s3 bucket to the salaries2 table in the MYSQL.
          Sqoop export --connect jdbc:mysql://database-1.chbg97eakeaq.us-east-1.rds.amazonaws.com/test1 --username root --password 12345678 --table salaries2 --export-dir s3a://pritam/Lab3.2/salarydata.txt --input-fields-terminated-by ","
          Sqoop export --connect jdbc:mysql://(dns endpoint)/test1 --username root --password 12345678 --table salaries2(dentination) --export-dir(export from ->) s3a://pritam/Lab3.2/salarydata.txt(source) --input-fields-terminated-by ","
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.2/2.PNG)
## Step 3) Total 10000 records exported.        
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.2/3.PNG)
## Step 4) Right clk on salaries2 table to check data is exported successfully.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/3.2/4.PNG)
