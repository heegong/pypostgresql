# pypostgresql


## How use ?
1. you must install pycopg2 module
pip install pycopg2 or pip3 install pycopg2

2. db = postgresql(host,db_name,user_id,user_password)

3. you can use postgresql method 

### method

##### 1.query_execute
###### parameter  
string : query


query execute



##### 2.select
###### parameter
column : select column      list
table : table name

return as tuple



##### 3.insert
###### parameter
column : insert column
values : insert values
table : table name

insert int table



##### 4.create_table
###### parameter
make : str or tuple(list) make colmun
table : make table name

create table



##### 5.return_query
###### parameter
string : query
ls : null

Used for query statements that require return



##### 6.where_select
###### parameter
column : select column     list
where_query : where query    
table : table name

Used for select that needs where




###### made by heegong
