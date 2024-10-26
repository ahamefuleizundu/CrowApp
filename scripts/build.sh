#!/bin/bash

# This script builds the project and accepts additional arguments for make targets

# Create the build directory if it doesn't exist
mkdir -p ../build

# Run make command from the project root directory with passed arguments
make -C .. "$@"
