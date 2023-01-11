import json

def extract(interface_group, interface):
    
    """
    Extracts specific details from interface configuration.
    Checks if dictionary contains value, if the value doesn't exist returns None
    """
    
    # Get value or return None
    max_frame_size = interface.get('mtu') 
    description = interface.get('description')  
    
    # Combine Group name with Interface name + convert interface name into str as some are ints
    name = interface_group + str(interface.get('name'))

    # Convert back to JSON
    config = json.dumps(interface) 

    try:  
        id = interface.get('Cisco-IOS-XE-ethernet:service').get('instance')[0]['id'] 
    except:
        id = None
    
    try:
        port_channel_id = interface.get('Cisco-IOS-XE-ethernet:channel-group')['number'] 
    except:
        port_channel_id = None          

    
    details = {
        'id_1': id,
        'connection': None,
        'name': name,
        'description': description,
        'config': config,
        'type': None,
        'infra_type': None,
        'port_channel_id': port_channel_id,
        'max_frame_size': max_frame_size,
    }
    
    return details