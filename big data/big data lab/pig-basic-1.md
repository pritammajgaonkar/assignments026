unzip labs folder <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/1.PNG)

unzip whitehouse_visits.zip from labs/Lab5.2 <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/2.PNG)

View the contents of this file whitehouse_visits.txt
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/3.PNG)

Start the Grunt shell:
pig

From the Grunt shell, make a new directory in HDFS named whitehouse
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/4.PNG)

Use the copyFromLocal command in the Grunt shell to copy the whitehouse_visits.txt file to the <br/>
whitehouse folder in HDFS, renaming the file visits.txt. (Be sure to enter this command on a single line)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/5.PNG)

Use the ls command to verify that the file was uploaded successfully:
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/6.PNG)

You will use the TextLoader to load the visits.txt file. <br/>
TextLoader simply creates a tuple for each line of text, and it uses a single <br/>
chararray field that contains the entire line. It allows you to load lines of text.<br>/
Use the LIMIT operator to define a new relation named A_limit that is limited to 10 records of A.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/7.PNG)

Use the DUMP operator to view the A_limit relation.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/8.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/8.2.PNG)

Load the White House data again, but this time use the PigStorage loader and also define a partial schema <br/>
Use the DESCRIBE command to view the schema
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/9.PNG)

Enter the following STORE command, which stores the B relation into a folder <br/>
named whouse_tab and separates the fields of each record with tabs.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/10.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/10.2.PNG)

Verify that the whouse_tab folder was created
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/11.PNG)

You should see two map output files. <br/>
View one of the output files to verify they contain the B relation in a tabdelimited format
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/12.PNG)

Enter the following command, which stores the same relation but in a JSON format
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/13.1.PNG)

Verify that the whouse_json folder was created
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/14.PNG)

View one of the output files
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/1/15.PNG)




