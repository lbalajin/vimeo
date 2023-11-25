"""
Auto-Scaler Script for Application Replicas based on the CPU Utilization.

Description:
This script interacts with an external application's API to monitor CPU utilization and dynamically adjust the number
of application replicas to maintain an average CPU utilization of 0.80 (80%).

Dependencies:
- Python 3.x
- 'requests' library (install using 'pip install requests')

Execution:
1. Ensure Python is installed on your system.
2. Install the 'requests' library by running 'pip install requests'.
3. Replace the placeholder URLs for the application's API endpoints:
   - status_endpoint: URL for fetching CPU utilization and current replicas
   - replicas_endpoint: URL for updating the number of replicas
4. Run the script, and it will continuously monitor CPU utilization and adjust replicas as needed.

Script Name: auto_scaler.py
Author: Balaji Lahade [bnlahade@gmail.com]
Created Date: Nov2k23
Modified Date: N/A
"""

import requests
import time
from datetime import datetime

# Get the current system time
current_time = datetime.now()

print(f"Script executed at: {current_time}")

# Get the API endpoints
status_endpoint = "http://auto_scaler_example.com/app/status"  # Need to replace with the actual URL
replicas_endpoint = "http://auto_scaler_example.com/app/status"  # Need to replace with the actual URL

def get_status():
    try:
        headers = {"Accept": "application/json"}
        response = requests.get(status_endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx)
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch status: {e}")
        return None

def update_replicas(new_replicas):
    try:
        headers = {"Content-Type": "application/json"}
        payload = {"replicas": new_replicas}
        response = requests.put(replicas_endpoint, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx)
        print(f"Replicas updated to {new_replicas}")
    except requests.RequestException as e:
        print(f"Failed to update replicas: {e}")

def calculate_replica_change(cpu_utilization):
    target_utilization = 0.80       # Target CPU utilization

    # Calculate the difference between the current and target utilization
    utilization_difference = target_utilization - cpu_utilization

    # Determine the change in replicas based on the utilization difference
    if utilization_difference > 0.05:       # If CPU utilization is above the target by more than 5%
        return 1
    elif utilization_difference < -0.05:
        return -1       # Decrease replicas by 1
    else:
        return 0        # Maintain the same number of replicas

# Main loop to periodically check and adjust replicas
while True:
    status = get_status()
    if status:
        cpu_utilization = status.get("cpu", {}).get("highPriority")
        current_replicas = status.get("replicas")

        # Calculate the necessary change in replicas based on CPU utilization
        change = calculate_replica_change(cpu_utilization)

        if change is not None:
            new_replicas = current_replicas + change

            # Ensure new_replicas stays within reasonable bounds
            if new_replicas < 1:        # To avoid having less than 1 replica
                new_replicas = 1
            elif new_replicas > 100:    ## To prevent an excessive number of replicas
                new_replicas = 100
            
            update_replicas(new_replicas)

    time.sleep(60)
