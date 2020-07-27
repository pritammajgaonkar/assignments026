You will use the TextLoader to load the visits.txt file. From the Pig Grunt shell,define the following LOAD relation <br/>
Define a new relation named B that is a group of all the records in A <br/>
Use DESCRIBE to view the schema of B.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/1.PNG)

The A field of the B tuple is a bag of all of the records in visits.txt. Use the COUNT <br/>
function on this bag to determine how many lines of text are in visits.txt <br>/
Use DUMP on A_count to view the result
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/2.1.PNG)

(rowcount,447598)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/2.2.PNG)

We now know how many records are in the data, but we still do not have a clear picture of what the records <br/>
look like. Let’s start by looking at the fields of each record. Load the data using PigStorage(‘,’) instead of TextLoader() <br/>
Use a FOREACH...GENERATE command to define a relation that is a projection of the first 10 fields of the visits relation <br/>
Use LIMIT to display only 50 records then DUMP the result
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/3.PNG)

There are 26 fields in each record, and one of them represents the visitee (the person being visited in the White House).<br/>
Your goal now is to locate this column and determine who has visited the President of the United States. Define a <br/>
relation that is a projection of the last seven fields ($19 to $25) of visits. <br/>
Use LIMIT to only output 500 records. The output should look like:
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/4.PNG)

Use FILTER to define a relation that only contains records of visits where field <br/>
$19 matches POTUS. Limit the output to 500 records
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/5.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/5.2.PNG)

Let’s discover how many people have visited the President. To do this, we need to count the number of records in visits where <br/>
field $19 matches POTUS. See if you can write a Pig script to accomplish this. Use the potus relation from the previous step <br/>
as a starting point. You will need to use GROUP ALL and then a FOREACH projection that uses the COUNT function.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/6.1.PNG)

If successful, you should get 21,819 as the number of visitors to the White House who visited the President
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/6.2.PNG)

Now FILTER the relation by visitors who met with the President <br/>
Define a projection of the potus relationship that contains the name and time of arrival of the visitor <br/>
Order the potus_details projection by last name <br/>
Store the records of potus_details_ordered into a folder named potus and using a comma delimiter 
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/7.1.PNG)


![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/7.2.PNG)

View the contents of the potus folder <br/>
View the contents of the output file using cat:
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-basic-2/8.PNG)
