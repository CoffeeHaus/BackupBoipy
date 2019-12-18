with open(text_file, "wb") as fw:
    print("Receiving..")
    while True:
        print('receiving')
        data = conn.recv(32)
        if data == b'BEGIN':
            continue
        elif data == b'ENDED':
            print('Breaking from file write')
            break
        else:
            print('Received: ', data.decode('utf-8'))
            fw.write(data)
            print('Wrote to file', data.decode('utf-8'))
    fw.close()
    print("Received..")
