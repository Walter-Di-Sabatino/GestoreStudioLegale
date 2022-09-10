from __future__ import print_function

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea
import pickle
import os

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools

class VistaVisualizzaAppuntamento(QMainWindow):
    appuntamentiList = []
    clientiList = []
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaVisualizzaAppuntamento, self).__init__(parent)
        self.scroll = QScrollArea()
        self.widget = QWidget()
        grifLayout = QGridLayout()
        grifLayout.addWidget(self.tool.rewindButton(self.rewindHomeCliente), 0, 0)
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista degli appuntamenti con le informazioni relative al cliente")
        textLabel1.setGeometry(QRect(0, 0, 200, 150))
        textLabel1.setFont(QFont('Arial', 10))
        textLabel2.setText(
            'Cliente: ' + '\n' + 'NOME: ' + f"{self.getDatiC()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.getDatiC()['Cognome']}" + '\n' + 'ID: ' + f"{self.getDatiC()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.getDatiC()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.getDatiC()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Arial', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        textLabel3 = QLabel()
        textLabel3.setText(
            'Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiA()['Tipo Procedimento']}"+'\n'+'ID: '+f"{self.getDatiA()['ID']}"+'\n'+'DATA E ORA INIZIO: '+f"{self.getDatiA()['Data e Ora Inizio']}"+'\n'+'DATA E ORA FINE'+f"{self.getDatiA()['Data e Ora Fine']}")
        textLabel3.setGeometry(QRect(0, 0, 350, 20))
        textLabel3.setFont(QFont('Arial', 10))
        '''textLabel2.setText('Cliente: '+'\n'+ 'NOME: '+f"{self.getDatiC()['Nome']}"+ '\n'+'COGNOME: '+f"{self.getDatiC()['Cognome']}"+'\n'+'ID: '+f"{self.getDatiC()['Id']}"+'\n'+'CODICE FISCALE: '+f"{self.getDatiC()['Codice fiscale']}"+'\n'+'EMAIL: '+f"{self.getDatiC()['Email']}"+'\n'+'NUMERO TELEFONO: '+f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Times', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        textLabel3 = QLabel()
        textLabel3.setText('Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiA()['Tipo Procedimento']}"+'\n'+'ID: '+f"{self.getDatiA()['ID']}")
        textLabel3.setGeometry(QRect(0, 0, 350, 20))
        textLabel3.setFont(QFont('Arial', 10))'''
        textLabel3.setStyleSheet("border: 1px solid black;")
        grifLayout.addWidget(textLabel2, 1, 1)
        grifLayout.addWidget(textLabel1, 2, 1)
        grifLayout.addWidget(textLabel3, 3, 1)
        #self.setLayout(grifLayout)
        self.widget.setLayout(grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Appuntamenti")
        self.show()

    def getDatiA(self):
        self.appuntamentiList = self.tool.loadAppuntamenti()
        for appuntamento in self.appuntamentiList:
            if appuntamento.Cliente.codiceFiscale == str(self.tool.leggi()).rsplit()[0]:
                return appuntamento.getDatiAppuntamento()


    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(self.tool.leggi(n=0)).rsplit()[0]:
                return cliente.getDatiCliente()

    def rewindHomeCliente(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
        self.vistaHome = VistaHomeAppuntamentiC()
        self.vistaHome.show()
        self.close()

    def getNum(self):
        n = 0
        self.appuntamentiList = self.tool.loadAppuntamenti()
        for appuntamento in self.appuntamentiList:
            n+=1
        return n