<div align="center">

# ⚡ PikachuCLI ⚡

**A lightweight, interactive Python command-line interface with local user registration and credential management.**

![GitHub Release](https://img.shields.io/badge/release-0.1.0--alpha-orange?style=for-the-badge&logo=git)
![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

</div>

---

## 🚀 About PikachuCLI

**PikachuCLI** is a modular command-line tool built from scratch in Python. It features a clean ASCII welcome screen, single-user registration (SUR), secure local credential storage, and an extensible command architecture. Designed for simplicity and performance right inside your terminal.

---

## 📂 Project Structure

```text
PikachuCLI/
│
├── register.py              # Handles initial user setup and token generation
├── welcome.py               # Main dashboard & command router
├── db/
│   └── credentials.json     # Local JSON storage for user session data
└── commands/
    ├── clear_credentials.py # Securely resets account data
    └── help.py              # Displays available CLI commands
