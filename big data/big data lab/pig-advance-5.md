## ** Splitting a Dataset **

>Research the White House visitor data and look for members of Congress.

Unzip labs/Lab5.1/whitehouse_visits.txt
enter into pig
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/1.PNG)

make directory as whitehouse in grunt
use copy from local to copy from labs/Lab5.1/whitehouse_visits.txt into whitehouse/visits.txt
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/2.PNG)

>In this step, you will explore the comments field of the White House visitor data. <br/>
From the Pig Grunt shell, start by loading visits.txt <br/>
>Field $25 is the comments. Filter out all records where field $25 is null <br/>
>Now define a new relation that is a projection of only column $25 <br/>
>View the schema of comments and make sure you understand how this relation ended up as a tuple with one field. <br/>
>A common Pig task is to test a relation to make sure it is consistent with what you are intending it to be. <br/>
But using DUMP on a big data relation might take too long or not be practical, so define a SAMPLE of comments.<br/>
>Now DUMP the comments_sample relation
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/3.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/3.2.PNG)

> Count the Number of Comments <br/>
The comments relation represents all non‐null comments from visits.txt. Write Pig statements that output the number <br/>
of records in the comments relation. The correct result is 222,839 records.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/4.1.PNG)

>correct result is 222,839 records
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/4.2.PNG)

>Use the SPLIT command to split the visits relation into two new relations named congress and not_congress <br/>
>Store the congress relation into a folder named ‘congress’. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/6.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/6.2.PNG)

>Similarly, STORE the not_congress relation in a folder named ‘not_congress’ <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/7.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/7.2.PNG)

>View the output folders using ls <br/>
>View one of the output files in congress and make sure the string “CONGRESS” appears in the comment field
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/9.PNG)

>Write Pig statements that output the number of records in the congress relation. <br/>
This will tell us how many visitors to the White House have “CONGRESS” in the comments of their visit log. The correct result is 102.
>Note = You now have two datasets: one in ‘congress,’ with 102 records, and the remaining records in the ‘not_congress’ folder.<br/>
>These records are still in their original, raw format.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/10.1.PNG)

>You have just split ‘visits.txt’ into two datasets, and you have also discovered that 102 visitors <br/>
to the White House had the word “CONGRESS” in their comments field.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-5/10.2.PNG)
