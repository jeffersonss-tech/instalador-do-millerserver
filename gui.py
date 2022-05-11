import os
import sys
from cProfile import label


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QToolTip)


def index():

    os.system('postgresql-9.6.12-2-windows.exe --unattendedmodeui minimal --mode unattended --superpassword "123" --servicename "postgreSQL" --servicepassword "123" --serverport 5432')


class janela (QMainWindow):
    def __init__(self):
        super().  __init__()
        
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600 
        self.titulo = 'primeira janela'
        
        self.botaoInstar = QPushButton('instalar', self)
        self.botaoInstar.move(100, 250)
        self.botaoInstar.resize(200, 100)
        self.botaoInstar.setStyleSheet('QPushButton {background-color:#0049fa; font:bold; font-size:30px}')
        
        self.botaoImportarBanco = QPushButton('importar\n banco', self)
        self.botaoImportarBanco.move(400, 250)
        self.botaoImportarBanco.resize(200, 100)
        self.botaoImportarBanco.setStyleSheet('QPushButton {background-color:#0049fa; font:bold; font-size:30px}')
        
        
        botaoSair = QPushButton('sair', self)
        botaoSair.move(50, 50)
        botaoSair.resize(50, 24)
        botaoSair.setStyleSheet('QPushButton {background-color:#ff0000; font:bold; font-size:15px}')
        
        self.botaoInstar.clicked.connect(self.botaoInstarClick)
        self.botaoImportarBanco.clicked.connect(self.botaoImportarBancoClick)
        botaoSair.clicked.connect(self.botaoSairClick)
        
        self.textoTitulo = QLabel(self)
        self.textoTitulo.setText('INSTALADOR MILLER SERVER')
        self.textoTitulo.move(250, 60)
        self.textoTitulo.setStyleSheet('QLabel {font:bold;font-size:24px;color:#59595a}')
        self.textoTitulo.resize(390, 25)
        
        self.textoClick = QLabel(self)
        self.textoClick.move(250, 150)
        self.textoClick.setStyleSheet('QLabel {font:bold;font-size:24px;color:#59595a}')
        self.textoClick.resize(390, 25)
        
        self.carregarJanela()
    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setStyleSheet("background-color: #13021d;")
        self.show()
    
    def botaoInstarClick(self):
        index()
    def botaoImportarBancoClick(self):
        print()
        
    def botaoSairClick(self):
        quit()
aplicacao = QApplication(sys.argv)
j = janela()
sys.exit(aplicacao.exec_())
