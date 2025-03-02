#!/usr/bin/env bash

if [[ $# -lt 1 || $# -gt 2 ]]; then
    printf "usage: %s PROT_ID [OUT_DIR]\n" $(basename "$0")
    exit 1
fi

PROT_ID=$1
OUT_DIR=${2:-fasta}


PROT_ID=$(echo "$PROT_ID" | tr -d '\r\n')
URL="https://www.uniprot.org/uniprot/${PROT_ID}.fasta"
OUT_FILE="$OUT_DIR/${PROT_ID}.fasta"
curl -s -L -o "$OUT_FILE" "$URL"

