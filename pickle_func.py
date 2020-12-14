import os
import pickle
import platform
import win32con, win32api

def create_file(filename: str):
    if not os.path.isfile(filename):
        open(filename, 'xb')
        if platform.system() == 'Windows':
            os.system(f'attrib +h {filename}')
        elif platform.system() == 'Darwin':
            os.rename(filename, f'.{filename}')

def write(filename: str, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
        f.close()

def read(filename: str):
    with open(filename, 'rb') as f:
        loaded_data = pickle.load(f)
        f.close()
        return loaded_data