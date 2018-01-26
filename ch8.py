import os

for folderName, subfolders, filenames in os.walk('/home/piotr/Pobrane/python/atbs/delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            # os.rmdir(subfolder)
            print(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
