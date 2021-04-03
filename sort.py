import os
import shutil
# os helps in handling folders while shutil helps in arranging files
folders = {
    'videos': ['.mp4'],
    'audios': ['.wav', '.mp3'],
    'images': ['.png', '.jpg'],
    'documents': ['.doc', '.xlsx', '.xls', '.pdf', '.zip', '.rar'],

}
print(folders)
for fname in folders:
    print(fname, folders[fname])


directory = input("Enter the location or path:")
# os.listdir() will take all the files and folders in the user given path and put it in a list

all_files = os.listdir(directory)
# all the files and folders are now in all_files
print(all_files)
