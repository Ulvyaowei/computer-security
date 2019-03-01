#!/usr/bin/python
# _*_ coding:utf-8 _*_

from collections import Counter

max_key_size = 25

def getMode():
    while True:
        print('Do You Want Decrypt,Encrypt Or BruteAttack')
        mode = input().lower()
        if mode in "decrypt d encrypt e bruteattack b".split():
            return mode
        else:
            print("Enter Either 'encrypt','e','decrypt','d','bruteattack' or 'b'")

def getMessage():
    print('Enter Your message')
    return input()


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)'%(max_key_size))
        key = int(input())
        if(key >= 1 and key <= max_key_size):
            return key

def getTranslatedMessage(mode,message,key):
    if mode[0] == 'd':
        key = -key

    plainText = ''

    for c in message:
        if c.isalpha():
            num = ord(c)
            num += key

            if c.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif c.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            plainText += chr(num)

        else:
            plainText += c

    return plainText

def bruteAttack(message):
    key = 1

    while key < 26:
        plainText = ''
        for c in message:
            if c.isalpha():
                num = ord(c)
                num += key

                if c.isupper():
                    if num > ord('Z'):
                        num -= 26
                    if num < ord('A'):
                        num += 26
                elif c.islower():
                    if num > ord('z'):
                        num -= 26
                    if num < ord('a'):
                        num += 26

                plainText += chr(num)
            else:
                plainText += c

        print(plainText)


        b= input("Is that what your want? Y/N:\n").lower()
        if b[0] == "y":
            print('Your Message Is:')
            return plainText
            break;
        else:
            key += 1
            continue





mode = getMode()
message = getMessage()

if mode in "encrypt e decrypt d".split():
    key = getKey()
    print('Your Translated Message is:')
    print(getTranslatedMessage(mode,message,key))
elif mode in "bruteattack b".split():
    print('Your Possible Message is:')
    print(bruteAttack(message))




