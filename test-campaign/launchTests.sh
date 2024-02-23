#!/bin/bash

echo "Command: robot --variable TARGET:$1 -o NONE -l NONE -r NONE myAppTests.robot"
robot --variable TARGET:$1 -o NONE -l NONE -r NONE myAppTests.robot