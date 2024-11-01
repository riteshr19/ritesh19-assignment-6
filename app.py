from flask import Flask, render_template, request, url_for
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI rendering
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

def generate_plots(N, mu, sigma2, S):
    # Ensure the static directory exists
    if not os.path.exists('static'):
        os.makedirs('static')

    # Generate a random dataset X of size N with values between 0 and 1
    rng = np.random.default_rng()
    X = rng.random(N)
    # Generate a random dataset Y with normal additive error (mean mu, variance sigma^2)
    Y = mu + np.sqrt(sigma2) * rng.standard_normal(N)

    # Fit a linear regression model to X and Y
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), Y)
    slope = model.coef_[0]
    intercept = model.intercept_

    # Generate a scatter plot of (X, Y) with the fitted regression line
    plt.figure()
    plt.scatter(X, Y, color='blue', label='Data points')
    plt.plot(X, model.predict(X.reshape(-1, 1)), color='red', label=f'Fit: Y = {slope:.2f}X + {intercept:.2f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Regression Line: Y = {slope:.2f}X + {intercept:.2f}')
    plt.legend()
    plot1_path = "static/plot1.png"
    plt.savefig(plot1_path)
    plt.close()

    # Run S simulations and create histograms of slopes and intercepts
    slopes = []
    intercepts = []
    for _ in range(S):
        Y_sim = mu + np.sqrt(sigma2) * rng.standard_normal(N)
        model.fit(X.reshape(-1, 1), Y_sim)
        slopes.append(model.coef_[0])
        intercepts.append(model.intercept_)

    plt.figure()
    plt.hist(slopes, bins=30, alpha=0.5, label='Slopes')
    plt.axvline(slope, color='red', linestyle='dashed', linewidth=1, label='Initial Slope')
    plt.hist(intercepts, bins=30, alpha=0.5, label='Intercepts')
    plt.axvline(intercept, color='blue', linestyle='dashed', linewidth=1, label='Initial Intercept')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histograms of Slopes and Intercepts')
    plt.legend()
    plot2_path = "static/plot2.png"
    plt.savefig(plot2_path)
    plt.close()

    slope_extreme = np.mean(np.abs(slopes) > np.abs(slope))
    intercept_extreme = np.mean(np.abs(intercepts) > np.abs(intercept))

    return plot1_path, plot2_path, slope_extreme, intercept_extreme

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        N = int(request.form['N'])
        mu = float(request.form['mu'])
        sigma2 = float(request.form['sigma2'])
        S = int(request.form['S'])
        plot1, plot2, slope_extreme, intercept_extreme = generate_plots(N, mu, sigma2, S)
        return render_template('index.html', plot1=plot1, plot2=plot2, slope_extreme=slope_extreme, intercept_extreme=intercept_extreme)
    return render_template('index.html', plot1=None, plot2=None)

if __name__ == '__main__':
    app.run(debug=True)