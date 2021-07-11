import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from graph_elements.controls import Controls
from data_reader import DataReader
import numpy as np 

#Use external stylesheet
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])





df, temp = DataReader.getData()
# instantiate plots and control panel 
controls = Controls.get_controls(df)
figScatter = px.scatter(df, x="curb-weight", y="city-mpg", color="make", custom_data=["index"],hover_name="index")
figScatter.update_layout(clickmode='event+select')
figScatter.update_layout()
figScatter1 = px.scatter(df, x="price", y="risk-factor")
df1 = pd.DataFrame(dict(
    r=[0, 0, 0, 0, 0],
    theta=['horse-power','mpg','weight',
           'price', 'engine-size']))
figRadar = px.line_polar(df1, r='r', theta='theta', line_close=True, range_r=[0,5])


#define app layout
app.layout = dbc.Container(
    [
        html.H4("Assignment 4 - Cars Dataset"),
        html.H5("by Matus Maruna (MM223FJ)"),
        html.Hr(),

        dbc.Row(
            [
            dbc.Col(controls, width={"size": 2}), 
            dbc.Col(
                [
                    dbc.Row(
                        [
                        dbc.Row(dcc.Graph(id="scatter", figure=figScatter, style={'width':'1300px', 'margin-left':'50px'})),
                        ]
                    ), 
                    dbc.Row(
                        [
                        dbc.Row(html.Div(id='detail-output',style={'width':'360px', 'padding-left': '100px'})) ,
                        dbc.Row(html.Div(id='detail-output1',style={'width':'340px'})) ,
                        dbc.Row(dcc.Graph(id="radar",figure=figRadar))   
                        ]

                    )
                ], 
            )
            ], align="top"
       )
    ], 
    fluid=True,
)

#define call backs 

# Update text output Price 

@app.callback(
    dash.dependencies.Output('output-price', 'children'),
    [dash.dependencies.Input('price-slider', 'value')])
def update_output(value):
    return value[0], ' - ', value[1]


# Update text output Horsepower

@app.callback(
    dash.dependencies.Output('output-horsepower', 'children'),
    [dash.dependencies.Input('horsepower-slider', 'value')])
def update_output(value):
    return value[0], ' - ', value[1]

# Update numElements 

@app.callback(
    dash.dependencies.Output('output-num-elements', 'children'),
    [dash.dependencies.Input('price-slider', 'value'), 
    dash.dependencies.Input('horsepower-slider', 'value'), 
    dash.dependencies.Input('brand-drop', 'value'), 
    dash.dependencies.Input('body-drop', 'value'), 
    dash.dependencies.Input('doors-list', 'value'), 
    dash.dependencies.Input('fuel-list', 'value')
    ])
def update_output(priceValue, horseValue, brandValue, bodyValue, doorValue, fuelValue):
    dff = df[df['price'].between(priceValue[0], priceValue[1])]
    dff = dff[dff['horsepower'].between(horseValue[0], horseValue[1])]
    dff =  dff[dff['num-of-doors'].isin(doorValue)]
    dff =  dff[dff['fuel-type'].isin(fuelValue)]
    if 'ALL' not in brandValue: 
        dff = dff[dff['make'].isin(brandValue)]
    if 'ALL' not in bodyValue: 
        dff = dff[dff['body-style'].isin(bodyValue)]
    return 'Number of cars: ', len(dff)

# Update scatterplot

@app.callback(
    dash.dependencies.Output('scatter', 'figure'),
    [dash.dependencies.Input('price-slider', 'value'), 
    dash.dependencies.Input('horsepower-slider', 'value'), 
    dash.dependencies.Input('brand-drop', 'value'), 
    dash.dependencies.Input('body-drop', 'value'), 
    dash.dependencies.Input('doors-list', 'value'), 
    dash.dependencies.Input('fuel-list', 'value'),
    dash.dependencies.Input('X-Axis', 'value'), 
    dash.dependencies.Input('Y-Axis', 'value')
    ])
def update_output(priceValue, horseValue, brandValue, bodyValue, doorValue, fuelValue, xAxis, yAxis):
    dff = df[df['price'].between(priceValue[0], priceValue[1])]
    dff = dff[dff['horsepower'].between(horseValue[0], horseValue[1])]
    dff =  dff[dff['num-of-doors'].isin(doorValue)]
    dff =  dff[dff['fuel-type'].isin(fuelValue)]
    if 'ALL' not in brandValue: 
        dff = dff[dff['make'].isin(brandValue)]
    if 'ALL' not in bodyValue: 
        dff = dff[dff['body-style'].isin(bodyValue)]
    if len(dff) is not 0:
        fig = px.scatter(dff, x=xAxis, y=yAxis, color="make", custom_data=["index"],hover_name="index")
    else:
        fig = px.scatter(dff, x=xAxis, y=yAxis, custom_data=["index"],hover_name="index")
    fig.update_layout(clickmode='event+select')
    return fig


# Update text output Horsepower

