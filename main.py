import requests
import os
import csv

# Load the API Key from an environment variable
API_KEY = os.getenv('MERAKI_DASHBOARD_API_KEY')
BASE_URL = 'https://api.meraki.com/api/v1'
HEADERS = {'X-Cisco-Meraki-API-Key': API_KEY, 'Content-Type': 'application/json'}


def get_device_appliance_uplinks_settings(org_id):
    """Fetch uplink settings for a specific appliance."""
    url = f'{BASE_URL}/organizations/{org_id}/appliance/uplink/statuses'
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_network_name(network_id):
    """Fetch network name for a specific network."""
    url = f'{BASE_URL}/networks/{network_id}'
    response = requests.get(url, headers=HEADERS)
    return response.json()['name']


def main():
    org_id = '1492405'  # Replace 'YOUR_ORG_ID' with your actual Organization ID

    # Prepare the CSV file for writing
    with open('meraki_mx_vlans_uplinks.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Network Name', 'WAN Interface', 'Interface IP Address', 'Public IP Address'])
        mx_statuses = get_device_appliance_uplinks_settings(org_id)
        for network in mx_statuses:
            print(get_network_name(network['networkId']), network['uplinks'])
            for uplink in network['uplinks']:
                print(uplink['interface'], uplink['ip'], uplink['publicIp'])
                writer.writerow([get_network_name(network['networkId']), uplink['interface'], uplink['ip'], uplink['publicIp']])


if __name__ == '__main__':
    main()
