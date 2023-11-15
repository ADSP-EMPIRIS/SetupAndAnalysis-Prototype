#!/bin/bash

echo -e "-----------------------\n[i] Setting up influxDB...\n"
bash influxdb.sh

echo -e "-----------------------\n[i] Running benchmark...\n"
bash benchmark.sh

echo -e "-----------------------\n[i] Fin.\n"