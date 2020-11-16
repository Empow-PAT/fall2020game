from pyads import ADS
from os import path
import pickle
import os

coins = 11

if not path.isfile('fake.txt'):
    open('coins', 'xb+')
    with open('coins', 'rb+') as f:
        pickle.dump('0', f)
        os.system('attrib +h coins')
        f.close()

if not path.isfile('fake.txt:coins'):
    open('fake.txt:coins', 'xb+')
    with open('fake.txt:coins', 'rb+') as f:
        pickle.dump('0', f)
        os.system('attrib +h fake.txt')
        f.close()

def write():
    with open('fake.txt:coins', 'rb+') as f:
        pickle.dump(coins, f)
        f.close()

def read():
    with open('fake.txt:coins', 'rb+') as f:
        loaded_coins = pickle.load(f)
        f.close()
        return loaded_coins

write()
print(read())

handler = ADS('fake.txt')

for streams in handler:
    print(streams)