# pypostgresql

<br/><br/>

## How to use ?
1. you must install psycopg2 module
pip install pycopg2 or pip3 install psycopg2

2. db = postgresql(host,db_name,user_id,user_password)

3. you can use postgresql method 
<br/><br/><br/>

### method

##### 1.query_execute
###### parameter  
string : query


query execute

<br/><br/><br/>

##### 2.select
###### parameter
column : select column      list
table : table name

return as tuple

<br/><br/><br/>

##### 3.insert
###### parameter
column : insert column
values : insert values
table : table name

insert int table

<br/><br/><br/>

##### 4.create_table
###### parameter
make : str or tuple(list) make colmun
table : make table name

create table

<br/><br/><br/>

##### 5.return_query
###### parameter
string : query
ls : null

Used for query statements that require return

<br/><br/><br/>

##### 6.where_select
###### parameter
column : select column     list
where_query : where query    
table : table name

Used for select that needs where

<br/><br/><br/><br/><br/>


###### made by heegong
