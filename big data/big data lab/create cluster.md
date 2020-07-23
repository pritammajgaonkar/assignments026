## **Steps to create cluster in AWS.**
## Step 1)servies -> EMR
![1](https://user-images.githubusercontent.com/63596484/88266489-edab5c00-ccec-11ea-878b-4fe54083ba92.PNG)
## Step 2)Click on create cluster.
![2](https://user-images.githubusercontent.com/63596484/88266493-f00db600-ccec-11ea-89de-db022b3bbf35.PNG)
## Step 3)Creating cluster without sqoop <br/>
## give cluster name -> uncheck logging box -> select software config. as shown in fig.
![3](https://user-images.githubusercontent.com/63596484/88266497-f13ee300-ccec-11ea-9741-da00a32b1a0c.PNG)
## Step 4) Make hardware config -> select key pair. -> And click on create cluster. 
![4](https://user-images.githubusercontent.com/63596484/88266500-f2701000-ccec-11ea-8142-877ff7ab32e8.PNG)
## Step 5) If your creating cluster for hadoop services then GO TO ADVANCE OPTIONS.
![5](https://user-images.githubusercontent.com/63596484/88266502-f308a680-ccec-11ea-8c40-10f9e086374d.PNG)
## Step 6) Make hardware config and select SQOOP 1.4.7
![6](https://user-images.githubusercontent.com/63596484/88266506-f56b0080-ccec-11ea-8704-da6779262118.PNG)
## Step 7)select your instance type and instance count and remove unwanted task.
![7](https://user-images.githubusercontent.com/63596484/88266513-f6039700-ccec-11ea-8a09-48b20a7ab112.PNG)
## Step 8) Make sure this box is uncheked and click on next.
![8](https://user-images.githubusercontent.com/63596484/88266518-f734c400-ccec-11ea-9be9-0ca5573ef67c.PNG)
## Step 9) Give name to your cluter -> uncheck these boxes -> select key and value -> click on next.
![9](https://user-images.githubusercontent.com/63596484/88266520-f7cd5a80-ccec-11ea-8853-42799bea2f2b.PNG)
## Step 10) Select your key pair and click on create cluster.
![10](https://user-images.githubusercontent.com/63596484/88266522-f865f100-ccec-11ea-874e-dbf1d8691ce2.PNG)
## Step 11)Wait until cluster enter into waiting state.
![11](https://user-images.githubusercontent.com/63596484/88266526-f9971e00-ccec-11ea-91a9-5cabd6288ab2.PNG)
## Step 12)To add security groups for master click here.
![12](https://user-images.githubusercontent.com/63596484/88266532-fb60e180-ccec-11ea-9ad4-938485b3cf52.PNG)
## Step 13)Select security group id in front of master.
![13](https://user-images.githubusercontent.com/63596484/88266535-fbf97800-ccec-11ea-88e9-402906e6c36f.PNG)
## Step 14)Edit inboound rules
![14](https://user-images.githubusercontent.com/63596484/88266538-fd2aa500-ccec-11ea-9ec2-519c917f9a1a.PNG)
## Step 15)Check if ssh rule exits already,make it anywhere,delete another ssh rule if exist,and save rules.
![15](https://user-images.githubusercontent.com/63596484/88266541-fdc33b80-ccec-11ea-88be-db4736996347.PNG)
## Step 16)Now to connect to mobaxterm click here.
![16](https://user-images.githubusercontent.com/63596484/88266543-fef46880-ccec-11ea-97f1-08ca668ed60d.PNG)
## Step 17)Copy the selected address.
![17](https://user-images.githubusercontent.com/63596484/88266545-ff8cff00-ccec-11ea-95c9-5335d5cbce08.PNG)
## Step 18)Open mobaxterm -> create new SSH session <br/>
![18](https://user-images.githubusercontent.com/63596484/88266547-00be2c00-cced-11ea-97e5-ae187ee4770b.PNG)
## Step 19) remote hostname - paste the selected address <br/>
## select your key-> OK.
![19](https://user-images.githubusercontent.com/63596484/88266550-0287ef80-cced-11ea-8640-5a56a1b0c9dc.PNG)
## Step 20)Your EMR is successfully connected.
![20](https://user-images.githubusercontent.com/63596484/88266554-03208600-cced-11ea-83e6-5c5d9dc4c5b8.PNG)
