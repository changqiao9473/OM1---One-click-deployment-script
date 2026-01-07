# 🚀 OM1 One-Click Deployer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: macOS / Ubuntu](https://img.shields.io/badge/Platform-macOS%20%2F%20Ubuntu-blue.svg)](https://github.com/OpenMind/OM1)

---

<a name="english"></a>
## 🌐 English

### 📖 Introduction
This is a zero-friction deployment tool for the **OpenMind OM1** project. It automates the complex environment setup on Unix-based systems (macOS and Ubuntu), allowing users to join the Fabric network in minutes.

### ✨ Key Features
- **Auto-Healing**: Automatically detects and installs system-level dependencies (`PortAudio`, `FFmpeg`, `python3-dev`).
- **Modern Toolchain**: Utilizes `uv` for 10x faster Python package management.
- **Interactive Wizard**: Step-by-step configuration for `.env` (No code editing required).
- **Audio Optimized**: Pre-launch check to ensure a smooth `conversation` mode experience.

### 🚀 Quick Start
Run the following command in your terminal:

```bash
curl -O https://raw.githubusercontent.com/你的用户名/仓库名/main/om1_universal_deploy.py && python3 om1_universal_deploy.py
