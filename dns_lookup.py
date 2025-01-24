import re
import dns.resolver
import socket

# Define the regex pattern for validating IPv4 addresses
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def get():
    global domain, userGiveType
    domain = input("dnslookup Domain: ")  # Assign to global variable
    userGiveType = input(f"dnslookup {domain} type: ")  # Assign to global variable

def check(userGiveIP):
    # Validate the IP address using regex (only if it's an IP address)
    if re.search(regex, userGiveIP): 
        print("Valid IP address") 
        return True
    else:
        # Check if it's a valid domain instead
        try:
            socket.gethostbyname(userGiveIP)
            print("Valid domain name")
            return True
        except socket.error:
            print("Invalid domain or IP address")
            return False

def checkType(userGiveType):
    # List of valid DNS record types
    valid_types = ['NS', 'CNAME', 'PTR', 'MX', 'TXT', 'SOA', 'A', 'AAAA']
    if userGiveType in valid_types:
        print("Valid DNS record type")
        return True
    else:
        print("Invalid DNS record type")
        return False

def exe(domain, type_valid):
    try:
        # Query DNS for the given domain and record type
        answers = dns.resolver.resolve(domain, type_valid)
        print(f"Results for {type_valid} records for {domain}:")
        for rdata in answers:
            print(rdata.to_text())
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get()  # Collect user input
    ip_valid = check(domain)  # Check if the IP address or domain is valid
    type_valid = checkType(userGiveType)  # Check if the DNS record type is valid
    
    # Now use the results of both checks
    if ip_valid and type_valid:
        exe(domain, userGiveType)  # Perform the DNS lookup
    else:
        print("Stop")
