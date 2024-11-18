# 🏰 8-Queens Problem Simulation with Pygame

Welcome to the **8-Queens Problem Simulation**! This repository showcases a dynamic visualization of solving the classic **8-Queens Problem** using a **Constraint Satisfaction Problem (CSP)** approach. The solution is implemented in Python with a real-time, interactive simulation powered by **Pygame**.

---

## 🎯 Problem Description

The **8-Queens Problem** is a famous puzzle in computer science and mathematics. The goal is to place 8 queens on an 8x8 chessboard such that no two queens threaten each other. This means:
- No two queens can be in the same row.
- No two queens can be in the same column.
- No two queens can be on the same diagonal.

This repository demonstrates the **backtracking algorithm** in action, complete with real-time visualization to make the solving process intuitive and fun to watch!

---

## 🎮 Features

- **Step-by-Step Visualization**: Watch the queens being placed on the board and removed during backtracking.
- **Color-Coded Simulation**: 
  - 🟢 **Green**: Safe placement of queens.
  - 🔴 **Red**: Highlights the current cell being evaluated.
- **Real-Time Updates**: Pygame dynamically updates the board as the algorithm runs.
- **Educational and Fun**: Great for understanding CSPs, backtracking, and visualization techniques.

---

## 🖥️ Demo

![8-Queens Simulation GIF](https://user-images.githubusercontent.com/example/8-queens-demo.gif)

---

## 🚀 Installation and Usage

Follow these steps to get the simulation running on your local machine:

### 1️⃣ Prerequisites
Make sure you have the following installed:
- **Python 3.7+**
- **Pygame Library**

### 2️⃣ Clone the Repository

git clone https://github.com/your-username/8-queens-simulation.git
cd 8-queens-simulation
3️⃣ Install Dependencies
Install the Pygame library using pip:

bash
Copy code
pip install pygame
4️⃣ Run the Simulation
Execute the Python script:

bash
Copy code
python nqueens_simulation.py
🛠️ How It Works
Backtracking Algorithm:
Starts from the first row and attempts to place a queen in a safe position.
If a placement leads to a conflict, it backtracks and tries the next position.
Real-Time Visualization:
Queens are placed one by one with pauses to let you observe.
Backtracking steps (removing queens) are also visualized.
📂 Project Structure
plaintext
Copy code
📦 8-queens-simulation
├── nqueens_simulation.py   # Main script for the simulation
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
🤝 Contributing
Contributions are welcome! If you have ideas for improvements or want to add new features, feel free to fork the repository and submit a pull request.

📜 License
This project is licensed under the MIT License. Feel free to use and modify the code.

🌟 Acknowledgments
Inspired by the classic 8-Queens Problem.
Built using Python and Pygame.
