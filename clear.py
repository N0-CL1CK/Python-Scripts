# -*- coding: utf-8 -*-
from os import chdir as cd, system as command

def clearPath(path):
    cd(path)
    command('del /q /f /s *')

def jumpLine(linhas):
    for i in range(linhas):
        command('echo.')

def main():
    paths=[
        'C:\\Windows\\Prefetch',
        'C:\\Windows\\Temp',
        'C:\\Users\\Luis\\AppData\\Local\\Temp'
    ]

    command('color a')
    command('cls')
    for path in paths:
        clearPath(path)
        jumpLine(1)
        command('echo '+'+'+'-'*100+'+')
        jumpLine(1)
    command('echo [*] Finalizado com sucesso!')
    jumpLine(1)
    command('pause')
    
if __name__=='__main__':
    main()
