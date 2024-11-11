

# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:11:57 2022

@author: user
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector
from mysql.connector import errorcode

class MainWindow (QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('MSEUFVaccinationRecords.ui', self)


        self.AddInfo.triggered.connect(self.show_addinfo)
        self.AddVax.triggered.connect(self.show_addvax)
        self.AddExp.triggered.connect(self.show_addexp)
        self.StudentsInfo.triggered.connect(self.show_info)
        self.VaxRec.triggered.connect(self.show_vax)
        self.StudentsExp.triggered.connect(self.show_exp)

    def show_addinfo(self):
        pdialog = AddInfo()
        pdialog.exec()

    def show_addvax(self):
        pdialog2 = AddVax()
        pdialog2.exec()
        
    def show_addexp(self):
        pdialog3 = AddExp()
        pdialog3.exec()
        
    def show_info(self):
        pdialog4 = StudentsInfo()
        pdialog4.exec()
        
    def show_vax(self):
        pdialog5 = VaxRec()
        pdialog5.exec()
        
    def show_exp(self):
        pdialog6 = StudentsExp()
        pdialog6.exec()


class StudentsInfo (QDialog):
    

    def __init__(self):
        super(StudentsInfo,self).__init__()
        loadUi('StudentsInfo.ui',self)

        self.tableInfo.setHorizontalHeaderLabels(["Student ID", "Department", "Course", "Yeal Level"])
        
        cnx = mysql.connector.connect(user="root", password="Frinces010123", host="localhost", database="studentsrecord")
        query = "Select * From tblInfo Order by Department"
        cursor = cnx.cursor()
        cursor.execute(query)

        for row in cursor:
            rowPosition = self.tableInfo.rowCount()
            self.tableInfo.insertRow(rowPosition)
            self.tableInfo.setItem(rowPosition, 0, QTableWidgetItem(row[0]))
            self.tableInfo.setItem(rowPosition, 1, QTableWidgetItem(row[1]))
            self.tableInfo.setItem(rowPosition, 2, QTableWidgetItem(row[2]))
            self.tableInfo.setItem(rowPosition, 3, QTableWidgetItem(row[3]))
        cnx.close ()

class VaxRec (QDialog):

    def __init__(self):
        super(VaxRec,self).__init__()
        loadUi('VaxRec.ui',self)

        self.tableVax.setHorizontalHeaderLabels(["Student ID", "First Vaccine", "Date", "Second Vaccine", "Date", "Booster Status", "Booster", "Date"])
        
        cnx = mysql.connector.connect(user="root", password="Frinces010123", host="localhost", database="studentsrecord")
        query = "Select * From tblVax"
        cursor = cnx.cursor()
        cursor.execute(query)

        for row in cursor:
            rowPosition = self.tableVax.rowCount()
            self.tableVax.insertRow(rowPosition)
            self.tableVax.setItem(rowPosition, 0, QTableWidgetItem(row[0]))
            self.tableVax.setItem(rowPosition, 1, QTableWidgetItem(row[1]))
            self.tableVax.setItem(rowPosition, 2, QTableWidgetItem(row[2]))
            self.tableVax.setItem(rowPosition, 3, QTableWidgetItem(row[3]))
            self.tableVax.setItem(rowPosition, 4, QTableWidgetItem(row[4]))
            self.tableVax.setItem(rowPosition, 5, QTableWidgetItem(row[5]))
            self.tableVax.setItem(rowPosition, 6, QTableWidgetItem(row[6]))
            self.tableVax.setItem(rowPosition, 7, QTableWidgetItem(row[7]))
        cnx.close ()

class StudentsExp (QDialog):

    def __init__(self):
        super(StudentsExp,self).__init__()
        loadUi('StudentsExp.ui',self)
 
        self.tableVax.setHorizontalHeaderLabels(["Student ID", "Total Face-To-Face Monthly Expenses", "Total Online Classes Monthly Expenses"])
        
        cnx = mysql.connector.connect(user="root", password="Frinces010123", host="localhost", database="studentsrecord")
        query = "Select * From tblExp"
        cursor = cnx.cursor()
        cursor.execute(query)

        for row in cursor:
            rowPosition = self.tableVax.rowCount()
            self.tableVax.insertRow(rowPosition)
            self.tableVax.setItem(rowPosition, 0, QTableWidgetItem(row[0]))
            self.tableVax.setItem(rowPosition, 1, QTableWidgetItem(row[6]))
            self.tableVax.setItem(rowPosition, 2, QTableWidgetItem(row[9 ]))
        cnx.close ()
        
class AddInfo(QDialog):

    connectconfig = {'user':'root', 'password':'Frinces010123', 'host':'localhost', 'database':'studentsrecord'}
   
    
    def __init__(self):
        super(AddInfo,self).__init__()
        loadUi('AddInfo.ui',self)

        self.fillcombobox()

        self.ButtonSearch.clicked.connect (self.clicksearch)
        self.ButtonAdd.clicked.connect(self.clickadd)
        self.ButtonDelete.clicked.connect(self.clickdelete)
        self.ButtonEdit.clicked.connect(self.clickedit)
        self.cboRecord.currentTextChanged.connect(self.changecbo)
        
    def fillcombobox(self):
        cnx = mysql.connector.connect(**self.connectconfig)
        cursor = cnx.cursor()
        cursor.execute("Select * From tblInfo")
        self.cboRecord.clear()
        self.cboRecord.addItem("- Student ID -")
        for row in cursor:
            self.cboRecord.addItem(row[0])
        
        cursor.close()
        cnx.close()

 
    def clicksearch(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.tbID.text ()

            cursor.execute("Select * From tblInfo Where StudentID = '%s'" % StudentID)
            row = cursor.fetchone()
            if row is not None:
                self.tbDept.setText(row[1])
                self.tbCourse.setText(row[2])
                self.tbLevel.setText(row[3])
            else:
                self.tbDept.setText("")
                self.tbCourse.setText("")
                self.tbLevel.setText("")
                QMessageBox.about(self, "Record", "Record Not Found")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()


    def changecbo(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.cboRecord.currentText()

            cursor.execute("Select * From tblInfo Where StudentID = '%s'" % StudentID)
            row = cursor.fetchone()
            self.tbID.setText(row[0])
            self.tbDept.setText(row[1])
            self.tbCourse.setText(row[2])
            self.tbLevel.setText(row[3])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()

 
    def clickadd(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.tbID.text()
            Department = self.tbDept.text()
            Course = self.tbCourse.text()
            YearLevel = self.tbLevel.text()

            cursor.execute("Insert Into tblInfo Values ('%s', '%s', '%s', '%s')" % (StudentID, Department, Course, YearLevel))
            cnx.commit()
         
            
            self.fillcombobox()

            self.tbID.setText("")
            self.tbDept.setText("")
            self.tbCourse.setText("")
            self.tbLevel.setText("")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()
            

   
    def clickdelete(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            reply = QMessageBox.question(self, "Delete", "Do you want to delete this record?")

            if reply == QMessageBox.StandardButton.Yes:
                cursor = cnx.cursor()
                StudentID = self.tbID.text()
                cursor.execute("Delete From tblInfo Where StudentID = '%s'" % StudentID)
                cnx.commit()

                self.tbID.setText("")
                self.tbDept.setText("")
                self.tbCourse.setText("")
                self.tbLevel.setText("")
                
                self.fillcombobox()
                
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
           cursor.close()
           cnx.close()


    def clickedit(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            reply = QMessageBox.question(self, "Edit", "Do you want to edit this record?")

            if reply == QMessageBox.StandardButton.Yes:
                cursor = cnx.cursor()
                StudentID = self.tbID.text()
                Department = self.tbDept.text()
                Course = self.tbCourse.text()
                YearLevel = self.tbLevel.text()
                sql = "Update tblInfo Set Department = '%s', Course = '%s', YearLevel = '%s' Where StudentID = '%s'" % (Department, Course, YearLevel, StudentID)
                cursor.execute(sql)
                cnx.commit()

                self.tbID.setText("")
                self.tbDept.setText("")
                self.tbCourse.setText("")
                self.tbLevel.setText("")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(err)
        else:
            cursor.close()
            cnx.close()

class AddVax(QDialog):

    connectconfig = {'user':'root', 'password':'Frinces010123', 'host':'localhost', 'database':'studentsrecord'}
   
    
    def __init__(self):
        super(AddVax,self).__init__()
        loadUi('AddVax.ui',self)

        self.fillcombobox()

        self.ButtonSearch.clicked.connect (self.clicksearch)
        self.ButtonAdd.clicked.connect(self.clickadd)
        self.ButtonDelete.clicked.connect(self.clickdelete)
        self.ButtonEdit.clicked.connect(self.clickedit)
        self.cboRecord.currentTextChanged.connect(self.changecbo)
        
    def fillcombobox(self):
        cnx = mysql.connector.connect(**self.connectconfig)
        cursor = cnx.cursor()
        cursor.execute("Select * From tblVax")
        self.cboRecord.clear()
        self.cboRecord.addItem("- Student ID -")
        for row in cursor:
            self.cboRecord.addItem(row[0])
        
        cursor.close()
        cnx.close()

 
    def clicksearch(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.tbID.text ()

            cursor.execute("Select * From tblVax Where StudentID = '%s'" % StudentID)
            row = cursor.fetchone()
            if row is not None:
                self.tbFirst.setText(row[1])
                self.tbDate1.setText(row[2])
                self.tbSecond.setText(row[3])
                self.tbDate2.setText(row[4])
                self.tbBooster.setText(row[6])
                self.tbDate3.setText(row[7])
            else:
                self.tbFirst.setText("")
                self.tbDate1.setText("")
                self.tbSecond.setText("")
                self.tbDate2.setText("")
                self.tbBooster.setText("")
                self.tbDate3.setText("")
                QMessageBox.about(self, "Record", "Record Not Found")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()


    def changecbo(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.cboRecord.currentText()

            cursor.execute("Select * From tblVax Where StudentID = '%s'" % StudentID)
            row = cursor.fetchone()
            self.tbID.setText(row[0])
            self.tbFirst.setText(row[1])
            self.tbDate1.setText(row[2])
            self.tbSecond.setText(row[3])
            self.tbDate2.setText(row[4])
            self.tbBooster.setText(row[6])
            self.tbDate3.setText(row[7])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()

 
    def clickadd(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.tbID.text()
            FirstVaccine = self.tbFirst.text()
            FirstDate = self.tbDate1.text()
            SecondVaccine = self.tbSecond.text()
            SecondDate = self.tbDate2.text()
            if self.rbyes.isChecked():
                BoosterStatus = "YES"
            elif self.rbno.isChecked():
                BoosterStatus = "NO"
            Booster = self.tbBooster.text()
            BoosterDate = self.tbDate3.text()

            cursor.execute("Insert Into tblVax Values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (StudentID, FirstVaccine, FirstDate, SecondVaccine, SecondDate, BoosterStatus, Booster, BoosterDate))
            cnx.commit()
         
            
            self.fillcombobox()

            self.tbID.setText("")
            self.tbFirst.setText("")
            self.tbDate1.setText("")
            self.tbSecond.setText("")
            self.tbDate2.setText("")
            self.tbBooster.setText("")
            self.tbDate3.setText("")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()
            

   
    def clickdelete(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            reply = QMessageBox.question(self, "Delete", "Do you want to delete this record?")

            if reply == QMessageBox.StandardButton.Yes:
                cursor = cnx.cursor()
                StudentID = self.tbID.text()
                cursor.execute("Delete From tblVax Where StudentID = '%s'" % StudentID)
                cnx.commit()

                self.tbID.setText("")
                self.tbFirst.setText("")
                self.tbDate1.setText("")
                self.tbSecond.setText("")
                self.tbDate2.setText("")
                self.tbBooster.setText("")
                self.tbDate3.setText("")
                
                self.fillcombobox()
                
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
           cursor.close()
           cnx.close()


    def clickedit(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            reply = QMessageBox.question(self, "Edit", "Do you want to edit this record?")

            if reply == QMessageBox.StandardButton.Yes:
                cursor = cnx.cursor()
                StudentID = self.tbID.text()
                FirstVaccine = self.tbFirst.text()
                FirstDate = self.tbDate1.text()
                SecondVaccine = self.tbSecond.text()
                SecondDate = self.tbDate2.text()
                if self.rbyes.isChecked():
                    BoosterStatus = "YES"
                elif self.rbno.isChecked():
                    BoosterStatus = "NO"
                Booster = self.tbBooster.text()
                BoosterDate = self.tbDate3.text()
                sql = "Update tblVax Set FirstVaccine = '%s', FirstDate = '%s' , SecondVaccine = '%s', SecondDate = '%s', BoosterStatus = '%s', Booster = '%s', BoosterDate = '%s' Where StudentID = '%s'" % (FirstVaccine, FirstDate, SecondVaccine, SecondDate, BoosterStatus, Booster, BoosterDate, StudentID)
                cursor.execute(sql)
                cnx.commit()

                self.tbID.setText("")
                self.tbFirst.setText("")
                self.tbDate1.setText("")
                self.tbSecond.setText("")
                self.tbDate2.setText("")
                self.tbBooster.setText("")
                self.tbDate3.setText("")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(err)
        else:
            cursor.close()
            cnx.close()

class AddExp(QDialog):

    connectconfig = {'user':'root', 'password':'Frinces010123', 'host':'localhost', 'database':'studentsrecord'}
   
    
    def __init__(self):
        super(AddExp,self).__init__()
        loadUi('AddExpenses.ui',self)

        self.fillcombobox()

        self.ButtonSearch.clicked.connect (self.clicksearch)
        self.ButtonAdd.clicked.connect(self.clickadd)
        self.ButtonDelete.clicked.connect(self.clickdelete)
        self.ButtonEdit.clicked.connect(self.clickedit)
        self.ButtonCompute.clicked.connect(self.clickcompute)
        self.cboRecord.currentTextChanged.connect(self.changecbo)
        
    def fillcombobox(self):
        cnx = mysql.connector.connect(**self.connectconfig)
        cursor = cnx.cursor()
        cursor.execute("Select * From tblExp")
        self.cboRecord.clear()
        self.cboRecord.addItem("- Student ID -")
        for row in cursor:
            self.cboRecord.addItem(row[0])
        
        cursor.close()
        cnx.close()

 
    def clicksearch(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.tbID.text ()
            
            cursor.execute("Select * From tblExp Where StudentID = '%s'" % StudentID)
            row = cursor.fetchone()
            if row is not None:
                self.tbTranspo.setText(row[1])
                self.tbMeal.setText(row[2])
                self.tbMasks.setText(row[3])
                self.tbSan.setText(row[4])
                self.tbFS.setText(row[5])
                self.tbTC1.setText(row[6])
                self.tbEB.setText(row[7])
                self.tbIB.setText(row[8])
                self.tbTC2.setText(row[9])
            else:
                self.tbTranspo.setText("")
                self.tbMeal.setText("")
                self.tbMasks.setText("")
                self.tbSan.setText("")
                self.tbFS.setText("")
                self.tbTC1.setText("")
                self.tbEB.setText("")
                self.tbIB.setText("")
                self.tbTC2.setText("")
                QMessageBox.about(self, "Record", "Record Not Found")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()


    def changecbo(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.cboRecord.currentText()

            cursor.execute("Select * From tblExp Where StudentID = '%s'" % StudentID)
            row = cursor.fetchone()
            self.tbID.setText(row[0])
            self.tbTranspo.setText(row[1])
            self.tbMeal.setText(row[2])
            self.tbMasks.setText(row[3])
            self.tbSan.setText(row[4])
            self.tbFS.setText(row[5])
            self.tbTC1.setText(row[6])
            self.tbEB.setText(row[7])
            self.tbIB.setText(row[8])
            self.tbTC2.setText(row[9])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()

 
    def clickadd(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            cursor = cnx.cursor()
            StudentID = self.tbID.text()
            Transportation = int(self.tbTranspo.text())
            Meal = int(self.tbMeal.text())
            Masks = int(self.tbMasks.text())
            Sanitizers = int(self.tbSan.text())
            FaceShields = int(self.tbFS.text())
            ExpF = str((Transportation + Meal + Masks + Sanitizers + FaceShields)*30)
            self.tbTC1.setText(ExpF)
            F2FExpenses = self.tbTC1.text()
            
            ElectricityBill = int(self.tbEB.text())
            InternetBill = int(self.tbIB.text())
            Exp0 = str(ElectricityBill + InternetBill)
            self.tbTC2.setText(Exp0)
            OnlineExpenses = self.tbTC2.text()
            
            cursor.execute("Insert Into tblExp Values ('%s', '%d', '%d', '%d','%d', '%d', '%s', '%d', '%d', '%s')" % (StudentID, Transportation, Meal, Masks, Sanitizers, FaceShields, F2FExpenses, ElectricityBill, InternetBill, OnlineExpenses))
            cnx.commit()
         
            
            self.fillcombobox()

            self.tbID.setText("")
            self.tbTranspo.setText("")
            self.tbMeal.setText("")
            self.tbMasks.setText("")
            self.tbSan.setText("")
            self.tbFS.setText("")
            self.tbTC1.setText("")
            self.tbEB.setText("")
            self.tbIB.setText("")
            self.tbTC2.setText("")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
            cursor.close()
            cnx.close()
            

   
    def clickdelete(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            reply = QMessageBox.question(self, "Delete", "Do you want to delete this record?")

            if reply == QMessageBox.StandardButton.Yes:
                cursor = cnx.cursor()
                StudentID = self.tbID.text()
                cursor.execute("Delete From tblExp Where StudentID = '%s'" % StudentID)
                cnx.commit()

                self.tbID.setText("")
                self.tbTranspo.setText("")
                self.tbMeal.setText("")
                self.tbMasks.setText("")
                self.tbSan.setText("")
                self.tbFS.setText("")
                self.tbTC1.setText("")
                self.tbEB.setText("")
                self.tbIB.setText("")
                self.tbTC2.setText("")
                
                self.fillcombobox()
                
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(str(err))
        else:
           cursor.close()
           cnx.close()


    def clickedit(self):
        try:
            cnx = mysql.connector.connect(**self.connectconfig)
            reply = QMessageBox.question(self, "Edit", "Do you want to edit this record?")

            if reply == QMessageBox.StandardButton.Yes:
                cursor = cnx.cursor()
                StudentID = self.tbID.text()
                Transportation = int(self.tbTranspo.text())
                Meal = int(self.tbMeal.text())
                Masks = int(self.tbMasks.text())
                Sanitizers = int(self.tbSan.text())
                FaceShields = int(self.tbFS.text())
                ExpF = str((Transportation + Meal + Masks + Sanitizers + FaceShields)*30)
                self.tbTC1.setText(ExpF)
                F2FExpenses = self.tbTC1.text()
                
                ElectricityBill = int(self.tbEB.text())
                InternetBill = int(self.tbIB.text())
                Exp0 = str(ElectricityBill + InternetBill)
                self.tbTC2.setText(Exp0)
                OnlineExpenses = self.tbTC2.text()
            
                sql = "Update tblExp Set Transportation = '%d', Meal = '%d', Masks = '%d', Sanitizers = '%d', FaceShields = '%d', F2FExpenses = '%s', ElectricityBill = '%d', InternetBill = '%d', OnlineExpenses = '%s' Where StudentID = '%s'" % (Transportation, Meal, Masks, Sanitizers, FaceShields, F2FExpenses, ElectricityBill, InternetBill, OnlineExpenses, StudentID)
                cursor.execute(sql) 
                cnx.commit()

                self.tbID.setText("")
                self.tbTranspo.setText("")
                self.tbMeal.setText("")
                self.tbMasks.setText("")
                self.tbSan.setText("")
                self.tbFS.setText("")
                self.tbTC1.setText("")
                self.tbEB.setText("")
                self.tbIB.setText("")
                self.tbTC2.setText("")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelStatus.setText("Something is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelStatus.setText("Database does not exist")
            else:
                self.labelStatus.setText(err)
        else:
            cursor.close()
            cnx.close()   
    
    def clickcompute(self):
            Transportation = int(self.tbTranspo.text())
            Meal = int(self.tbMeal.text())
            Masks = int(self.tbMasks.text())
            Sanitizers = int(self.tbSan.text())
            FaceShields = int(self.tbFS.text())
            ExpF = str((Transportation + Meal + Masks + Sanitizers + FaceShields)*30)
            self.tbTC1.setText(ExpF)
            
            ElectricityBill = int(self.tbEB.text())
            InternetBill = int(self.tbIB.text())
            Exp0 = str(ElectricityBill + InternetBill)
            self.tbTC2.setText(Exp0)

            
app = QApplication(sys.argv)
widget = MainWindow()
widget.showMaximized()
sys.exit(app.exec())
