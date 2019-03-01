#!/usr/bin/python
# _*_ coding:utf-8 _*_
import re
import random

#question <a>
##step1
def combinedLiner(m1,a1,m2,a2):
    i = 0
    R1 =[]
    y01 = random.randint(1,m1-1)
    y02 = random.randint(1,m2-1)
    while i < 3:
        #step2
        y01 = (a1*y01)%m1
        y02 = (a2*y02)%m2
        #step3
        x1 = (y01-y02)%(m1-1)
        #step4
        if x1 > 0:
            R1.append(x1/m1)
        elif x1 == 0:
            R1.append((m1-1)/m1)
        i+=1
    return R1

#question <b>
def Diffe_hellman(q,a):
    #compute the public key of user A and B
    xa = combinedLiner(2147483642,450,2147483423,234)[0]
    xb = combinedLiner(2147483642,450,2147483423,234)[1]
    yb = pow(a,xb)%q
    #compute the secret key of user A and B
    key = pow(yb,xa)%q
    return key

#question <c>
##create block message
def create_blockMessage(message):
    if len(message) < 8:
        message = input('Please re-enter the message that length is longer than 64-bits\n')
        message = message.replace ( " ", '' )
        inital_block = re.split ( '(\w{8})', message )
        final_block = []
        for i in inital_block:
            if len(i) == 8:
                final_block.append(i)
        last_block = final_block[(len(final_block)-1)]
    else:
        message = message.replace(" ",'')
        inital_block = re.split('(\w{8})',message)
        final_block = []
        #print(inital_block)
        for i in inital_block:
            if len(i) == 8:
                final_block.append(i)
        last_block = final_block[(len(final_block)-1)]

    return last_block


#RC4
def RC4(key,message):
    message = create_blockMessage ( message )  # get the last block cipher
    #inital s-box
    s = []
    t = []
    j = 0
    k = 0
    for i in range(256):
        s.append(i)
        t.append(key[i%(len(key))])
    for i in range(256):

        j = (j+s[i]+s[j])%256
        s[i],s[j] = s[j],s[i]
    a_message = ''
    while k<len(message):
        ord_message = ord(message[k])
        i = (i+1)%256
        j = (j+s[i])%256
        s[i],s[j] = s[j],s[i]
        t = (s[i]+s[j])%256
        data = ord_message + s[t]
        k+=1
        a_message += chr(data)
    return a_message

def decrypt(key,ciphertext):
    s = []
    t = []
    j = 0
    k = 0
    for i in range ( 256 ):
        s.append ( i )
        t.append ( key[i % (len ( key ))] )
    for i in range ( 256 ):
        j = (j + s[i] + s[j]) % 256
        s[i], s[j] = s[j], s[i]
        a_ciphertext = ''
    while k<len(ciphertext):
        ord_ciphertext = ord(ciphertext[k])
        i = (i+1)%256
        j = (j+s[i])%256
        s[i],s[j] = s[j],s[i]
        t = (s[i]+s[j])%256
        data = ord_ciphertext - s[t]
        k+=1
        a_ciphertext += chr(data)
    return a_ciphertext



print('The One-Time private key for User A is:')
print(combinedLiner(2147483642,450,2147483423,234)[0])
print('The One-Time private key for User B is:')
print(combinedLiner(2147483642,450,2147483423,234)[1])
print('The secret key for user A and B is')
print(str(Diffe_hellman(353,3)))
message = input('Please Enter your Plaintext:\n')
print('the ciphertext is:',RC4(str(Diffe_hellman(353,3)),message))
print('the plaintexr is:',decrypt(RC4(str(Diffe_hellman(353,3)),message),RC4(str(Diffe_hellman(353,3)),message)))



