import hashlib
i_string = input("Frase: \n")
i_sha256 = input("SHA256: \n")
i_md5 = input("MD5: \n")
hashed_sha256 = hashlib.sha256(i_string.encode('utf-8')).hexdigest()
hashed_md5 = hashlib.md5(i_string.encode('utf-8')).hexdigest()
state_sha256=0
state_md5=0
if(i_sha256==hashed_sha256):
  print("SHA256 Correto")
  print(hashed_sha256)
  state_sha256 += 1
else:
  print("SHA256 Incorreto")
  print(hashed_sha256)
  
if(i_md5==hashed_md5):
  print("MD5 Correto")
  print(hashed_md5)
  state_md5 += 1
else:
  print("MD5 Incorreto")
  print(hashed_md5)

if state_sha256 == 1 and state_md5 == 1:
  print("###Frase Verdadeira###")
  print("SHA256 e MD5 corretos")
elif state_sha256 == 0 and state_md5 == 1:
  print("###Frase Falsa###")
  print("SHA256 incorreto e MD5 correto")
elif state_sha256 == 1 and state_md5 == 0:
  print("###Frase Falsa###")
  print("SHA256 correto e MD5 incorreto")
elif state_sha256 == 0 and state_md5 == 0:
  print("###Frase Falsa###")
  print("SHA256 e MD5 incorretos")
  

