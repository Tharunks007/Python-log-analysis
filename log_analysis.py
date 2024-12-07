
import csv
from collections import defaultdict

# Configuration
FAILED_LOGIN_THRESHOLD = 10

# Helper functions
def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def count_requests_by_ip(log_lines):
    ip_count = defaultdict(int)
    for line in log_lines:
        ip = line.split()[0]
        ip_count[ip] += 1
    return dict(sorted(ip_count.items(), key=lambda x: x[1], reverse=True))

def find_most_accessed_endpoint(log_lines):
    endpoint_count = defaultdict(int)
    for line in log_lines:
        if '"' in line:
            endpoint = line.split('"')[1].split()[1]
            endpoint_count[endpoint] += 1
    most_accessed = max(endpoint_count, key=endpoint_count.get, default=None)
    return most_accessed, endpoint_count[most_accessed]

def detect_suspicious_activity(log_lines, threshold=FAILED_LOGIN_THRESHOLD):
    failed_login_count = defaultdict(int)
    for line in log_lines:
        if "401" in line or "Invalid credentials" in line:
            ip = line.split()[0]
            failed_login_count[ip] += 1
    return {ip: count for ip, count in failed_login_count.items() if count > threshold}

def save_to_csv(ip_requests, most_accessed, suspicious_ips, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write Requests per IP
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_requests.items():
            writer.writerow([ip, count])
        
        # Write Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow([most_accessed[0], most_accessed[1]])
        
        # Write Suspicious Activity
        writer.writerow([])
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in suspicious_ips.items():
            writer.writerow([ip, count])

# Main script
if __name__ == "__main__":
    log_file = "sample.log"
    output_file = "log_analysis_results.csv"
    
    log_lines = parse_log_file(log_file)
    
    # Analysis
    ip_requests = count_requests_by_ip(log_lines)
    most_accessed = find_most_accessed_endpoint(log_lines)
    suspicious_ips = detect_suspicious_activity(log_lines)
    
    # Output results
    print("Requests per IP Address:")
    for ip, count in ip_requests.items():
        print(f"{ip:20} {count}")
    
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")
    
    print("\nSuspicious Activity Detected:")
    for ip, count in suspicious_ips.items():
        print(f"{ip:20} {count}")
    
    # Save to CSV
    save_to_csv(ip_requests, most_accessed, suspicious_ips, output_file)
    print(f"Results saved to {output_file}")
