#!/bin/bash

# Get the current folder path
CURRENT_FOLDER=$(pwd)
CURRENT_DIRECTORY_NAME=$(basename "$CURRENT_FOLDER")

# Create the result file
RESULT_FILE="HostEnergy_$CURRENT_DIRECTORY_NAME.txt"
rm -f "$RESULT_FILE"  # Remove the existing result file, if any

# Loop over subdirectories
for folder in "$CURRENT_FOLDER"/*/; do
  # Extract the directory name
  directory=$(basename "$folder")
  
  # Check if the OSZICAR file exists
  if [ -e "$folder/Relaxation/OSZICAR" ]; then
    # Retrieve the last line of OSZICAR
    last_line=$(tail -n 1 "$folder/Relaxation/OSZICAR")
  
    # Append directory name and last line to the result file
    echo "$directory $last_line" >> "$RESULT_FILE"
  fi
done

