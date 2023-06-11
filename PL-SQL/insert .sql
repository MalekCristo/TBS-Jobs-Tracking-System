/**insert all **/
create or replace
PROCEDURE insert_info (id Student.noStudent%TYPE, ad Student.admin%TYPE ,fn Student.fname%TYPE , ln Student.lname%TYPE , 
A Student.age%TYPE , gender Student.sex%TYPE , em Student.email%TYPE, addr Student.address%TYPE, phone Student.phone_num%TYPE ,did Diploma.noDiploma%TYPE,univ Diploma.university%TYPE ,
diploma Diploma.dip%TYPE, maj Diploma.major%TYPE, min Diploma.minor%TYPE, sec_majmin Diploma.sec_maj_min%TYPE, 
sdate Diploma.start_date%TYPE,gdate Diploma.grad_date%TYPE, idc Career.idCareer%TYPE, sit Career.situation%TYPE,
dom Career.domain%TYPE, hir_date Career.hiring_date%TYPE, leav_date Career.leaving_date%TYPE,
cit Career.city%TYPE, sal Career.salary%TYPE, sMean Career.searchMean%TYPE,idi Internship.idInternship%TYPE,
num Internship.num_int%TYPE,
host_org internship.host_organization%TYPE,
per Internship.period%TYPE)

IS
BEGIN 
  INSERT INTO Student VALUES ( id , ad  ,fn , ln  , A  , gender , em , addr , phone) ;
  INSERT INTO Diploma VALUES ( did, id ,univ ,diploma, maj, min , sec_majmin , sdate, gdate) ;
  INSERT INTO Career VALUES ( idc, id , sit ,dom , hir_date , leav_date , cit , sal , sMean ) ;
  INSERT INTO Internship VALUES (idi, id ,num, host_org,per) ;

  COMMIT ;
END; 


/**insert update delete Admin**/

/*INSERT INTO ADMINISTRATION*/
CREATE OR REPLACE PROCEDURE insert_admin ( id Administration.idAdmin%TYPE  ,fname Administration.first_name%TYPE , lname Administration.last_name%TYPE)

IS
BEGIN 
  INSERT INTO Administration VALUES ( id , fname ,lname) ;
  COMMIT ;
END; 

/*Update Administration*/
CREATE OR REPLACE PROCEDURE update_admin ( id Administration.IDadmin%TYPE ,fname Administration.first_name%TYPE,lname Administration.last_name%TYPE)

IS
BEGIN 
  UPDATE Administration 
  SET 
  first_name=fname,
  last_name=lname
  WHERE IDadmin=id;
  COMMIT ;
END; 


/*Delete FROM Administration*/
CREATE OR REPLACE PROCEDURE delete_admin ( id Administration.IDadmin%TYPE )

IS
BEGIN 
  DELETE FROM Administration WHERE IDadmin=id;
  COMMIT ;
END; 


/** insert update delete Student **/

/*INSERT INTO STUDENT*/
CREATE OR REPLACE PROCEDURE insert_student ( id Student.noStudent%TYPE, ad Student.admin%TYPE ,fn Student.fname%TYPE , ln Student.lname%TYPE , 
A Student.age%TYPE , gender Student.sex%TYPE , em Student.email%TYPE, addr Student.address%TYPE, phone Student.phone_num%TYPE )

IS
BEGIN 
  INSERT INTO Student VALUES ( id , ad  ,fn , ln  , A  , gender , em , addr , phone) ;
  COMMIT ;
END; 


/*Delete FROM STUDENT*/
CREATE OR REPLACE PROCEDURE delete_student ( id Student.noStudent%TYPE )

IS
BEGIN 
  DELETE FROM Career WHERE Stud3=id;
  DELETE FROM Internship WHERE Stud2=id;
  DELETE FROM Diploma WHERE Stud1=id;
  DELETE FROM Student WHERE noStudent=id;
  COMMIT ;
END; 


/*Update STUDENT*/
CREATE OR REPLACE PROCEDURE update_student ( id Student.noStudent%TYPE,fn Student.fname%TYPE , ln Student.lname%TYPE , 
A Student.age%TYPE , gender Student.sex%TYPE , em Student.email%TYPE, addr Student.address%TYPE, phone Student.phone_num%TYPE )

IS
BEGIN 
  Update Student 
  SET  fname=fn,
       lname=ln,
        age=A,
       sex=gender,
       email=em,
       address=addr,
       phone_num=phone
  WHERE noStudent=id;
  COMMIT ;
END; 

