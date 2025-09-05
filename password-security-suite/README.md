# Password Security Suite 🔐

A simple Python program that checks the strength of passwords and gives feedback to help users create strong, secure passwords.  

---

## **Features**

- Checks if a password meets **minimum length** requirements.  
- Ensures the password contains **uppercase and lowercase letters**.  
- Ensures the password contains **numbers**.  
- Ensures the password contains **special characters** (e.g., `!@#$%^&*()-+`).  
- Rates the password strength as **Weak, Medium, Strong, or Very Strong**.  
- Provides **specific suggestions** to improve weak passwords.  
- Optional: Keeps a log of tested passwords (if enabled in `main.py`).  

---

## **Installation**

1. Clone this repository:  
   ```bash
   git clone <your-repo-link>

2. Navigate to the project folder:
  ```bash
  cd CyberProofs/password-security-suite

3. (Optional) Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate      # Linux/macOS
  venv\Scripts\activate         # Windows

4. Install dependencies (if any):
  ```bash
  pip install -r requirements.txt

## **Usage**

Run the program:
    ```bash
    python main.py
- Enter a password when prompted.  
- The program will display the **strength rating** and **feedback**.  

**Example:**
  ```text
  Enter your password: Abc123
  Your password strength is: Medium (2/4)
  → Password must contain at least one special character
  → Password must be at least 8 characters