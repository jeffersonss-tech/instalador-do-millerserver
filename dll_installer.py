import os
import platform
import shutil
import subprocess
import time
from pathlib import Path

import py7zr

os.system('cls')
input('Esse script faz a instalação de DLLs em seus devidos diretórios, e trabalha em conjunto e depende dos arquivos localizados em "C:\SeniorFood\DLL x86" , e também pode ser executado apartir de qualquer localização do windoows.\n aperte ENTER para continuar, ou crtl + c para sair:')

if '64bit' in platform.architecture():
    print('sistema x64 detectado.')

    downloads_path = str(Path.home() / "Downloads")
    os.chdir('C:\SeniorFood\DLL x86')
    print('copiando arquivoss...')
    time.sleep(3)
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
    input('system32 concluido!\npressione ENTER para continuar:')
    os.system('cls')
    subprocess.call([r'C:\Windows\SysWOW64\instala.bat'])
    print('syswow64 concluido!')

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
print('copiando atalhos para o menu iniciar...\n')
time.sleep(3)

programs_path = str(Path.home() / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs")

shutil.copy2('C:/SeniorFood/DLL x86/atalhos/AnyDesk.lnk', 'C:/Users/Public/Desktop'), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/Miller.lnk', 'C:/Users/Public/Desktop'), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', 'C:/Users/Public/Desktop')
shutil.copy2('C:/SeniorFood/DLL x86/atalhos/Miller.lnk', programs_path), shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', programs_path)
print('atalhos criados com sussesso!\n')

#aqui ele manda um atalho para o diretorio que o kernel autoexecuta oque tem dentro
auto_start = ''
while auto_start != 's' and auto_start !=  'n' and auto_start != 'S' and auto_start != 'N':
    os.system('cls')
    auto_start = input('deseja ativar a auto inicialização do MillerServer? (S/N)\n')
    if auto_start == 's' or auto_start == 'S':
        startup_path = str(Path.home() / "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
        shutil.copy2('C:/SeniorFood/DLL x86/atalhos/MillerServer.lnk', startup_path)
        print('auto inicialização ativada com sucesso\n')
    elif auto_start == 'n' or auto_start == 'N':
        os.system('cls')
        pass
input('\npressione (ENTER) para sair:')
        
