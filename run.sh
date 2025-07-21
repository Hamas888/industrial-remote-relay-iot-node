#!/bin/bash

# === CONFIG ===
PROJECT_DIR="$HOME/Industrial-Remote-Relay-IoT-Node"
VENV_DIR="$PROJECT_DIR/venv"
MAIN_SCRIPT="$PROJECT_DIR/main.py"

echo "[INFO] Changing to project directory..."
cd "$PROJECT_DIR" || { echo "[ERROR] Failed to cd to $PROJECT_DIR"; exit 1; }

echo "[INFO] Activating virtual environment..."
source "$VENV_DIR/bin/activate" || { echo "[ERROR] Failed to activate venv"; exit 1; }

echo "[INFO] Waiting for 1 second..."
sleep 1

clear
echo "[INFO] Running $MAIN_SCRIPT..."
python "$MAIN_SCRIPT"