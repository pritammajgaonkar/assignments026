## **Joining Datasets in Hive**

>View the contents of the file setup.hive in labs/Lab7.4
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/1.PNG)

>Run the setup.hive script from the Joining Datasets in Hive lab folder
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/2.PNG)

>To verify that the script worked, enter the Hive Shell and run the following following queries. <br/>
>You should see daily stock prices and dividends from stocks that start with the letter K. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/3.PNG)

>The stock_aggregates table should be empty, but view its schema to verify that <br/>
it was created successfully, then type quit to exit the Hive Shell. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/4.PNG)

>Use gedit to create a new text in the labs/Lab7.4/ folder named join.hive. <br/>
>First, the result of the join is going to be put into the stock_aggregates table, which requires an insert. <br/>
>The result is going to contain the stock symbol, date traded, maximum high for the stock, minimum low, average <br/>
close, and the sum of dividends, as shown here. <br/>
>The from clause is the nyse_data table <br/>
>The join is going to be a left outer join of the dividends table <br/>
>The join is by stock symbol and trade date <br/>
>Let’s group the result by symbol and trade date <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/5.1.PNG)

>Run the query and wait for Tez to execute <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/5.2.PNG)

>Enter the Hive Shell and run a select query to view the contents of stock_aggregates <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/6.PNG)

>List the contents of the stock_aggregates directory in HDFS. The 000000_0 file was created as a result of the join query <br/>
>View the contents of the stock_aggregates table using the cat command. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-3/7.PNG)
