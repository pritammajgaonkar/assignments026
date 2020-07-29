## **Computing ngrams of Emails in Avro Format**

>Change directories to the /labs/Lab7.5 folder. Notice this folder contains an Avro file named sample.avro. <br/>

>Link to download avro jar file. -> <br/>
>https://repo1.maven.org/maven2/org/apache/avro/avro-tools/1.8.2/avro-tools-1.8.2.jar

>command to convert avro file to avsc file -> <br/>
>java -jar ~/avro-tools-1.7.4.jar getschema twitter.snappy.avro > twitter.avsc

>Put the schema file in HDFS <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/1.PNG)

>Create a Hive Table from an Avro Schema View the contents of the CREATE TABLE query defined in the <br/>
>create_sample_table.hive file in your Computing ngrams of Emails in Avro Format lab folder: <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/2.1.PNG)

>Make sure the avro.schema.url property points to the schema file you created in the previous step: <br/>
> OLD METHOD where input and outputs needed to specify <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/2.2.PNG)

>Start the Hive shell. <br/>
>Run the show tables command and verify that you have a table named sample_table. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/3.PNG)

>Copy sample.avro into the Hive warehouse folder by running the following command <br/>
>View the contents of sample_table, then quit the Hive Shell <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/4.PNG)

>Put the Avro schema file into in HDFS <br/>
>Use more to view the contents of the create_email_table.hive ;:script in your /labs/Lab7.5 folder. <br/>
>Verify the avro.schema.url property is correct. <br/>
>Run the script to create the hive_user_email table <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/5.1.PNG)

> NEW METHOD (where you have no need to define input and output formats) <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/5.2.PNG)

>Copy mbox7.avro into the warehouse directory <br/>
>Start the Hive shell and verify the table has data in it. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/6.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/6.2.PNG)

>Use the Hive ngrams function to create a bigram of the words in mbox7.avro <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/7.PNG)

>To clean this up, use the Hive explode function to display the output in a more readable format <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/8.PNG)

>Typically when working with word comparison we ignore case. Run the query again, but this time add the Hive <br/>
lower function and compute 20 bigrams <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/9.PNG)

>From the Hive shell, run the following query, which uses the context_ngrams function to find the top 20 terms <br/>
that follow the word “error”. <br>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/10.PNG)

>Run a Hive query that finds the top 20 results for words in mbox7.avro that follow the phrase “error in.” <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-advance-4/11.PNG)
