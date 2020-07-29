>perform pig advnace lab2 ->so you can get data which required to be filled in the table.(data is part m files)
> perform hive basic lab1 -> so you can get data in your table wh_visits.

>start the hive basic lab2 <br/>

>Start by selecting all columns where the time_of_arrival is not empty <br/>
>To find the first visit, we need to sort the result. This requires converting the time_of_arrival string into a timestamp. <br/>
>We will use the unix_timestamp function to accomplish this. Add the following order by clause. <br/>
>Let’s limit the result to 10 rows, so we can view the first 10 visitors <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/1.1.PNG)

>Execute the script whitehouse.hive and wait for the results to be displayed <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/1.2.PNG)

>Find the Last Visit ->just take the previous query and reverse the order by adding desc to the order by clause <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/2.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/2.2.PNG)

>Start by using gedit to create a new text file named comments.hive and save it in /labs/Lab7.2 folder. <br/>
>You will now create a query that displays the 10 most frequently occurring comments. Start with the following select clause <br/>
>Group the results of the query by the info_comment column <br/>
>Order the results by comment_count, because we are only interested in comments that appear most frequently <br/>
>We only want the top results, so limit the result set to 10 <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/2.3.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/2.4.PNG)

>Modify the query so that it ignores empty comments <br/>
>In comments.hive, insert the following line between your select and group statements <br/>
> where info_comment != "" <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/3.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/4.PNG)

>Run the previous query again, but this time, find the 10 least occurring comments <br/>
>Remove DESC from your order statement. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/5.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/6.PNG)

>Instead of searching for empty comments.Search for comments that contain variations of the string “GEN RECEP.” <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/7.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/8.PNG)

>Let’s try one more query to try and narrow GENERAL RECEPTION visit. Modify the WHERE clause in comments.hive to include “%GEN%” <br/>
>Leave the limit at 30, save your changes, and run the query again <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/9.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/10.PNG)

>Notice there are 2,697 visits to the POTUS with GEN RECEP in the comment field, <br/>
>which is about 12% of the 21,819 total visits to the POTUS in our dataset. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/11.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/12.PNG)

>We have 12% of visitors to the POTUS going for a general reception, but there were a lot of statements in the comments that <br/>
>contained WHO and EOP. Modify the query from the last step and display the top 30 comments that contain “WHO” and “EOP.” <br/>
>Add the DESC command back to the end of the order statement <br/>
>Make sure the "as..." portion is there <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/13.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/14.PNG)

>Modify the script again, this time to run a query that counts the number of records with WHO and EOP in the comments, and run the query <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/15.PNG)

>You should get 1,687 visits, or 7.7% of the visitors to the POTUS. So GENERAL RECEPTION still appears to be the most frequent comment. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/16.PNG)

>Find the Most Visits <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/17.PNG)

>To verify that your script worked, here are the top 20 individuals who visited the POTUS along with the number of visits <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/hive-basic-2/18.PNG)

