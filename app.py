from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from werkzeug.utils import secure_filename
from utils.helper import *

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
templates = list(plotly.io.templates.keys())

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super_secret_key'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        flash('File uploaded successfully')
        data, columns = get_data(app.config['UPLOAD_FOLDER'], filename)
        return render_template('visualize.html', filename=filename, columns=columns, templates=templates)
    else:
        flash('Allowed file types are .csv and .xlsx')
        return redirect(request.url)

@app.route('/visualize', methods=['POST'])
def visualize():
    data = request.form   
    print(data)
    data = {key: value if len(value) > 1 else value[0] for key, value in data.lists()}
    print(data)

    df, columns = get_data(app.config['UPLOAD_FOLDER'], data['filename'])
    
    fig = generate_graph(df, data)
    
    graphJSON = fig.to_json()

    return render_template(
        'visualize.html',
        filename=data['filename'],
        columns=columns,
        templates=templates,
        graphJSON=graphJSON,
        Type=data['Type'],
        x_axis=data['x_axis'],
        y_axis=data['y_axis'],
        hover_name=data['hover_name'],
        color=data['color'],
        template=data['template'],
        title=data['title'],
        line_shape=data["line_shape"],
        line_dash_sequence=data['line_dash_sequence'],
        markers=data['markers'],
        symbol_sequence_line=data['symbol_sequence_line'],
        size = data["size"],
        opacity = data["opacity"],
        size_max = data["size_max"],
        symbol_sequence_scatter = data["symbol_sequence_scatter"],
        marginal_x = data["marginal_x"],
        marginal_y = data["marginal_y"],
        opacity_bar = data["opacity_bar"],
        barmode = data["barmode"],
        orientation = data["orientation"],
        pattern_shape = data["pattern_shape"],
        text = data["text"],
        text_auto = data["text_auto"],
        boxmode = data["boxmode"],
        orientation_box = data["orientation_box"],
        points_box = data["points_box"],
        notched = data["notched"],
        violinmode = data["violinmode"],
        points_violin = data["points_violin"],
        box = data["box"],
        pattern_shape_hist = data["pattern_shape_hist"],
        marginal = data["marginal"],
        opacity_hist = data["opacity_hist"],
        orientation_hist = data["orientation_hist"],
        barnorm = data["barnorm"],
        histnorm = data["histnorm"],
        histfunc = data["histfunc"],
        cumulative = data["cumulative"],
        nbins = data["nbins"],
        text_auto_hist = data["text_auto_hist"],
        opacity_pie = data["opacity_pie"],
        hole = data["hole"],
        animation_frame = data["animation_frame"],
        animation_group = data["animation_group"],
        facet_row = data["facet_row"], 
        facet_col = data["facet_col"], 
        facet_col_wrap = data["facet_col_wrap"], 
        facet_row_spacing = data["facet_row_spacing"], 
        facet_col_spacing = data["facet_col_spacing"]
    )


if __name__ == '__main__':
    app.run(debug=True)
