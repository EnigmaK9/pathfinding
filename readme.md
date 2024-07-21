# 🛤️ Pathfinding Algorithms Comparison

This project demonstrates the comparison between Dijkstra and A\* algorithms for pathfinding in a 20x20 grid environment. The comparison is made for both fixed and random obstacles.

## 📦 Installation

To run this project, you need to have Python installed along with the following libraries:

- `pygame`
- `tkinter`

You can install these libraries using pip:

```bash
pip install pygame
```

## 🚀 Usage

1. **Initialize Pygame**: Make sure Pygame is installed and properly configured.
2. **Run the Script**: Execute the script to start the Tkinter input configuration window where you can specify the start and goal positions for two agents (A1 and A2), and choose between fixed or random obstacles.

```bash
python main.py
```

## ⚙️ Functionality

### 🧩 Matrix Creation

The project allows for two types of obstacle matrices:

- **🪵 Fixed Obstacles**: Predefined obstacles in specific positions.
- **🎲 Random Obstacles**: Randomly generated obstacles based on user input.

### 🔍 Pathfinding Algorithms

The project uses two pathfinding algorithms:

- **🔄 Dijkstra**: Finds the shortest path from the start to the goal position without considering heuristics.
- **⭐ A\***: Uses heuristics (Manhattan distance) to find the shortest path more efficiently.

### 🖼️ Visualization

The project visualizes the matrices and paths using Pygame, displaying:

- Fixed Obstacles
- Random Obstacles
- Fixed Obstacles with paths found by Dijkstra and A\*
- Random Obstacles with paths found by Dijkstra and A\*

### 📸 Screenshots

<p align="center">
  <img src="screenshot.png" alt="Screenshot 1">
  <img src="screenshot2.png" alt="Screenshot 2">
</p>

## 🧮 Algorithms

### 🔄 Dijkstra's Algorithm

Dijkstra's algorithm is implemented to find the shortest path in a grid. It uses a priority queue to explore the neighboring cells and updates the shortest distance found so far.

The algorithm works as follows:

1. Initialize the distance to the start node \( S \) as 0, and all other nodes as \( \infty \).
2. Set the start node \( S \) as the current node.
3. For the current node \( u \), update the distance to its neighbors \( v \) as \( \text{dist}(u) + \text{weight}(u, v) \) if this is smaller than the current known distance to \( v \).
4. Mark the current node \( u \) as visited and select the unvisited node with the smallest tentative distance as the new current node.
5. Repeat steps 3 and 4 until all nodes have been visited or the smallest tentative distance among the unvisited nodes is \( \infty \).

The distance update formula is:

$$
\text{dist}(v) = \min(\text{dist}(v), \text{dist}(u) + \text{weight}(u, v))
$$

### ⭐ A\* Algorithm

A\* algorithm combines the features of Dijkstra's algorithm and a heuristic to improve the search. It uses the Manhattan distance as the heuristic function:

$$
h(x) = |x_1 - x_2| + |y_1 - y_2|
$$

The total cost function in A\* is given by:

$$
f(x) = g(x) + h(x)
$$

where:

- \( f(x) \) is the total cost function.
- \( g(x) \) is the cost from the start node to the current node.
- \( h(x) \) is the estimated cost from the current node to the goal node.

## 🛠️ Code Modularization

The code is modularized into several files to improve maintainability and readability. Here is a brief explanation of the modularization:

- **main.py**: The main script that initializes the program, configures the matrices, executes the pathfinding algorithms, and displays the results.
  - **Pattern Used**: Facade Pattern - Simplifies the interaction with the system by providing a unified interface to various functionalities.
- **obstacles.py**: Contains functions to create fixed and random obstacles in the matrices.
  - **Pattern Used**: Factory Pattern - Handles the creation of different configurations of obstacles.
- **pathfinding.py**: Implements the Dijkstra and A\* algorithms.
  - **Pattern Used**: Strategy Pattern - Allows using different pathfinding algorithms interchangeably.
- **utils.py**: Contains utility functions such as calculating neighbors, Manhattan distance, and reconstructing the path.
  - **Pattern Used**: Utility Pattern - Provides reusable helper functions.
- **visualization.py**: Manages the visualization of the matrices and paths using Pygame.
  - **Pattern Used**: Template Method Pattern - Defines the skeleton of the drawing algorithm.
- **input_data.py**: Handles user input via Tkinter for setting up start and goal positions and choosing obstacle types.
  - **Pattern Used**: Builder Pattern - Constructs the initial configuration based on user input.
- **results.py**: Displays the results of the pathfinding algorithms in a Tkinter window.
  - **Pattern Used**: Singleton Pattern - Ensures only one instance of the results window is displayed.

## 🧮 Functions and Classes

- **🔄 `create_random_obstacles(matrix, num_obstacles)`**: Adds random obstacles to the matrix.
- **🪵 `create_fixed_obstacles(matrix)`**: Adds fixed obstacles to the matrix.
- **🔍 `neighbors(matrix, current)`**: Returns a list of neighboring cells.
- **🔄 `Dijkstra(matrix, start, goal)`**: Implements Dijkstra's algorithm.
- **⭐ `A_star(matrix, start, goal)`**: Implements A\* algorithm.
- **🔗 `get_path(matrix, current, g_cost, start)`**: Reconstructs the path from start to goal.
- **🖼️ `draw_all_matrices()`**: Draws all matrices and paths using Pygame.
- **🖥️ `get_input_data()`**: Collects input data from the user using Tkinter.
- **📊 `show_results()`**: Displays the results of the pathfinding algorithms in a Tkinter window.

## 📈 Results

The results of the pathfinding algorithms are displayed in a Tkinter window, showing the path lengths for each scenario:

- **Fixed Obstacles Dijkstra - A1 Path Length**: path_length
- **Fixed Obstacles Dijkstra - A2 Path Length**: path_length
- **Fixed Obstacles A\* - A1 Path Length**: path_length
- **Fixed Obstacles A\* - A2 Path Length**: path_length
- **Random Obstacles Dijkstra - A1 Path Length**: path_length
- **Random Obstacles Dijkstra - A2 Path Length**: path_length
- **Random Obstacles A\* - A1 Path Length**: path_length
- **Random Obstacles A\* - A2 Path Length**: path_length

## 📜 Conclusion

This project provides a comprehensive comparison between Dijkstra and A\* algorithms for pathfinding in different obstacle environments. It demonstrates the efficiency and effectiveness of each algorithm in finding the shortest path.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

EnigmaK9
