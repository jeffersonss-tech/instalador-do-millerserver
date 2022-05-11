import os
import platform
import shutil
import subprocess
import time
from pathlib import Path
from time import sleep

import py7zr
import PySimpleGUI as sg


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
    

sg.theme('random')

def atalhoMenuIniciar():
    programs_path = str(Path.home() / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs")
    shutil.copy2('C:/SeniorFood/DLL x86/atalhos/AnyDesk.lnk', 'C:/Users/Public/Desktop'), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/Miller.lnk', 'C:/Users/Public/Desktop'), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', 'C:/Users/Public/Desktop')
    shutil.copy2('C:/SeniorFood/DLL x86/atalhos/Miller.lnk', programs_path), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', programs_path)

def autoIniciar():
    startup_path = str(Path.home() / "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', startup_path)
    
def dllInstaller():
    if '64bit' in platform.architecture():

        downloads_path = str(Path.home() / "Downloads")
        os.chdir('C:\SeniorFood\DLL x86')
        print('copiando arquivoss...')
        os.system('cls')
                #aqui ele copia as dlls
        shutil.copy2('capicom.dll', 'C:\Windows\System32'), shutil.copy2('instala.bat', 'C:\Windows\System32'), shutil.copy2('instalador_capicom.iss', 'C:\Windows\System32'), shutil.copy2('libeay32.dll', 'C:\Windows\System32'), shutil.copy2('midas.dll', 'C:\Windows\System32'), shutil.copy2('msxml5.dll', 'C:\Windows\System32'), shutil.copy2('msxml5r.dll', 'C:\Windows\System32'), shutil.copy2('openssl.exe', 'C:\Windows\System32'), shutil.copy2('ssleay32.dll', 'C:\Windows\System32')
        shutil.copy2('capicom.dll', 'C:\Windows\SysWOW64'), shutil.copy2('instala.bat', 'C:\Windows\SysWOW64'), shutil.copy2('instalador_capicom.iss', 'C:\Windows\SysWOW64'), shutil.copy2('libeay32.dll', 'C:\Windows\SysWOW64'), shutil.copy2('midas.dll', 'C:\Windows\SysWOW64'), shutil.copy2('msxml5.dll', 'C:\Windows\SysWOW64'), shutil.copy2('msxml5r.dll', 'C:\Windows\SysWOW64'), shutil.copy2('openssl.exe', 'C:\Windows\SysWOW64'), shutil.copy2('ssleay32.dll', 'C:\Windows\SysWOW64')
        print('arquivos copiados!')
        time.sleep(1)
        #aqui ele executa os batchs que assinam as dlls
        print('instalando e assinando DLLs...')
        time.sleep(1)
        subprocess.call([r'C:\Windows\System32\instala.bat'])
        print('system32 concluido!:')
        time.sleep(0.5)
        os.system('cls')
        subprocess.call([r'C:\Windows\SysWOW64\instala.bat'])
        print('syswow64 concluido!')
        time.sleep(0.5)

    else:
        #aqui é o mesmo processo, mas para sistemas de 32bits
        print('sistema x86 detectado')
        #nessa parte é feita a verificação se existe o diretorio x86 se não ele cria e em seguida ele extrai as dlls de 32bits para esse diretorio
        if os.path.exists('C:/SeniorFood/DLL x86') == False:
            os.mkdir('C:/SeniorFood/DLL x86/x86')
        archive = py7zr.SevenZipFile('C:/SeniorFood/DLL x86/DLL x86.7z', mode='r')
        archive.extractall(path="C:/SeniorFood/DLL x86/x86")
        archive.close()
        #aqui ele muda o diretorio
        os.chdir('C:/SeniorFood/DLL x86/x86')
        print('copiando arquivoss...')
        time.sleep(3)
        os.system('cls')
        #aqui ele copia as dlls
        shutil.copy2('capicom.dll', 'C:\Windows\System32'), shutil.copy2('instala.bat', 'C:\Windows\System32'), shutil.copy2('instalador_capicom.iss', 'C:\Windows\System32'), shutil.copy2('libeay32.dll', 'C:\Windows\System32'), shutil.copy2('midas.dll', 'C:\Windows\System32'), shutil.copy2('msxml5.dll', 'C:\Windows\System32'), shutil.copy2('msxml5r.dll', 'C:\Windows\System32'), shutil.copy2('openssl.exe', 'C:\Windows\System32'), shutil.copy2('ssleay32.dll', 'C:\Windows\System32')
        shutil.copy2('capicom.dll', 'C:\Windows\SysWOW64'), shutil.copy2('instala.bat', 'C:\Windows\SysWOW64'), shutil.copy2('instalador_capicom.iss', 'C:\Windows\SysWOW64'), shutil.copy2('libeay32.dll', 'C:\Windows\SysWOW64'), shutil.copy2('midas.dll', 'C:\Windows\SysWOW64'), shutil.copy2('msxml5.dll', 'C:\Windows\SysWOW64'), shutil.copy2('msxml5r.dll', 'C:\Windows\SysWOW64'), shutil.copy2('openssl.exe', 'C:\Windows\SysWOW64'), shutil.copy2('ssleay32.dll', 'C:\Windows\SysWOW64')
        print('arquivos copiados!')
        time.sleep(2)
        #aqui ele executa os batches que assinam
        print('instalando e assinando DLLs...')
        time.sleep(2)
        subprocess.call([r'C:\Windows\System32\instala.bat'])
        input('system32 concluido!\npressione ENTER para continuar:')
        os.system('cls')

        subprocess.call([r'C:\Windows\SysWOW64\instala.bat'])
        print('syswow64 concluido!')


def importDb():
    while os.path.exists('c:\SeniorFood') == False:
        os.makedirs('c:\SeniorFood/')

        if os.path.exists('c:\SeniorFood'):
            print('diretorio existe')
            pass

    while os.path.exists('c:\php') == False:
        os.makedirs('c:\php/')
        if os.path.exists('c:\php'):
            print('diretorio existe')
            pass

    os.system('xcopy  /E /s SeniorFood\*.* "C:\SeniorFood\" /y')
    os.system(' xcopy  /E /s php\*.* "C:\php\" /y')

    os.system(' taskkill /f /im pgAdmin4.exe')
    os.system(' taskkill /f /im MillerServer.exe')

    if os.path.exists('C:\Program Files (x86)'):
        os.system('  copy *.conf "%programfiles(x86)%\Postgresql\9.6\data" /y')
        os.system('cls')
        
        os.system('"C:\Program Files (x86)/PostgreSQL/9.6/bin/dropdb.exe" --if-exists -h localhost --username postgres SOFTMOBILE')
        os.system('"C:\Program Files (x86)/PostgreSQL/9.6/bin/createdb.exe"  -U postgres -W  -T template1 -E UTF-8 SOFTMOBILE ')
        os.system('"C:\Program Files (x86)/PostgreSQL/9.6/bin/pg_restore.exe" --host localhost --port 5432 --username postgres --dbname SOFTMOBILE carga.backup')
    else:
        os.system('copy *.conf "%programfiles%\Postgresql\9.6\data" /y')
        os.system('cls')

        os.system('"C:\programfiles/PostgreSQL/9.6/bin/dropdb.exe" --if-exists -h localhost --username postgres SOFTMOBILE')
        os.system('"C:\programfiles/PostgreSQL/9.6/bin/createdb.exe"  -U postgres -W  -T template1 -E UTF-8 SOFTMOBILE')
        os.system('"C:\programfiles/PostgreSQL/9.6/bin/pg_restore.exe" --host localhost --port 5432 --username postgres --dbname SOFTMOBILE carga.backup')
    dllInstaller()


def telaFinal():
    flayout = [
        [sg.Text('Concluido!')], #row 1
        [sg.Button('Ok')]#row 2
    ]
    window = sg.Window('MillerServer', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    if button == 'Ok':
        window.close()
        

def telaAutoIniciar():
    flayout = [
        [sg.Text('Deseja ativar a auto inicialização do sistema?')], #row 1
        [sg.Button('sim'), sg.Button('não')]#row 2
    ]
    window = sg.Window('auto inicialização', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    if button == 'sim':
        window.close()
        autoIniciar()
        
        
    elif button == 'não':
        window.close()
    telaFinal()

def telaAtalhos():
    flayout = [
        [sg.Text('Deseja criar atalhos na area de trabalho e no menu iniciar?')], #row 1
        [sg.Button('sim'), sg.Button('não')]#row 2
    ]
    window = sg.Window('atalhos', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    if button == 'sim':
        window.close()
        atalhoMenuIniciar()
        
    elif button == 'não':
        window.close()
    telaAutoIniciar()

def telaSistemaNaoInstalado():
    flayout = [
        [sg.Text('O sistema não está instalado')], #row 1
        [sg.Button('Ok')]#row 2
    ]
    window = sg.Window('oops', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    if button == 'Ok':
        window.close()
        front()

def telaInstalar():
    
    flayout = [
        [sg.Text('Deseja instalar com runtimes?')], #row 1
        [sg.Button('sim'), sg.Button('não')]#row 2
    ]
    window = sg.Window('runtimes', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    
    if button == 'sim':
        window.close()
        os.system('postgresql-9.6.12-2-windows.exe --unattendedmodeui minimal --mode unattended --superpassword "123" --servicename "postgreSQL" --servicepassword "123" --serverport 5432')
        importDb()
        telaAtalhos()
        
    elif button == 'não':
        window.close()
        os.system('postgresql-9.6.12-2-windows.exe --unattendedmodeui minimal --mode unattended --superpassword "123" --servicename "postgreSQL" --servicepassword "123" --serverport 5432 --install_runtimes 0')
        importDb()
        telaAtalhos()

def telaImportar():
    flayout = [
        [sg.Text('deseja realmente importar o banco de dados?')], #row 1
        [sg.Button('sim'), sg.Button('não')]#row 2
    ]
    window = sg.Window('runtimes', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    if button == 'sim':
        window.close()
        if os.path.exists('C:\SeniorFood') == False:
            window.close()
            telaSistemaNaoInstalado()
        else:
            importDb()
            telaAtalhos()
        
    elif button == 'não':
        window.close()
        front()
        
def front():
    flayout = [
        [sg.Text('Bem-Vindo')], #row 1
        [sg.Button('Instalar'), sg.Button('Importar'), sg.Button('Sair')]#row 2
    ]
    
    #window
    window = sg.Window('Instalador MillerServer', flayout, size=(500, 100), element_justification='center')
    button, values = window.read()
    
    if button == 'Instalar':
        window.close()
        telaInstalar()
        
    elif button == 'Importar':
        window.close()
        telaImportar()
        
    elif button == 'Sair':
        window.close()
        
front()
