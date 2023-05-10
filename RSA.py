import math


def isnotprime(n) :
  for i in range (2,n) :
    if n % i == 0 :
      return True 
  return False


def modularInv(x,n):
  for i in range(1,n):
    if( (x*i) % n == 1):
      return i
  return -1


p = int(input("Enter first prime number :"))
while(isnotprime(p)) :
  print(p,'is not a prime number')
  p = int(input("Enter first prime number :"))


q = int(input("Enter Second prime number :"))
while(True) :
  if(p == q):
    print('Both numbers cannot be equal')
    q = int(input("Enter Second prime number :"))
  elif (isnotprime(q)) :
    print(q,'is not a prime number')
    q = int(input("Enter Second prime number :"))
  else :
    break


n = p * q
phi = (p - 1) * (q - 1)


e = 2
while math.gcd(e,phi) != 1 :
  e += 1
  if e >= phi :
    print(e," greater then phi ",phi)
    break;


d = modularInv(e,phi)


M = int(input("Enter plain text : "))
C = math.pow(M,p)
C = C % n
print('public key : (' ,p,',',n,')')
print('Cipher text : ',C)


D = math.pow(C,d)
D = D % n
print('Private key : (' ,d,',',n,')')
print('Cipher text : ',D)
