## **Understanding Partitions and Skew**

# To understand how Hive partitioning and skewed tables work.

> open labs/demos/hivedemo.sql -> copy the create table query and run in hive shell.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/1.PNG)

>Load Data into the Table <br/>
>When you load data into a partitioned table, you specify which partition the data goes into. <br/>
>Load the CO and SD files also <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/2.PNG)

>Verify that all of the data made it into the names table <br/>
>List the partitions and view the contents <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/3.PNG)

>Notice that each partition has its own subfolder for storing its contents. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/4.PNG)

>You can select the partition field, even though it is not actually in the data file. Hive <br/>
uses the directory name to retrieve the value. <br/>
>You can still run queries across the entire dataset. For example, the following query spans <br/>
multiple partitions. When you are done, use quit to exit the Hive shell. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/5.PNG)

>create directory **salarydata** in hdfs <br/>
>Verify the existence of the salaries.txt folder in /labs/demos/ and then put it into the /home/hadoop/salarydata/ folder in HDFS. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/6.PNG)

>View the contents of demos/skewdemo.hive, which defines a skewed table named skew_demo using the salaries.txt data <br/>
>Answer: The skewed values are the 95102 and 94040 zip codes. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/7.PNG)

>Run the skewdemo.hive script <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/8.PNG)

>View the contents of the underlying Hive warehouse folder <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/9.PNG)

>Select a few records to make sure the table has data behind it <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/10.PNG)

>Run the show_skewdemo.hive script <br/>
>shows 20 record as mentioned LIMIT 20.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-5/11.PNG)
