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




services = load_services('./service_lists/svc_details.2023-06-23.json')

service_name_list=[]
service_vendor_list=[]

print("[i] Starting to parse services..")

for service in services:
    service_name = services[service]['name']
    #service_vendor = services[service]['vendor']
    service_name_list.append(service_name)
    #service_vendor_list.append(service_vendor)

# Dedup Lists
service_name_list = list(set(service_name_list))
#service_vendor_list = list(set(service_vendor_list))



service_name_list.remove('HTTP')

print(f"[i] Service Name List Formed, De-dupped, and cleaned up..\n\n{service_name_list}")

client = MsfRpcClient("randori", server="127.0.0.1", port=55553, ssl=True)

print("[i] Starting process to match service names to modules...")
potential_module_matches = []
for service in service_name_list:
    modules = client.modules.search("type:exploit " + service)
    if modules:
        potential_module_matches = potential_module_matches + modules

print(f"Potential Relevant Modules:\n\n{potential_module_matches}")

print("[i] Writing data to json file")
write_json_to_file("potential_modules", potential_module_matches)


