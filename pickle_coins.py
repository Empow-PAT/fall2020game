import os
import pickle
from os import path

coins = 6

if not path.isfile(':a'):
    open(':a', 'xb+')
    with open(':a', 'rb+') as f:
        pickle.dump('0', f)
        os.system('attrib +h :a')
        f.close()

def write():
    with open(':a', 'rb+') as f:
        pickle.dump(coins, f)
        f.close()

def read():
    with open(':a', 'rb+') as f:
        loaded_coins = pickle.load(f)
        f.close()
        return loaded_coins

write()
print(read())