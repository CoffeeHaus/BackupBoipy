Client will take pull all filenames and md5s of the files in the user directory
The client will then send this infomation as a plain text file for now.
data will be in json format


""""
init\0
C:\Users\andrew\PycharmProjects\Testfile.txt, [md5 hash]
C:\Users\andrew\PycharmProjects\Anotherfile.txt, [md5 hash]
""""

""""
resp\0
1,2
""""

""""
file\0
[zipped file]
""""

hasing code:
hashlib.md5(w).hexdigest()[:9]

Server will response with a series of numbers that corelates to each file that it is requesting.
The client then will send files one at a time, if connection is lost then the process restarts
