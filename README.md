[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/rinoo9/u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/rinoo9/u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)

# One Word for the Boss — CircleBack

Entry for the [make.fun bounty "One Word for the Boss"](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735).

The entry is exactly one word describing a boss — no phrase, no caption, no explanation:

`CircleBack` — 10 characters, and it lands on its own.

The boss who never decides: every question gets a "let's circle back", every decision gets circled back to next week, and the circle never closes. Funny, true, fresh, and it travels from office to kitchen to warehouse. (Round 1 entry was `Meetingaholic`.)

## How it works

`main.py` is deterministic — no network, no randomness, no input. It writes exactly `CircleBack` (10 bytes, no trailing newline) to `/output/entry.txt`.

## Run it

```sh
python3 main.py
cat /output/entry.txt   # CircleBack
```

Run it twice and the output is byte-identical.
