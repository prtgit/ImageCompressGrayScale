import socket                   # Import socket module
import os,sys
import Image
import time
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect(('127.0.0.1', port))
print 'Client connected'
#with open('Simba.jpg', 'r') as f:
#    print 'file opened'
#    file_content=f.read(256467)
#    s.send(file_conent)
#    print 'file sent'
#with Image.open('simba_1024.JPG') as img:
#    print 'file_opened'
#    print 'Image Size='
#    print img.size
#    s.send(img)
#    print 'file sent'  
with open("Simba256.jpeg","rb") as f:
     print 'file opened'
     file_content=f.read(625583)
     #file_content=f.readlines()
     size=s.send(file_content)
     print 'Size of file=',size
     print 'file sent'
     img_pkt_rcvd=s.recv(625583)
     img_file=open('Image_client','wb')
     img_file.write(img_pkt_rcvd)
     img_file.close()
     print 'Modified image received at client'
    
