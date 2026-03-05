import subprocess, sys

def setup():
    print("--- Starting Environment Setup ---\n")
    
    # Install pip requirements
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("\n--- Setup Complete! Run 'python src/main.py' to start. ---")

if __name__ == "__main__":
    setup()