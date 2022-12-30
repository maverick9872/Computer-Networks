from http import server
import socket

HOST = "127.0.0.1"  
PORT = 1234
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((HOST,PORT))
aff="yes"
while(aff=="yes"):
    msg= server.recv(2048)
    msg= msg.decode("utf-8")
    print(msg)
    ans=str(input( "Please enter the course you want to know about :)\n"))
    server.send(bytes(ans,"utf-8"))
    resp= server.recv(16384)
    resp= resp.decode("utf-8")
    print(resp)
    choice = str(input("\nEnter your choice:\n"))
    server.send(bytes(choice,"utf-8"))
    y= input("Do you want to look at the subject hours?")
    server.send(bytes(y,"utf-8"))
    p= server.recv(1024)
    p=p.decode("utf-8")
    print(f"The hours required for the subject is: {p} ")
    buy= input("Do you want to take up this course? ")
    server.send(bytes(buy,"utf-8"))
    prn= server.recv(2048)
    prn=prn.decode("utf-8")
    print(prn)
    mode=input("Enter mode of payment: ")
    server.send(bytes(mode,"utf-8"))
    snd=server.recv(2048)
    snd= snd.decode("utf-8")
    print(snd)
    aff=input("\nDo you want to take a look at the courses again?\n")
print("Thank you for visiting Amrita School")
