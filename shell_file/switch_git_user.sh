#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Path to the JSON file containing user configs
USER_CONFIG_JSON="$PROJECT_ROOT/data/git_user_configs.json"

# Check if jq is installed
if ! command -v jq >/dev/null 2>&1; then
    echo "Error: 'jq' is required but not installed. Please install jq and try again."
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$USER_CONFIG_JSON" ]; then
    echo "Error: $USER_CONFIG_JSON not found."
    echo "Please create a JSON file with an array of objects like:"
    echo '[{"name": "@username", "email": "username@example.com"}, {"name": "@username2", "email": "username2@example.com"}]'
    exit 1
fi

# Read user configurations from JSON file
USER_NAMES=($(jq -r '.[].name' "$USER_CONFIG_JSON"))
USER_EMAILS=($(jq -r '.[].email' "$USER_CONFIG_JSON"))

# Check if we got any configurations
if [ ${#USER_NAMES[@]} -eq 0 ] || [ ${#USER_EMAILS[@]} -eq 0 ]; then
    echo "Error: No user configurations found in $USER_CONFIG_JSON"
    echo "Please ensure the JSON file contains an array of objects with 'name' and 'email' fields."
    exit 1
fi

# Prompt user to select a configuration
echo "Select Git user configuration:"
for i in "${!USER_NAMES[@]}"; do
    echo "$i. ${USER_NAMES[$i]} ${USER_EMAILS[$i]}"
done

read -p "Enter the number of the configuration you want to use: " CHOICE

# Validate input
if ! [[ "$CHOICE" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid number."
    exit 1
fi

if ((CHOICE >= ${#USER_NAMES[@]} || CHOICE < 0)); then
    echo "Error: Invalid choice. Please select a number between 0 and $(( ${#USER_NAMES[@]} - 1 ))."
    exit 1
fi

# Set Git global user configuration
git config --global user.name "${USER_NAMES[$CHOICE]}"
git config --global user.email "${USER_EMAILS[$CHOICE]}"

echo "Git user configuration set to: ${USER_NAMES[$CHOICE]} ${USER_EMAILS[$CHOICE]}"
