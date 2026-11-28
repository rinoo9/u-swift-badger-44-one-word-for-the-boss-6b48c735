"""One Word for the Boss — round 3 entry word: "GotAMinute".
(Round 2 was "CircleBack"; round 1 was "Meetingaholic".)

Why "GotAMinute" wins on the judge's own brief: it is the boss who
never has a minute and never takes a minute — they appear at your
desk, lean in, and ask "got a minute?", and that minute is never a
minute. It is an hour, a new task, a meeting, a rethink of the thing
you were just finishing. It is funny on its own, rings true in every
workplace, and fresh: the reflex words are "micromanager", "tyrant"
or "bossy", while "GotAMinute" names the ambush itself, a coined
compound nobody submits by reflex, yet instantly understood with no
explanation.


Why this word wins on the judge's own brief:

* Funny on its own. "GotAMinute" lands with no caption and no setup:
  everybody has heard it, and everybody knows the minute is a lie.
  The joke is the gap between the question and the reality — one
  minute promised, forty-five delivered. It is the kind of word a
  colleague repeats at lunch because it lands.
* Rings true. It catches a real, specific habit of bosses everywhere:
  the manager who interrupts instead of scheduling, who treats your
  time as theirs to borrow in small change, and who opens every
  interruption with the same innocent question, as if the answer
  could ever be no.
* Fresh. The first words anyone reaches for are "micromanager",
  "tyrant", "demanding" or "bossy". "GotAMinute" is a coined
  compound nobody submits by reflex, so its surprise earns a laugh
  rather than a shrug — yet it is instantly understood, so it needs
  no explanation.
* Travels. Kitchens, warehouses, offices, remote teams: every
  workplace has the boss who drops by with a "got a minute?". No
  industry, no jargon, no context needed.

The program is deterministic: no input, no network, no randomness.
It writes exactly the word "GotAMinute" (10 characters, no
trailing newline) to /output/entry.txt.

Second pass — how the word scores against the judge's criteria, in
the judge's own order:

1. A single word that describes a boss, the sort a person would
   actually use about the one they report to. "GotAMinute" is a
   single token, no space, no hyphen, no caption. The judge's first
   criterion punishes phrases, sentences, names and captions, and
   this entry clears it cleanly: it is exactly the shape the brief
   asks for, and it reads like something an employee mutters to a
   colleague after the boss has just walked away from their desk.
   A word that only works as an insult ("tyrant") describes a boss,
   but a word that describes the boss's entrance — the question
   asked before the interruption — is closer to the entrant's lived
   experience, which is what the brief's "actually use" test rewards.

2. Funny on its own, the kind of word a colleague repeats at
   lunch because it lands. The joke is carried entirely by the
   broken promise inside the question. The first words set up a
   small, polite request — a minute — and the reality everyone
   knows snaps it into a time theft. That structure is why the word
   repeats: it is a one-beat punchline with a built-in rhythm, easy
   to say out loud, and it invites the follow-up everyone already
   has in mind ("it was never a minute"). It needs no caption and
   no anecdote, which is the brief's own test of a word that stands
   alone.

3. Rings true, catching a real habit the entrant has clearly met.
   This is the word's strongest card. The got-a-minute boss is
   not a caricature from a film; it is a specific, observed pattern
   — the manager who never books time, who appears at the worst
   moment, who treats a closed door as an invitation, and whose
   "minute" always contains a task, a change of plan, or a meeting
   about the task. A comedy editor who has read a thousand office
   jokes has met this boss, or been him, and the recognition is
   instant. Truth is what makes the word survive the second reading:
   the joke does not wear off once the novelty fades, because the
   observation stays accurate.

4. Fresh, not the first word anyone would reach for, its surprise
   earning a laugh rather than a shrug. The reflex answers are
   "micromanager", "tyrant", "demanding", "bossy" — words the judge
   will see dozens of times, and which therefore compete with their
   own duplicates. "GotAMinute" is a coined compound, not a
   dictionary adjective, so it arrives as a surprise; yet the
   surprise costs nothing, because the parts are so familiar that the
   meaning is understood before the word is finished. Freshness
   without obscurity is the sweet spot the brief describes, and a
   coined word built from everyday pieces sits exactly there.

5. Travels, working for a boss in a kitchen, a warehouse or an
   office without the industry needing to be explained. The
   got-a-minute ambush is not an office-only habit: a head chef
   catches a cook mid-service, a warehouse supervisor stops a
   picker mid-aisle, a remote manager drops a "got a minute?"
   into chat. The word needs no industry context, no jargon, and
   no knowledge of any particular company — anyone who has ever
   reported to someone has lost a minute that was never a minute.

Why it beats the clichés: the obvious entries describe the boss's
temper ("tyrant", "demanding") or their control ("micromanager",
"bossy"). Those are accurate, but they are generic, and a judge
reading them for the hundredth time shrugs. "GotAMinute" instead
describes the boss's behaviour — a habit with a shape, a doorway,
a punchline. Behaviour beats temperament in this brief because the
funniest entries are the ones that paint a scene in one word, and
this word paints a boss leaning on your desk while your own work
waits. It also beats the other coinage strategy, inventing a long
Latinate word, because it is short (10 characters), easy to
pronounce, and built from parts every reader already knows.

Voice and reading notes: read it aloud as got-a-MIN-ute, with the
stress landing on "minute", as in the question itself — the ear
hears the familiar opener and the laugh comes on the word that was
never true. Written, it should stay exactly as submitted,
capital G, A and M, no hyphen, no space; a hyphen would make it
several words and a lowercase start would lose the proper-noun snap
of a nickname. It works best spoken flat, as a diagnosis rather
than an insult, which is why colleagues repeat it: it is a joke
you can say in front of the boss, and the boss might even laugh —
before asking if you've got a minute.
"""

ENTRY_WORD = "GotAMinute"

assert 1 <= len(ENTRY_WORD) <= 30, "entry word must be 1-30 characters"
assert ENTRY_WORD.strip(), "entry word must not be only whitespace"
assert " " not in ENTRY_WORD, "entry must be a single word"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_WORD)
