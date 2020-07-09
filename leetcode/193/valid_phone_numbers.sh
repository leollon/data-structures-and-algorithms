#!/bin/bash

# Author: leollon
# github: leollon
# date: Thu 09 Jul 2020 10:16:10 PM HKT
# Read from the file file.txt and output all valid phone numbers to stdout.
awk '
BEGIN {
    FS="\n"
}
{
    for (i = 1; i <= NF; i++) {
        if ($i ~  /[1-9]{3}-[1-9]{3}-[0-9]{4}/ || $i ~  /\([1-9]{3}\) [1-9]{3}-[0-9]{4}/) {
            print $i
        }
    }
}' file.txt

