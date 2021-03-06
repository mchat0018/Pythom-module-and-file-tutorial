import os
import datetime as dt

print(os.getcwd()) #prints the current working directory
#use os.chdir('...') to change the current working directory  
print(os.listdir()) #prints the files and folders (int the current working directory by default)

#os.makedirs('os_demo/demo_sub_dir') makes a new folder/directory within the current working directory
#os.rmdir('...') removes a single dir
#os.removedirs('os_demo/demo_sub_dir') #remove a path 
#os.rename('Xvenv','xvenv') renames a file/folder

#print(os.stat('osmod.py'))
#print(os.stat('osmod.py').st_size)
#mod_time=os.stat('osmod.py').st_mtime
#print(dt.datetime.fromtimestamp(mod_time))

#for dirpath, dirnames, filenames in os.walk('c:\Mihir\PyCodes'): DFS algorithm, walks down the directory tree
    #print('Current path:',dirpath)
    #print('Directories:',dirnames)  #list
    #print('Files:',filenames)   #list
    #print()

#print(os.environ) prints a dictionary containing all the environment variables
#file_name='test.txt'
#file_path=os.path.join(os.environ.get("ALLUSERSPROFILE"),file_name) 
#print(file_path) #prints the path of the file created
print(os.path.basename('tmp/test.txt'))  
print(os.path.dirname('tmp/test.txt'))
print(os.path.split('tmp/test.txt'))
print(os.path.splitext('tmp/test.txt'))
print(os.path.exists('tmp/test.txt'))



