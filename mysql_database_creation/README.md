
The software I am currently exploring is MYSQL, an open source relational database management system that utilizes SQL and has the functionality to 
connect and interact with other programming languages. 

In my case, I am creating and accessing my MYSQL databases using Python via. Jupyter Notebooks through JupyterHub, connecting to the
MSU MYSQL servers which are accessibile to any students with an engineering account.

MYSQL is used in engineering and scientific pursuits, especially on the topics of Data Analysis and Data Science. Because MYSQL
(and SQL in general) is used as a means to store and query data, it is a crutch to anyone working with both high level data
and large quantities of data.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ACCESSING MYSQL ON THE HPCC (from the command line):

1) Access MySQL via. commandline or HPCC, then type in the following:

mysql -u USERNAME -pPASSWORD -h HOSTNAMEORIP DATABASENAME 

-u: username

-p: password (no space between -p and the password text)

-h: host

The last option (-h: host) is name of the database that you want to connect.

For more information, visit this link: https://dev.mysql.com/doc/refman/8.0/en/connecting.html 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ACCESSING MySQL in the example script 

To use the example scripts provided in this directory, insert the necessary information where the hashtags are within the script

To run the python script from the command line, do python3 "insert script name"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
References, Links, etc

1) The best buy data came from my CSE 482 class (Big Data Analysis)

2) The code / script provided was written by me
