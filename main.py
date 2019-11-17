import requests


PROTOCOL = 'http'
MASTER_IP = 'localhost'
MASTER_PORT = '4000'


def requestURL(req):
    return PROTOCOL + '://' + MASTER_IP + ':' + MASTER_PORT + '/api/' + req


def printPossibleActions():
    print()
    print('List of possible actions:')
    print('1 - INITIALIZE File System (Clean all data)')
    print('2 - CREATE an empty FILE in the File System')
    print('3 - DOWNLOAD a file from the File System')
    print('4 - UPLOAD a file to the File System')
    print('5 - DELETE file from the File System')
    print('6 - GET INFORMATION about file in the File System')
    print('7 - Create a COPY of the xisting file in the File System')
    print('8 - MOVE existing FILE to a specified path in the File System')
    print('9 - CHANGE your current DIRECTORY in the File System')
    print('10 - SHOW list of files and folders, stored in current directory')
    print('11 - CREATE a new DIRECTORY')
    print('12 - DELETE existing DIRECTORY in the File System')
    print('20 - Show this list again')
    print('0 - Exit')
    print()


def initializeFS():
    response = requests.request('POST', url=requestURL('init'))


def createFile(cwd):
    filename = input('Specify name of new file to create: ')
    data = { 'name': filename, 'path': cwd }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('POST', url=requestURL('touch'), data=data, headers=headers)


def downloadFile(cwd):
    filename = input('Specify name of file to download: ')
    data = { 'name': filename, 'path': cwd }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('GET', url=requestURL('download'), data=data, headers=headers)
    f = open(filename, 'w')
    f.write(response.content)
    f.close()


def uploadFile(cwd):
    filename = input('Specify name of file to upload: ')
    files = { 'u_file': open(filename, 'rb') }
    headers = { 'Content-Type': 'multi/form-data' }
    response = requests.request('POST', url=requestURL('upload'), files=files, headers=headers)


def deleteFile(cwd):
    filename = input('Specify name of file to delete: ')
    data = { 'name': filename, 'path': cwd }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('DELETE', url=requestURL('file'), data=data, headers=headers)


def getInfo(cwd):
    filename = input('Specify name of file to get info from: ')
    data = { 'name': filename, 'path': cwd }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('GET', url=requestURL('fileinfo'), data=data, headers=headers)


def copyFile(cwd):
    filename = input('Specify name of file you want to copy: ')
    data = { 'name': filename, 'path': cwd }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('POST', url=requestURL('filecopy'), data=data, headers=headers)


def moveFile(cwd):
    filename = input('Specify name of file to move: ')
    newLocation = input('Specify new file location: ')
    data = { 'name': filename, 'path': cwd, 'newPath': newLocation }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('POST', url=requestURL('filemove'), data=data, headers=headers)


def changeDirectory(cwd):
    cwdBackup = cwd
    dirName = input('Specify name of directory to move to: ')

    for p in dirName.split('/'):
        if p == '.':
            continue
        elif p == '..':
            if (cwd == '/'):
                print('Incorrect path')
                return cwdBackup
            cwd = cwd[:(cwd.rfind('/') - 1)]
        else:
            cwd = cwd + p + '/'

    print('cwd = {0}'.format(cwd))
    return cwd


def showListOfFiles(cwd):
    data = { 'path': cwd }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('GET', url=requestURL('ls'), data=data, headers=headers)


def createDirectory(cwd):
    dirName = input('Sprecify name of new directory: ')
    data = { 'path': (cwd + dirName + '/') }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('POST', url=requestURL('mkdir'), data=data, headers=headers)


def deleteDirectory(cwd):
    dirName = input('Sprecify name of directory to delete: ')
    data = { 'path': (cwd + dirName + '/'), 'force': True }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request('DELETE', url=requestURL('dir'), data=data, headers=headers)


if __name__ == "__main__":
    answer = -1
    cwd = '/'

    print('Welcome to CLI Application for DFS!')
    printPossibleActions()
    
    while answer != 0:
        answer = int(input('Type a number of action, that you want to perform: '))

        if answer == 1:
            initializeFS()
        if answer == 2:
            createFile()
        if answer == 3:
            downloadFile()
        if answer == 4:
            uploadFile()
        if answer == 5:
            deleteFile()
        if answer == 6:
            getInfo()
        if answer == 7:
            copyFile()
        if answer == 8:
            moveFile()
        if answer == 9:
            cwd = changeDirectory(cwd)
        if answer == 10:
            showListOfFiles()
        if answer == 11:
            createDirectory()
        if answer == 12:
            deleteDirectory()
        if answer == 20:
            printPossibleActions()
