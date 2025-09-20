# EX01 Developing a Simple Webserver

# Date: 19.09.2025
# AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol suite.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''
<html>

<h1>
    TCP/IP NETWORK MODEL
</h1>


<br>


<h3>
    Application Layer:
</h3>

<h4>
    Provides network services to users and applications.
</h4>

<h4>
    Eg:HTTP,FTP
</h4>

<h3>
    Transport Layer:
</h3>
<h4>
    Ensures reliable or fast delivery of data between devices.
</h4>

<h3>
    Network Layer:
</h3>
<h4>
    Logical addressing and rounting of data packet from source to destination by identifing neighbors.
</h4>

<h3>
  Data Link Layer:

</h3>

<h4>
    combine raw data into frames,errorrecovery and retransmissions.
</h4>

<h3>
    Physical Layer:
</h3>
<h4>
    Provide the Physical interface for data transmission.
</h4>

</html>


'''
          

class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
httpd=HTTPServer(server_address,Myserver)
httpd.serve_forever()
```
# OUTPUT:
![alt text](<WhatsApp Image 2025-09-20 at 08.16.34_e3a4a4ac.jpg>)

![alt text](<WhatsApp Image 2025-09-20 at 08.16.35_c0fa01cf.jpg>)


# RESULT:
The program for implementing simple webserver is executed successfully.
