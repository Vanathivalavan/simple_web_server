from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''
<html>
<body bgcolor="purple" style="color: white;">

<h1>
    TCP/IP NETWORK MODEL
</h1






<h3>
    Application Layer:
</h3>

<h4>
Presents data to the users,Encoding and session Controit,data translation with help of protocols.
    </h4>


<h3>
    Transport Layer:
</h3>
<h4>
    Support end to end Connection establishment of data segments and delivery with error control by using TCP and UDP protocols.
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


</body>

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