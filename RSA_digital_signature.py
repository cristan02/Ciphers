import rsa
(pubkey, privkey) = rsa.newkeys(1024)

#sender
message = input("Enter your message : ").encode('utf8')
signed = rsa.sign(message, privkey, 'SHA-512')

while True :
  snd = int(input("Send UnAltered : 1\tSend Altered : 2\n"))
  if(snd == 1 or snd == 2) : break
  else : print("Invalid input!!")

if(snd == 1) : msgSnd = [ message , signed ] 
else : msgSnd = [ input("Alter message : ").encode('utf8') , signed ]

#reciever
recvMsg = msgSnd

try : 
  if 'SHA-512' == rsa.verify(recvMsg[0], recvMsg[1], pubkey) :
    print('Message :', recvMsg[0].decode('utf8'))
except: print ("Message has been altered!!")