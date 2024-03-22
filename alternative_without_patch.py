import json
import numpy as np
import pandas as pd
df= pd.read_csv("Environment world.csv")
import plotly.express as px
from dash import Dash, dcc, dash_table, html, Input, Output, State, MATCH, ALL, Patch
import dash_bootstrap_components as dbc
import matplotlib.colors as mcolors
def generate_colors(strings):
    unique_strings = list(set(strings))
    num_unique = len(unique_strings)
    colors = np.linspace(0, 1, num_unique)  # You can choose any colormap you like
    color_dict = {}

    for i, string in enumerate(unique_strings):
        rgba_color = mcolors.hsv_to_rgb([colors[i], 1, 1])
        hex_color = mcolors.to_hex(rgba_color)
        color_dict[string] = hex_color

    return color_dict

def assign_colors(strings, color_dict):
    colors = []
    for string in strings:
        colors.append(color_dict[string])
    return colors

app = Dash(__name__)
template_df_num = df.select_dtypes(include=['int', 'float','int64','float64'])
template_df_char = df.select_dtypes(exclude=['int', 'float','int64','float64'])

template_num_unique = template_df_num.columns.unique()
template_char_unique = template_df_char.columns.unique()



graph_r1_c3 = px.bar(df, x=template_num_unique[0], y=template_char_unique[0], color=template_char_unique[1], orientation= "h",)
graph_r1_c3.update_layout(margin=dict(l=0, r=0, t=40, b=0, pad=0),
                          title={'xanchor': 'center', 'yanchor': 'top', 'y': 0.99, 'x': 0.5, },

                          plot_bgcolor="white",
                          paper_bgcolor="white",
                          xaxis=dict(showline=True, showgrid=True, showticklabels=True,linecolor="RGBA(224,224,224,1)"),
                          yaxis=dict(showline=True, showgrid=True, showticklabels=True,linecolor="RGBA(224,224,224,1)"))
graph_r1_c3.update_yaxes(gridcolor='RGBA(228,225,233,1)', )
fig_json = graph_r1_c3.to_json()

app.layout= html.Div([
    html.Div([
                    dbc.FormText("Horizontal (X) Axis"),
                    dcc.Dropdown(template_num_unique, value=template_num_unique[0], id='template_dropdown_x_r1_c3'),
                    dbc.FormText("Vertical (Y) Axis"),
                    dcc.Dropdown(template_char_unique, value=template_char_unique[0], id='template_dropdown_y_r1_c3'),
                    dbc.FormText("Line color: IMPLEMENT PATCH HERE"),
                    dcc.Dropdown(template_char_unique, value=template_char_unique[1],id='template_dropdown_color_r1_c3',),
                ]),
        html.Div([dcc.Graph(id='template_graph_r1_c3', figure=graph_r1_c3, config={'editable': True})])
])

@app.callback(
    Output('template_graph_r1_c3', 'figure'),
    Input('template_dropdown_x_r1_c3', 'value'),
    Input('template_dropdown_y_r1_c3', 'value'),
    Input('template_dropdown_color_r1_c3','value')
    )
def graph_r1_c3(template_dropdown_x_r1_c3, template_dropdown_y_r1_c3,template_dropdown_color_r1_c3):
    graph_r1_c3 = px.bar(df, x=template_dropdown_x_r1_c3, y=template_dropdown_y_r1_c3, color=template_dropdown_color_r1_c3, orientation= "h",)
    graph_r1_c3.update_layout(margin=dict(l=0, r=0, t=40, b=0, pad=0),
                            title={'xanchor': 'center', 'yanchor': 'top', 'y': 0.99, 'x': 0.5, },

                            plot_bgcolor="white",
                            paper_bgcolor="white",
                            xaxis=dict(showline=True, showgrid=True, showticklabels=True,linecolor="RGBA(224,224,224,1)"),
                            yaxis=dict(showline=True, showgrid=True, showticklabels=True,linecolor="RGBA(224,224,224,1)"))
    graph_r1_c3.update_yaxes(gridcolor='RGBA(228,225,233,1)', )
    return graph_r1_c3



app.run_server(debug=True, use_reloader=False)