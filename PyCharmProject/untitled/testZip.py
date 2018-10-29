import zipfile
import os


def doZip(folder):
    os.chdir(folder)
    print('current directory : ', os.getcwd())

    zip_filename = os.path.basename(folder) + '.zip'
    print('zip file name : ', zip_filename)

    os.mkdir('../backup')

    backupzip = zipfile.ZipFile('../backup/' + zip_filename, 'w')

    for folder_name, subfolders, file_names in os.walk('.') :

        backupzip.write(folder_name)

        for subfolder in subfolders :
            backupzip.write(os.path.join(folder_name, subfolder))

        for fileName in file_names :
            if( '__' in fileName):
                print('skip __', fileName)
            else :
                backupzip.write(os.path.join(folder_name, fileName))


    backupzip.close()
    print('backup completed')


def main():
    doZip('./services')


if __name__ == '__main__':
    main()