@app.callback(
    dash.dependencies.Output('radar', 'figure'),
    [dash.dependencies.Input('scatter', 'hoverData'), 
    dash.dependencies.Input('scatter', 'selectedData')])
def update_output(value, selectedValue):
    if selectedValue is None: 
        if value is not None: 
            index = value['points'][0]['customdata']
            dff = temp[temp['index'] == index[0]]

            #creating figure
            df1 = pd.DataFrame(dict(
            r=[dff['horsepower'].values[0], dff['mpg'].values[0], dff['curb-weight'].values[0], dff['price'].values[0], dff['engine-size'].values[0]],
            theta=['horse-power','mpg','weight',
            'price', 'engine-size']))
            fig = px.line_polar(df1, r='r', theta='theta', line_close=True, range_r=[0,5])
            return fig
        else: 
            df1 = pd.DataFrame(dict(
            r=[0, 0, 0, 0, 0],
            theta=['horse-power','mpg','weight',
            'price', 'engine-size']))
            fig = px.line_polar(df1, r='r', theta='theta', line_close=True, range_r=[0,5])
            return fig
    else: 
        df1 = pd.DataFrame(dict(
        r=[0, 0, 0, 0, 0],
        theta=['horse-power','mpg','weight',
        'price', 'engine-size']))
        fig = px.line_polar(df1, r='r', theta='theta', line_close=True, range_r=[0,5])
        for point in selectedValue['points']: 
            index = point['customdata']
            dff = temp[temp['index'] == index[0]]
            #creating figure
            df1 = pd.DataFrame(dict(
            r=[dff['horsepower'].values[0], dff['mpg'].values[0], dff['curb-weight'].values[0], dff['price'].values[0], dff['engine-size'].values[0], dff['horsepower'].values[0]],
            theta=['horse-power','mpg','weight',
            'price', 'engine-size', 'horse-power']))
            lineName = str(dff['make'].values[0]) + ' ID: ' + str(index[0])
            fig.add_trace(go.Scatterpolar(r=df1['r'], theta=df1['theta'], name=lineName))
        return fig

#Update detail output text

@app.callback(
    dash.dependencies.Output('detail-output', 'children'),
    [dash.dependencies.Input('scatter', 'hoverData')])
def update_output(value):
    if value is not None: 
        index = value['points'][0]['customdata']
        dff = df[df['index'] == index[0]]
        info = 'ID: ' +  str(index[0])  + '\n' + 'Brand: ' + dff['make'].values[0] + ' \n'

        return html.Div(html.P(['ID: ', str(index[0]), html.Br(),
         'Brand: ',dff['make'].values[0],html.Br(),
         'Risk-Factor: ',dff['risk-factor'].values[0],html.Br(),
         'Normalized-Losses: ',dff['normalized-losses'].values[0],html.Br(),
         'Fuel Type: ',dff['fuel-type'].values[0],html.Br(),
         'Aspiration: ',dff['aspiration'].values[0],html.Br(),
         'No. of doors: ',dff['num-of-doors'].values[0],html.Br(),
         'Body Style: ',dff['body-style'].values[0],html.Br(),
         'Drive Wheels: ',dff['drive-wheels'].values[0],html.Br(),
         'Engine Location: ',dff['engine-location'].values[0],html.Br(),
         'Wheel base: ',dff['wheel-base'].values[0],html.Br(),
         'Length: ',dff['length'].values[0],html.Br(),
         'Width: ',dff['width'].values[0],html.Br(),
         'Height: ',dff['height'].values[0],html.Br()]))
    else: 
        return ''

#Update detail output second column text 

@app.callback(
    dash.dependencies.Output('detail-output1', 'children'),
    [dash.dependencies.Input('scatter', 'hoverData')])
def update_output(value):
    if value is not None: 
        index = value['points'][0]['customdata']
        dff = df[df['index'] == index[0]]
        info = 'ID: ' +  str(index[0])  + '\n' + 'Brand: ' + dff['make'].values[0] + ' \n'

        return html.Div(html.P([
         'Height: ',dff['height'].values[0],html.Br(),
         'Curb Weight: ',dff['curb-weight'].values[0],html.Br(),
         'Engine Type: ',dff['engine-type'].values[0],html.Br(),
         'No. of cylinders: ',dff['num-of-cylinders'].values[0],html.Br(),
         'Engine Size: ',dff['engine-size'].values[0],html.Br(),
         'Fuel System: ',dff['fuel-system'].values[0],html.Br(),
         'Bore: ',dff['bore'].values[0],html.Br(),
         'Stroke: ',dff['stroke'].values[0],html.Br(),
         'Compression Ration: ',dff['compression-ratio'].values[0],html.Br(),
         'Horse Power: ',dff['horsepower'].values[0],html.Br(),
         'Peak RPM: ',dff['peak-rpm'].values[0],html.Br(),
         'City MPG: ',dff['city-mpg'].values[0],html.Br(),
         'Highway MPG: ',dff['highway-mpg'].values[0],html.Br(),
         'Price: ',dff['price'].values[0]]))
    else: 
        return ''





if __name__ == "__main__":
    app.run_server()