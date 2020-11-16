import os
import stat

os.chmod('readonly.txt', stat.S_IRUSR)
os.system('attrib +h readonly.txt')
