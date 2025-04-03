#!/bin/bash

mkdir -p trash

# Pattern-based cleanup: Move all stray .py files with suspiciously long or descriptive names
find . -maxdepth 1 -type f -name "*.py" | while read -r file; do
  filename=$(basename "$file")
  if [[ "$filename" =~ [[:space:]] || "$filename" =~ [A-Z] || "$filename" =~ [\!\,\?] ]]; then
    echo "[CLEANUP] Moving stray file: $filename"
    mv "$file" trash/
  fi
done

echo "[CLEANUP COMPLETE] Stray .py files moved to ./trash/"
