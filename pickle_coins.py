import os
import pickle
from os import path
import stat

coins = 6

if not path.isfile('coins'):
    open('coins', 'xb+')
    with open('coins', 'rb+') as f:
        pickle.dump('0', f)
        os.system('attrib +h coins')
        os.chmod('coins', stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        f.close()

def write():
    os.chmod('coins', stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)
    with open('coins', 'rb+') as f:
        pickle.dump(coins, f)
        os.chmod('coins', stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        f.close()

def read():
    os.chmod('coins', stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)
    with open('coins', 'rb+') as f:
        loaded_coins = pickle.load(f)
        f.close()
        os.chmod('coins', stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        return loaded_coins

write()
print(read())