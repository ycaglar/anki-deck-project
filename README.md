# Anki Deck Project

## Overview
This project is a custom Anki deck designed to help users interactively practice fundamental algorithms such as **BFS**, **Binary Search**, and **Dijkstra's Algorithm**. It features a unique learning experience by integrating **CodeMirror**, enabling users to type, test, and compare their solutions within Anki.

## Features
- **Interactive Coding Practice**: Users write algorithm implementations directly on the front of the card using a CodeMirror-enabled input.
- **Real-Time Feedback**:
  - If the answer is **correct**, flipping the card displays a congratulatory message.
  - If the answer is **incorrect**, the back of the card shows a **split-view comparison**:
    - **Left**: User’s code.
    - **Right**: The correct solution.
- Focused on **learning through comparison** to help users pinpoint and understand mistakes.

## Algorithms Included
- Breadth-First Search (BFS)
- Binary Search (BS)
- Dijkstra's Algorithm
- (Add more algorithms are being implemented.)

## How to Use
1. Import the deck into your Anki app.
2. Start practicing by reviewing cards:
   - Write your solution to the algorithm problem on the front.
   - Flip the card to see feedback and, if needed, a side-by-side comparison.
3. Use the split-view feedback to refine your understanding of the algorithms.

## Prerequisites
- [Anki](https://apps.ankiweb.net/) (latest version).
- Basic knowledge of programming and algorithms.

## Installation
1. Clone the repository:
```bash
   git clone https://github.com/yourusername/anki-deck-algorithms.git
```
2. Open a terminal at the project folder
3. Run the build script
```bash
python3 build/build_deck.py
```
4. Import the generated unki deck which is located under the output folder within the project directory.

<!-- ![Screenshot](./) -->

## How to Contribute

Contributions are always welcome. Please follow the steps below for your pull request.

1. Fork this project to your account
2. Create a branch for the change you are proposing
3. Apply changes to your fork
4. Send a pull request after referring to the **[contributing guidelines](https://github.com/ycaglar/.github/blob/master/CONTRIBUTING.md)**
