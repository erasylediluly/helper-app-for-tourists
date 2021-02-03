from __future__ import print_function
import sys 
import os 
import cx_Oracle
import time
from PyQt5 import QtWidgets,QtGui,QtSvg
from PyQt5.QtGui import QPixmap,QColor
from PyQt5.QtWidgets import *
import mainWindowDesign
import secondWindowDesign
import placesWindowDesign
import routesWindowDesign
import newRouteWindowDesign1
import newRouteWindowDesign2
from sys import maxsize 
from itertools import permutations
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

class MainWindow(QtWidgets.QMainWindow, mainWindowDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onClickBtn)
        self.secondWindow = SecondWindow()
        pixmap = QPixmap('..\\Images\\verynice.jpg')
        self.label_2.setPixmap(pixmap)
        self.label_2.resize(pixmap.width(), pixmap.height())
        self.label_2.setScaledContents(True)
        pixmap2 = QPixmap('..\\QT\\svg\\svg1.svg')
        self.label_4.setPixmap(pixmap2)
        self.label_4.setScaledContents(True)
        pixmap3 = QPixmap('..\\QT\\svg\\svg2.svg')
        self.label_5.setPixmap(pixmap3)
        self.label_5.setScaledContents(True)
        shadow = QGraphicsDropShadowEffect() 
        shadow.setBlurRadius(200)
        self.pushButton.setGraphicsEffect(shadow) 
    def onClickBtn(self):
        self.close()
        self.secondWindow.show() 
class SecondWindow(QtWidgets.QMainWindow, secondWindowDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onClickBtn)
        self.pushButton_2.clicked.connect(self.onClickBtn2)
        self.pushButton_3.clicked.connect(self.onClickBtn3)
        self.placesWindow = PlacesWindow()
        self.routesWindow = RoutesWindow()
        self.newRouteWindow1 = newRouteWindow1()
        pixmap3 = QPixmap('..\\QT\\svg\\svg3.svg')
        self.label.setPixmap(pixmap3)
        self.label.setScaledContents(True)
        shadow = QGraphicsDropShadowEffect() 
        shadow.setBlurRadius(200)
        shadow.setColor(QColor("2C335C"))
        self.pushButton.setGraphicsEffect(shadow) 
        shadow2 = QGraphicsDropShadowEffect() 
        shadow2.setBlurRadius(200)
        shadow2.setColor(QColor("2C335C"))
        self.pushButton_2.setGraphicsEffect(shadow2) 
        shadow3 = QGraphicsDropShadowEffect() 
        shadow3.setBlurRadius(200)
        shadow3.setColor(QColor("2C335C"))
        self.pushButton_3.setGraphicsEffect(shadow3) 
        pixmap = QPixmap('..\\QT\\svg\\svg4.svg')
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        pixmap2 = QPixmap('..\\QT\\svg\\svg5.svg')
        self.label_3.setPixmap(pixmap2)
        self.label_3.setScaledContents(True)
        pixmap3 = QPixmap('..\\QT\\svg\\svg6.svg')
        self.label_4.setPixmap(pixmap3)
        self.label_4.setScaledContents(True)
        shadow4 = QGraphicsDropShadowEffect() 
        shadow4.setColor(QColor("#009998"))
        shadow4.setBlurRadius(20)
        shadow4.setOffset(0,0)
        self.pushButton_4.setGraphicsEffect(shadow4) 
        shadow5 = QGraphicsDropShadowEffect() 
        shadow5.setColor(QColor("#009998"))
        shadow5.setBlurRadius(20)
        shadow5.setOffset(0,0)
        self.pushButton_5.setGraphicsEffect(shadow5) 
        shadow6 = QGraphicsDropShadowEffect() 
        shadow6.setColor(QColor("#009998"))
        shadow6.setBlurRadius(20)
        shadow6.setOffset(0,0)
        self.pushButton_6.setGraphicsEffect(shadow6) 
    def onClickBtn(self):
        self.placesWindow.show() 
    def onClickBtn2(self):
        self.routesWindow = RoutesWindow()
        self.routesWindow.show()
    def onClickBtn3(self):
        self.newRouteWindow1.show()
