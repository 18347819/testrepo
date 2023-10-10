#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#file name to execute in ibm cloud enviro    python3 DV0101EN-Final_Assign_Part_2_Questions.py

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')
data2 = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv')
max_payload = data2['Payload Mass (kg)'].max()
min_payload = data2['Payload Mass (kg)'].min()

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
#app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
#ropdown_options = [
    #{'label': 'Yearly_Statistics', 'value': 'Yearly_Statistics'},
    #{'label': 'Recession_Period_Statistics', 'value': 'Recession_Period_Statistics'}]
# List of years 
#year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------


# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("SpaceX Launch Records Dashboard",#May include style for title
    style={'textAlign': 'center', 'color': '#503D36','font-size': 40}),
   
    html.Br(),
    html.Br(),
    #html.Div(dcc.Dropdown(id='site-dropdown')), #test
    #html.Br(),
    #html.Div(dcc.Graph(id='success-pie-chart')),  #10-8-23 Moved this line down further below so dropdown appears at top before pie chart
    
    #html.Div(id='output-container-range-slider'),  #10-8-23 test line added
                                #])

    html.Div([#TASK 2.2: Add two dropdown menus
        
        #html.Label("Select_Statistics:"),
        
        dcc.Dropdown(
            id='site-dropdown',
            options=[
                            #{'label': 'Yearly_Statistics', 'value': 'Yearly_Statistics'},
                            #{'label': 'Recession_Period_Statistics', 'value': 'Recession_Period_Statistics'},
                            {'label': 'All Sites', 'value': 'ALL'},
                            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC 40'},
                            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC 4E'},
                            {'label': 'KSC LC-39A', 'value': 'KSC LC 39A'},
                            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC 40'}
                           ],
            value='ALL',
            placeholder='Select a Launch Site Here',
            searchable = True
        )
        ,

        html.Div(dcc.Graph(id='success-pie-chart')),  #10-8-23 had to add this line based upon airine template 
        
        
        dcc.RangeSlider(
            id='payload-slider',
            min=0, max=10000, step=1000,
            #marks={2500: '2500'},
                      # 100: '100'},
            value=[min_payload, max_payload]),
    
        html.Div(dcc.Graph(id='success-payload-scatter-chart')),  #10-8-23 had to add this line based upon airine template 
        
        #additional pie chart created for testing
        html.Div(dcc.Graph(id='success-pie-chart2'))  #10-8-23 had to add this line based upon airine template 

    ]),
    
    #html.Div([#TASK 2.3: Add a division for output display
    #html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),])
])


#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
#@app.callback(
    #Output(component_id='success-pie-chart', component_property='figure'),
    #Input(component_id='site-dropdown',component_property='value'))

#def update_input_container(select_statistics):
    #if select_statistics =='Yearly_Statistics': 
     #   return False
    #else: 
    #    return True
    
#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value')])
    #Input(component_id='select-year', component_property='value')])

#test callback  for task 4
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
    Input(component_id='payload-slider', component_property='value')
    #)
    ,
    Input(component_id='site-dropdown', component_property='value')])

#additional pie chart created for testing (the callback portion)
@app.callback(
    Output(component_id='success-pie-chart2', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value')])
   
    #Input(component_id='select-year', component_property='value')])






#component_id='site-dropdown', component_property='value'


#def update_output_container(select_statistics, input_year):
    #if select_statistics == 'Recession_Period_Statistics':
       # # Filter the data for recession periods
        #recession_data = data[data['Recession'] == 1]

#PIE CHART PLOT
def get_pie_chart(entered_site):
    
    filtered_df1 = data2.groupby('Launch Site')['class'].sum().reset_index()
    
    if entered_site == 'ALL':
       
        fig = px.pie(filtered_df1, 
            values='class', 
            names='Launch Site', 
            title='Total Success Launches By Site')
        return fig
    
    else:
        fig = px.pie(filtered_df1, 
            values='class', 
            names='Launch Site', 
            title='Total Success Launches By Site')
        return fig
        # return the outcomes piechart for a selected site


#test pie chart




#SCATTER PLOT CHART
def get_scatter_chart(entered_site):
    
    #filtered_df2 = data2.groupby('Payload Mass (kg)')['class'].mean().reset_index()
    filtered_df2 = data2

    if entered_site == 'ALL':
       
        fig = px.scatter(filtered_df2, 
            x='Payload Mass (kg)',
            y='class',
            #values='class', 
            #names='Launch Site',
            color='BoosterVersion', 
            title='Total Success Launches By Site')
        return fig
    
    else:
        fig = px.scatter(filtered_df2, 
            x='Payload Mass (kg)',
            y='class',
            #values='class', 
            #names='Launch Site', 
            color='BoosterVersion',
            title='Total Success Launches By Site')
        return fig
        # return the outcomes piechart for a selected site

       
        
#TASK 2.5: Create and display graphs for Recession Report Statistics

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        #yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        # Plotting the line graph
        #R_chart1 = dcc.Graph(
           # figure=px.line(yearly_rec, 
               # x='Year',
                #y='Automobile_Sales',
                #title="Average Automobile Sales fluctuation over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # use groupby to create relevant data for plotting
        #average_sales=recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                           
        #R_chart2  = dcc.Graph(
            #figure=px.bar(average_sales,
                #x='Vehicle_Type',
                #y='Automobile_Sales',
                #title="Average Vehicles Sold By Vehicle Type over Recession Period"))

# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        #exp_rec=recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()    
        #R_chart3  = dcc.Graph(
            #figure=px.pie(exp_rec,
                #values='Advertising_Expenditure',
                #names='Vehicle_Type',
                #title="Advertising Expenditure By Vehicle Type over Recession Period"))

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        #un_emp=recession_data.groupby('Vehicle_Type',)['Automobile_Sales'].mean().reset_index()   
        #R_chart4  = dcc.Graph(
            #figure=px.bar(un_emp,
                #x='Vehicle_Type',
                #y='Automobile_Sales',
                #title="Effect of Unemployment On Vehicle Sales over Recession Period"))


        #return [
               # html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children=R_chart2)],style={'display': 'flex-wrap'}),
                #html.Div(className='chart-item', children=[html.Div(children=R_chart3),html.Div(children=R_chart4)],style={'display': 'flex-wrap'})
               # ]

# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                             
   # elif (input_year and select_statistics=='Yearly_Statistics') :
        #yearly_data = data[data['Year'] == input_year]
                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Average Automobile sales using line chart for the whole period. CONFIRMED
        # note that datasource should be data for this chart and not yearly_data because all years must be considered
        #average_sales1=data.groupby('Year')['Automobile_Sales'].sum().reset_index()
        #Y_chart1 = dcc.Graph(
            #figure=px.line(average_sales1, 
                #x='Year',
                #y='Automobile_Sales',
                #title="Yearly Average Automobile Sales")) 

#TASK 2.6: Returning the graphs for displaying Yearly data
        #return [
                #html.Div(className='chart-item', children=[html.Div(children=Y_chart1),html.Div(children=Y_chart2)],style={'display': 'flex-wrap'}),
                #html.Div(className='chart-item', children=[html.Div(children=Y_chart3),html.Div(children=Y_chart4)],style={'display': 'flex-wrap'})
                #]
        
    #else:
        #return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

