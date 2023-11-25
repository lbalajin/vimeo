# High-Level Design for Auto-Scaler Solution:

#### Components:
1. **API Interaction Module:**
   - Handles communication with the external application's API.
   - Uses the `requests` library to make HTTP requests for retrieving CPU utilization and updating the number of replicas.

2. **Auto-Scaling Logic:**
   - Contains the logic to calculate the necessary changes in replica count based on CPU utilization.
   - Determines whether to increase, decrease, or maintain the number of replicas to achieve a target CPU utilization.

3. **Logging and Observability:**
   - Integrates the `logging` module to record events, errors, and replica count changes in a log file (`autoscaler.log`).
   - Logs events at the INFO/DEBUG level for successful actions and at the ERROR level for encountered errors during API calls.

4. **Main Control Loop:**
   - Periodically fetches the current CPU utilization and number of replicas.
   - Utilizes the auto-scaling logic to decide on adjustments to the replica count.
   - Updates the number of replicas through API calls as required.

#### Workflow:
1. **Initialization:**
   - Initializes necessary variables, API endpoint URLs, and sets up the environment.
   - Configures logging using the `logging` module for observability.

2. **Monitoring and Scaling Loop:**
   - Fetches the CPU utilization and current replica count using API calls.
   - Utilizes the auto-scaling logic to calculate the required change in replicas to maintain the target utilization (0.80).
   - Makes API requests to adjust the number of replicas based on calculated changes.

3. **Error Handling and Logging:**
   - Incorporates error handling using `try-except` blocks for API interactions.
   - Logs events, successful actions, encountered errors, and replica count changes to the `autoscaler.log` file.

4. **Testing, Optimization, and Monitoring:**
   - Includes testing suites to validate the auto-scaler's behavior in different scenarios.
   - Optimizes the auto-scaling algorithm and error handling based on performance observations and log analysis.
   - Monitors the log file for observability, tracking system behavior, errors, and scaling actions.

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

## Logging and Observability
- The script utilizes the `logging` module to create a log file named `autoscaler.log`.
- Logs at the INFO level for successful events and at the ERROR level for encountered errors during API calls.
- Use the log file to track the script's behavior, monitor replica count changes, and identify any errors encountered.

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

