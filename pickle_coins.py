import os
import pickle
from os import path

coins = 6

if not path.isfile('coins'):
    with open('coins', 'rb+') as f:
        pickle.dump('0', f)
        os.system('attrib +h coins')
        f.close()

def write():
    with open('coins', 'rb+') as f:
        pickle.dump(coins, f)
        f.close()

def read():
    with open('coins', 'rb+') as f:
        loaded_coins = pickle.load(f)
        f.close()
        return loaded_coins

write()
print(read())