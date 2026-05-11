📡 SameNetworkChats

A lightweight LAN-based real-time chat system built with Python sockets and threading.
Supports password-protected server access, username handling, and multi-client messaging on the same network.

🚀 Features
🔐 Password-protected server login
💬 Real-time group chat (LAN / same network)
👥 Multi-client support using threads
🧠 Username system for identity
🚫 IP validation on client side
⚡ Lightweight socket-based communication (no frameworks needed)
🛠️ Technologies Used
Python 3
socket (networking)
threading (multi-client support)
re (IP validation)
📁 Project Structure
SameNetworkChats/
│
├── main.py        # Server + Client chat system
├── README.md      # Project documentation
⚙️ How It Works
🖥️ Server
Starts a TCP socket server
Requires a password before allowing access
Accepts multiple client connections
Broadcasts messages to all connected users
💻 Client
Connects using server IP
Validates IP format
Enters password to join server
Chooses username
Sends/receives messages in real time
▶️ How to Run
1. Start the Server
python main.py

Select:

[1] Start Chat Server

Set a password when prompted.

2. Join as Client

Run the same file on another device:

python main.py

Select:

[2] Join Chat

Then enter:

Server IP
Password
Username
🌐 Example Flow
Server:
[SYSTEM] Listening on 5000...
[CONNECT] ('192.168.1.5', 54321) joined network
Client:
SERVER IP > 192.168.1.5
Password: *****
USERNAME > John
CONNECTED TO ALLHOME CHAT
⚠️ Notes
Works only on same network (LAN/WiFi)
Firewall may block port 5000
Use correct server IP (not localhost if connecting from another device)
🔧 Future Improvements
Add private messaging (/msg)
Add admin commands (/kick, /ban)
Save chat logs
GUI version (Tkinter / PyQt)
🔐 Encryption layer for secure data transmission (planned future upgrade)
🔐 Security Roadmap

I am currently planning to improve this project by adding encryption for all transmitted data, making the chat system more secure and resistant to packet sniffing or unauthorized interception.

👨‍💻 Author

Developed by @iamjhonaldrix

📜 License

This project is for educational purposes.
