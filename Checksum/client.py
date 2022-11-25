import time, socket
# Function to find the Checksum of Sent Message
def findChecksum(SentMessage):
    k=8
    # Dividing sent message in packets of k bits.
    c1 = SentMessage[0:k]
    c2 = SentMessage[k:2*k]
    c3 = SentMessage[2*k:3*k]
    c4 = SentMessage[3*k:4*k]
    # Calculating the binary sum of packets
    Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]
    # Adding the overflow bits
    if(len(Sum) > k):
        x = len(Sum)-k
        Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
    if(len(Sum) < k):
        Sum = '0'*(k-len(Sum))+ Sum
    # Calculating the complement of sum
    Checksum = ''
    for i in Sum:
     if(i == '1'):
        Checksum += '0'
     else:
        Checksum += '1'
    return Checksum
def chekCheksum(checksumC,cheksumS):
    if len(checksumC)!=len(cheksumS):
        return False
    for i in range(len(checksumC)):
        if checksumC[i]==cheksumS[i]:
            return False
    return True
def connectiontoserver():
    print("Initialising Client....\n")
    time.sleep(1)
    # create a socket object
    s = socket.socket()
    # get local machine name
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    print(shost, "(", ip, ")\n")
#getting host info

# host = input(str("Enter server address: "))
    host= input(str("Enter server address: "))
    port = 1234
    print("\nTrying to connect to ", host, "(", port, ")\n")
    time.sleep(1)
    # connecting to the host
    s.connect((host, port))
    print("Connected...\n")
    # sendmsg = "10010101011000111001010011101100"
    sendmsg = "1000100010001000100010001000"
    cheksum=findChecksum(sendmsg)
    finalsend=sendmsg+" "+cheksum
    #sending name to host
    s.send(finalsend.encode())
    # Receive no more than 1024 bytes
    cheksumS = s.recv(1024)
    cheksumS = cheksumS.decode()
    # Printing Checksum
    print("SENDER SIDE CHECKSUM: ", cheksum.strip())
    print("RECEIVER SIDE CHECKSUM: ", cheksumS.strip())
    # If sum = 0, No error is detected
    if(chekCheksum(cheksum,cheksumS)):
        print("Sum of Sender and Reciver Checksums is 0")
        print("STATUS: ACCEPTED")
    else:
        print("Sum of Sender and Reciver Checksums is 0")
        print("STATUS: DENIED")
        
connectiontoserver()
