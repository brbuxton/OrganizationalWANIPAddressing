# Meraki MX VLANs Uplinks Checker
This Python script retrieves and exports the uplink settings for Meraki MX appliances in a specified organization. It utilizes the Meraki Dashboard API to gather information about WAN interfaces, interface IP addresses, and public IP addresses for each network associated with the organization.

## Prerequisites
Before using this script, ensure you have:

* Meraki Dashboard API Key: Obtain an API key from the Meraki Dashboard.
* Python 3: Ensure you have Python 3 installed on your system.
## Setup
1. Install Required Packages: Make sure you have the requests library installed. You can install it via pip:

```Copy code
pip install requests
```

2. Environment Variable: Set up an environment variable named MERAKI_DASHBOARD_API_KEY and assign it your Meraki Dashboard API key.

3. Organization ID: Replace 'YOUR_ORG_ID' in the script with your actual Organization ID.

## Usage
Run the script using Python:

```Copy code
python script_name.py
```
The script will generate a CSV file named meraki_mx_vlans_uplinks.csv containing the following information:

* Network Name
* WAN Interface
* Interface IP Address
* Public IP Address
## Notes
* Ensure proper permissions and network access to fetch data from the Meraki Dashboard API.
* Review and modify the script according to your organization's specific requirements or environment setup.
* For any issues or inquiries regarding the Meraki Dashboard API, refer to the Meraki API Documentation.
* For assistance or inquiries regarding this script, feel free to contact the script author.
## License

https://github.com/CiscoSE/cisco-sample-code/blob/master/LICENSE