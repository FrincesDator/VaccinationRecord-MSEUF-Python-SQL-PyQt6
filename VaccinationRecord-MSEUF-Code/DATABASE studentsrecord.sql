Create Database studentsrecord;
Use studentsrecord;

# Table 1
Create Table tblInfo (
StudentID varchar (50) not null primary key,
Department varchar (50) not null,
Course varchar (50) not null,
YearLevel varchar (50) not null);

# Table 2
Create Table tblVax (
StudentID varchar (50) not null primary key,
FirstVaccine varchar (50) not null,
FirstDate varchar (50) not null,
SecondVaccine varchar (50) not null,
SecondDate varchar (50) not null,
BoosterStatus varchar (50) not null,
Booster varchar (50) not null,
BoosterDate varchar (50) not null);

Create Table tblExp (
StudentID varchar (50) not null primary key,
Transportation varchar (50) not null,
Meal varchar (50) not null,
Masks varchar (50) not null,
Sanitizers varchar (50) not null,
FaceShields varchar (50) not null,
F2FExpenses varchar (50) not null,
ElectricityBill varchar (50) not null,
InternetBill varchar (50) not null,
OnlineExpenses varchar (50) not null);


Select * From tblInfo;