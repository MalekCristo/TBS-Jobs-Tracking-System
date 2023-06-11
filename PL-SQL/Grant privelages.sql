/**Create A DBA admin**/
CREATE USER admin IDENTIFIED BY SYSTEM;
GRANT CONNECT, RESOURCE, DBA TO admin;

/*Create Student user**/
CREATE USER STUDENT IDENTIFIED BY SYSTEM;
/**Grant only select update delete on Student**/
GRANT
 SELECT,
 INSERT,
 UPDATE,
 DELETE
ON
 Student
TO
 STUDENT
/**Grant only select update delete on Diploma**/
GRANT
 SELECT,
 INSERT,
 UPDATE,
 DELETE
ON
 Diploma
TO
 STUDENT

/**Grant only select update delete on Career**/
GRANT
 SELECT,
 INSERT,
 UPDATE,
 DELETE
ON
 Career
TO
 STUDENT


/**Grant only select update delete on Internship**/
GRANT
 SELECT,
 INSERT,
 UPDATE,
 DELETE
ON
 Internship
TO
 STUDENT
