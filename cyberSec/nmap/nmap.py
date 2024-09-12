import re
import subprocess
import os

def run_nmap_scan(target, output_file):
    # Run the Nmap command and save the output to the specified file
    subprocess.run(f"nmap {target} --script vuln --min-rate=5000 -Pn -oN {output_file}", shell=True)

def parse_nmap_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    target = None
    vulnerabilities = []

    for line in lines:
        if "Nmap scan report for" in line:
            target = line.split("Nmap scan report for ")[1].strip()
        elif "VULNERABLE:" in line:
            vuln = line.strip()
            vulnerabilities.append(vuln)
        elif "CVE:" in line:
            cve = line.strip()
            vulnerabilities.append(cve)
        elif "References:" in line:
            references = line.strip()
            vulnerabilities.append(references)
        elif "https://" in line or "http://" in line:
            link = line.strip()
            vulnerabilities.append(link)

    return target, vulnerabilities

def main():
    ip_input = input("Enter the IP address or range (e.g., 192.168.1.1 or 192.168.1.1-192.168.1.10): ")

    # Create the scans directory if it doesn't exist
    if not os.path.exists('scans'):
        os.makedirs('scans')

    if '-' in ip_input:
        ip_list = ip_input.split('-')
        if len(ip_list) != 2:
            print("Invalid IP range format.")
            return

        start_ip = ip_list[0]
        end_ip = ip_list[1]

        # Generate the list of IPs in the range
        start_octets = start_ip.split('.')
        end_octets = end_ip.split('.')

        if start_octets[:3] != end_octets[:3]:
            print("IP range must be in the same subnet.")
            return

        start_last_octet = int(start_octets[3])
        end_last_octet = int(end_octets[3])

        for i in range(start_last_octet, end_last_octet + 1):
            current_ip = f"{start_octets[0]}.{start_octets[1]}.{start_octets[2]}.{i}"
            output_file = f"scans/scan_{current_ip}.txt"
            run_nmap_scan(current_ip, output_file)
            target, vulnerabilities = parse_nmap_output(output_file)

            if target:
                print(f"Target: {target}")
            else:
                print("Target not found.")

            if vulnerabilities:
                print("Vulnerabilities found:")
                for vuln in vulnerabilities:
                    print(f"- {vuln}")
            else:
                print("No vulnerabilities found.")
    else:
        output_file = f"scans/scan_{ip_input}.txt"
        run_nmap_scan(ip_input, output_file)
        target, vulnerabilities = parse_nmap_output(output_file)

        if target:
            print(f"Target: {target}")
        else:
            print("Target not found.")

        if vulnerabilities:
            print("Vulnerabilities found:")
            for vuln in vulnerabilities:
                print(f"- {vuln}")
        else:
            print("No vulnerabilities found.")

if __name__ == "__main__":
    main()