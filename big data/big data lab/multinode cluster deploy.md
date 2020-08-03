## **multinode cluster deploy**

>Launch instance – amazon linux 2 AMI. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/1.PNG)

>Chose an instance type -> select t2 large -> next <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/2.PNG)

>3)	Configure instance details ->no of instances =3  ->next (add storage) <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/3.PNG)

>Add storage -> size =100gb <br/>
>Skip tag <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/4.PNG)

>Configure security group ->security group name =xyz <br/>
Ssh tcp port 22 <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/5.PNG)

>Launch ->select your key <br/>
>Launch instance <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/6.PNG)

>We get three instances ->rename them <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/7.PNG)

>We have to perform ssh on all three instances using mobaxterm. <br/>
>Select master (first that you renamed as hdp-m) ->copy ip address and open in mobaxterm. <br/>
>13)	If ssh wont worked properly then go to inbound rules and check ssh port. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/8.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/9.PNG)

>Select worker 0 (first that you renamed as hdp-w0) ->copy ip address and open in mobaxterm. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/10.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/11.PNG)

>Select worker 1 (first that you renamed as hdp-w1) ->copy ip address and open in mobaxterm. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/12.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/13.PNG)

>15)	Perform sudo su on all shh ,it will take you to the root. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/14.PNG)

>Perform these commands on all three ssh  <br/>
>#OS firewall - stop/disable <br/>
-> yum install -y  iptables-services <br/>
   -> service iptables stop <br/>
   -> chkconfig iptables off <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/15.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/16.PNG)

>18)	This is optional as it’s already installed. <br/>
->yum -y install wget
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/17.PNG)

>Directly sed like this  in all ssh-> (to disable the selinux) <br/>
->sudo sed -i 's/enforcing/disabled/g' /etc/selinux/config /etc/selinux/config
>Perform in all ssh and make ssure  it is disabled . <br/>
->sudo sestatus
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/18.PNG)

>Perform  in all ssh -> yum -y install ntp <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/19.PNG)

>Make sure the on all ssh -> yum -y install ntp is installed ,then this command will run successfully ,otherwise shows error as not installed. <br/>
-> chkconfig ntpd on <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/20.PNG)

>Perform on all ssh ,it will get you ambary repo <br/>
->wget -nv http://public-repo-1.hortonworks.com/ambari/amazonlinux2/2.x/updates/2.7.4.0/ambari.repo -O /etc/yum.repos.d/ambari.repo <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/21.PNG)

>To check ambary repo is there or not on all shh  -> <br/>
-> yum repolist <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/22.PNG)

>As we are going to install AMBARI SERVER on master node ,perform this on master shh <br/>
->yum -y install ambari-server <br/>
>If you haven’t put –y in the command then you have configure if every time by typing ‘y’,which –y does automatically does for all. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/23.PNG)

>Now we are going to install AMBARI AGENT on remaining two ssh by -> (hd-w1) <br/>
->yum -y install ambari-agent <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/24%20hd%20w1.PNG)

>We are also going to install AMBARI AGENT on master ssh also -> type y at last to allow. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/25.PNG)

>To to allow communication between AMBARI SERVER  and  AMBARI AGENT we need to provide ip of SERVER to the AGENT. <br/>
>Copy the private dns from here -> <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/26.PNG)

>Now you have to give this ip to the AMBARI AGENT -> vi  this file. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/27.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/28.PNG)

>Insert mode -> remove localhost and paste ip there ->do it wherever your AMBARI AGENT is present. <br/>
>E.g My AMBARI AGENT is present on two slave nodes and one master node. On mater node is it optional to do becaz <br/>
>AMBARI SERVER itself is present there , but it is necessary to do for two salve nodes. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/29.PNG)

>Perform this on all ssh. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/30.PNG)

>Perform this on all ssh. <br/>
>Add this to .ini file in security section /etc/ambari-agent/conf/.ini <br/>
>sed -i '65 a force_https_protocol=PROTOCOL_TLSv1_2' /etc/ambari-agent/conf/ambari-agent.ini <br/>

>>download and install mYsql jars and mysql server package <br/>
->wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm  <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/31.PNG)

>sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/32.PNG)

>wget https://rpmfind.net/linux/mageia/distrib/3/x86_64/media/core/release/mysql-connector-java-5.1.22-2.mga3.noarch.rpm <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/33.PNG)

>yum install mysql-connector-java-5.1.22-2.mga3.noarch.rpm  <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/34.PNG)

>cd /var/lib/ambari-server/resources/ <br/>
>ln -s /usr/share/java/mysql-connector-java.jar mysql-connector-java.jar <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/35.PNG)

>Now we are going to setup AMBARI SERVER -> perform  this only on the AMBARI SERVER (master node) <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/36.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/37.PNG)

>Now we are going to start the AMBARI SERVER. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/38.PNG)

>Now we are going to start the AMBARI AGENT. Perform this on all ssh. (on master)<br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/39.PNG)

> (on worker 0)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/40.PNG)

> (on worker 1)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/41.PNG)

>copy the public IP of master, to start AMBARI <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/42.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/43.PNG)

>need to open 8080 port,go to security group of master <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/44.PNG)

>cutum tcp 8080 anywhere <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/45.PNG)

>default username and password is admin. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/46.PNG)

>Launch install wizard <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/47.PNG)

>name of cluster ->next <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/48.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/49.PNG)

>copy the private DNS of all instances. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/50.PNG)

>paste privat DNS here -> mannual registration <br/>
>warning ->ok <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/51.PNG)

>if progress fails then check the status that AMBARI-AGNET is running or not. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/52.PNG)

>Open this port on same salve port.-> <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/53.PNG)

>click on retry failed,and process is successfull. <br/>
.clicking on the "click here to see check result" can see the HOST CHECKS. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/54.PNG)

>Select the services you want ,also possible to add some services later. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/55.1.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/55.2.PNG)

>Assign slaves and clients. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/56.PNG)

>Create a password and write same password in all boxes. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/57%20pritam1234.PNG)

>shows customise services. <br>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/58.PNG)

>deploy <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/59.PNG)

>Install start and test. it will take 20-25 min to start. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/60.PNG)

>complie. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/61.PNG)

>all services are shown here ,green dot indicates services are active . <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/62.PNG)

>can stop the sevices by -> <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/63.PNG)

>By clickcing on namenode it shows all details. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/64.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/65.PNG)

>We can add another services by-> <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/66.PNG)

>We can also check properties here and by using filter we can directly find desired property. <br/>
>We can also change replication factor ,after changing it asks what changes has been made ,because it saves changes by making version, <br/>
so even we need to roll back some changes we can easily get them. <br/>
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/67.PNG)
![](https://github.com/pritammajgaonkar/assignments026/blob/Big-data/big%20data/images/cluster%20deploy/68.PNG)

