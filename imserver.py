import socket                   # Import socket module
import Image
import os,sys
import io
import time
import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
#host = socket.gethostname()     # Get local machine name
print 'Server listening....'
s.bind(('', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.



while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr   
    img_pkt_rcvd=conn.recv(625583)
    img_file=open('Server_img.jpg','wb')
    img_file.write(img_pkt_rcvd)
    img_file.close()
    

    img_modi=Image.open('Server_img.jpg')                              #Compressing Image
   
    img_modi.save("Server_img_modified.jpg",optimize=True,quality=25)
    
    #img_modi=Image.open('Server_img.jpg').convert('L')                #Converting to Gray Scale
    #img_modi.save('Server_img_modified.jpg')
    img_modifile=open('Server_img_modified.jpg','rb')
    img_pkt_send=img_modifile.read(625583)
    size=conn.send(img_pkt_send)
    print 'Size of modified image sent=', size


  

    
    









