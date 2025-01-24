import subprocess
import sys

def install_dnspython():
    """Installs the dnspython library if it's not already installed."""
    try:
        import dns.resolver
    except ImportError:
        print("Installing dnspython...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "dnspython"])
        print("The dnspython library was successfully installed!")
    else:
        print("The dnspython library is already installed!")

if __name__ == "__main__":
    install_dnspython()  # Installs dnspython if necessary
    print("Setup complete! You can now run 'python dns_lookup.py' in the terminal.")
