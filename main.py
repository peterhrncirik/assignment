import json

from extract_details import extract
from export import export_to_db

# Load Config and turn it into Dict
with open('configClear_v2.json', 'r') as file:
    
    data = json.loads(file.read())

# Path to Interfaces 
INTERFACES_CONFIG_PATH = data['frinx-uniconfig-topology:configuration']['Cisco-IOS-XE-native:native']['interface']

# Interfaces to check
INTERFACES_TO_EXTRACT = ['Port-channel', 'TenGigabitEthernet', 'GigabitEthernet'] 

# Init List to store all details
config_details = []

# Loop through config
for interface_group in INTERFACES_CONFIG_PATH:
    
    # Only check group if we are interested in it
    if interface_group in INTERFACES_TO_EXTRACT:
            
        for interface_config in INTERFACES_CONFIG_PATH[interface_group]:
            
            # Extract config of specific group & append it to a List
            match interface_group:
                
                case 'Port-channel':
                    
                    config_details.append(extract(interface_group, interface_config))
                    
                case 'TenGigabitEthernet':
                    
                    config_details.append(extract(interface_group, interface_config))
                    
                case 'GigabitEthernet':
                    
                    config_details.append(extract(interface_group, interface_config))
                    
                case 'BDI':
                    
                    config_details.append(extract(interface_group, interface_config))
                    
                case 'Loopback':
                    
                    config_details.append(extract(interface_group, interface_config))
         


# Export into DB
export_to_db(config_details)

            


