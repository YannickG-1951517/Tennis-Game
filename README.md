# Tennis Game

 My entry for a job application technical screening focussing on TDD.

## Scoring rules

- Scores progress as: `love → 15 → 30 → 40`
- If both players reach 40: **deuce**
- After deuce:
  - A player scoring a point gets **advantage**
  - If they win again: **they win the game**
  - If they lose the next point: back to **deuce**
- A player wins by reaching at least **4 points** and being **2 points ahead**

## How to Run

1. Clone the repo and navigate into it:

```bash
git clone https://github.com/YannickG-1951517/Tennis-Game.git
cd Tennis-Game
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1 # or source venv/bin/activate on Unix
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run tests:

```bash
pytest
```

## Tests

The implementation is fully test driven, with coverage for:

- Score progression for both players
- Deuce and advantage scenarios
- Game-winning conditions
- Edge case: score does not change after game is won
