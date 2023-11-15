#!/bin/bash

# Output file
output_file="benchmark_result.csv"

# Write the header to the CSV file
#echo "Timestamp,PointsWritten,PercentComplete,TotalThroughput,CurrentThroughput,Errors,AvgLatency,90thPercentileLatency,95thPercentileLatency,99thPercentileLatency" > $output_file
echo "Timestamp,PointsWritten,TotalThroughput,CurrentThroughput"> $output_file #,AvgLatency,90thPercentileLatency,95thPercentileLatency,99thPercentileLatency" > $output_file

# Read the benchmark_result.txt file line by line
while IFS= read -r line
do
    # Check if the line starts with 'T='
    if [[ $line == T=* ]]; then
        # Extract the measurements
        timestamp=$(echo $line | awk '{print $1}' | tr -d 'T=')
        points_written=$(echo $line | awk '{print $2}' | tr -d 'points written')
        total_throughput=$(echo $line | awk -F '|' '{print $1}' | awk '{print $(NF-1), $NF}')
        current_throughput=$(echo $line | awk -F '|' '{print $2}' | awk '{for(i=1;i<=NF;i++) if ($i=="throughput:") print $(i+1), $(i+2)}')        
        #avg_latency=$(echo $line | awk -F '|' '{print $2}' | awk -F ':' '{print $2}' | awk '{print $1}')
        #percentile_90_latency=$(echo $line | awk '{print $7}' | tr -d ', 90%:')
        #percentile_95_latency=$(echo $line | awk '{print $8}' | tr -d ', 95%:')
        #percentile_99_latency=$(echo $line | awk '{print $9}' | tr -d ', 99%:')

        # Write the measurements to the CSV file
        #echo "$timestamp,$points_written,$percent_complete,$total_throughput,$current_throughput,$errors,$avg_latency,$percentile_90_latency,$percentile_95_latency,$percentile_99_latency" >> $output_file
        echo "$timestamp,$points_written,$total_throughput,$current_throughput" >> $output_file #,$avg_latency,$percentile_90_latency,$percentile_95_latency,$percentile_99_latency" >> $output_file   
    fi
done < "benchmark_result.txt"