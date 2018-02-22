#! by unknwhp
import hashlib, os
os.system('clear') #linux
#os.system('cls') #windows
print '''
 _   _           _     _  ___ _ _           
| | | | __ _ ___| |__ | |/ (_) | | ___ _ __ 
| |_| |/ _` / __| '_ \| ' /| | | |/ _ \ '__|
|  _  | (_| \__ \ | | | . \| | | |  __/ |   
|_| |_|\__,_|___/_| |_|_|\_\_|_|_|\___|_|

############### by unknwhp ###############
'''
wd = raw_input('Wordlist to use: ')
hash = raw_input('Type a hash to crack: ')
hasht = raw_input('Type the hash type : ')
acpt = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

if hasht not in acpt:
	print '[!] Hash not suported!'
	print '[*] Suported hashes: '
	print '[+] md5, sha1, sha224, sha256, sha384, sha512'
	exit()

list = open(wd)
text = list.readlines()
encontrado = 0
for word in text:

	if word.endswith('\n'):

		word = word[:-1]
	if hasht == 'md5':
		brute = hashlib.md5(word).hexdigest()
	elif hasht == 'sha1':
		brute = hashlib.sha1(word).hexdigest()
	elif hasht == 'sha224':
		brute = hashlib.sha224(word).hexdigest()
	elif hasht == 'sha256':
		brute = hashlib.sha256(word).hexdigest()
	elif hasht == 'sha384':
		brute = hashlib.sha384(word).hexdigest()
	elif hasht == 'sha512':
		brute = hashlib.sha512(word).hexdigest()

	if brute == hash:
		encontrado = 1
		break
if encontrado == 1:
	print '[+] Hash founded!'
        print '[*] Your hash is: '+word
else:
	print '[-] Hash not founded'
