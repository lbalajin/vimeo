# Auto-Scaler for Application Replicas Based on CPU Utilization.

## Overview
This script is designed to automatically adjust the number of application replicas based on CPU utilization metrics obtained from an external application's API. The goal is to maintain an average CPU utilization of 0.80 (80%) by scaling the number of replicas up or down as needed.

## Dependencies
- Python 3.x
- `requests` library (install using `pip install requests`)

## Setup
1. Ensure Python is installed on your system.
2. Install the required `requests` library by running:
    ```
    pip install requests
    ```
3. Replace the placeholder URLs in the script:
   - `status_endpoint`: URL for fetching CPU utilization and current replicas
   - `replicas_endpoint`: URL for updating the number of replicas

## Usage
1. Run the script `auto_scaler.py`.
2. The script will continuously monitor CPU utilization and adjust replicas as necessary to maintain the target average.

## File Structure
- `auto_scaler.py`: Main script for the auto-scaler solution.
- `README.md`: This file containing information about the script and its usage.

## Author
- Balaji Lahade [bnlahade@gmail.com]

## Date
- Nov2k23

## Additional Notes
- Customize the auto-scaling logic and error handling as per your application's requirements.
- Ensure proper testing and monitoring to validate the script's behavior in different scenarios.
- For any issues or improvements, feel free to raise an issue.
