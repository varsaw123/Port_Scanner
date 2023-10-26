import socket
import sys

#entering domain name of ip address
print("Enter the domain name/ip address:")
HOST = input('')

#changing domain name to ip address
ip = socket.gethostbyname(HOST)
print("IP:", ip)

#Setting a ranges for port as default, fullport, important
print("Enter the range (Default: 0-1000, Full_Port: 0-65535, Important: 80, 443, 445, 8080, 20, 21, 22, 25):")
ranges = input("")
if ranges == 'Default':
    start_port, end_port = 0, 1000
elif ranges == "Full_Port":
    start_port, end_port = 0, 65535
elif ranges == "Important":
    important_range = [80, 443, 445, 8080, 20, 21, 22, 25]
    start_port, end_port = min(important_range), max(important_range)
else:
    print("Enter a valid range option (Default, Full_Port, or Important)")
    exit()

#making to connection to the ip and port ranges given by the user
try:
 for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((HOST, port))
    if result == 0:
        service_name = socket.getservbyport(port)
        print("Port {} is open. Service: {}".format(port, service_name))

    s.close()
    
#expection handling
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()