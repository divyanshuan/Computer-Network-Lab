import time, socket
# Function to find the Checksum of Sent Message
def findReciverChecksum(RecivedMessage):
    k=8
    # Dividing sent message in packets of k bits.
    c1 = RecivedMessage[0:k]
    c2 = RecivedMessage[k:2*k]
    c3 = RecivedMessage[2*k:3*k]
    c4 = RecivedMessage[3*k:4*k]

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
        Checksum += '1'
     else:
        Checksum += '0'

    #checksum with ones complement 
    return Checksum


def msgSeprator(rcvdmsg):
    messageary=rcvdmsg.split(" ")
    return messageary


def connection():
    print("Initialising Server....\n")
    time.sleep(1)

    # creating a socket object
    s = socket.socket()

    # get local machine name
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 1234

    #bind to the port
    s.bind((host, port))
    print(host, "(", ip, ")\n")


    #queue upto 1 requests
    s.listen(1)
    print("\nWaiting for incoming connections...\n")

    #estabilshed a connection 
    conn, addr = s.accept()
    #print message if connection established
    print("Received connection from ", addr[0], "(", addr[1], ")\n")

    # Receive no more than 1024 bytes
    ClientMessage = conn.recv(1024)
    ClientMessage = ClientMessage.decode()
    print(ClientMessage)

    recivedmsg,checksum=msgSeprator(ClientMessage)

    print(f"Message  from client is : {recivedmsg}")
    print(f"Checksum  from client is : {checksum}")

    # recivedmsg="10000101011000111001010011101101"
    # if wrong msg

    recivercheksum=findReciverChecksum(recivedmsg)


    time.sleep(2)


    # sending checksum to client 
    conn.send(recivercheksum.encode())

connection()
