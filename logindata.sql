CREATE DATABASE deviflasksql;
USE deviflasksql;
CREATE TABLE usertable(user_id varchar(30) NOT NULL,password_user varchar(30) NOT NULL);
INSERT INTO usertable(user_id,password_user) VALUES ('devik01','devi123');
SELECT * from usertable;

