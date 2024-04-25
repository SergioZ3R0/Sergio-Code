#!/bin/bash
# Author: SergioZ3R0
# Requirements: sudo apt install p7zip-full
name_decompressed=$(7z l $1 | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
7z x $1 > /dev/null 2>&1

while true; do
    7z l $name_decompressed > /dev/null 2>&1
    if [ "$(echo $?)" == "0" ]; then
        decompressed_next=$(7z l $name_decompressed | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
        if [ "$decompressed_next" == "$name_decompressed" ]; then
            cat $name_decompressed; rm data* 2>/dev/null
            exit 0
        fi
        7z x $name_decompressed > /dev/null 2>&1 && name_decompressed=$decompressed_next
    else
        exit 1
    fi
done
