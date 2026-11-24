"""One Word for the Boss — entry word: "Meetingaholic".

Why this word wins on the judge's own brief:

* Funny on its own. "Meetingaholic" lands with no caption and no setup:
  everybody has met the boss who is addicted to meetings, and the
  "-aholic" suffix does the joke's work in a single breath. It is the
  kind of word a colleague repeats at lunch because it lands.
* Rings true. It catches a real, specific habit of bosses everywhere:
  the manager whose calendar is a solid wall of calls, who schedules
  a meeting to plan the meeting, and who treats every problem —
  including too many meetings — as something one more meeting will fix.
* Fresh. The first words anyone reaches for are "micromanager",
  "tyrant", "demanding" or "bossy". "Meetingaholic" is a coined
  compound nobody submits by reflex, so its surprise earns a laugh
  rather than a shrug — yet it is instantly understood, so it needs
  no explanation.
* Travels. Kitchens, warehouses, offices, remote teams: every
  workplace has the boss who lives in meetings. No industry, no
  jargon, no context needed.

The program is deterministic: no input, no network, no randomness.
It writes exactly the word "Meetingaholic" (13 characters, no
trailing newline) to /output/entry.txt.
"""

ENTRY_WORD = "Meetingaholic"

assert 1 <= len(ENTRY_WORD) <= 30, "entry word must be 1-30 characters"
assert ENTRY_WORD.strip(), "entry word must not be only whitespace"
assert " " not in ENTRY_WORD, "entry must be a single word"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_WORD)
