import pandas as pd
import plotly
import os
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_data(folder_path, filename):
    filepath = os.path.join(folder_path, filename)
    if filename.rsplit('.', 1)[1].lower() == 'csv':
        df = pd.read_csv(filepath)
        columns = df.columns.tolist()
        return df, columns
    elif filename.rsplit('.', 1)[1].lower() == 'xlsx':
        df = pd.read_excel(filepath)
        columns = df.columns.tolist()
        return df, columns
    else:
        flash(f'Allowed file types are - {0}'.format(ALLOWED_EXTENSIONS))
        return redirect(request.url)

    
def generate_graph(df, data):    
    Type = data.get("Type")
    x_axis = data.get("x_axis")
    y_axis = data.get("y_axis")
    hover_name = data.get("hover_name")
    color = data.get("color")
    title = data.get("title")
    template = data.get("template")
    facet_row = data.get("facet_row", None)
    facet_col = data.get("facet_col", None)
    facet_col_wrap = data.get("facet_col_wrap", None)
    facet_row_spacing = data.get("facet_row_spacing", None)
    facet_col_spacing = data.get("facet_col_spacing", None)
    
    animation_frame = data.get("animation_frame", None)
    animation_group = data.get("animation_group", None)
    
    if animation_frame == 'None':
        animation_frame = None
    if animation_group == 'None':
        animation_group = None
    
    if facet_row == 'None':
        facet_row = None
    if facet_col == 'None':
        facet_col = None
    if facet_col_wrap == 'None' or facet_col_wrap == '':
        facet_col_wrap = None
    else:
        facet_col_wrap = float(facet_col_wrap)
    if facet_row_spacing == 'None' or facet_row_spacing == '':
        facet_row_spacing = None
    else:
        facet_row_spacing = float(facet_row_spacing)
    if facet_col_spacing == 'None' or facet_col_spacing == '':
        facet_col_spacing = None
    else:
        facet_col_spacing = float(facet_col_spacing)

    # Fields for line graphs
    line_dash_sequence = [data.get("line_dash_sequence", None)]
    markers = data.get("markers", None)
    symbol_sequence_line = [data.get("symbol_sequence_line", None)]
    line_shape = data.get("line_shape", None)
    
    if hover_name == 'None':
        hover_name = None
    if color == 'None':
        color = None
    if markers == 'true':
        markers = True
    elif markers == 'false':
        markers = False
    if symbol_sequence_line == ['None']:
        symbol_sequence_line = [None]
    
    # Fields for scatter graphs
    size = data.get("size", None)
    opacity = data.get("opacity", None)
    size_max = data.get("size_max", None)
    symbol_sequence_scatter = [data.get("symbol_sequence_scatter", None)]
    marginal_x = data.get("marginal_x", None)
    marginal_y = data.get("marginal_y", None)
    
    if symbol_sequence_scatter == ['None']:
        symbol_sequence_scatter = [None]
    if size == 'None':
        size = None
    if opacity == 'None' or opacity == '':
        opacity = None
    else:
        opacity = float(opacity)
    if size_max == 'None' or size_max == '':
        size_max = None
    else:
        size_max = int(size_max)
    if marginal_x == 'None':
        marginal_x = None
    if marginal_y == 'None':
        marginal_y = None
        
    # Fields for bar graphs
    opacity_bar = data.get("opacity_bar", None)
    barmode = data.get("barmode", None)
    orientation = data.get("orientation", None)
    text_auto = data.get("text_auto", None)
    text = data.get("text", None)
    pattern_shape = data.get("pattern_shape", None)

    if opacity_bar == 'None' or opacity_bar == '':
        opacity_bar = None
    else:
        opacity_bar = float(opacity_bar)
    if barmode == 'None':
        barmode = None
    if text_auto == 'true':
        text_auto = True
    elif text_auto == 'false':
        text_auto = False
    if text == 'None':
        text = None
    if pattern_shape == 'None':
        pattern_shape = None
        
    # Fields for box graphs
    orientation_box = data.get("orientation_box", None)
    boxmode = data.get("boxmode", None)
    points_box = data.get("points_box", None)
    notched = data.get("notched", None)

    if boxmode == 'None':
        boxmode = None
    if points_box == 'None':
        points_box = None
    if notched == 'true':
        notched = True
    elif notched == 'false':
        notched = False
        
    # Fields for violin graphs
    points_violin = data.get("points_violin", None)
    violinmode = data.get("violinmode", None)
    box = data.get("box", None)

    if violinmode == 'None':
        violinmode = None
    if points_violin == 'None':
        points_violin = None
    if box == 'true':
        box = True
    elif box == 'false':
        box = False
    
    # Fields for histogram graphs
    pattern_shape_hist = data.get("pattern_shape_hist", None)
    marginal = data.get("marginal", None)
    opacity_hist = data.get("opacity_hist", None)
    orientation_hist = data.get("orientation_hist", None)
    barnorm = data.get("barnorm", None)
    histnorm = data.get("histnorm", None)
    histfunc = data.get("histfunc", None)
    cumulative = data.get("cumulative", None)
    nbins = data.get("nbins", None)
    text_auto_hist = data.get("text_auto_hist", None)
    
    print(marginal, type(marginal))
    
    if opacity_hist == 'None' or opacity_hist == '':
        opacity_hist = None
    else:
        opacity_hist = float(opacity_hist)
    if pattern_shape_hist == 'None':
        pattern_shape_hist = None
    if marginal == 'None':
        marginal = None
    if barnorm == 'None' or barnorm == '':
        barnorm = None
    if histnorm == 'None' or histnorm == '':
        histnorm = None
    if nbins == 'None' or nbins == '':
        nbins = None
    if cumulative == 'true':
        cumulative = True
    elif cumulative == 'false':
        cumulative = False
    if text_auto_hist == 'true':
        text_auto_hist = True
    elif text_auto_hist == 'false':
        text_auto_hist = False

    # Fields for pie graphs
    hole = data.get("hole", None)
    opacity_pie = data.get("opacity_pie", None)
    
    if hole == 'None' or hole == '':
        hole = None
    else:
        hole = float(hole)
    if opacity_pie == 'None' or opacity_pie == '':
        opacity_pie = None
    else:
        opacity_pie = float(opacity_pie)
    
    if Type == "Line":
        fig = px.line(
                df,
                x=x_axis,
                y=y_axis,
                hover_name=hover_name,
                color=color,
                title=title,
                template=template,
                line_shape=line_shape,
                line_dash_sequence=line_dash_sequence,
                markers=markers,
                symbol_sequence=symbol_sequence_line,
                animation_frame=animation_frame,
                animation_group=animation_group,
                facet_row=facet_row, 
                facet_col=facet_col, 
                facet_col_wrap=facet_col_wrap, 
                facet_row_spacing=facet_row_spacing, 
                facet_col_spacing=facet_col_spacing
            )
            
    elif Type == "Scatter":
        fig = px.scatter(
                df,
                x=x_axis,
                y=y_axis,
                hover_name=hover_name,
                color=color,
                title=title,
                template=template,
                size = size,
                opacity = opacity,
                size_max = size_max,
                symbol_sequence = symbol_sequence_scatter,
                marginal_x = marginal_x,
                marginal_y = marginal_y,
                animation_frame=animation_frame,
                animation_group=animation_group,
                facet_row=facet_row, 
                facet_col=facet_col, 
                facet_col_wrap=facet_col_wrap, 
                facet_row_spacing=facet_row_spacing, 
                facet_col_spacing=facet_col_spacing
            )
            
    elif Type == "Bar":
        fig = px.bar(
                df,
                x=x_axis,
                y=y_axis,
                hover_name=hover_name,
                color=color,
                title=title,
                template=template,
                opacity = opacity_bar,
                barmode = barmode,
                orientation = orientation,
                pattern_shape = pattern_shape,
                text = text,
                text_auto = text_auto,
                animation_frame=animation_frame,
                animation_group=animation_group,
                facet_row=facet_row, 
                facet_col=facet_col, 
                facet_col_wrap=facet_col_wrap, 
                facet_row_spacing=facet_row_spacing, 
                facet_col_spacing=facet_col_spacing
            )
        
    elif Type == "Pie":
        fig = px.pie(
                df,
                names=x_axis,
                values=y_axis,
                hover_name=hover_name,
                color=color,
                title=title,
                template=template,
                opacity = opacity_pie,
                hole = hole,
                facet_row=facet_row, 
                facet_col=facet_col, 
                facet_col_wrap=facet_col_wrap, 
                facet_row_spacing=facet_row_spacing, 
                facet_col_spacing=facet_col_spacing
            )
        
    elif Type == "Box":
        fig = px.box(
                df,
                x=x_axis,
                y=y_axis,
                hover_name=hover_name,
                color=color,
                title=title,
                template=template,
                boxmode = boxmode,
                orientation = orientation_box,
                points = points_box,
                notched = notched,
                animation_frame=animation_frame,
                animation_group=animation_group,
                facet_row=facet_row, 
                facet_col=facet_col, 
                facet_col_wrap=facet_col_wrap, 
                facet_row_spacing=facet_row_spacing, 
                facet_col_spacing=facet_col_spacing
            )
        
    elif Type == "Violin":
        fig = px.violin(
                df,
                x=x_axis,
                y=y_axis,
                hover_name=hover_name,
                color=color,
                title=title,
                template=template,
                violinmode = violinmode,
                points = points_violin,
                box = box,
                animation_frame=animation_frame,
                animation_group=animation_group,
                facet_row=facet_row, 
                facet_col=facet_col, 
                facet_col_wrap=facet_col_wrap, 
                facet_row_spacing=facet_row_spacing, 
                facet_col_spacing=facet_col_spacing
            )
        
    elif Type == "Histogram":
        fig = px.histogram(
                df,
                x=x_axis,
                y=y_axis,
                hover_name=hover_name,
                color=color,
                title=title,
                template=template,
                pattern_shape=pattern_shape_hist,
                marginal=marginal,
                orientation=orientation_hist,
                barnorm=barnorm,
                histnorm=histnorm,
                histfunc=histfunc,
                cumulative=cumulative,
                nbins=nbins,
                text_auto=text_auto_hist,
                animation_frame=animation_frame,
                animation_group=animation_group,
                facet_row=facet_row, 
                facet_col=facet_col, 
                facet_col_wrap=facet_col_wrap, 
                facet_row_spacing=facet_row_spacing, 
                facet_col_spacing=facet_col_spacing
        )

            
    print(fig)
    return fig
