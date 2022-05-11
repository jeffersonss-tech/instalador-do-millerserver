import os
import platform
import shutil
import subprocess
import time
from pathlib import Path
from time import sleep

import py7zr


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

def index():

    usuario_escolhe = ''
    while usuario_escolhe != '1' and usuario_escolhe != '2':
        os.system('cls')
        print(f'{bcolors.HEADER}                               INSTALADOR MILLER SERVER{bcolors.ENDC}\n')
        usuario_escolhe = input(f'{bcolors.OKGREEN}digite "1" para instalar ou "2" para importar o banco:{bcolors.ENDC}')
    if usuario_escolhe == str(1):
        runtimes = ''
        while runtimes != 's' and runtimes != 'S' and runtimes != 'n' and runtimes != 'N':
            os.system('cls')
            runtimes = input(f'{bcolors.OKGREEN}gostaria de instalar com runtimes?{bcolors.WARNING} (S/N){bcolors.ENDC}')
            if runtimes == 's' or runtimes == 'S':
                os.system('cls')
                print(f'{bcolors.OKBLUE}instalando postgreSQL...{bcolors.ENDC}')
                os.system('postgresql-9.6.12-2-windows.exe --unattendedmodeui minimal --mode unattended --superpassword "123" --servicename "postgreSQL" --servicepassword "123" --serverport 5432')
                print('postgre instalado com sucesso!')
                sleep(3)
                os.system('cls')
                pass
            elif runtimes == 'n' or runtimes == 'N':
                print('instalando postgre sem runtimes...')
                os.system('postgresql-9.6.12-2-windows.exe --unattendedmodeui minimal --mode unattended --superpassword "123" --servicename "postgreSQL" --servicepassword "123" --serverport 5432 --install_runtimes 0')        
                print(f'{bcolors}postgre instalado com sucesso!{bcolors.ENDC}')
                sleep(3)
                os.system('cls')
                pass
    elif usuario_escolhe == str(2):
        os.system('cls')
        if os.path.exists('C:\SeniorFood') == False:
            input(f'{bcolors.FAIL}Para usar este recurso, faça a instalação antes.\n aperte (ENTER) para continuar:{bcolors.ENDC}')
            index()
            os.system('cls')
            #quit()
        else:
            print(f'{bcolors.WARNING}ATENÇÃO! O BANCO DE DADOS ATUAL ESTÁ PRESTES A SER REMOVIDO!! {bcolors.ENDC}')
            pass

    #os.startfile('importar.exe')

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

    os.system('xcopy  /E /s SeniorFood\*.* "C:\SeniorFood\" ')
    os.system('cls')
    os.system('xcopy  /E /s php\*.* "C:\php\" ')
    os.system('cls')
    os.system('taskkill /f /im pgAdmin4.exe')
    os.system('taskkill /f /im MillerServer.exe')

    if os.path.exists('C:\Program Files (x86)'):
        os.system('  copy *.conf "%programfiles(x86)%\Postgresql\9.6\data"')
        os.system('cls')
        
        os.system('"C:\Program Files (x86)/PostgreSQL/9.6/bin/dropdb.exe" --if-exists -h localhost --username postgres SOFTMOBILE')
        os.system('"C:\Program Files (x86)/PostgreSQL/9.6/bin/createdb.exe"  -U postgres -W  -T template1 -E UTF-8 SOFTMOBILE')
        os.system('"C:\Program Files (x86)/PostgreSQL/9.6/bin/pg_restore.exe" --host localhost --port 5432 --username postgres --dbname SOFTMOBILE carga.backup')
        #dllInstaller()
    # print(os.getcwd())
        sleep(3)
    else:
        os.system('  copy *.conf "%programfiles%\Postgresql\9.6\data"')
        os.system('cls')

        os.system('"C:\programfiles/PostgreSQL/9.6/bin/dropdb.exe" --if-exists -h localhost --username postgres SOFTMOBILE')
        os.system('"C:\programfiles/PostgreSQL/9.6/bin/createdb.exe"  -U postgres -W  -T template1 -E UTF-8 SOFTMOBILE')
        os.system('"C:\programfiles/PostgreSQL/9.6/bin/pg_restore.exe" --host localhost --port 5432 --username postgres --dbname SOFTMOBILE carga.backup')
        #os.startfile('dll_installer.exe')
        #dllInstaller()
        sleep(3)

