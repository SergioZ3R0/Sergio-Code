import re
import subprocess
import os

# Lista de puertos conocidos.
known_ports = {
    20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080
}

def run_nmap_scan(target, output_file):
    # Run the Nmap command and save the output to the specified file
    subprocess.run(f"nmap {target} -p 1-65535 -T4 -oN {output_file}", shell=True)

def parse_nmap_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    target = None
    open_ports = []

    for line in lines:
        if "Nmap scan report for" in line:
            target = line.split("Nmap scan report for ")[1].strip()
        elif "/tcp" in line and "open" in line:
            port = int(line.split("/")[0])
            open_ports.append(port)

    return target, open_ports

def classify_ports(open_ports):
    known = []
    redirected = []

    for port in open_ports:
        if port in known_ports:
            known.append(port)
        else:
            redirected.append(port)

    return known, redirected

def save_results(target, known, redirected):
    with open(f"scans/scan_{target}.txt", "w") as file:
        file.write(f"Resultados del escaneo para {target}\n")
        file.write(f"Puertos conocidos abiertos: {known}\n")
        file.write(f"Posibles puertos redirigidos: {redirected}\n")

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
            target, open_ports = parse_nmap_output(output_file)
            known, redirected = classify_ports(open_ports)

            if target:
                print(f"Target: {target}")
            else:
                print("Target not found.")

            if known or redirected:
                save_results(target, known, redirected)
                print(f"Results saved to scans/scan_{target}.txt")
            else:
                print("No open ports found.")
    else:
        output_file = f"scans/scan_{ip_input}.txt"
        run_nmap_scan(ip_input, output_file)
        target, open_ports = parse_nmap_output(output_file)
        known, redirected = classify_ports(open_ports)

        if target:
            print(f"Target: {target}")
        else:
            print("Target not found.")

        if known or redirected:
            save_results(target, known, redirected)
            print(f"Results saved to scans/scan_{target}.txt")
        else:
            print("No open ports found.")

if __name__ == "__main__":
    main()