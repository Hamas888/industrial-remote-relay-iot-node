#!/bin/bash

# === CONFIG ===
SERIAL_DEV="/dev/serial0"

echo "[INFO] Cleaning up..."

# 1. Kill all PPP connections
echo "[INFO] Killing PPP processes..."
sudo pkill -f pppd

# 2. Restore wlan0 as default route
echo "[INFO] Setting wlan0 as default route..."
sudo ip route del default 2>/dev/null
sudo ip route add default dev wlan0

# 3. Free /dev/serial0
echo "[INFO] Releasing $SERIAL_DEV..."
PID=$(lsof "$SERIAL_DEV" 2>/dev/null | awk 'NR>1 {print $2}' | sort -u)
if [ ! -z "$PID" ]; then
    echo "[INFO] Killing process $PID using $SERIAL_DEV..."
    sudo kill -9 $PID
fi

# 4. Kill all python processes (or only main.py if you prefer)
echo "[INFO] Killing all Python processes..."
pkill -f python

# Optional: Kill only main.py
# pkill -f remote-relay/main.py

# 5. Wait 1 second and clear terminal
echo "[INFO] Waiting 1 second..."
sleep 1
clear

echo "[INFO] Cleanup complete."
