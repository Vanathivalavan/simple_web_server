# EX01 Developing a Simple Webserver

# Date: 20.09.2025
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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TCP/IP Model – Layers Explained</title>
  <style>
    body 
    {
      background: linear-gradient(135deg, #f7f7f7, #dbe9f6);
      color: #333;
      font-family: "Segoe UI", Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    header 
    {
      background-color: #004d99;
      color: #ffffff;
      padding: 30px;
      text-align: center;
    }
    header h1 
    {
      margin: 0;
      font-size: 2.5em;
    }
    header p 
    {
      margin: 5px 0 0;
      font-style: italic;
    }

    .container 
    {
      max-width: 900px;
      margin: auto;
      padding: 20px;
    }

    h2
    {
      color: #004d99;
      border-left: 5px solid #ff6600;
      padding-left: 10px;
    }

 
    table 
    {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    th, td
    {
      padding: 14px;
      border: 1px solid #ccc;
      text-align: left;
    }

    th 
    {
      background-color: #ff6600;
      color: white;
      font-size: 1.1em;
    }

    tr:nth-child(even) 
    {
      background-color: #f2f2f2;
    }

    ul 
    {
      background: #e8f0fe;
      border-left: 4px solid #004d99;
      padding: 15px 25px;
      list-style-type: square;
    }

    footer 
    {
      background: #004d99;
      color: white;
      text-align: center;
      padding: 15px 0;
      margin-top: 40px;
    }
  </style>
</head>
<body>

  <header>
    <h1>TCP/IP Network Model</h1>
    <p>Understanding the Layers of Modern Networking</p>
  </header>

  <div class="container">
    <h2>About TCP/IP Model</h2>
    <p>
      The TCP/IP model is a concise framework used to transmit data across networks. 
      It simplifies communication by splitting tasks into different layers, each with its own function.
    </p>

    <h2>Layers of TCP/IP Model</h2>
    <table>
      <tr>
        <th>Layer</th>
        <th>Main Function</th>
        <th>Examples</th>
      </tr>
      <tr>
        <td><b>Application Layer</b></td>
        <td>Network services to users and applications.</td>
        <td>HTTP, FTP, SMTP</td>
      </tr>
      <tr>
        <td><b>Transport Layer</b></td>
        <td>Ensures reliable or fast delivery of data.</td>
        <td>TCP, UDP</td>
      </tr>
      <tr>
        <td><b>Network Layer</b></td>
        <td>Logical addressing and routing of packets.</td>
        <td>IP, ICMP</td>
      </tr>
      <tr>
        <td><b>Data Link Layer</b></td>
        <td>Frames data, error recovery & retransmissions.</td>
        <td>Ethernet, ARP</td>
      </tr>
      <tr>
        <td><b>Physical Layer</b></td>
        <td>Physical interface for data transmission.</td>
        <td>Cables, Hubs</td>
      </tr>
    </table>

    <h2>Key Points</h2>
    <ul>
      <li>TCP/IP model has 5 layers – simpler than OSI’s 7 layers.</li>
      <li>Layers communicate with the ones directly above and below.</li>
      <li>It is the foundation of modern Internet communication.</li>
    </ul>
  </div>

  

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

```
# OUTPUT:

![alt text](<Screenshot 2025-09-22 120612.png>)

![alt text](<Screenshot 2025-09-22 120623.png>)


# RESULT:
The program for implementing simple webserver is executed successfully.
