---

# ♟️ Python Arcade Chess Game

A fully playable Chess game built with **Python** using the **Arcade** graphics library.
Includes player vs AI gameplay with adjustable AI search depth.

---

## 📌 Features

* 🎮 Player (White) vs AI (Black)
* 🧠 AI powered by Minimax tree search
* ♟️ Full chess rule validation
* ✅ Check prevention logic
* 🔄 Automatic pawn promotion
* 🖱️ Drag-and-drop piece movement
* 🎚️ Adjustable AI depth
* 🖼️ Sprite-based chessboard and pieces

---

## 📂 Project Structure

```
.
├── main.py                # Main game window and event loop
├── ChessGameRules.py      # Chess rules and board logic
├── ChessAI.py             # AI decision-making logic (minimax)
├── chess_board_img.jpg
├── *_img.jpg              # White piece sprites
├── B_*_img.jpg            # Black piece sprites
```

---

## 🛠 Requirements

* Python 3.8+
* Arcade

Install dependency:

```bash
pip install arcade
```

---

## 🚀 How to Run

From the project directory:

```bash
python main.py
```

You will be prompted:

```
Enter The Difficulty Level:
```

### 🎚️ What Difficulty Means

The number you enter is the **Minimax search depth**.

* `1` → Looks 1 move ahead
* `2` → Looks 2 moves ahead
* `3` → Looks 3 moves ahead
* `4+` → Deeper search (much stronger but slower)

⚠️ Important:

* Each increase in depth grows the search tree exponentially.
* Higher depths significantly increase computation time.
* Depth 3–4 is usually a good balance.
* Depth 5+ may become slow depending on your CPU.

---

## 🎮 How to Play

* You play as **White**
* Click a piece to select it
* Drag it to a valid square
* Release to make the move
* The AI (Black) will automatically respond

Pawn promotion happens automatically when a pawn reaches the end of the board.

---

## 🧠 AI Logic

The AI uses a Minimax-based search:

```python
search_best_move(board, "black", depth)
```

The `depth` parameter directly controls how many levels down the game tree the AI evaluates.

Higher depth:

* Better positional understanding
* Stronger tactical play
* Slower move calculation

---

## 🏗 Architecture

### `ChessGame`

Handles:

* Rendering
* Input
* Turn management
* Syncing sprites with board logic

### `ChessGameRules`

Handles:

* Board state (8x8 array)
* Legal move generation
* Check validation
* Special rules

### `ChessGameAI`

Handles:

* Move evaluation
* Minimax search
* Best move selection based on depth

---


