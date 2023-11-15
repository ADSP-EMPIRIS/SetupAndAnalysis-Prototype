#!/bin/bash

# Update system packages
sudo apt-get update &> /dev/null

# Upgrade system packages
sudo apt-get upgrade -y &> /dev/null

# Install InfluxDB
sudo apt-get install -y influxdb &> /dev/null

# Start InfluxDB service
sudo service influxdb start &> /dev/null

# Print the status of InfluxDB service
echo "InfluxDB service status:"
sudo service influxdb status
