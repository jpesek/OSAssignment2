"""
Title: Assignment #2 - Option #2
Author: Jordan Pesek
Date: October 2020
Course: CS 4312 Operating Systems
"""

import subprocess
import platform
import sys


# Simple file I/O to read in a list of IP addresses into an array.
def open_file(file_name):
    file_data = ''
    file = open(file_name, encoding="utf8")
    file_data += file.read()
    file.close()
    data = file_data.split()
    return data


# Here I use the subprocess library to sequentially ping all the addresses in the IP address list.
# I also use the os library to detect which OS type is used to correctly form the ping command.
def ping_addresses(ip_list):
    results = []
    parameter = "-n" if platform.system().lower() == "windows" else "-c"
    for ip in ip_list:
        p = subprocess.call(["ping", parameter, '1', '-w', '1', '-i', '1', ip], stdout=subprocess.DEVNULL)
        results.append(p)
        print(str(p) + ", " + ip)
    return results


# In this method, I count each of the available and unavailable addresses, and relay that data.
def get_and_print_availability(ip_list, results):
    available_count = 0
    unavailable_count = 0
    for ip, p in zip(ip_list, results):
        if p == 0:
            available_count += 1
        else:
            unavailable_count += 1
    print(str(available_count) + " addresses were available. " + str(unavailable_count) + " were not.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Try again with the following command line interface: 'py main.py files verbose' "
              "where files is a txt file containing a list of IP addresses.")
        sys.exit()

    list_of_ips = open_file(sys.argv[1])
    list_of_results = ping_addresses(list_of_ips)
    get_and_print_availability(list_of_ips, list_of_results)
