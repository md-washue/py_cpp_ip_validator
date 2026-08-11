# 🌐  IP Address Validator

A high-performance desktop application that validates IPv4 and IPv6 addresses. 

This project demonstrates cross-language integration by pairing a rapid **Python** graphical user interface with a low-level **C++** backend engine. The backend utilizes the industry-standard `inet_pton` function for precise and secure network protocol validation.

## ✨  Features
* **Dual-Language Architecture:** Python handles the UI and session logging, while C++ handles heavy-duty string parsing.
* **Strict Validation:** Accurately identifies Valid IPv4, Valid IPv6, and Invalid network addresses.
* **Session Logging:** Automatically logs all validation attempts with timestamps to a local CSV file (`history/validation_history.csv`).
* **Cross-Platform:** The C++ backend can be compiled for Linux, macOS, or Windows.

