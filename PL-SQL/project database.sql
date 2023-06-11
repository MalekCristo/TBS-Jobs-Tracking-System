
/* CREATE ADMINISTRATION */
CREATE TABLE Administration(
idAdmin  NUMBER(10),
first_name  VARCHAR2(30),
last_name  VARCHAR2(30));

/* CREATE STUDENT */
CREATE TABLE Student(
noStudent  NUMBER(10),
admin NUMBER(10),
fname  VARCHAR2(30),
lname  VARCHAR2(30),
age NUMBER(2),
sex  CHAR,
email VARCHAR2(30),
address  VARCHAR2(30),
phone_num NUMBER);

/* CREATE DIPLOMA */
CREATE TABLE Diploma(
noDiploma  VARCHAR2(30),
Stud1 NUMBER(10),
university  VARCHAR2(30),
dip VARCHAR2(50),
major VARCHAR2(30),
minor VARCHAR2(30),
sec_maj_min VARCHAR2(30),
start_date DATE,
grad_date DATE);


/* CREATE INTERNSHIP */
CREATE TABLE Internship(
idInternship  VARCHAR2(30),
Stud2 NUMBER(10),
num_int NUMBER,
host_organization  VARCHAR2(30),
period NUMBER(2));


/* CREATE CAREER */
CREATE TABLE Career(
idCareer  VARCHAR2(30),
Stud3 NUMBER(10),
situation  VARCHAR2(30),
domain VARCHAR2(30),
hiring_date DATE,
leaving_date DATE,
city VARCHAR2(30),
salary VARCHAR2(30),
searchMean VARCHAR2(30));

/*Create Table Classification*/
CREATE TABLE Classification (
Very_low  VARCHAR2(30),
Low VARCHAR2(30),
Modeste  VARCHAR2(30),
Meduim  VARCHAR2(30),
High  VARCHAR2(30),
Very_high  VARCHAR2(30),
Excellent  VARCHAR2(30)
);

/*ALTER ADMINISTRATION */
ALTER TABLE Administration
ADD ( CONSTRAINT C1_admin PRIMARY KEY(idAdmin));

/*ALTER Student */
ALTER TABLE Student
ADD ( CONSTRAINT C1_student PRIMARY KEY(noStudent),
            CONSTRAINT C2_student FOREIGN KEY(admin) REFERENCES Administration(idAdmin));
            
/*ALTER Diploma */
ALTER TABLE Diploma
ADD ( CONSTRAINT C1_diploma PRIMARY KEY(noDiploma),
            CONSTRAINT C2_diploma FOREIGN KEY(Stud1) REFERENCES Student(noStudent));

/*ALTER INTERNSHIP*/

ALTER TABLE Internship
ADD ( CONSTRAINT C1_internship PRIMARY KEY(idInternship),
            CONSTRAINT C2_internship FOREIGN KEY(Stud2) REFERENCES Student(noStudent));
            
/*ALTER CAREER*/
ALTER TABLE  Career
ADD ( CONSTRAINT C1_career PRIMARY KEY(idCareer),
            CONSTRAINT C2_career FOREIGN KEY(Stud3) REFERENCES Student(noStudent));
            
            
/*Fill Classification*/
INSERT INTO Classification VALUES('Below 1000','1000-1500','1500-2000','2500-3000','3000-4000','4000-5000','Above 5000');