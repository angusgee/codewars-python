#!/usr/bin/bash

# Help message function
show_help() {
    echo "Usage: $0 <challenge_name>"
    echo
    echo "Initializes Python files for a Codewars challenge."
    echo
    echo "Options:"
    echo "  -h, --help    Show this help message and exit"
}

# Check for help flag
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
    exit 0
fi

# Require at least one argument
if [[ -z "$1" ]]; then
    echo -e "Error: Challenge name required as argument e.g 'fizz_buzz'\n"
    show_help
    exit 1
fi

touch "$1.py";
echo -e "import codewars_test as test\nfrom $1 import *\n" >> "$1.test.py";
