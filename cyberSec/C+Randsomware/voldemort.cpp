#include <iostream>
#include <fstream>
#include <stdexcept>
#include <string>
#include <cstdlib>
#include <sys/utsname.h>
#include <curl/curl.h>

using namespace std;

struct SystemInfo {
    string system;
    string arch;
};

SystemInfo get_system_info() {
    struct utsname buffer;
    if (uname(&buffer) != 0) {
        throw runtime_error("Unable to get system information");
    }
    return {buffer.sysname, buffer.machine};
}

size_t write_data(void* ptr, size_t size, size_t nmemb, FILE* stream) {
    size_t written = fwrite(ptr, size, nmemb, stream);
    return written;
}

void download_executable(const string& system, const string& arch) {
    string base_url = "https://example.com/downloads/";
    string url;

    if (system == "Linux") {
        if (arch == "x86_64") {
            url = base_url + "my_program_linux_x86_64";
        } else if (arch == "aarch64") {
            url = base_url + "my_program_linux_aarch64";
        } else {
            throw runtime_error("Unsupported architecture");
        }
    } else if (system == "Windows") {
        url = base_url + "my_program_windows.exe";
    } else if (system == "Darwin") {
        url = base_url + "my_program_mac";
    } else {
        throw runtime_error("Unsupported operating system");
    }

    CURL* curl;
    FILE* fp;
    CURLcode res;
    string filename = url.substr(url.find_last_of("/") + 1);

    curl = curl_easy_init();
    if (curl) {
        fp = fopen(filename.c_str(), "wb");
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        fclose(fp);

        if (res == CURLE_OK) {
            cout << "Downloaded " << filename << endl;
        } else {
            cout << "Failed to download " << filename << endl;
        }
    }
}

int main() {
    try {
        SystemInfo system_info = get_system_info();
        download_executable(system_info.system, system_info.arch);
    } catch (const exception& e) {
        cerr << e.what() << endl;
    }
    return 0;
}