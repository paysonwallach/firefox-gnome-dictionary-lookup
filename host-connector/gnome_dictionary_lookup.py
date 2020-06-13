#!/usr/bin/python -u

# Note that running python with the `-u` flag is required on Windows,
# in order to ensure that stdin and stdout are opened in binary, rather
# than text, mode.

import json
import struct
import subprocess
import sys


def get_message():
    raw_length = sys.stdin.buffer.read(4)

    if not raw_length:
        sys.exit(0)

    message_length = struct.unpack("=I", raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")

    return json.loads(message)


while True:
    message = get_message()

    if message:
        proc = subprocess.Popen(
            ["gnome-dictionary", message],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        proc.detach()
