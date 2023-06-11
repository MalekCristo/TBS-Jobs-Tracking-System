/****delete*****/
CREATE OR REPLACE  PACKAGE used_tools
IS
cursor c1 IS select sex,COUNT(noStudent) from  Student GROUP BY sex;
cursor c2 IS select major,COUNT(Stud1) from Diploma GROUP BY major;
cursor c3 IS select minor,COUNT(Stud1) from Diploma GROUP BY minor;
cursor c4 IS select minor,COUNT(Stud1) from Diploma GROUP BY minor;
cursor c5 IS select major,sex,COUNT(Stud1) from Diploma,Student WHERE Student.noStudent=Diploma.Stud1 GROUP BY major,sex;
cursor c6 IS Select  major,sex,Count(Stud1) FROM  Diploma,Student WHERE round((grad_date-start_date)/365)>4 AND Student.noStudent=Diploma.noDiploma GROUP BY major,sex;
cursor C7 IS Select  noStudent,fname,Address FROM  Diploma,Student  WHERE round((grad_date-start_date)/365)>4 AND Student.noStudent=Diploma.noDiploma GROUP BY major,sex;
TRIGGER TRG_Deleted BEFORE DELETE ON Student;
CREATE OR REPLACE TRIGGER TRG_Update AFTER UPDATE ON Student;
CREATE OR REPLACE FUNCTION AVG_hired_student(I NUMBER);
CREATE OR REPLACE FUNCTION jobs_per_domain(I NUMBER);
END used_tools;

CREATE OR REPLACE PACKAGE BODY used_tools AS
Declare
cursor c1 IS 
   select sex,COUNT(noStudent) from  Student 
   GROUP BY sex;
   Psex Student.sex%TYPE;
   PSnostudent Student.noStudent%TYPE;
 BEGIN 
 open C1;
 loop 
    fetch sex,Count(noStudent) INTO Psex,PSnoStudent;
    exit when C1%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(PnoStudent,Psex);
    END loop ;
    close C1;
 END;

Declare
cursor c2 IS 
   select major,COUNT(Stud1) from Diploma 
   GROUP BY major
   Pmajor Diploma.major%TYPE;
   PStud1 Diploma.Stud1%TYPE;
 BEGIN 
 open C2;
 loop 
    fetch major,COUNT(Stud1) INTO Pmajor,PSStud1;
    exit when C2%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(Pmajor,PSStud1);
     END loop ;
     close c2;
 END;
Declare
cursor c3 IS select minor,COUNT(Stud1) from Diploma GROUP BY minor;
   Pminor Diploma.minor%TYPE;
   PSStud1 Diploma.Stud1%TYPE;
 BEGIN 
 open C3;
 loop 
    fetch minor,COUNT(Stud1) INTO Pminor,PSStud1;
    exit when C3%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(Pminor,PSStud1);
    END loop ;
    close C3;
 END;
Declare
cursor c4 IS select minor,COUNT(Stud1) from Diploma GROUP BY minor;
   Pminor Diploma.minor%TYPE;
   PSStud1 Diploma.Stud1%TYPE;
 BEGIN 
 open C4;
 loop 
    fetch minor,COUNT(Stud1) INTO Pminor,PSStud1;
    exit when C3%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(Pminor,PSStud1);
     END loop ;
     close c4;
 END;
Declare
cursor c5 IS select major,sex,COUNT(Stud1) from Diploma,Student WHERE Student.noStudent=Diploma.Stud1 GROUP BY major,sex;
   Psex Student.Student%TYPE;
   pmajor Diploma.major%TYPE;
   PSStud1 Diploma.Stud1%TYPE;
 BEGIN 
 open C5;
 loop 
    fetch major,COUNT(Stud1),sex INTO Pmajorr,PSStud1;Psex
    exit when C4%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(Pmajor,PSStud1,Psex);
   END loop ;
   close C5;
 END;
