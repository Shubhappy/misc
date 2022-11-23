#import libraries
import dash
from dash import html, dcc, dash
from dash import dash_table as dt
from dash.dependencies import Input, Output
from pandas import *

#Reading data file
dataframe=read_csv('Madhya Pradesh Population Data.csv')

#Web page initialization
app=dash.Dash()

#city=dataframe.State/City.unique().tolist()

#Layout design
app.layout=html.Div (children=[
    
    html.H1 ("Census-2011 Analysis of Districs of Madhaya Pradesh", style={ 'color':'green','text-align':'center'}),

    #html.Div( children=[dcc.Dropdown(id= 'Dropdown', 
    #options=[{'label':ct, 'value':ct} for ct in city], 
    #placeholder="-Choose the State/City-",
    #multi=False,
    #clearable=False,
    #value=dataframe.City.values
    #)]),
html.Div([dt.DataTable(
    id='Table Container',
    columns=[{"name":i, "id":i} for i in dataframe.columns],
    style_cell_conditional=[{'if': {'column_id': c},'font-size': '15px','textAlign': 'center','backgroundColor':'pink','border': '1px solid black'} for c in dataframe.columns],
    
    style_header={'backgroundColor':'rgb(210, 210, 210)', 'fontWeight':'bold','textAlign': 'center','font-size': '18px','border': '1px solid black'},
    data=dataframe.to_dict("records"),
    style_table={'overflowY':'scroll','maxHeight':'550px'},
    fixed_rows={'header':True},
    filter_action="native",
    filter_options={"case": "insensitive"},
    selected_rows=[],
    style_cell={'textAlign':'center'}
)
]
)
]
)


#Callback
@app.callback(
    Output(component_id='Table Container',component_property='children'),
    Input(component_id='Dropdown', component_property='value')
)
def update_row(value):
    #dff=dataframe.copy()
    val=value
    i=0
    while i<51:
        if value==dataframe.City[i]:
            
                #demo1=dataframe.columns
                '''demo1=dataframe.columns[2]
                demo1=dataframe.columns[3]
                demo1=dataframe.columns[4]
                demo1=dataframe.columns[5]
                demo1=dataframe.columns[6]'''
                return value
        i=i+1
        
#calling the server to run the dashboard
if __name__=='__main__':
    app.run_server()