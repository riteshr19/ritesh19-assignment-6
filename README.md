# CS506 Assignment 6 - Linear Regression

## Overview

In this assignment, you'll explore the impact of changing parameters on linear regression. The goal is to create an interactive webpage to demonstrate how modifying these parameters affects regression results, especially when there is no actual relationship between X and Y. By tweaking these settings, you’ll observe how randomness can influence the slope and intercept in a regression model.

## Features

- **Interactive Form**: Users can input the sample size (N), mean (mu), variance (sigma²), and number of simulations (S).
- **Generate Button**: Generates scatter plots and regression lines based on user inputs.
- **Clear Button**: Clears all input fields.
- **Random Button**: Fills the input fields with random values.
- **Results Display**: Shows scatter plots, regression lines, and histograms of slopes and intercepts.

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

2. **Click "Generate"** to create the scatter plot and regression line, and histograms of slopes and intercepts.

3. **Click "Clear"** to reset all input fields.

4. **Click "Random"** to fill the input fields with random values.

## Code Explanation

### `app.py`

This file contains the main Flask application code.

- **Imports**: Necessary libraries including Flask, NumPy, Matplotlib, and scikit-learn.
- **`generate_plots` function**: Generates the scatter plot, regression line, and histograms based on the input parameters.
- **Flask Routes**:
  - **`/` route**: Handles both GET and POST requests. On POST, it processes the form data, generates plots, and renders the results.

### `index.html`

This file contains the HTML template for the web page.

- **Form**: Allows users to input parameters and includes "Generate", "Clear", and "Random" buttons.
- **JavaScript**: Functions to clear the form and fill it with random values.
- **Results Section**: Displays the generated plots and statistical information.

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

Create a short demo video (1-2 minutes) explaining the functionality and your observations. You can either embed the demo video in your portfolio website or create an unlisted YouTube video and include the link in your assignment repository's README.

## Key Takeaways

This assignment helps you see how randomness can affect regression estimates. By experimenting with different parameters, you’ll get a better feel for how much variability there can be in slopes and intercepts when there’s no true relationship between X and Y. Using your observations and analysis will allow you to get a better and deeper understanding of Linear Regression.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
