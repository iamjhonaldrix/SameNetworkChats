import socket
import threading
import re

HOST = "0.0.0.0"
PORT = 5000

clients = []

def broadcast(message, sender_conn=None):
    for conn, _ in clients:
        if conn != sender_conn:
            try:
                conn.send(message.encode())
            except:
                pass

def handle_client(conn, addr):
    try:
        conn.send("ENTER_NAME>".encode())
        name = conn.recv(1024).decode().strip()

        clients.append((conn, name))
        broadcast(f"[+] {name} joined the chat -")

        while True:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            broadcast(f"{name}: {msg}", conn)

    except:
        pass
    finally:
        conn.close()
        clients.remove((conn, name))
        broadcast(f"[-] {name} left the chat ")

def start_server():
    PASSWORD = input("Set a password for the underground chatroom: ")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("""
░╔═════╗╔═╗░╔════╗░░╔═════╗╔══════╗╔═╗░░░░░╔═╗░╔════╗░╔═╗░░╔═╗╔══════╗╔══════╗╔═╗░░╔═╗
╔╝██████║██╔╝█████╗╔╩██████╚███████║██░╔═╗░║██╔╝█████╗║██░░║██╚███████╚███████║██░░║██
╚██═══╗░║██║██░░║██╚██══╝██░░╔══╝██║██╔╝██╗║██║██░░║██║██══╝██░░░░░║██░░░░░║██║██══╝██
░╚█████╗║██║██░░║██╔╩██████░░╚█████║██╝████╝██║██░░║██║███████░░░░░║██░░░░░║██║███████
╔════╝██║██╚██══╝██╚██══╝██╔════╝██║████░╚████╚██══╝██║██░░║██░░░░░║██░░░░░║██╚██══╝██
╚██████░╚██░╚█████░░╚██████╚███████╚███░░░╚███░╚█████░╚██░░╚██░░░░░╚██░░░░░╚██░╚█████░
""")

    print(f"[SYSTEM] Listening on {PORT}...\n")

    while True:
        conn, addr = server.accept()
        print(f"[CONNECT] {addr} joined network")

        conn.send(b"Enter password: ")

        client_pass = conn.recv(1024).decode().strip()

        if client_pass != PASSWORD:
            conn.send(b"bye! You're not a real allhomebois!")
            conn.close()
            print("Wrong password attempt. Connection closed.")
            continue
        conn.send(b"Access granted yow welcome G!")

        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

def start_client():
    ip_pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"

    valid = False

    while not valid:
        ip = input("SERVER IP > ")

        if re.match(ip_pattern, ip):
            valid = True
        else:
            print("invalid input, try again homeboi!")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, PORT))

    print(client.recv(1024).decode())

    password = input("Password: ")
    client.send(password.encode())

    response = client.recv(1024).decode()
    print(response)

    if "bye!" in response:
        client.close()
        return
    while True:
        name = input("USERNAME > ")
        client.recv(1024)
        client.send(name.encode())

        if any(n == name for _, n in clients):
            conn.send(b"Name already taken, try again!")
            continue

        valid_name = name
        break

    print("\n CONNECTED TO ALLHOME CHAT \n")

    def receive():
        while True:
            try:
                msg = client.recv(1024).decode()
                print(f"\n{msg}")
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    while True:
        msg = input(f"{name} > ")
        client.send(msg.encode())

if __name__ == "__main__":
    print("""
╔══════════════════════════════╗
║       ALLHOMEBOIS CHAT       ║
║     Underground Home Chat    ║
╚══════════════════════════════╝
""")

    choice = input("[1] Start Chat Server\n[2] Join Chat\n> ")

    if choice == "1":
        start_server()
    else:
        start_client()