class PlacesWindow(QtWidgets.QMainWindow, placesWindowDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setTypesComboBox()
        self.setRegionsComboBox()
        self.setElementsListWidget()
        self.comboBox.activated.connect(self.eventListenerFilter)
        self.comboBox_2.activated.connect(self.eventListenerFilter)
        self.textEdit.textChanged.connect(self.eventListenerFilter)
        self.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        pixmap = QPixmap('..\\QT\\svg\\svg7.svg')
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)
        pixmap2 = QPixmap('..\\QT\\svg\\svg8.svg')
        self.label_11.setPixmap(pixmap2)
        self.label_11.setScaledContents(True)
    def selectionChanged(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        c.execute("SELECT name,region,type,details,image FROM TABLE(detailedInfo.getInfo(" + self.listWidget.currentItem().text()[:2]+"))")
        output = c.fetchall()
        self.label.setText(output[0][0])
        self.label_2.setText(output[0][1].strip())
        self.label_3.setText(output[0][3])
        self.label_4.setText(output[0][2])
        self.label_3.setWordWrap(True )
        qimg = QtGui.QImage.fromData(output[0][4].read())
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.label_12.setPixmap(pixmap)
        self.label_12.setScaledContents(True)
        c.close()
        connection.commit()
    def eventListenerFilter(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT i,name FROM table(filterPlaces.filterPlacesByTypeRegionName(\'"+
        self.comboBox.currentText() + "\',\'"+ self.comboBox_2.currentText()+"\',\'"+self.textEdit.toPlainText()+"\'))")
        self.listWidget.clear()
        for i in items:
            item = QListWidgetItem(str(i[0]) + ". " + i[1])
            self.listWidget.addItem(item) 
        c.close()
        connection.commit()
    def setElementsListWidget(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT ID,Name FROM place")
        for i in items:
            item = QListWidgetItem(str(i[0]) + ". " + i[1])
            self.listWidget.addItem(item) 
        c.close()
        connection.commit()
    def setTypesComboBox(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor() 
        items = c.execute("SELECT DISTINCT type FROM place")
        self.comboBox.addItem("")
        for i in items:
            self.comboBox.addItem(i[0])
        c.close()
        connection.commit()
    def setRegionsComboBox(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT DISTINCT region.name FROM place INNER JOIN region ON region.ID = place.regionID")
        self.comboBox_2.addItem("")
        for i in items:
            self.comboBox_2.addItem(i[0])
        c.close()
        connection.commit()
class RoutesWindow(QtWidgets.QMainWindow, routesWindowDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setElementsListWidget()
        shadow = QGraphicsDropShadowEffect() 
        shadow.setBlurRadius(50)
        shadow.setOffset(0,0)
        shadow.setColor(QColor("#000000"))
        self.listWidget.setGraphicsEffect(shadow) 
        pixmap = QPixmap('..\\QT\\svg\\svg9.svg')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        pixmap2 = QPixmap('..\\QT\\svg\\svg10.svg')
        self.label_3.setPixmap(pixmap2)
        self.label_3.setScaledContents(True)
    def setElementsListWidget(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT places FROM routes")
        for i in items:
            item = QListWidgetItem(str(i[0]))
            self.listWidget.addItem(item) 
        c.close()
        connection.commit()
class newRouteWindow1(QtWidgets.QMainWindow, newRouteWindowDesign1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFuelComboBox()
        self.setCitiesComboBox()
        self.setTypesComboBox()
        self.setRegionsComboBox()
        self.setElementsListWidget()
        self.comboBox.activated.connect(self.eventListenerFilter)
        self.comboBox_2.activated.connect(self.eventListenerFilter)
        self.textEdit.textChanged.connect(self.eventListenerFilter)
        self.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        self.pushButton_2.clicked.connect(self.onClickBtn_2)
        self.pushButton.clicked.connect(self.onClickBtn)
        self.pushButton_3.clicked.connect(self.onClickBtn_3)
        pixmap = QPixmap('..\\QT\\svg\\svg11.svg')
        self.label_6.setPixmap(pixmap)
        self.label_6.setScaledContents(True)
        pixmap2 = QPixmap('..\\QT\\svg\\svg12.svg')
        self.label_8.setPixmap(pixmap2)
        self.label_8.setScaledContents(True)
        shadow = QGraphicsDropShadowEffect() 
        shadow.setBlurRadius(20)
        shadow.setOffset(0,0)
        self.pushButton.setGraphicsEffect(shadow) 
        shadow2 = QGraphicsDropShadowEffect() 
        shadow2.setBlurRadius(20)
        shadow2.setOffset(0,0)
        self.pushButton_2.setGraphicsEffect(shadow2)
        shadow3 = QGraphicsDropShadowEffect() 
        shadow3.setBlurRadius(20)
        shadow3.setOffset(0,0)
        self.pushButton_3.setGraphicsEffect(shadow3)
        self.error_dialog = QtWidgets.QErrorMessage()
    def onClickBtn_2(self):
        try:
            self.newRouteWindow2 = newRouteWindow2([str(self.listWidget_2.item(i).text()[:2]) for i in range(self.listWidget_2.count())],self.textEdit_2.toPlainText()
            ,self.comboBox_3.currentText(),self.comboBox_4.currentText())
        except:
            print(",,,,,,,,,,,,,,,,,")
            self.error_dialog.showMessage('Fuel can not be negative number')
            return
        self.newRouteWindow2.show()
    def onClickBtn_3(self):
        self.listWidget_2.takeItem(self.listWidget_2.currentRow())
    def onClickBtn(self):
        for i in range(self.listWidget_2.count()):
            if(self.listWidget_2.item(i).text() == self.listWidget.currentItem().text()):
                self.statusBar().showMessage("Место уже добавлено в вашу корзину", 5000)
                return
        item = QListWidgetItem(self.listWidget.currentItem().text())
        self.listWidget_2.addItem(item) 
    def selectionChanged(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        c.execute("SELECT name,region,type,image FROM TABLE(detailedInfo.getInfo(" + self.listWidget.currentItem().text()[:2]+"))")
        output = c.fetchall()
        self.label_12.setText(output[0][0])
        self.label_13.setText(output[0][1].strip())
        self.label_14.setText(output[0][2])
        qimg = QtGui.QImage.fromData(output[0][3].read())
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.label_15.setPixmap(pixmap)
        self.label_15.setScaledContents(True)
        c.close()
        connection.commit()
    def eventListenerFilter(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT i,name FROM table(filterPlaces.filterPlacesByTypeRegionName(\'"+
        self.comboBox.currentText() + "\',\'"+ self.comboBox_2.currentText()+"\',\'"+self.textEdit.toPlainText()+"\'))")
        self.listWidget.clear()
        for i in items:
            item = QListWidgetItem(str(i[0]) + ". " + i[1])
            self.listWidget.addItem(item) 
        c.close()
        connection.commit()
    def setElementsListWidget(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT ID,Name FROM place")
        for i in items:
            item = QListWidgetItem(str(i[0]) + ". " + i[1])
            self.listWidget.addItem(item) 
        c.close()
        connection.commit()
    def setFuelComboBox(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor() 
        items = c.execute("SELECT name FROM table(comboBoxItems.getFuel())")
        self.comboBox_3.addItem("")
        for i in items:
            self.comboBox_3.addItem(i[0])
        c.close()
        connection.commit()
    def setCitiesComboBox(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT name FROM table(comboBoxItems.getCities())")
        self.comboBox_4.addItem("")
        for i in items:
            self.comboBox_4.addItem(i[0])
        c.close()
        connection.commit()
    def setTypesComboBox(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor() 
        items = c.execute("SELECT DISTINCT type FROM place")
        self.comboBox.addItem("")
        for i in items:
            self.comboBox.addItem(i[0])
        c.close()
        connection.commit()
    def setRegionsComboBox(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        items = c.execute("SELECT DISTINCT region.name FROM place INNER JOIN region ON region.ID = place.regionID")
        self.comboBox_2.addItem("")
        for i in items:
            self.comboBox_2.addItem(i[0])
        c.close()
        connection.commit()
class newRouteWindow2(QtWidgets.QMainWindow, newRouteWindowDesign2.Ui_MainWindow):
    def __init__(self,places,consumption,fuel,departureCity):
        super().__init__()
        self.setupUi(self)
        self.places=[]
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        r = c.execute("SELECT id FROM place WHERE name=\'{}\'".format(departureCity))
        self.places.append(str(r.fetchall()[0][0]))
        for i in places:
            self.places.append(i)
        self.consumption = consumption
        self.fuel = fuel
        self.total_expenses=0
        self.departureCity = departureCity
        self.route = self.getOptimalRoute()
        self.insertRoute()
        pixmap = QPixmap('..\\QT\\svg\\svg13.svg')
        self.label_4.setPixmap(pixmap)
        self.label_4.setScaledContents(True)
        pixmap2 = QPixmap('..\\QT\\svg\\svg14.svg')
        self.label_5.setPixmap(pixmap2)
        self.label_5.setScaledContents(True)
        shadow = QGraphicsDropShadowEffect() 
        shadow.setBlurRadius(20)
        shadow.setOffset(0,0)
        self.listWidget.setGraphicsEffect(shadow)
        c.close()
        connection.commit()
    def getOptimalRoute(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        distances = []
        for i in self.places:
            temp = []
            for j in self.places:
                r = c.execute("SELECT distance FROM distances WHERE (placeID1={} AND placeID2={}) OR (placeID2={} AND placeID1={})".format(
                    int(''.join(e for e in i if e.isalnum())),int(''.join(e for e in j if e.isalnum())),
                    int(''.join(e for e in i if e.isalnum())),int(''.join(e for e in j if e.isalnum()))
                ))
                distance = r.fetchall()
                if(len(distance) == 0):
                    temp.append(0)
                else:
                    temp.append(distance[0][0])
            distances.append(temp)
        data = create_data_model(distances)
        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),data['num_vehicles'], data['depot'])
        routing = pywrapcp.RoutingModel(manager)
        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]
        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        solution = routing.SolveWithParameters(search_parameters)
        self.places_names = []
        print(self.places)
        if solution:
            print(solution.ObjectiveValue())
            places,self.distance = print_solution(manager, routing, solution)
            print(places)
            for i in places:
                r = c.execute("SELECT name FROM place WHERE ID = {}".format(self.places[i]))
                self.places_names.append(r.fetchall()[0][0])
            for i in self.places_names:
                item = QListWidgetItem(str(i))
                self.listWidget.addItem(item) 
            self.textEdit.setText(str(self.distance))
            self.calculateExpenses(self.distance)
        c.close()
        connection.commit()
    def calculateExpenses(self,distance):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        r = c.execute("SELECT price FROM fuel WHERE name = \'{}\'".format(self.fuel))
        price = r.fetchall()[0][0]
        c.close()
        connection.commit()
        self.textEdit_2.setText(str(distance/100*int(self.consumption)*price))
    def insertRoute(self):
        connection = cx_Oracle.connect("SYSTEM/password@localhost:1521/xe")
        c = connection.cursor()
        places = ""
        for i in self.places_names:
            places += str(i) + "$"
        places = places[:-1]
        self.total_expenses = self.textEdit_2.toPlainText()
        c.execute(
        "DECLARE places VARCHAR2(3000) := \'{}\'; distance NUMBER := {}; consumption NUMBER := {};total_expenses NUMBER := {};fuel VARCHAR2(50) := \'{}\'; plsql_block VARCHAR2(3500); BEGIN plsql_block := \'BEGIN INSERT INTO routes VALUES(:places, :distance, :consumption, :total_expenses, :fuel);END;\'; EXECUTE IMMEDIATE plsql_block USING places, distance, consumption, total_expenses, fuel;COMMIT; EXCEPTION WHEN others THEN ROLLBACK; END;".format(places,int(self.distance),int(self.consumption),int(float(self.total_expenses)),self.fuel))
        r = c.execute("SELECT * FROM routes WHERE places = \'{}\'".format(places))
        if(len(r.fetchall()) == 0):
            raise Exception("")
        c.close()
        connection.commit()
def create_data_model(distance_matrix):
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data
def print_solution(manager, routing, solution):
    plan_output=""
    plan_output+='Длина пути: {} километров\n'.format(solution.ObjectiveValue())
    index = routing.Start(0)
    route_distance = 0
    places = []
    while not routing.IsEnd(index):
        plan_output += ' {} $'.format(manager.IndexToNode(index))
        places.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    places.append(manager.IndexToNode(index))
    return places,solution.ObjectiveValue()
def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    app.exec_() 
if __name__ == '__main__': 
    main() 