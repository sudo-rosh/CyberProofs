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
