import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


class Controls:


    def get_controls(df): 
        controls = dbc.Card(
            [
                dbc.FormGroup(
                    [   #Define brand dropdown
                        dbc.Label("Brand"),
                        dcc.Dropdown(
                            options=[
                                {'label': 'All', 'value': 'ALL'},
                                {'label': 'Volvo', 'value': 'volvo'},
                                {'label': 'Volkswagen', 'value': 'volkswagen'},
                                {'label': 'Toyota', 'value': 'toyota'},
                                {'label': 'Subaru', 'value': 'subaru'},
                                {'label': 'SAAB', 'value': 'saab'},
                                {'label': 'Renault', 'value': 'renault'},
                                {'label': 'Porsche', 'value': 'porsche'},
                                {'label': 'Plymouth', 'value': 'plymouth'},
                                {'label': 'Peugot', 'value': 'peugot'},
                                {'label': 'Nissan', 'value': 'nissan'},
                                {'label': 'Mitsubishi', 'value': 'mitsubishi'},
                                {'label': 'Mercedes-Benz', 'value': 'mercedes-benz'},
                                {'label': 'Mazda', 'value': 'mazda'},
                                {'label': 'Jaguar', 'value': 'jaguar'},
                                {'label': 'Honda', 'value': 'honda'},
                                {'label': 'Isuzu', 'value': 'isuzu'},
                                {'label': 'Dodge', 'value': 'dodge'},
                                {'label': 'Chevrolet', 'value': 'chevrolet'},
                                {'label': 'BMW', 'value': 'bmw'},
                                {'label': 'Audi', 'value': 'audi'},
                                {'label': 'Alfa-Romeo', 'value': 'alfa-romeo'}
                            ],
                            multi=True, id='brand-drop', value=['ALL']
                        )             
                    ]
                ),
                dbc.FormGroup(
                    [   #Define body dropdown
                        dbc.Label("Body Type"),
                        dcc.Dropdown(
                            options=[
                                {'label': 'All', 'value': 'ALL'},
                                {'label': 'Convertible', 'value': 'convertible'},
                                {'label': 'Hardtop', 'value': 'hardtop'},
                                {'label': 'Hatchback', 'value': 'hatchback'},
                                {'label': 'Wagon', 'value': 'wagon'},
                                {'label': 'Sedan', 'value': 'sedan'}
                            ],
                            multi=True, id='body-drop', value=['ALL']
                        )              
                    ]
                ),
                dbc.FormGroup(
                    [   #Define price range slider
                        dbc.Label("Price"), 
                        dcc.RangeSlider(id='price-slider',min=0,max=50000,step=1000,value=[0, 50000], marks={
                            0: '0',
                            10000: '10k',
                            20000: '20k',
                            30000: '30k',
                            40000: '40k',
                            50000: '50k'
                        },),
                        html.Div(id='output-price', style={'padding-left':'35%'})
                    ],
                style={"align":"center"}),
                dbc.FormGroup(
                    [   #Define horsepower range slider
                        dbc.Label("Horse Power"), 
                        dcc.RangeSlider(id='horsepower-slider',min=0,max=300,step=10,value=[0, 300], marks={
                            0: '0',
                            50: '50',
                            100: '100',
                            150: '150',
                            200: '200',
                            250: '250',
                            300: '300'
                        },),
                        html.Div(id='output-horsepower', style={'padding-left':'35%'})
                    ]
                ),
                dbc.FormGroup(
                    [   #Define number of doors checklist
                        dbc.Label("No. of Doors"),
                        dcc.Checklist(
                            options=[
                                {'label': ' 2 Door', 'value': '2'},
                                {'label': ' 4 Door', 'value': '4'}
                                
                            ],
                            value=['2', '4'], 
                            labelStyle={'display': 'inline-block', 'margin': '10px'}, 
                            id='doors-list'
                        )  
                    ]
                ),
                dbc.FormGroup(
                    [   #Define fueltype checklist
                        dbc.Label("Fuel Type"),
                        dcc.Checklist(
                            options=[
                                {'label': ' Petrol', 'value': 'gas'},
                                {'label': ' Diesel', 'value': 'diesel'}
                                
                            ],
                            value=['gas', 'diesel'], 
                            labelStyle={'display': 'inline-block', 'padding': '11px'}, 
                            id='fuel-list'
                        ), html.Hr()  
                    ]
                ),
                dbc.FormGroup(
                    [
                        html.Div(id='output-num-elements', style={'padding-left':'15%'}), 
                    ]
                ),
                dbc.FormGroup(
                    [   #Define X-Axis Dropdown
                        dbc.Label("X-Axis"),
                        dcc.Dropdown(
                            options=[
                                {'label': ' Risk Factor', 'value': 'risk-factor'},
                                {'label': ' Normalized Loss', 'value': 'normalized-losses'},
                                {'label': ' Wheel base', 'value': 'wheel-base'},
                                {'label': ' Length', 'value': 'length'},
                                {'label': ' Width', 'value': 'width'},
                                {'label': ' Curb Weight', 'value': 'curb-weight'},
                                {'label': ' Engine Size', 'value': 'engine-size'},
                                {'label': ' Bore', 'value': 'bore'},
                                {'label': ' Stroke', 'value': 'stroke'},
                                {'label': ' Compression', 'value': 'compression'},
                                {'label': ' Horse Power', 'value': 'horsepower'},
                                {'label': ' Peak RPM', 'value': 'peak-rpm'},
                                {'label': ' City MPG', 'value': 'city-mpg'},
                                {'label': ' Highway MPG', 'value': 'highway-mpg'},
                                {'label': ' Price', 'value': 'price'}
                                
                            ],
                            value='price', 
                            id='X-Axis', clearable=False)
                        
                    ]
                ),
                dbc.FormGroup(
                    [   #Define Y-Axis dropdown
                        dbc.Label("Y-Axis"),
                        dcc.Dropdown(
                            options=[
                                {'label': ' Risk Factor', 'value': 'risk-factor'},
                                {'label': ' Normalized Loss', 'value': 'normalized-losses'},
                                {'label': ' Wheel base', 'value': 'wheel-base'},
                                {'label': ' Length', 'value': 'length'},
                                {'label': ' Width', 'value': 'width'},
                                {'label': ' Curb Weight', 'value': 'curb-weight'},
                                {'label': ' Engine Size', 'value': 'engine-size'},
                                {'label': ' Bore', 'value': 'bore'},
                                {'label': ' Stroke', 'value': 'stroke'},
                                {'label': ' Compression', 'value': 'compression'},
                                {'label': ' Horse Power', 'value': 'horsepower'},
                                {'label': ' Peak RPM', 'value': 'peak-rpm'},
                                {'label': ' City MPG', 'value': 'city-mpg'},
                                {'label': ' Highway MPG', 'value': 'highway-mpg'},
                                {'label': ' Price', 'value': 'price'}
                                
                            ],
                            value='risk-factor', 
                            id='Y-Axis',clearable=False)
                    ]
                ),
            ],
            body=True,
        )
        return controls 