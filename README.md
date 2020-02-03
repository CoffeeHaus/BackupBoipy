Client will take pull all filenames and md5s of the files in the user directory
The client will then send this infomation as a plain text file for now.
data will be in json format

""""
C:\Users\andrew\PycharmProjects\Testfile.txt, [md5 hash]

""""
hasing code:
hashlib.md5(w).hexdigest()[:9]

Server will response with a series of numbers that corelates to each file that it is requesting.
