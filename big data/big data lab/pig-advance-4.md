## ** Analyzing Stock Market Data using Quantiles **

Use DataFu to compute quantiles

>Change directories to the ~/devph/labs/Lab6.5 folder. <br/>
View the contents of the stocks.csv file, which contains the historical prices for <br/>
New York Stock Exchange stocks that begin with the letter “Y” <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/1.PNG)

>Put stocks.csv into your /user/root folder in HDFS (if you already have a <br/>
stocks.csv file in your HDFS home directory from exercising the block storage <br/>
demonstration, please delete the existing file first as the contents are different):
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/2.PNG)

>download the jar file and unzip
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/3.PNG)

change the location and chnage name of jar file(datafu-pig-1.6.0.jar)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/4.PNG)

Save your changes to quantile.pig <br/>
Run the script <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/5.1.PNG)

There is stock information in the input data, so the output will be the quantiles of the high price of these five stocks <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/5.2.PNG)

![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/6.PNG)

Run the modified script and view the results
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/7.1.PNG)

The output will be the median values for the same five stocks
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/pig-advance-4/7.2.PNG)

