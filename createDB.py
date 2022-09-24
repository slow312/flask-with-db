import sqlite3

connect = sqlite3.connect('./flask-with-db/patients.db')
db = connect.cursor()

db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            zipcode CHAR(25) NOT NULL, 
            race CHAR(25) NOT NULL, 
            ethnicity CHAR(25) NOT NULL, 
            lengthOfStay CHAR(25) NOT NULL, 
            admissionType CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit()

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, zipcode, race, ethnicity, lengthOfStay,admissionType) values('12345', 'John', 'Smith', '01/01/1989', '10011', 'White', 'Not Hispanic', '4','Emergency')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, zipcode, race, ethnicity, lengthOfStay,admissionType) values('23456', 'Jane', 'Kim', '02/02/2000','10543', 'Asian', 'Not Hispanic', '1','Elective')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, zipcode, race, ethnicity, lengthOfStay,admissionType) values('34567', 'Sophia', 'Castillo', '03/03/2002','10234', 'White', 'Hispanic', '1','Newborn')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, zipcode, race, ethnicity, lengthOfStay,admissionType) values('45678', 'David', 'Smith', '04/04/1995','10678', 'Black', 'Not Hispanic', '2','Urgent')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, zipcode, race, ethnicity, lengthOfStay,admissionType) values('56789', 'Jane', 'Brown', '05/05/2004','10765', 'White', 'Not Hispanic', '2','Urgent')")

connect.commit()

connect.close()

