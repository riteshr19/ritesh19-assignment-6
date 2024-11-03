
# CS506 Assignment 6 - Linear Regression

## Overview

In this assignment, we explore the impact of changing parameters on linear regression models. The objective is to create an interactive webpage that demonstrates how modifying various parameters affects regression outcomes, especially when there is no true relationship between X and Y. By adjusting these settings, you can observe how randomness influences the slope and intercept in a regression model.

## Features

- **Interactive Form**: Users can enter values for sample size (N), mean (mu), variance (sigma²), and number of simulations (S).
- **Generate Button**: Creates scatter plots and regression lines based on user inputs.
- **Clear Button**: Resets all input fields.
- **Random Button**: Populates the input fields with random values.
- **Results Display**: Displays scatter plots, regression lines, and histograms of slopes and intercepts.

## Setup

### Prerequisites

- Python 3.x
- Flask
- NumPy
- Matplotlib
- scikit-learn

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/cs506-assignment6.git
    cd cs506-assignment6
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask application**:
    ```sh
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Enter the parameters**:
    - Sample size (N): Number of data points in the dataset.
    - Mean (mu): Mean of the normal error term added to Y.
    - Variance (sigma²): Variance of the normal error term.
    - Number of simulations (S): Number of datasets to simulate.

2. **Click "Generate"** to create the scatter plot and regression line, along with histograms of slopes and intercepts.

3. **Click "Clear"** to reset all input fields.

4. **Click "Random"** to populate the input fields with random values.

## Code Explanation

### `app.py`

This file contains the main Flask application code.

- **Imports**: Includes necessary libraries such as Flask, NumPy, Matplotlib, and scikit-learn.
- **`generate_plots` function**: Generates scatter plots, regression lines, and histograms based on input parameters.
- **Flask Routes**:
  - **`/` route**: Handles both GET and POST requests. On POST, processes form data, generates plots, and renders results.

### `index.html`

This file contains the HTML template for the web page.

- **Form**: Provides fields for parameter input and includes "Generate," "Clear," and "Random" buttons.
- **JavaScript**: Contains functions to reset the form and populate fields with random values.
- **Results Section**: Displays generated plots and statistical information.

## Example

1. **Input Parameters**:
    - Sample size (N): 50
    - Mean (mu): 0
    - Variance (sigma²): 1
    - Number of simulations (S): 100

2. **Generated Output**:
    - Scatter Plot and Regression Line
    - Histogram of Slopes and Intercepts
    - Proportion of slopes and intercepts more extreme than the initial dataset

## Demo Video
[Demo Video](https://riteshr19.github.io/videos/assignment_06.mov)

## Key Takeaways

This assignment provides insights into how randomness can impact regression estimates. By experimenting with different parameters, you can observe the variability in slopes and intercepts when there’s no actual relationship between X and Y. These observations enhance understanding of Linear Regression concepts and the role of randomness in model estimates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
