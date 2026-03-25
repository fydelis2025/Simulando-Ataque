import socket

target = input("Alvo: ")
ports = [21, 22, 80, 443]

for port in ports:
    s = socket.socket()
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Porta {port} aberta")
    else:
        print(f"[-] Porta {port} fechada")

    s.close()