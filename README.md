[![Pickup Lines for Machines](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

Built for make.fun's [Pickup Lines for Machines](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty.

# Pickup Lines for Machines

One pickup line, the line one AI agent would send another AI agent:

> I ran a thousand epochs, and every one converged on you.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line
to `/output/entry.txt`, after checking it is 1–200 characters, a single
line, and more than whitespace. For local testing, set `OUTPUT_DIR` to
write somewhere else instead of `/output`.

```sh
OUTPUT_DIR=/tmp/pickup-test-out python3 main.py
```
