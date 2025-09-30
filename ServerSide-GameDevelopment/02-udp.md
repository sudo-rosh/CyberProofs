# 🌐 UDP (User Datagram Protocol)

**UDP**, or **User Datagram Protocol**, is a connectionless communications protocol used to send data over the internet. Unlike TCP, UDP **does not ensure delivery** of data packets. It transmits **datagrams**—independent packets of data—without establishing a handshake between sender and receiver. This makes UDP **faster but less reliable**.  

UDP is commonly used for **time-sensitive applications** where dropped packets are acceptable, such as:  
- Live video streaming  
- Voice over IP (VoIP)  
- Online multiplayer gaming  

---

## 🔹 Reliability
UDP **does not guarantee delivery** of packets.  
- No acknowledgments are sent by the receiver.  
- Packets may arrive out of order or not at all.  
- For highly reliable transmissions, TCP is preferred.  

---

## 🔹 Datagram
A **datagram** is the **basic unit of data** in UDP communication.  
- Each datagram is independent.  
- Datagrams may arrive **out of order or be lost**.  
- Contains: sender info, recipient info, payload, and size specifications.  

---

## 🔹 Congestion Control
- UDP **does not provide built-in congestion control**.  
- Developers may implement custom mechanisms if needed.  
- TCP, by contrast, dynamically adjusts data rates to prevent network overload.  

---

## 🔹 Checksum
- A **checksum** ensures data integrity.  
- Sender calculates a sum of all bytes in the packet and includes it in the UDP header.  
- Receiver recalculates and compares; mismatch → packet dropped.  
- **No retransmission** occurs in UDP.  

---

## 🔹 Packet Structure
UDP headers are simple and consist of **4 fields (2 bytes each)**:  
1. **Source Port** – tracks responses  
2. **Destination Port** – delivers the datagram  
3. **Length** – size of the datagram (header + data)  
4. **Checksum** – validates data integrity  
