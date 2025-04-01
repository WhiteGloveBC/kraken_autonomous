#!/bin/bash

# Load .env values safely
set -a
source .env
set +a

# Verify required env vars
if [[ -z "$GITHUB_USER" || -z "$GITHUB_PAT" || -z "$GITHUB_PROJECT" ]]; then
  echo "[ERROR] Missing GITHUB_USER, GITHUB_PAT, or GITHUB_PROJECT in .env"
  exit 1
fi

# Initialize Git and add remote
git init
git branch -M main
git remote remove origin 2>/dev/null
git remote add origin https://${GITHUB_USER}:${GITHUB_PAT}@github.com/${GITHUB_USER}/${GITHUB_PROJECT}.git

# Stage, commit, and push
git add .
git commit -m "Initial ASZA bootstrap commit"
git push -u origin main

echo "[SUCCESS] Git repository initialized and pushed."
