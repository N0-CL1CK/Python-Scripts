# Author: Luís Gonzaga | N0-CL1CK
# GitHub: n0-cl1ck

# Created in Python 3.11 and tested in Docker 24.0.5
# 2023-11-08

# Docker cleaner

from sys import argv as args
from subprocess import run, Popen, PIPE

commands = [
	'docker image prune -a',
	'docker container prune',
	'docker volume prune',
	'docker network prune',
	'docker system prune -a',
]

def execNormal():
	for command in commands:
		print(f'\n\n\t[!] "{command}" is running...\n')
		run(command.split())

def execForce():
	for command in commands:
		print(f'\n\n\t[!] "{command}" is running...\n')
		proc1 = Popen(['yes'], stdout=PIPE)
		proc2 = Popen(command.split(), stdin=proc1.stdout, stdout=PIPE, stderr=PIPE)
		proc1.stdout.close()
		out, err = proc2.communicate()

		if (err):
			print('\t'+err.decode())
		else:
			print('\t'+out.decode())

def main():
	try:
		if (len(args) > 1 and (args[1] == '--force' or args[1] == '-F')):
			execForce()
		else:
			execNormal()

		print('\n\n\t[!] script is finished.\n')
	except Exception as e:
		print('Ocorreu um erro:', e)

if __name__ == '__main__':
	main()
