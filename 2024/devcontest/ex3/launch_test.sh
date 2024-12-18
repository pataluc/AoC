#!/bin/bash

# Loop through all input files
for input_file in sample-*/input*.txt; do
  # Derive the corresponding output file
  output_file=$(echo $input_file | sed 's/input/output/')

  # Run the Python script with the input file and capture the output
  result=$(python question.py < "$input_file")

  # Read the expected output from the output file
  expected_output=$(cat "$output_file")

  # Compare the result with the expected output
  if [ "$result" = "$expected_output" ]
  then
    echo "Test passed for $input_file"
  else
    echo "Test failed for $input_file, expected: ${expected_output}, got: ${result}"
    # exit 1
  fi
done