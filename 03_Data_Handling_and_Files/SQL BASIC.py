'''
THERE ARE THREE TYPES OF COMANDS IN SQL:
DDL=> datadefinatio language
DML=> data manuplation language
TCL=> transtation control language

"DDL COMMAND"=>All commands that are related to create Modify or remove thestructure of the
database comes in DDL command.

"DML COMMAD"=> All he commands that are related to manuplating the databases comes in DML.

"TCL COMMAND"=>All the command that are related to control the transitataion of the
databases comes in TCL command
----------------------------------------------------------------------------------------------
{DATA TYES IN SQL}
#1.CHARE=> To store fixed character length of data
#2.VARCHAR=> To store the variable characters length data
#3.NUMARIC=> To store numaric data
#4.BOOLEN=> To store logical data
#5.TRUE/FALSE=> To store logical values
#6.LOB/BLOB=> To store long objects
 Example=>"long text data or binary data that is images"
----------------------------------------------------------------------------------------------
{DIFFERENCE BETWEEN "CHARE" AND "VARCHAR"}

#CHARE=>
*Chare is used to store fixed characte data
*In case of chare memory can be wasted
*It is easy to manuplated the char type

#VARCHAR=>
*Varchare used to store variable length data
*In case of char memory is saved
*It is diffccult to manuplate the varchar data type
----------------------------------------------------------------------------------------------
{SQL Comands}
_______________________________________________________________________________________________
#1.create the table:
{create data base'data base name';}
Example:create data base shaurya;
______________________________________________________________________________________________
#2.view the list of data bases:
{show data bases;}
______________________________________________________________________________________________
#3.remove the data base:
{drop data base'data base name';}
Example:drop data base shaurya;
______________________________________________________________________________________________
#4.open data base:
{use 'data base name';}
Example:use shaurya;
________________________________________________________________________________________________
#5.create the table of data base:
{create table'table name'(collumn name data type);}
Example:create table student(eno nummeric,name varchar(20),course varchar(20),fees numeric);
________________________________________________________________________________________________
#6.view the list of all table:
{show table}
_______________________________________________________________________________________________
#7.view the structure of the table:
{desc 'data base name';}
Example:desc shaurya;
_______________________________________________________________________________________________
#8.remove the table:
{drop table(table name);}
"This command will remove all the recordsas well as structure of the table"
Example:drop table student;
----------------------------------------------------------------------------------------------
***{modify the table}***
"In modify we can add new column,remove existing column,change width of column"

#1.add new column"gender" in table
{alter "table name" add "column name" char("char value");}
Example:alter student table add gender char(20);
'''
