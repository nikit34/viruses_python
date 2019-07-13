from sys import argv
from hashlib import sha256, sha512, md5

try:
	hashAlgoritm, hash_file, dict_file = argv[1],argv[2],argv[3]
except IndexError:
	print("Error: Arguments!")
	raise SystemExit

with open(hash_file) as file:
	hash_func = file.read()
	hash_func = hash_func.replace('\n','')

def generator(string):
	for word in string:
		password = word.replace('\n','')
		if encrypt(password) == hash_func:
			yield "\n[True]: " + password
			return
		else:
			yield "[False]: " + password

def encrypt(string):
	password = string.encode()
	if hashAlgoritm  == "md5":
		signature = md5(password).hexdigest()
	elif hashAlgoritm  == "sha25 6":
		signature = sha256(password).hexdigest()
	elif hashAlgoritm  == "sha51 2":
		signature = sha512(password).hexdigest()
	else: raise SystemExit
	return signature

with open(dict_file, errors = "ignore") as dictionary:
	for password in generator(dictionary):
		print(password)