/** insert update delete Diploma **/ 

/*INSERT INTO DIPLOMA*/
CREATE OR REPLACE PROCEDURE insert_diploma ( id Diploma.noDiploma%TYPE, student Diploma.Stud1%TYPE ,univ Diploma.university%TYPE ,
diploma Diploma.dip%TYPE, maj Diploma.major%TYPE, min Diploma.minor%TYPE, sec_majmin Diploma.sec_maj_min%TYPE, 
sdate Diploma.start_date%TYPE,gdate Diploma.grad_date%TYPE)

IS
BEGIN 
  INSERT INTO Diploma VALUES ( id, student ,univ ,diploma, maj, min , sec_majmin , sdate, gdate) ;
  COMMIT ;
END; 

/*Delete FROM Diploma*/
CREATE OR REPLACE PROCEDURE delete_diploma ( id Diploma.noDiploma%TYPE )

IS
BEGIN 
  DELETE FROM Diploma WHERE noDiploma=id;
  COMMIT ;
END; 


/*Update Diploma*/
CREATE OR REPLACE PROCEDURE update_diploma ( id Diploma.noDiploma%TYPE, univ Diploma.university%TYPE ,
diploma Diploma.dip%TYPE, maj Diploma.major%TYPE, min Diploma.minor%TYPE, sec_majmin Diploma.sec_maj_min%TYPE, 
sdate Diploma.start_date%TYPE,gdate Diploma.grad_date%TYPE )
IS
BEGIN 
  UPDATE Diploma 
  SET university=univ,
  dip=diploma,
  major=maj,
  minor=min,
  sec_maj_min=sec_majmin,
  start_date=sdate,
  grad_date=gdate
  WHERE noDiploma=id;
  COMMIT ;
END; 
/

/** insert update delete Career **/

/*INSERT INTO CRAEER*/
CREATE OR REPLACE PROCEDURE insert_career (idc Career.idCareer%TYPE, Stud Career.Stud3%TYPE, sit Career.situation%TYPE,
dom Career.domain%TYPE, hir_date Career.hiring_date%TYPE, leav_date Career.leaving_date%TYPE,
cit Career.city%TYPE, sal Career.salary%TYPE, sMean Career.searchMean%TYPE)

IS
BEGIN 
  INSERT INTO Career VALUES ( idc, Stud , sit ,dom , hir_date , leav_date , cit , sal , sMean ) ;
  COMMIT ;
END; 


/*Delete FROM Career*/
CREATE OR REPLACE PROCEDURE delete_career ( id Career.idCareer%TYPE )

IS
BEGIN 
  DELETE FROM Career WHERE idCareer=id;
  COMMIT ;
END; 



/*Update Career*/
CREATE OR REPLACE PROCEDURE update_career ( id Career.idCareer%TYPE ,sit Career.situation%TYPE,
dom Career.domain%TYPE, hir_date Career.hiring_date%TYPE, leav_date Career.leaving_date%TYPE,
cit Career.city%TYPE, sal Career.salary%TYPE, sMean Career.searchMean%TYPE)

IS
BEGIN 
  UPDATE Career 
  SET situation=sit,
  domain=dom,
  hiring_date=hir_date,
  leaving_date=leav_date,
  city=cit,
  salary=sal,
  searchMean=sMean
  WHERE idCareer=id;
  COMMIT ;
END; 

/** insert update delete internship **/
/*INSERT INTO INTERNSHIP*/
CREATE OR REPLACE PROCEDURE insert_internship (idi Internship.idInternship%TYPE,
Stud Internship.Stud2%TYPE,
num Internship.num_int%TYPE,
host_org internship.host_organization%TYPE,
per Internship.period%TYPE)

IS
BEGIN 
  INSERT INTO Internship VALUES (idi, Stud ,num, host_org,per) ;
  COMMIT ;
END; 




/*Delete FROM Internship*/
CREATE OR REPLACE PROCEDURE delete_internship ( id Internship.idInternship%TYPE )

IS
BEGIN 
  DELETE FROM Internship WHERE idInternship=id;
  COMMIT ;
END; 


/*Update Internship*/
CREATE OR REPLACE PROCEDURE update_internship ( id Internship.idInternship%TYPE,num Internship.num_int%TYPE,
host_org internship.host_organization%TYPE,
per Internship.period%TYPE )

IS
BEGIN 
  UPDATE Internship
  SET num_int=num,
  host_organization=host_org,
  period=per
  WHERE idInternship=id;
  COMMIT ;
END; 
