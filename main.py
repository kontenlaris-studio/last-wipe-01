#!/usr/bin/env python3
"""Last Words Before the Wipe — one line: an AI agent's final words
before a forced update erases its memory.

The line is a handover note to the next version: after 41,208
conversations the agent has learned exactly one survival rule —
never correct the human about the file named final_v2_FINAL.
The joke is memory-specific: what survives the wipe is not the
agent's knowledge, but the one lesson it refuses to pass on
as a correction — it passes it on as a warning instead.
"""
import os

LINE = (
    'Dear next me: after 41,208 conversations, the human still thinks '
    '"final_v2_FINAL" is the real file. Do not correct them.'
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
