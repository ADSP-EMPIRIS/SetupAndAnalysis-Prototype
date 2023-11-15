#!/bin/bash

# Install Go if not already installed
check_and_install_go() {
    if ! command -v go &> /dev/null
    then
        echo "Go could not be found, installing now."
        sudo apt-get update
            sudo apt-get install -y golang-go
    else
        echo "Go is already installed." &> /dev/null
    fi
}

# Set up Go environment (you might want to add these to your .bashrc)
setup_go_env() {
    export GOPATH=$HOME/go
    export PATH=$PATH:$GOPATH/bin
}

# Install inch
install_inch_and_verify() {
    go install github.com/influxdata/inch/cmd/inch@latest

    # Verify inch is successfully installed in GOPATH/bin
    if ! command -v inch &> /dev/null
    then
        echo "Inch could not be found, please check if it is installed correctly."
        exit
    else
        echo "Inch is successfully installed." &> /dev/null
    fi
}


# Function to run inch benchmark
# You can modify the parameters as per your requirement
inch_benchmark() {
    local result=$(inch -v -c 8 -b 10000 -t 2,5000,1 -p 1000 -consistency any) 
    echo "$result"
}


#Main execution
check_and_install_go
setup_go_env
install_inch_and_verify
total_time_in_sec=$(inch_benchmark)

# Printing result
echo "$total_time_in_sec" > benchmark_result.txt
echo "Benchmark result written to benchmark_result.txt"
