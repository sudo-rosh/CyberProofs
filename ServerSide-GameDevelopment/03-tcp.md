# 🌐 TCP (Transmission Control Protocol)

**TCP**, or **Transmission Control Protocol**, is a **connection-oriented, reliable transport protocol** that sits at the **transport layer** of the OSI model.  

- Establishes a connection between two hosts  
- Ensures **data is delivered accurately and in order**  
- Provides **error checking** and retransmission of lost data  
- Implements **flow control** and **congestion control** for efficient network usage  

TCP is essential for applications where **reliability is critical**, such as online banking, email, and multiplayer games that require guaranteed delivery.  

---

## 🔹 Checksum
- 16-bit field in the TCP header used for **error checking**.  
- Sender computes and attaches checksum; receiver recalculates and compares.  
- If mismatch → packet considered corrupted → **retransmission occurs**.  
- Helps maintain data integrity, but not foolproof for all possible errors.  

---

## 🔹 Segment Structure
TCP divides data into smaller chunks called **segments**.  

**A TCP segment consists of:**  
- **Header** – contains:  
  - Source Port  
  - Destination Port  
  - Sequence Number  
  - Acknowledgment Number  
  - Data Offset  
  - Reserved Bits  
  - Control Bits (e.g., SYN, ACK, FIN)  
  - Window Size  
  - Checksum  
  - Urgent Pointer  
  - Options  
- **Data** – the actual payload being transmitted  

Segmentation allows **reliable, ordered transmission** of data across networks. Understanding TCP segments is key to understanding how much of the Internet functions.  

---

## 🔜 Operations (To Be Completed)

- [ ] **Max Segment Size (MSS)** – Defines maximum segment data size to avoid fragmentation  
- [ ] **Window Scaling** – Adjusts window size for high-latency or high-bandwidth networks  
- [ ] **Connection** – TCP connection establishment (Three-Way Handshake)  
- [ ] **Resource Usage** – How TCP consumes network and system resources  
- [ ] **Max Segment Scaling** – Scaling MSS for large networks  
- [ ] **Timestamp** – Used to measure RTT and manage packet timing  
- [ ] **Data Transfer** – Mechanism for sending and receiving data reliably  
- [ ] **Out-of-Band Data** – Handling urgent data with TCP  
- [ ] **Selective Acknowledgment (SACK)** – Acknowledging specific segments for efficiency

---

## 🔜 Flow Control and Related

- [ ] **Congestion Control** – Avoid network congestion (Slow Start, Fast Retransmit, etc.)  
- [ ] **Reliable Transmission** – Retransmission mechanisms for lost segments  
- [ ] **Flow Control** – Window-based control to prevent overwhelming the receiver  
- [ ] **Error Detection** – Detect and handle transmission errors

---

## 🔜 Vulnerabilities (To Be Completed)

- [ ] **Denial of Service (DoS)** – TCP-based DoS attacks  
- [ ] **Connection Hijacking** – Unauthorized takeover of TCP connections  
- [ ] **Veto** – Mechanisms to prevent or mitigate TCP attacks

---

> ⚠️ Notes for Later: Each subsection will include explanations, diagrams if necessary, and code examples when implemented. The checklist shows remaining topics to be completed for a comprehensive TCP module.
