import os
import subprocess
import sys
import platform
import shutil

# =======================================================
# OM1 One-Click Deployment Script (macOS & Ubuntu)
# Mission: Zero-friction setup for OpenMind OM1 Agent
# =======================================================

def log(icon, message):
    print(f"{icon} {message}")

def run_cmd(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        log("❌", f"Error executing: {command}")
        return False

def check_env():
    os_type = platform.system()
    log("🔍", f"Detecting OS: {os_type}")
    
    if os_type == "Darwin": # macOS
        log("🍎", "Configuring for macOS...")
        if not shutil.which("brew"):
            log("⚠️", "Homebrew not found. Please install it first at https://brew.sh/")
            sys.exit(1)
        run_cmd("brew install portaudio ffmpeg git")
        
    elif os_type == "Linux": # Ubuntu/Debian
        log("🐧", "Configuring for Linux (Ubuntu/Debian)...")
        run_cmd("sudo apt-get update")
        run_cmd("sudo apt-get install -y python3-dev portaudio19-dev ffmpeg git python3-pip")
    
    else:
        log("❌", f"OS {os_type} is not fully supported by this script yet.")
        sys.exit(1)

def setup_uv():
    log("🐍", "Installing 'uv' for high-speed dependency management...")
    run_cmd(f"{sys.executable} -m pip install uv")

def configure_project():
    # Clone if not exists
    if not os.path.exists("OM1"):
        log("🚚", "Cloning OM1 repository...")
        run_cmd("git clone https://github.com/OpenMind/OM1")
    
    os.chdir("OM1")
    
    # Interactive Configuration
    if not os.path.exists(".env"):
        print("\n" + "⚙️  " + "="*30)
        eth = input("🔹 Enter ETH_ADDRESS (EVM Address): ").strip()
        key = input("🔹 Enter M_API_KEY (from portal.openmind.orgr: ").strip()
        urid = input("🔹 Enter URID (from fabric.openmind.org 的 Agent ID): ").strip()
        print("="*34 + "\n")
        
        with open(".env", "w") as f:
            f.write(f"ETH_ADDRESS={eth}\nOM_API_KEY={key}\nURID={urid}\n")
        log("✅", ".env file generated successfully.")

def start_conversation():
    print("\n" + "🎧" * 10)
    log("⚠️", "IMPORTANT: Please connect HEADPHONES to prevent audio feedback!")
    print("🎧" * 10 + "\n")
    
    input("👉 Press Enter to start 'conversation' mode...")
    run_cmd("uv run src/run.py conversation")

if __name__ == "__main__":
    try:
        check_env()
        setup_uv()
        configure_project()
        start_conversation()
    except KeyboardInterrupt:
        log("🛑", "Deployment stopped by user.")
