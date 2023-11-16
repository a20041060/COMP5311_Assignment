import ssl
import socket
def socket_conn():
# Define and open socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Input the host from user
  clientInput = input('Please input link here: ') 
  # Connect the host with 443 port (instead of port 80, 443 allows data transmission over a secure network) 
  s.connect((clientInput, 443))
  # Use ssl to wrap socket and define protocol
  s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
  # Set header and method
  s.sendall(b"GET / HTTP/1.1\r\nConnection: close\r\n\r\n")

  while True:
      # define receive buffer size
      resp = s.recv(4096).decode()
      if not resp:
        # Close the socket if not response
        s.close()
        break
      print(resp)

while True:
   socket_conn()
# End
