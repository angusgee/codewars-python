#!/usr/bin/bash

touch "$1.py";
echo -e "import codewars_test as test\nfrom $1 import *\n" >> "$1.test.py";
