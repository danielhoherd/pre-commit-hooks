#!/usr/bin/env bash

# Get the list of staged files
staged_files=$(git diff --cached --name-only)

# Check if any filename contains whitespace
if echo "$staged_files" | grep -q '[[:space:]]'; then
    echo "Error: Filenames cannot contain whitespace characters (spaces, tabs, etc.):"
    echo "$staged_files" | grep '[[:space:]]'
    exit 1
fi

exit 0
