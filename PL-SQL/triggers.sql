
CREATE TABLE del_info_stud (
Delete_date DATE,
id NUMBER,
f VARCHAR2(30),
l VARCHAR2(30) );

CREATE TABLE up_info_stud (
Update_date DATE,
id NUMBER,
f VARCHAR2(30),
l VARCHAR2(30) ,
age NUMBER,
sex CHAR(1),
email VARCHAR(30),
Ad VARCHAR(50),
Phone_num NUMBER);

CREATE TABLE del_info_dip (
Delete_date DATE,
id VARCHAR2(30),
stud NUMBER,
dip VARCHAR2(50));

CREATE TABLE up_info_dip (
Update_date DATE,
id VARCHAR2(30),
stud NUMBER,
dip VARCHAR2(50),
university VARCHAR(30),
major VARCHAR2(30),
minor VARCHAR2(30),
sec_maj_min VARCHAR2(30),
start_date DATE,
grad_date DATE);


CREATE TABLE del_info_career (
Delete_date DATE,
id VARCHAR2(30),
stud NUMBER,
situation VARCHAR2(30),
domain VARCHAR2(30));

CREATE TABLE up_info_career (
Update_date DATE,
id VARCHAR2(30),
stud NUMBER,
situation VARCHAR2(30),
domain VARCHAR2(30),
hiring_date DATE,
leaving_date DATE,
city VARCHAR2(30),
salary VARCHAR2(30),
searchmean VARCHAR2(30));

CREATE TABLE del_info_internship (
Delete_date DATE,
id VARCHAR2(30),
stud NUMBER,
num_int NUMBER,
host VARCHAR2(30),
period NUMBER);


CREATE TABLE up_info_internship (
Update_date DATE,
id VARCHAR2(30),
num_int NUMBER,
stud NUMBER,
host VARCHAR2(30),
period NUMBER);


/**BEFORE INSERT ON Student**/

CREATE OR REPLACE TRIGGER Insert_criteria
BEFORE INSERT OR UPDATE ON Student
FOR EACH ROW

BEGIN

/*Check Whether email is valid*/
IF ( INSTR(:NEW.email,'@')=0 ) OR ( INSTR(:NEW.email,'.')=0 )
THEN RAISE_APPLICATION_ERROR (-20500, 'Insert A Valid Email');
END IF;

END Insert_criteria;

/** Backup Information **/

/** Contol deleted tables **/

/**student**/
CREATE OR REPLACE TRIGGER backup_info_del
AFTER DELETE ON Student
FOR EACH ROW
BEGIN
INSERT INTO del_info_stud (Delete_date, id, f, l)
VALUES(SYSDATE, :OLD.noStudent, :OLD.fname, :OLD.lname);
END;

/**diploma**/
CREATE OR REPLACE TRIGGER backup_info_dip
AFTER DELETE ON  Diploma
FOR EACH ROW
BEGIN
INSERT INTO del_info_dip (Delete_date, id, stud, dip)
VALUES(SYSDATE, :OLD.noDiploma, :OLD.stud1, :OLD.dip);
END;



/**Career**/
CREATE OR REPLACE TRIGGER backup_info_career
AFTER DELETE ON  Career
FOR EACH ROW
BEGIN
INSERT INTO del_info_career (Delete_date, id, stud, situation, domain)
VALUES(SYSDATE, :OLD.IDcareer, :OLD.stud3, :OLD.situation, :OLD.domain);
END;


/*internship*/
CREATE OR REPLACE TRIGGER backup_info_internship
AFTER DELETE ON  Internship
FOR EACH ROW
BEGIN
INSERT INTO del_info_internship (Delete_date, id, stud , host)
VALUES(SYSDATE, :OLD.IDinternship, :OLD.stud2, :OLD.host_organization);
END;

/** Contol updated tables **/

/**student**/
CREATE OR REPLACE TRIGGER backup_info_up
AFTER UPDATE ON Student
FOR EACH ROW
BEGIN  
INSERT INTO up_info_stud (Update_date, id, f, l, age , sex, email, Ad , Phone_num)
VALUES(SYSDATE, :OLD.noStudent, :OLD.fname, :OLD.lname,:OLD.age,:OLD.sex,:OLD.email,:OLD.Address,:OLD.phone_num);
END;

/**diploma**/
CREATE OR REPLACE TRIGGER backup_info_dip2
AFTER UPDATE ON  Diploma
FOR EACH ROW
BEGIN
INSERT INTO up_info_dip (Update_date, id, stud, dip,university,major,minor,sec_maj_min,start_date,grad_date)
VALUES(SYSDATE, :OLD.noDiploma, :OLD.stud1, :OLD.dip,:OLD.university,:OLD.major,:OLD.minor,:OLD.sec_maj_min,:OLD.start_date,:OLD.grad_date);
END;

/**Career**/
CREATE OR REPLACE TRIGGER backup_info_career2
AFTER Update ON  Career
FOR EACH ROW
BEGIN
INSERT INTO up_info_career (Update_date, id, stud, situation, domain,leaving_date,city,salary ,searchmean)
VALUES(SYSDATE, :OLD.IDcareer, :OLD.stud3, :OLD.situation, :OLD.domain,:OLD.leaving_date ,:OLD.city,:OLD.salary,:OLD.searchmean);
END;


/*internship*/
CREATE OR REPLACE TRIGGER backup_info_internship2
AFTER UPDATE ON  Internship
FOR EACH ROW
BEGIN
INSERT INTO up_info_internship (Update_date, id, stud ,num_int , host , period)
VALUES(SYSDATE, :OLD.IDinternship, :OLD.stud2, :OLD.num_int, :OLD.host_organization,:OLD.period);
END;

/**Clear Student Archive**/

CREATE OR REPLACE PROCEDURE del_stud (I NUMBER)
IS
BEGIN 
  DELETE FROM del_info_stud ;
  COMMIT ;
END; 

CREATE OR REPLACE PROCEDURE up_stud (I NUMBER)
IS
BEGIN 
  DELETE FROM up_info_stud ;
  COMMIT ;
END; 

/**Clear Diploma Archive**/

CREATE OR REPLACE PROCEDURE del_dip (I NUMBER)
IS
BEGIN 
  DELETE FROM del_info_dip ;
  COMMIT ;
END; 

CREATE OR REPLACE PROCEDURE up_dip (I NUMBER)
IS
BEGIN 
  DELETE FROM up_info_dip ;
  COMMIT ;
END; 
/**Clear Career Archive**/

CREATE OR REPLACE PROCEDURE del_career (I NUMBER)
IS
BEGIN 
  DELETE FROM del_info_career ;
  COMMIT ;
END; 

CREATE OR REPLACE PROCEDURE up_career1 (I NUMBER)
IS
BEGIN 
  DELETE FROM up_info_career ;
  COMMIT ;
END; 


/**Clear Internship Archive**/

CREATE OR REPLACE PROCEDURE del_internship (I NUMBER)
IS
BEGIN 
  DELETE FROM del_info_internship ;
  COMMIT ;
END; 

CREATE OR REPLACE PROCEDURE up_internship (I NUMBER)
IS
BEGIN 
  DELETE FROM up_info_internship ;
  COMMIT ;
END; 

