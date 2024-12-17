import subprocess

def query_dns(domain, record_type):
    try:
        # Run the dig command to fetch DNS records
        result = subprocess.run(["dig", "+short", record_type, domain], capture_output=True, text=True)
        
        if result.returncode == 0:
            records = result.stdout.strip().split('\n')
            if records:
                print(f"{record_type} Records for {domain}:")
                for record in records:
                    print(f"  - {record}")
            else:
                print(f"No {record_type} records found for {domain}.")
        else:
            print(f"Error running dig: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
domain = "ger512.com"
record_types = ["A", "AAAA", "CNAME", "MX", "TXT"]

print(f"DNS Query Results for {domain}:\n")
for record in record_types:
    query_dns(domain, record)
    print("-")
