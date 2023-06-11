/**Average time students wait before graduation**/

CREATE OR REPLACE FUNCTION avg_waiting_time( I NUMBER)
RETURN FLOAT
IS 
Waiting FLOAT;
BEGIN
Select  AVG(round((hiring_date-grad_date)/30))
INTO Waiting
FROM Student, Diploma, Career
WHERE Student.noStudent=Diploma.stud1 AND Student.noStudent=Career.stud3 AND  hiring_date IS NOT NULL;
RETURN Waiting;
END avg_waiting_time;

/**NUMBER of STUDENTS HIRED EVEN BEFORE GRADUATION**/

CREATE OR REPLACE FUNCTION hired_before_graduation( I NUMBER)
RETURN FLOAT
IS 
num NUMBER;
BEGIN
Select  COUNT(noStudent)
INTO num
FROM Student, Diploma, Career
WHERE Student.noStudent=Diploma.stud1 AND Student.noStudent=Career.stud3  AND hiring_date IS NOT NULL AND round((hiring_date-grad_date)/30)<0;
RETURN num;
END hired_before_graduation;


/**Master Students**/

CREATE OR REPLACE FUNCTION Master_students( I NUMBER)
RETURN FLOAT
IS 
mnum NUMBER;
allnum NUMBER;
perc Float;
BEGIN

Select  COUNT(Stud3)
INTO mnum
FROM  Career
WHERE situation='Master Student';


Select  COUNT(noStudent)
INTO allnum
FROM  Student;

perc:=round((mnum/allnum)*100);

RETURN perc;
END Master_students;


/**Master Students In TBS**/

CREATE OR REPLACE FUNCTION Master_students_tbs( I NUMBER)
RETURN FLOAT
IS 
mnumt NUMBER;
allnum NUMBER;
perc NUMBER;
BEGIN

Select  COUNT(Stud3)
INTO allnum
FROM  Career
WHERE situation='Master Student';


Select  COUNT(IDcareer)
INTO mnumt
FROM  Career 
WHERE city='TBS'  OR city='Tunis Business School' OR city='Ben Arous' AND situation='Master Student';

perc:=round((mnumt/allnum)*100);

RETURN perc;
END Master_students_tbs;

/**Master Students In Tunisia But not in TBS**/

CREATE OR REPLACE FUNCTION Master_students_tun( I NUMBER)
RETURN FLOAT
IS 
mnumt NUMBER;
allnum NUMBER;
perc NUMBER;
BEGIN

Select  COUNT(Stud3)
INTO allnum
FROM  Career
WHERE situation='Master Student';


Select  COUNT(IDcareer)
INTO mnumt
FROM  Career 
WHERE (city LIKE '%Carthage%' OR city LIKE '%tunis%' OR city LIKE '%tunisia%') AND city IS NOT NULL AND situation='Master Student';

perc:=round((mnumt/allnum)*100);

RETURN perc;
END Master_students_tun;




/**Master Students Abroad**/

CREATE OR REPLACE FUNCTION Master_students_abroad( I NUMBER)
RETURN FLOAT
IS 
mnumt NUMBER;
allnum NUMBER;
perc NUMBER;
BEGIN

Select  COUNT(Stud3)
INTO allnum
FROM  Career
WHERE situation='Master Student';


Select  COUNT(IDcareer)
INTO mnumt
FROM  Career 
WHERE city NOT IN ('Tunis', 'tunisia', 'Ben Arous','Ariana','ISG Tunis','TBS','Tunis Business School','Ihec Carthage','Carthage', 'Manouba','hay el ghazela' ) AND city NOT LIKE '%tunisia%' AND city IS NOT NULL AND
situation='Master Student';

perc:=round((mnumt/allnum)*100);

RETURN perc;
END Master_students_abroad;


/**Number of business Owners**/

CREATE OR REPLACE FUNCTION Business_owners( I NUMBER)
RETURN FLOAT
IS 
num NUMBER;

BEGIN

Select  COUNT(IDcareer)
INTO num
FROM  Career 
WHERE situation='Business Owner';

RETURN num;
END Business_owners;


/**Number of students working and studying**/

CREATE OR REPLACE FUNCTION Working_and_studying( I NUMBER)
RETURN FLOAT
IS 
num float;

BEGIN

Select  COUNT(IDcareer)
INTO num
FROM  Career 
WHERE (situation='Master Student' AND hiring_date IS NOT NULL) OR situation='Alternate' OR situation='Part time employee';

RETURN num;
END working_and_studying;



/**Spending more than 4 years in TBS**/
CREATE OR REPLACE FUNCTION late_grad( I NUMBER)
RETURN float
IS 
num NUMBER;

BEGIN

Select  Count(Stud1)
INTO num
FROM  Diploma
WHERE round((grad_date-start_date)/365)>4;
RETURN num;
END late_grad;


/**Jobs**/
/* Average hired students*/
CREATE OR REPLACE FUNCTION AVG_hired_student(I NUMBER)
RETURN FLOAT
IS
totnumber NUMBER;
tothired NUMBER;
work_perc FLOAT:=0; 
BEGIN
Select count(stud3) into tothired FROM career WHERE situation='Employee' OR hiring_date IS NOT NULL;
SELECT COUNT(NOSTUDENT) INTO totnumber FROM STUDENT;
work_perc:= (tothired/totnumber)*100;
RETURN work_perc;
END AVG_hired_student;