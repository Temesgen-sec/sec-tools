#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <target-ip> <nse-script-name>"
    exit 1
fi

TARGET="$1"
SCRIPT_NAME="$2"

echo "Running Nmap scan on target: $TARGET using script: $SCRIPT_NAME..."


nmap --script "$SCRIPT_NAME" "$TARGET"
