#!/bin/bash

PROFILE="$1"
TARGET="$2"

if [[ "$PROFILE" == "fast" ]]; then
    nmap -sV -T4 -O -F --version-light "$TARGET"

elif [[ "$PROFILE" == "intense" ]]; then
    nmap -T4 -A -v -sS -sU -p- "$TARGET"

elif [[ "$PROFILE" == "full" ]]; then
    nmap -sS -sT -sV -sU -A -vv -p- -T4 -PE -PS80,443 -PA3389 -PP -PU40125 -PY --script "default or (discovery and safe)" "$TARGET"

else
    echo "Usage: $0 {fast|intense|full} <target>"
    exit 1
fi
