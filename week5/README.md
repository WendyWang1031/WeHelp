# week5

## task2: Create database and table in your MySQL server

* Create a new database named website.

      create database website;
      show databases;
      select database();
      use website;
![task2-1](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task2/week5-task2-1.png)

***

* Create a new table named member, in the website database, designed as below:

      create table member(
      id bigint not null auto_increment,
      name varchar(255) not null,
      username varchar(255) not null,
      password varchar(255) not null,
      follower_count int unsigned not null default 0,
      time datetime not null default current_TIMESTAMP,
      PRIMARY KEY(id)
      );
  
      show columns from member;
      describe member;
![task2-2](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task2/wee5-task2-2inDB.png)
![task2-2](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task2/wee5-task2-2showDatail.png)
![task2-2](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task2/wee5-task2-2showDatail2.png)

## task3: SQL CRUD

* INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.

      insert into member (name,username,password) values ('test','test','test');
      insert into member (name,username,password) values ('Wendy','wendywang','wendypw');
      insert into member (name,username,password) values ('Yoyo','yoyoking','yoyopw');
      insert into member (name,username,password) values ('Peter','peterlee','peterpw');
      insert into member (name,username,password) values ('Hani','honey','hanipw');

![task3-1](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-1and2.png)

***


* SELECT all rows from the member table.

      select * FROM member;

![task3-2](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-1and2.png)

***


* SELECT all rows from the member table, in descending order of time.

      select * FROM member order by time desc;

![task3-3](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-3.png)  

***


* SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.

      select * from member order by time desc limit 3 offset 1;

![task3-4](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-4.png)    

***


* SELECT rows where username equals to test.

      select * from member where username='test';

![task3-5](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-5.png) 

***


* SELECT rows where name includes the es keyword.

      select * from member where name like '%es%';

![task3-6](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-6.png) 

***


* SELECT rows where both username and password equal to test.

      select * from member where username = 'test' AND password ='test';

![task3-7](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-7.png) 

***


* UPDATE data in name column to test2 where username equals to test.

      update member set name='test2' where username='test';

![task3-8](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task3/week5-task3-8.png) 


## task4: SQL Aggregation Functions

* SELECT how many rows from the member table.

      select count(*) from member;

![task4-1](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task4/week5-task4-1.png) 

***


* SELECT the sum of follower_count of all the rows from the member table.

      select sum(follower_count) FROM member;

![task4-2](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task4/week5-task4-2.png) 

***


* SELECT the average of follower_count of all the rows from the member table.

      select AVG(follower_count) from member;

![task4-3](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task4/week5-task4-3.png) 

***


* SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.

      select avg(follower_count) from (
      select follower_count from member
      order by follower_count desc
      limit 2
      ) top_two;

![task4-4](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task4/week5-task4-%EF%BC%94.png) 

## task5: SQL JOIN

* Create a new table named message, in the website database. designed as below:

      create table message(
      id bigint primary key auto_increment,
      member_id bigint not null,
      content varchar(255) not null,
      like_count int unsigned not null default 0,
      time datetime not null default current_TIMESTAMP,
      FOREIGN KEY (member_id) REFERENCES member(id)
      );
      show columns from message;
    
      insert into message (member_id,content,like_count) values (1,"first message",10);
      insert into message (member_id,content,like_count) values (2,"hello world",2);
      insert into message (member_id,content,like_count) values (4,"meow",12);
      insert into message (member_id,content,like_count) values (3,"good",1);
      insert into message (member_id,content,like_count) values (5,"well done",8);
      
      select * FROM message;

![task5-1](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task5/week5-task5-1.png) 
![task5-1](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task5/week5-task5-1and2.png) 

***


* SELECT all messages, including sender names. We have to JOIN the member table to get that.

      select message.id, member.name, message.content, message.like_count, message.time
      from message
      inner join member
      on message.member_id = member.id;

![task5-2](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task5/week5-task5-2.png) 

***


* SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.

      select message.id, member.name, message.content, message.like_count, message.time
      from message 
      inner join member on message.member_id = member.id
      where member.username = 'test';

![task5-3](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task5/week5-task5-3.png) 

***


* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.

      select avg(message.like_count)
      from message 
      inner join member on message.member_id = member.id
      where member.username = 'test';

![task5-4](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task5/week5-task5-4.png) 

***


* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.

      select member.username, avg(message.like_count) as avg_like_count
      from message
      inner join member on message.member_id = member.id
      group by member.username;

![task5-5](https://github.com/WendyWang1031/WeHelp/blob/main/week5/task5/week5-task5-5.png) 
