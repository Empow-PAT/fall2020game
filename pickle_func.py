import os
import pickle
import platform

# Use this to create a pickle file
def create_file(filename: str):
    # Checks if the file doesn't exist
    if not os.path.isfile(filename):
        # Creates the file
        open(filename, 'xb')
        # Checks whether the person is using Windows or MacOS(Darwin) and according to that, decides how to hide the file
        if platform.system() == 'Windows':
            os.system(f'attrib +h {filename}')
        elif platform.system() == 'Darwin':
            os.rename(filename, f'.{filename}')
    # Writes some blank text to the file
    write(filename, "")

# Use this to write to a pickle file
def write(filename: str, data):
    # Opens the file in writing mode
    with open(filename, 'wb') as f:
        # Dumps data into the file using pickle
        pickle.dump(data, f)
        # Closes the file
        f.close()

# Use this to read from a pickle file
def read(filename: str):
    # Opens the file in reading mode
    with open(filename, 'rb') as f:
        # Creates a variable with the value of the data in the file
        loaded_data = pickle.load(f)
        # Closes the file
        f.close()
        # Returns the variable with the contents of the file
        return loaded_data