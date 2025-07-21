# 🧩 State Search Solver

A Python implementation of classic search algorithms to solve the 8-puzzle problem (or NxN sliding puzzles). This project demonstrates both uninformed and informed search strategies for AI coursework.

---

## 📁 Project Structure

```
State Search/
│
├── file_handle.py         # File I/O utilities for reading puzzle states
├── game_machenics.py      # Core puzzle mechanics (moves, state transitions)
├── uninformed_search.py   # BFS, DFS, UCS, DLS, IDS algorithms
├── informed_search.py     # Greedy and A* search (to be implemented)
├── main.py                # Entry point for running experiments
├── start.txt              # Example start state for the puzzle
├── goal.txt               # Example goal state for the puzzle
└── README.md              # This documentation
```

---

## 🕹️ How It Works

- **Puzzle Representation:**  
  The puzzle is represented as a 2D list, with `0` denoting the blank tile.

- **Search Algorithms:**  
  - **Uninformed:**  
    - Breadth-First Search (BFS)
    - Depth-First Search (DFS)
    - Uniform Cost Search (UCS)
    - Depth-Limited Search (DLS)
    - Iterative Deepening Search (IDS)
  - **Informed:**  
    - Greedy Search (to be implemented)
    - A* Search (to be implemented)

- **File Input:**  
  - `start.txt` and `goal.txt` define the initial and goal states.
  - Each file contains a grid of numbers, ending with `END OF FILE`.

---

## 🚀 Getting Started

1. **Install Python 3.8+**

2. **Run the Solver:**
   ```sh
   python main.py
   ```

3. **Modify Puzzle States:**
   - Edit `start.txt` and `goal.txt` to try different puzzles.

---

## 📝 Example Puzzle

**start.txt**
```
2 3 6
1 0 7
4 8 5
END OF FILE
```

**goal.txt**
```
1 2 3
4 5 6
7 8 0
END OF FILE
```

---

## 🛠️ Key Components

- `file_handle.py`: Reads puzzle states from files.
- `game_machenics.py`: Handles moves, state flattening, and successors.
- `uninformed_search.py`: Implements BFS, DFS, UCS, DLS, IDS.
- `informed_search.py`: Placeholder for Greedy and A* search.

---

## 📚 References

- [8-puzzle problem - Wikipedia](https://en.wikipedia.org/wiki/15_puzzle)
- Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach*.

---

## ✨ Author

- *Abinash Bastola*

---