create database Mycollege;
use MYcollege;
create table student(std_id int primary key auto_increment,
name varchar(50),
age tinyint,
phone bigint,
email varchar(100));

insert into student(name,age,phone,email)
values
 ("shejal",18,7618957947,"shejal@email.com"),
("riya",20,7896546789,"riya@email.com");

select * from student;

alter table student add column Address varchar(100);   #to add column in table
alter table student change column phone mobile_no bigint;   #to change the name of column in table
alter table student modify column age smallint;			#change the datatype of column in table


update student 
set mobile_no = "1234567890" 
where std_id = 1; 		#single update
set sql_safe_updates = 0;  #disable safe mode
set sql_safe_updates = 1;		#enable the safe mode

update student set address = "varanasi" where age=20;  	#multiple/range update







