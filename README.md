# SAME NETWORK CHATS

A lightweight LAN-based real-time chat system built with Python sockets and threading.
Supports password-protected server access, username handling, and multi-client messaging on the same network.

FEATURES
Password-protected server login
Real-time group chat over LAN (same network)
Multi-client support using threading
Username system for user identity
IP address validation on client side
Lightweight socket-based communication (no external frameworks)
TECHNOLOGIES USED
Python 3
socket (networking)
threading (multi-client handling)
re (IP validation)
PROJECT STRUCTURE
SameNetworkChats/
```
  ├── main.py        # Server and client chat system
  ├── README.md      # Documentation
```
## HOW IT WORKS

### The server:

Starts a TCP socket server
Requires a password before allowing connections
Accepts multiple clients using threads
Broadcasts messages to all connected users
CLIENT

### The client:

Connects using server IP
Validates IP format before connection
Enters password to join server
Chooses username
Sends and receives messages in real time
HOW TO RUN
```
1. START SERVER
python main.py

Select:

[1] Start Chat Server

Set a password when prompted.
```
```
2. JOIN AS CLIENT

Run the program on another device:

python main.py

Select:

[2] Join Chat

Then enter:

### Server IP address
Password
Username
EXAMPLE FLOW
SERVER OUTPUT
[SYSTEM] Listening on 5000...
[CONNECT] ('192.168.1.5', 54321) joined network
CLIENT OUTPUT
SERVER IP > 192.168.1.5
Password: *****
USERNAME > John
CONNECTED TO ALLHOME CHAT
```

## NOTES
```
Works only on the same network (LAN/WiFi)
Port 5000 must be open on firewall
Use correct server IP and correct format for connection
```
## FUTURE IMPROVEMENTS:
```
Make it not only within LAN
Add private messaging (/msg)
Add admin controls (/kick, /ban)
Save chat logs locally
GUI version using Tkinter or PyQt
Planned: encryption layer for secure data transmission
SECURITY ROADMAP
```

Future versions will implement end-to-end encryption for all messages, improving privacy and preventing packet interception or sniffing.

## AUTHOR

### iamjhonaldrix/b3rl1n

### LICENSE

This project is for educational purposes only.
