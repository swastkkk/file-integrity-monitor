# 🔐 File Integrity Monitoring System

A simple cybersecurity tool developed using Python to detect unauthorized or accidental modifications to files using **SHA-256 cryptographic hashing**.

---

## 📌 Project Overview

File integrity is an important aspect of cybersecurity. If an important file is modified without authorization, the change may go unnoticed.

This project provides a simple way to monitor a file's integrity by:

1. Generating its SHA-256 hash.
2. Storing the original hash as a baseline.
3. Generating the hash again during subsequent checks.
4. Comparing the current hash with the original hash.
5. Alerting the user if the hashes are different.

---

## 🎯 Problem Statement

Important files may be modified accidentally or without authorization.

A simple file integrity monitoring mechanism is required to identify whether a monitored file has changed since its original state.

---

## 💡 Proposed Solution

The system uses **SHA-256 hashing** to create a unique cryptographic fingerprint of the monitored file.

If the file remains unchanged:

```text
Original Hash = Current Hash
        ↓
   File is Safe

If the file is modified:

Original Hash ≠ Current Hash
        ↓
 Modification Detected
        ↓
   Security Alert

⚙️ Technologies Used
Python
SHA-256
hashlib
JSON
VS Code
GitHub

No external Python libraries are required.

🏗️ Project Structure
File-Integrity-Monitor/
│
├── integrity_checker.py
├── monitored_file.txt
├── hashes.json
│
├── screenshots/
│   ├── baseline.png
│   ├── file-safe.png
│   └── modification-detected.png
│
└── README.md
🔄 How It Works
              Monitored File
                    ↓
              SHA-256 Hash
                    ↓
             Store Baseline
                    ↓
              Check File Later
                    ↓
             Generate New Hash
                    ↓
              Compare Hashes
                ↙       ↘
             Same      Different
              ↓            ↓
            SAFE       🚨 ALERT

🚀 How to Run
1. Clone the repository
git clone <your-repository-url>
2. Open the project folder
cd File-Integrity-Monitor
3. Run the program
python integrity_checker.py
🧪 Demonstration
Test 1: File Unchanged

When the monitored file has not been modified:

[✓] STATUS: FILE INTEGRITY VERIFIED
[✓] No modification detected.
Test 2: File Modified

After changing the contents of the monitored file:

[!] SECURITY ALERT
[!] File modification detected!
[!] Integrity verification FAILED.

The alert occurs because the SHA-256 hash of the modified file differs from the stored baseline hash.

📊 Results

The system successfully demonstrates basic file integrity monitoring by detecting changes made to a monitored file.

Condition	Result
File unchanged	✅ Integrity Verified
File modified	🚨 Modification Detected
🎓 Key Learning Outcomes

Through this project, I gained practical understanding of:

Cryptographic hashing
SHA-256
File handling in Python
Data integrity
Basic security monitoring
Python programming
Project documentation using GitHub

🔮 Future Improvements

Possible future enhancements include:

Monitoring multiple files
Automatic periodic monitoring
Email/security notifications
Graphical user interface
Monitoring entire directories
Maintaining an activity log
Integration with security monitoring systems

👨‍💻 Author

Swastik Gupta