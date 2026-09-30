#!/bin/bash
# Export the deck as images and copy the given slide numbers to the scratchpad as look-N.png.
S=/private/tmp/claude-501/-Users-rolle-Projects-keynote-base/c26984b9-15ab-4610-9987-b4f97c97e0e0/scratchpad
O=$(mktemp -d "$S/ex.XXXX")
osascript -e "tell application \"Keynote\" to export document \"Sovereign by habit.key\" to POSIX file \"$O\" as slide images with properties {image format:PNG}" >/dev/null
for k in "$@"; do cp "$O"/*.$(printf %03d $k).png "$S/look-$k.png"; echo "$S/look-$k.png"; done
rm -rf "$O"
