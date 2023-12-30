from flask import Flask, render_template, request
import numpy as np
import plotly.graph_objects as go
from regressionCode import create_dist, convert_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get parameters from the form
        x_mean = float(request.form['x_mean'])
        x_std = float(request.form['x_std'])
        y_mean = float(request.form['y_mean'])
        y_std = float(request.form['y_std'])
        num_of_points = int(request.form['num_of_points'])
        order = int(request.form['order'])

        # Create the plot
        fig = create_dist(x_mean, x_std, y_mean, y_std, num_of_points, order)

        # Save the plot as an HTML file
        plot_div = fig.to_html(full_html=False, default_height=500, default_width=700)

        return render_template('index.html', plot_div=plot_div)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