def dllInstaller():
    os.system('cls')
    input(f'{bcolors.OKGREEN}aperte (ENTER) para instalar as dlls, ou crtl + c para sair:{bcolors.ENDC}')

    if '64bit' in platform.architecture():
        print('sistema x64 detectado.')

        downloads_path = str(Path.home() / "Downloads")
        os.chdir('C:\SeniorFood\DLL x86')
        print('copiando arquivoss...')
        time.sleep(2)
        os.system('cls')
                #aqui ele copia as dlls
        shutil.copy2('capicom.dll', 'C:\Windows\System32'), shutil.copy2('instala.bat', 'C:\Windows\System32'), shutil.copy2('instalador_capicom.iss', 'C:\Windows\System32'), shutil.copy2('libeay32.dll', 'C:\Windows\System32'), shutil.copy2('midas.dll', 'C:\Windows\System32'), shutil.copy2('msxml5.dll', 'C:\Windows\System32'), shutil.copy2('msxml5r.dll', 'C:\Windows\System32'), shutil.copy2('openssl.exe', 'C:\Windows\System32'), shutil.copy2('ssleay32.dll', 'C:\Windows\System32')
        shutil.copy2('capicom.dll', 'C:\Windows\SysWOW64'), shutil.copy2('instala.bat', 'C:\Windows\SysWOW64'), shutil.copy2('instalador_capicom.iss', 'C:\Windows\SysWOW64'), shutil.copy2('libeay32.dll', 'C:\Windows\SysWOW64'), shutil.copy2('midas.dll', 'C:\Windows\SysWOW64'), shutil.copy2('msxml5.dll', 'C:\Windows\SysWOW64'), shutil.copy2('msxml5r.dll', 'C:\Windows\SysWOW64'), shutil.copy2('openssl.exe', 'C:\Windows\SysWOW64'), shutil.copy2('ssleay32.dll', 'C:\Windows\SysWOW64')
        print('arquivos copiados!')
        time.sleep(2)
        #aqui ele executa os batchs que assinam as dlls
        print('instalando e assinando DLLs...')
        time.sleep(2)
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

    #aqui ele copia os atalhos para seus lugares
    os.system('cls')
    simOuNao = ''
    while simOuNao != 's' and simOuNao != 'S' and simOuNao != 'n' and simOuNao != 'N':
        os.system('cls')
        simOuNao = input(f'{bcolors.OKGREEN}Deseja criar atalhos no menu iniciar e na area de trabalho?(S/N){bcolors.ENDC}\n')
        if simOuNao == 's' or simOuNao == 'S':    
            programs_path = str(Path.home() / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs")

            shutil.copy2('C:/SeniorFood/DLL x86/atalhos/AnyDesk.lnk', 'C:/Users/Public/Desktop'), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/Miller.lnk', 'C:/Users/Public/Desktop'), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', 'C:/Users/Public/Desktop')
            shutil.copy2('C:/SeniorFood/DLL x86/atalhos/Miller.lnk', programs_path), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', programs_path)
            print('atalhos criados com sussesso!\n')
            print('criando atalhos...')
            time.sleep(1.5)
        elif simOuNao == 's' or simOuNao == 'N':
            break
    #aqui ele manda um atalho para o diretorio que o kernel autoexecuta oque tem dentro
    auto_start = ''
    while auto_start != 's' and auto_start !=  'n' and auto_start != 'S' and auto_start != 'N':
        os.system('cls')
        auto_start = input(f'{bcolors.OKGREEN}deseja ativar a auto inicialização do MillerServer? (S/N){bcolors.OKGREEN}\n')
        if auto_start == 's' or auto_start == 'S':
            startup_path = str(Path.home() / "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
            shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', startup_path)
            print('auto inicialização ativada com sucesso\n')
        elif auto_start == 'n' or auto_start == 'N':
            os.system('cls')
            pass
    input(f'\n{bcolors.OKGREEN}pressione (ENTER) para sair:{bcolors.ENDC}')
    
index()
importDb()
dllInstaller()
