from http import server
import socket

HOST = "127.0.0.1"  
PORT = 1234
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
while True:
    client,address = server.accept()
    print(f"Connected by : {address}") 
    wc= "Welcome to Socket Amrita School\n\n"
    client.send(bytes(wc,"utf-8"))
    ans= client.recv(1024)
    ans=ans.decode("utf-8")
    print(ans)
    if(ans=="CSE"):
        resp="The subjects are \n1.Physics \n2.Maths \n3.C Programming"
        client.send(bytes(resp,"utf-8"))
    elif(ans=="Biology"):
        resp="The subjects are \n1.Biology \n2.Zoology \n3.Botany"
        client.send(bytes(resp,"utf-8"))
    elif(ans=="Commerce"):
        resp="The subjects are \n1.commerce \n2.Buisness maths \n3.Statistics"
        client.send(bytes(resp,"utf-8"))
    else:
        resp="The entered course is currently unavailable\n"
        client.send(bytes(resp,"utf-8"))

    choice= client.recv(1024)
    choice=choice.decode("utf-8")
    y= client.recv(1024)
    y=y.decode("utf-8")
    if(y=="yes"):
        if(choice=="1"):
            p="32 hours"
            client.send(bytes(p,"utf-8"))
        elif(choice=="2"):
            p="27 hours"
            client.send(bytes(p,"utf-8"))
        elif(choice=="3"):
            p="40 hours"
            client.send(bytes(p,"utf-8"))
    buy= client.recv(1024)
    buy=buy.decode("utf-8")
    if(buy=="yes"):
        prn= "Thanks for picking up this course"
        client.send(bytes(prn,"utf-8"))
    else:
        client.close()
        break
    mode= client.recv(1024)
    mode=mode.decode("utf-8")
    if(mode=="cash"):
        snd="\nPlease pay the required amount to the cashier\n"
        client.send(bytes(snd,"utf-8"))
    elif(mode=="gpay"):
        snd="\nPlease scan the QR code"
        client.send(bytes(snd,"utf-8"))
    else:
        snd="\nPlease do the necessary "
        client.send(bytes(snd,"utf-8"))
    
        


    client.close()
    
