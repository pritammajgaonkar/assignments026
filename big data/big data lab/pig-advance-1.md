**Joining Datasets with Pig**

Put the file labs/Lab6.2/congress.txt into the whitehouse directory in HDFS.
Use the hdfs dfs -ls command to verify that the congress.txt file
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/1.PNG)

use hdfs dfs -cat to view its contents.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/2.PNG)

Click the Save button and save the new, empty file as join.pig in the labs/Lab6.2 folder:

## $$steps$$ <br/> 
## TASK -> Click the Save button and save the new, empty file as join.pig in the <br/>
## labs/Lab6.2 folder: <br/>

## PROCEDURE -> <br/>

## on mobaxterm -> <br/>
## *type ->vi join.pig <br/>
## * press enter <br/>
## * press i to insert the data. <br/>
## * copy text and paste in here. <br/>
## * press enter <br/>
## * to close -> press escape  <br/>
## * then press -> :wq (for save and quit) <br/>

>Define the following visitors relations, which will contain the first and last names of all White House visitors <br/>
Add the following load command that loads the ‘congress.txt’ file into a relation named congress. <br/> 
The data is tab‐delimited, so no special Pig loader is needed <br/>
>The names in visits.txt are all uppercase, but the names in congress.txt are not. <br/>
Define a projection of the congress relation that consists of the following fields <br/>
>Define a new relation named join_contact_congress that is a JOIN of visitors <br/>
and congress_data. Perform the join on both the first and last names <br/>
>Use the STORE command to store the result of join_contact_congress into a directory named ‘joinresult’.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/3.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/4.PNG)

Run the script using the following command
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/5.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/5.2.PNG)

>The output will be in the joinresult folder in HDFS. Verify that the folder was created
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/6.PNG)

>View the resulting file
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/7.PNG)

>Delete the joinresult directory in HDFS
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/8.1.PNG)

>Modify your JOIN statement in join.pig so that is uses replication. It should look like this
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/8.2.PNG)

>Save your changes to join.pig and run the script again.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/9.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/10.PNG)

>Notice in the output of your join.pig script that we know which party the visitor belongs to: <br/>
Democrat, Republican,or Independent. Using the join_contact_congress relation as a starting point,<br/>
see if you can figure out how to output the number of Democrat, Republican, and Independent members <br/>
of Congress that visited the White House. Name the relation counters and use the DUMP command to output the results
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/11.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/12.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-1/13.PNG)
