PROTOCOL = "http"
MASTER_IP = "localhost"
MASTER_PORT = "4000"

def requestURL(req):
    return PROTOCOL + "://" + MASTER_IP + ":" + MASTER_PORT + "/api/" + req


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
    # TODO File system initializing
    return


def createFile():
    filename = input('Specify name of new file to create: ')
    # TODO Creating an empty file


def downloadFile():
    filename = input('Specify name of file to download: ')
    # TODO File Downloading


def uploadFile():
    filename = input('Specify name of file to upload: ')
    # TODO File Uploading


def deleteFile():
    filename = input('Specify name of file to delete: ')
    # TODO Deleting file


def getInfo():
    filename = input('Specify name of file to get info from: ')
    # TODO Getting file info


def copyFile():
    filename = input('Specify name of file you want to copy: ')
    # TODO Creating a file copy


def moveFile():
    filename = input('Specify name of file to move: ')
    newLocation = input('Specify new file location: ')
    # TODO Moving file to a new location


def changeDirectory():
    dirName = input('Sprecify name of directory to move to: ')
    # TODO cd


def showListOfFiles():
    # TODO ls
    return


def createDirectory():
    dirName = input('Sprecify name of new directory: ')
    # TODO mkdir


def deleteDirectory():
    dirName = input('Sprecify name of directory to delete: ')
    # TODO rm -rf


if __name__ == "__main__":
    answer = -1

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
            changeDirectory()
        if answer == 10:
            showListOfFiles()
        if answer == 11:
            createDirectory()
        if answer == 12:
            deleteDirectory()
        if answer == 20:
            printPossibleActions()
