#!/usr/bin/env bash
export LC_ALL=C

for FILE in "${@}" ; do
  sort -u -o "${FILE}" "${FILE}"
done
