import socket
import termcolor

def scan(targets, ports):
    print('\n' + ' Starting Scan For ' + str(targets))
    for port in range(1,ports):
        port_scan(targets, port)



def port_scan(ip_address, port):
    try:
        #create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect socket to port and IP
        sock.connect((ip_address, port))
        #print(f"[+] connected to port {port}")
        try:
            banner = s.recv(1024).decode()
            termcolor.cprint("[+] port {} is open with banner {}" .format(port, banner), 'yellow')
        except:
            termcolor.cprint(f" [+] port {port} is open ", 'green')
        
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets To Scan(split up by ,): ")
ports = int(input("[*] Enter How Many Ports Would You Like To Scan: "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'cyan'))
    for ip_address in targets.split(','):
        scan(ip_address.strip(' '),ports)
else:
    scan(targets,ports)

