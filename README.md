# Knight Survival — Scratch Project Files

This repository contains the source assets and a local builder for a compact Scratch 3 survival game inspired by the idea: a knight survives while enemies attack from the left and right.

What is included
- `project.json`: project source for the Scratch project
- `assets/background.svg`: pixel-art style backdrop
- `assets/player.svg`: knight sprite
- `assets/enemy.svg`: enemy sprite
- `assets/attack.svg`: attack effect
- `build_sb3.py`: builds a Scratch `.sb3` archive locally
- `README.md`: this guide

How to build the Scratch file locally

1. Make sure Python 3 is installed.
2. In the repository root, run:

```bash
python build_sb3.py
```

This creates a file named:

```bash
Knight-Survival.sb3
```

3. Open the generated `.sb3` file in Scratch 3.

Notes
- This is a project source scaffold for a survival game prototype.
- Since Scratch project files are ZIP archives with a specific internal format, this script packages the project in the expected layout for local building.
- The game logic can be expanded in Scratch by editing the blocks in `project.json`, or by working directly in Scratch and re-exporting.

Recommended gameplay idea
- Player is a knight who moves on a 2D plane.
- Enemies spawn from the left and right sides.
- The player survives as long as possible.
- Use `WASD` or arrow keys, and `Space` to attack.
- Add cooldowns, hit effects, enemy speed scaling, and score/time-based difficulty as you iterate.
