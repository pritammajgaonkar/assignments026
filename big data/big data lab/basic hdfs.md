## **Using HDFS Commands**
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/1.PNG)

You do not have any files in /user/root yet, so no output is displayed. <br/>
Run the -ls command again, but this time specify the root HDFS folder <br/>
create a directory named test in HDFS <br/>
-p command can be used to create multiple directories. The second command above will fail if you omit the -p.<br/>
To recursively view the contents of a folder, use -ls -R:
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/2.PNG)

Delete the test2 folder (and recursively, its subcontents) using the -rm -R command
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/3.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/4.1.PNG)

Run the following -put command to copy data.txt into the test folder in HDFS
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/4.2.PNG)

copy the data.txt file in test to another folder in HDFS using the -cp command <br/>
Now delete the data2.txt file using the -rm command
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/5.PNG)

You can use the -cat command to view text files in HDFS
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/6.1.PNG)

use the ‐tail command to view the end of a file
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/6.2.PNG)

See if you can figure out how to use the get command to copy test/data.txt from HDFS into your local /tmp folder
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/7.PNG)

Put the file /root/devph/labs/demos/small_blocks.txt into the test folder in HDFS.<br/>
You should now have two files in test: data.txt and small_blocks.txt. <br/>
The two files that were in the test folder in HDFS were merged into a single file and stored on the local file system.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/8.PNG)

The blocksize is defined using the dfs.blocksize property on the command line. <br/>
The file should be broken down into two blocks.
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/basic%20lab1/9.PNG)