Declare
cursor c6 IS Select  major,sex,Count(Stud1) FROM  Diploma,Student WHERE round((grad_date-start_date)/365)>4 AND Student.noStudent=Diploma.noDiploma GROUP BY major,sex;
   Psex Student.Student%TYPE;
   pmajor Diploma.major%TYPE;
   PSStud1 Diploma.Stud1%TYPE;
 BEGIN 
 open C6;
 loop 
    fetch major,COUNT(Stud1),sex INTO Pmajor,PSStud1;Psex
    exit when C6%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(Pmajor,PSStud1,Psex);
    END loop ;
    close c6;
END;
Declare
cursor C7 IS Select  noStudent,fname,Address FROM  Diploma,Student  WHERE round((grad_date-start_date)/365)>4 AND Student.noStudent=Diploma.noDiploma GROUP BY major,sex;
   PnoStudent Student.noStudent%TYPE;
   Pfname Student.fname%TYPE;
   PAddress Student.Address%TYPE;
 BEGIN 
 open C7;
 loop 
    fetch noStudent,fname,Address INTO PnoStudent,Pfname;PAddress
    exit when C7%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(PnoStudent,Pfname,PAddress);
   END loop ;
   close c7;
END;

CREATE OR REPLACE TRIGGER TRG_Deleted
   BEFORE DELETE
   ON Student
   FOR EACH ROW
BEGIN
   INSERT INTO Deleted_Students
      SELECT *
        FROM Student
       WHERE Student.P_ID = Student.P_ID;
END;

CREATE OR REPLACE TRIGGER TRG_Update
  AFTER UPDATE ON Student
  FOR EACH ROW
BEGIN
  IF( UPDATING( 'P_id' ) )
  THEN
    INSERT INTO Delete_tab( P_id, P_id_value )
      VALUES( 'p_id', :new.P_id );
  END IF;

  IF( UPDATING( 'P_email' ) )
  THEN
    INSERT INTO Delete_tab( P_email, P_email_value )
      VALUES( 'P_email', :new.P_email );
   IF( UPDATING( 'P_name' ) )
  THEN
    INSERT INTO Delete_tab( P_name, P_name_value )
      VALUES( 'P_name', :new.P_name );
  END IF;
  IF( UPDATING( 'P_name' ) )
  THEN
    INSERT INTO Delete_tab( P_addr, P_addr_value )
      VALUES( 'P_addr', :new.P_addr );
  END IF;
   IF( UPDATING( 'P_age' ) )
  THEN
    INSERT INTO Delete_tab( P_age, P_age_value )
      VALUES( 'P_age', :new.P_age );
  END IF;
  IF( UPDATING( 'career' ) )
  THEN
    INSERT INTO Delete_tab( career, career_value )
      VALUES( 'career', :new.career );
  END IF;
  IF( UPDATING( 'internship' ) )
  THEN
    INSERT INTO Delete_tab( internship, internship_value )
      VALUES( 'internship', :new.internship );
  END IF;
  IF( UPDATING( 'diploma' ) )
  THEN
    INSERT INTO Delete_tab( diploma, diploma_value )
      VALUES( 'diploma', :new.diploma );
  END IF;
  
END;
/* Average hired students*/
CREATE OR REPLACE FUNCTION AVG_hired_student(I NUMBER)
RETURN FLOAT
IS
totnumber NUMBER;
tothired NUMBER;
work_perc FLOAT:=0; 
BEGIN
Select count(stud3) into tothired FROM career WHERE situation='Employee' ;
SELECT COUNT(NOSTUDENT) INTO totnumber FROM STUDENT;
work_perc:= (tothired/totnumber)*100;
RETURN work_perc;
END AVG_hired_student;
/* jobs per domain*/
CREATE OR REPLACE FUNCTION jobs_per_domain(I NUMBER)
RETURN FLOAT
IS
BEGIN
Declare
cursor C IS 
   SELECT COUNT(NOSTUDENT) FROM  Student WHERE Sex='F';
   nbr NUMBER;
 BEGIN 
 open C;
 LOOP 
    fetch C INTO nbr;
    exit when C%NOTFOUND;
    END loop ;
    close C;
    DBMS_OUTPUT.PUT_LINE(nbr);
 END;
 End ;
END used_tools; 
