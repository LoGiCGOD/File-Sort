import os
import shutil
# os helps in handling folders while shutil helps in arranging files
folders = {                                  # Dictionary
    'videos': ['.mp4'],
    'audios': ['.wav', '.mp3'],
    'images': ['.png', '.jpg'],
    'documents': ['.doc', '.xlsx', '.xls', '.pdf', '.zip', '.rar'],

}


def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, folder)) == True:
            os.rename(os.path.join(directory, folder),
                      os.path.join(directory, folder.lower()))


print(folders)
for fname in folders:
    print(fname, folders[fname])  # fname ~ foldername


directory = input("Enter the location or path:")
# os.listdir() will take all the files and folders in the user given path and put it in a list
other_name = input("Enter the folder name for unknown files")
rename_folder()

all_files = os.listdir(directory)
# all the files and folders are now in all_files
print(all_files)


def mov(extension, filename):

    # def mov(extension, filename):
    # print(extension, filename)
    # try this to check the format and name of the file
    find = False
    for fname in folders:
        if "."+extension in folders[fname]:
            if fname not in os.listdir(directory):
                os.mkdir(os.path.join(directory, fname))
            shutil.move(os.path.join(directory, filename),
                        os.path.join(directory, fname))
            find = True
            break
    if find != True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory, other_name))
        shutil.move(os.path.join(directory, filename),
                    os.path.join(directory, other_name))


for i in all_files:
    # isfile returns true if any files are present in the given path
    if os.path.isfile(os.path.join(directory, i)) == True:
        print("file exists")
        # i.split will extract the extension while i will give the whole filename
        mov(i.split(".")[-1], i)
