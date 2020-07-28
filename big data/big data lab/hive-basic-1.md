## **Understand how Hive table data is stored in HDFS**
>(starting procedure -> pig advance 2nd lab)
>unzip labs
>unzip labs/Lab5.1/whitehouse
>View the contents of wh_visits.pig <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/1.PNG)

>STORE project_potus INTO '/apps/hive/warehouse/wh_visits/';

>create a directory od name whitehouse in hdfs.
>copy  labs/Lab5.1/whitehouse_visits.txt in whitehouse directory with name visits.txt <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/2.1.PNG)

>Open wh_visits.pig with the gedit text editor <br/>
>Add the following command at the bottom of the file, which stores the project_potus relation into a very specific folder in the Hive warehouse <br/>
> store the result as project_potus in s3 bucket,result is two part m files. (you can also save the result in hdfs by making dir. in hdfs) <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/2.2.PNG)

>Save your changes to wh_visits.pig and Run the script from the command line <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/3.PNG)

>check the data in the s3 bucket which is stored in s3->pritam->project_potus.you can see two part m files. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/4.PNG)

> go to Lab7.1 -> and perform -> more wh_visits.hive, you can see table,it is the table where you need to update your data <br/>
which is currently in the s3 bucket. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/5.1.PNG)

> location of data is given from where you want to get your data. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/5.2.PNG)

>Start the Hive Shell <br/>
>From the hive> prompt, enter the “show tables” command <br/>
>You should see wh_visits in the list of tables. <br/>
>Use the describe command to view the details of wh_visits <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/6.PNG)

>You should see 20 rows returned <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/7.PNG)

>Enter the following Hive query, which outputs the number of rows in wh_visits <br/>
>Answer: 21,819 <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/8.PNG)

>Hive has two virtual columns that get created automatically for every table <br/>
INPUT__FILE__NAME and BLOCK__OFFSET__INSIDE__FILE. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/9.PNG)

>Let’s see what happens when a managed table is dropped. Start by defining a simple table called names using the Hive Shell <br/>
>Use the Hive dfs command to put Lab7.1/names.txt into the table’s warehouse folder <br/>
>View the contents of the table’s warehouse folder <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/10.PNG)

![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/11.PNG)

>>View the contents of the table’s warehouse folder again. Notice the names folder is gone (no such file or direc(mistake in path)) <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/12.PNG)

>In this step you will see how **external** tables work in Hive. Start by putting names.txt into HDFS <br/>
>Create a folder in HDFS for the external table to store its data in <br/>
>Load data into the table <br/>
>Notice the names.txt file has been moved to /user/hadoop/hivedemo <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/13.PNG)

>Similarly, verify that names.txt is no longer in your /user/root folder in HDFS <br/>
>Answer: The LOAD command moved the file from /user/hadoop to /user/hadoop/names.The LOAD command does not copy files; it moves them. <br/>
>(ignore second command) <br/>
>Now drop the names table <br/>
>View the contents of /user/root/hivedemo. Notice that names.txt is still there <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-1/14.PNG)
