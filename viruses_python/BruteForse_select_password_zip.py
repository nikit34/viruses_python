from zipfile import ZipFile
from os import mkdir

def generator(string):
	for word in string:
		password = word.replace('\n','')
		archive.setpassword(password.encode())
		try:
			archive.extractall(directory)
		except:
			yield "[False]: " + password
		else:
			yield "\n[True]: " + password; return

directory = "ExtractArchive"
try: mkdir(directory)
except FileExistsError: pass

# dictionary - файл с паролями для перебора
with open(input("Dictionary: "), errors='ignore') as dictionary:
	with ZipFile(input("Archive: ")) as archive:
		for password in generator(dictionary):
			print(password)
