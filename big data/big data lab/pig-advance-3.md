## **Analyzing Clickstream Data**

>Become familiar with using the DataFu library to sessionize clickstream data.

>If not already done as part of the prior demonstration, install DataFu
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/1.PNG)

View the contents of clicks.csv:
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/2.PNG)

Put the file in HDFS
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/3.PNG)

Using the gedit text editor, open the file labs/Lab6.4/sessions.pig.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/4.PNG)

Add the following DEFINE statement to define the Sessionize UDF.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/5.PNG)

download the ** datafu jar file **
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/6.PNG)

reset the location as we unzipped both files in 6.4. and change respective names.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/7.PNG)

Let’s verify that the Sessionized function is working by running the script
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/8.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/8.2.PNG)

Comment out the dump statement
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/9.PNG)

Comment out the dump statement
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/10.PNG)

Verify the output, which should be a single value representing the average session <br/>
time <br/>
(11.88608076923077)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/11.PNG)

A quick solution for computing the median is to simply add it to the <br/>
existing nested FOREACH statement in the sessiontimes_avg definition<br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/12.PNG)

Verify that you got the following value for the median session length <br/>
(1.9482833333333334) <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-3/13.PNG)
