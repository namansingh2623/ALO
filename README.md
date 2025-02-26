# Ant Lion Optimizer (ALO)

## Project Overview
The Ant Lion Optimizer (ALO) is a metaheuristic optimization algorithm inspired by the predatory behavior of antlions and the cooperative behavior of ants. This algorithm emulates the natural interactions between antlions and ants to discover optimal solutions for complex optimization problems. In this project, we test the ALO using 23 benchmark functions to evaluate its performance across various scenarios.

## Features
- **Implementation of ALO**: Simulates the hunting mechanism of antlions to perform optimization.
- **Benchmark Testing**: Evaluates the optimizer using 23 standard benchmark functions.
- **Visualization Tools**: Provides plots to visualize the optimization process and results.

## Repository Structure
- `ALO.py`: Contains the main implementation of the Ant Lion Optimizer algorithm.
- `Final.ipynb`: Jupyter Notebook demonstrating the usage of ALO with benchmark functions.
- `Random_walk_around_antlion.py`: Module for simulating the random walk behavior of ants around antlions.
- `RouletteWheelSelection.py`: Module implementing the roulette wheel selection mechanism.
- `func_plot.py`: Script for plotting benchmark functions and optimization results.
- `get_function_details.py`: Retrieves details of benchmark functions used in testing.
- `initialization.py`: Handles initialization routines for the optimizer.
- `main.py`: Main script to execute the optimization process.
- `matlab.txt`: Contains MATLAB code or references related to the project.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries: `numpy`, `matplotlib`, `scipy`

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/namansingh2623/ALO.git
   cd ALO
   ```

2. **Install dependencies**:
   ```bash
   pip install numpy matplotlib scipy
   ```

## Usage
1. **Running the Optimizer**:
   - Open and execute `Final.ipynb` to see the ALO in action with various benchmark functions.
   - Alternatively, run `main.py` to execute the optimization process directly:
     ```bash
     python main.py
     ```
2. **Customization**:
   - Modify `get_function_details.py` to add or change benchmark functions.
   - Adjust parameters in `main.py` to tune the optimizer's performance.

## Results
The optimizer's performance is evaluated using 23 benchmark functions, with results visualized in `Final.ipynb`. These visualizations demonstrate the convergence behavior and effectiveness of the ALO across different optimization scenarios.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or address any bugs.

## License
This project is licensed under the MIT License.

## References
- S. Mirjalili, "The Ant Lion Optimizer," Advances in Engineering Software, vol. 83, pp. 80-98, 2015.
- Benchmark functions source: [Optimization Test Functions](https://www.sfu.ca/~ssurjano/optimization.html)

---
*For more details, visit the [GitHub repository](https://github.com/namansingh2623/ALO).*
