#!/usr/bin/env python3

from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole

import json

def write_json_to_file(filename, exploit_dict):
    f = open(f"{filename}.json", "w")
    f.write(json.dumps(exploit_dict, indent=2))
    f.close()

def load_services(filename):
    f = open(f"{filename}", 'r')
    services = json.loads(f.read())
    f.close()
    return services

def load_cves(filename)
    f = open(f"{filename}", 'r')
    cves = f.read()
    f.close()
    return cves


#services = load_services('./service_lists/svc_details.2023-06-23.json')
cve_list = load_cves('./cve-list.txt')


# Connect to `msfrpcd` 
client = MsfRpcClient("randori", server="127.0.0.1", port=55553, ssl=True)

print("[i] Starting process to match service names to modules...")
potential_module_matches = []
for cve in cve_list:
    modules = client.modules.search("type:exploit cve:" + cve)
    if modules:
        potential_module_matches = potential_module_matches + modules

print(f"Potential Relevant Modules:\n\n{potential_module_matches}")

print("[i] Writing data to json file")
write_json_to_file("potential_modules", potential_module_matches)

