CREATE DATABASE deviflasksql;
USE deviflasksql;
CREATE TABLE usertable(user_id varchar(30) NOT NULL,password_user varchar(30) NOT NULL,name_user varchar(30) NOT NULL,Rollno varchar(50) NOT NULL,streamuser varchar(30) NOT NULL);
INSERT INTO usertable(user_id,password_user,name_user,Rollno,streamuser) VALUES ('devik01','devi123','Devi Krishna','MITU19IMBI0015','Bioengineering');
SELECT * from usertable;
INSERT INTO usertable(user_id,password_user,name_user,Rollno,streamuser) VALUES ('diyak06','diya456','Diya Krishna','MITU25EMBS0022','Commerce');
SELECT * from usertable;