import dash
import dash_core_components as dcc
import dash_html_components as html
from graph_data import *
from summary import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Analysis of Life in Europe',
            style={'color': 'ghostwhite', 'fontSize': 50, 'font-family': 'cursive', 'text-align': 'center',
                   'backgroundColor': '#311e73'}),
    html.H3(children='Created by:',
            style={'color': '#9fb4cc', 'fontSize': 24, 'text-align': 'center', 'backgroundColor': '#140057'}),
    html.H2(
        children='Kunal PATIL (Artificial Intelligence System) & Salil MARATH-PONMADOM (Data Science and Analytics)',
        style={'color': '#efedf5', 'fontSize': 20, 'text-align': 'center', 'backgroundColor': '#6b54ba'}),
    html.H3(children='######################################',
            style={'color': '#180847', 'fontSize': 10, 'text-align': 'center', 'backgroundColor': '#180847'}),
    html.H5(children='''
        The aim is to analyse the data which compares multiple factors for European countries which are resposnsible for life in Europe. 
        With the help of DASH: A python web framework for visualization we visualise and compare some of the key factors – 
        like Economy, Politics, Environment, Health and so many for all European countries.''',
            style={'text-align': 'center', 'fontSize': 18}),
    html.H3(children='######################################',
            style={'color': '#180847', 'fontSize': 10, 'text-align': 'center', 'backgroundColor': '#180847'}),

    html.H4(
        children="Economy",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),
    dcc.Graph(
        id='gdp',
        figure=fig_gdp
    ),
    html.H5(
        children="Observation and Comments: By observing above distribution, we can see that Countries like UK, France, Italy and Spain have highest GDP than other european countries, Whereas Germany have Highest GDP among all.",
        style={'color': 'darkslateblue', 'fontSize': 16}),

    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='low_savings',
        figure=fig_low_savings
    ),
    html.H5(
        children="Observation and Comments: Countries like Bulgaria, Cyprus, Greece, Croatia, Lithuania, Romania have Lower savings that other european countries, Whereas Latvia have Lowest savings, i.e. 60%",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='median_income_and_population',
        figure=fig_median_income_population
    ),
    html.H5(
        children="Observation and Comments: Comparing population with respect to median income, Luxembourg has Highest median income and less population. "
                 "Romania have lowest median income but population is about 20M, whereas Germany having highest population almost 80M still have quite good median income about 21k",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),

    html.H4(
        children="Employment",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),

    dcc.Graph(
        id='job_satisfaction',
        figure=fig_job_satisfaction
    ),
    html.H5(
        children="Observation and Comments: Only two of the European Countries are having low Job Satisfaction, Turkey and Bulgaria. Rest all citizens in rest countries are satified with their jobs.",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='unemployment',
        figure=fig_unemployment
    ),
    html.H5(
        children="Observation and Comments: The rate of unemployment is highest in Greece at 23% and lowest in Iceland at only 3%",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),

    html.H4(
        children="Politics",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),
    dcc.Graph(
        id='close_relations',
        figure=fig_close_relation
    ),
    html.H5(
        children="Observation and Comments: Countries like Czechia, Slovakia and Finland are among those High Percentage of Close Relations in Europe."
                 "Other Countries like Hungary, Spain, Cyprus also have a good percentage in Close Relations. "
                 "While Countries like Italy, Luxembourg and Portugal are the countries with least percantage in comparison to other countries in Europe.",
        style={'color': 'black', 'fontSize': 16}),

    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='political_trust',
        figure=fig_political_trust
    ),
    html.H5(
        children="Observation and Comments: Citizens of Switzerland have more trustful Political department, "
                 "followed by Finland Denmark, Norway and Malta. Whereas Italy, Portugal, Slovenia, Greece and Spain have least trust in Political department.",
        style={'color': 'darkslateblue', 'fontSize': 16}),

    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),
    html.H4(
        children="Legal",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),

    dcc.Graph(
        id='crime_rate',
        figure=fig_crime_rate
    ),
    html.H5(
        children="Observation and Comments: Bulgaria have the highest crime rate in the European Countries, But the Countries like Netherlands, UK, France and Italy are also having crime rates in second to the highest, Whereas Iceland have the lowest crime rate.",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='legal_trust',
        figure=fig_legal_trust_subplot
    ),
    html.H5(
        children="Observation and Comments: Citizens of Finland are most trustful with Police department. Whereas Citizens of Denmark are trustful with Police as well as Legal department "
                 "On average, Slovania have both values low, the country with less trust on police and legal system!",
        style={'color': 'darkslateblue', 'fontSize': 16}),

    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),

    html.H4(
        children="Environment",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),

    dcc.Graph(
        id='weather',
        figure=fig_avg_temp
    ),
    html.H5(
        children="Observation and Comments: Countries Like Greece , Spain , Portugal leads in Average Temperature in Europe while Finland , Iceland , Norway are those with less in average temparature in Comparison to the rest of EU Countries.",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='env_satisfaction',
        figure=fig_env_satisfaction
    ),
    html.H5(
        children="Observation and Comments: Austria has the highest percentage of environment satisfaction followed by Denmark and Norway. While Bulgaria has the Least Environmental Satisfaction percentage where as Italy and Cyprus is also Low in Percentage.",
        style={'color': 'darkslateblue', 'fontSize': 16}),

    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),

    html.H4(
        children="Health",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),

    dcc.Graph(
        id='health_data',
        figure=fig_health_data
    ),
    html.H5(
        children="Observation and Comments: Cyprus, Greece, Ireland, Iceland, Norway, Sweden, Switchzerland and "
                 "UK have very high rate of good health.",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='pollution',
        figure=fig_pollution
    ),
    html.H5(
        children="Observation and Comments: Most polluted country reported is Malta. Germany and Turkey are also high on chart."
                 "Whereas Ireland reported least pollution.",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#5d5179', 'fontSize': 2, 'text-align': 'center', 'backgroundColor': '#5d5179'}),
    dcc.Graph(
        id='life_expectancy',
        figure=fig_life_expectation
    ),
    html.H5(
        children="Observation and Comments: Life expectancy in Europe is really higher than whole world, where Italy "
                 "and Spain have highest among all european countries."
                 "All countries, on average have life expectancy above 75%",
        style={'color': 'darkslateblue', 'fontSize': 16}),
    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),

    html.H4(
        children="Life Satisfaction",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),

    dcc.Graph(
        id='life_satisfaction',
        figure=fig_life_satisfaction_subplot
    ),
    html.H5(
        children="Observation and Comments: Countries like Denmark, Iceland, Finland have High rate of Leisure and Life Satisfaction."
                 "Where as Bulgaria, Hungry, Turkey are those countries with least rates in Comparison."
                 "In general that the scandinavian countries has the good rate Leisure as well as Life Satisfaction.",
        style={'color': 'darkslateblue', 'fontSize': 16}),

    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),
    html.H6(children='######################################',
            style={'color': 'white', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': 'white'}),
    html.H6(children='######################################',
            style={'color': 'white', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': 'white'}),
    html.H4(
        children="Summary",
        style={'color': '#44874e', 'fontSize': 28, 'text-align': 'center'}),

    html.Div(
        [
            dcc.Dropdown(
                id="Country",
                options=[{
                    'label': i,
                    'value': i
                } for i in summary['Country']], value='Belgium'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='line_polar'),
    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),
    html.H4(
        children="Conclusion",
        style={'color': '#44874e', 'fontSize': 30, 'text-align': 'center'}),
    html.H5(
        children="The country having Highest Economy is Germany."
                 " Highest rate of Employment is Iceland,"
                 " Good Politics establishment in Denmark,"
                 " Good Environment in Austria,"
                 " Better Health facilities in Sweden,"
                 "One can look for Life Satisfaction in Denmark "
                 "And Legal department is very trustful in Denmark too."
                 " So we can say in multiple aspects, Denmark is really good country to live!",
        style={'color': 'darkslateblue', 'fontSize': 18}),
    html.H6(children='######################################',
            style={'color': '#180847', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': '#180847'}),
    html.H6(children='######################################',
            style={'color': 'white', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': 'white'}),
    html.H6(children='######################################',
            style={'color': 'white', 'fontSize': 7, 'text-align': 'center', 'backgroundColor': 'white'}),
    html.H1(children='Merci à tous!!',
            style={'color': 'ghostwhite', 'fontSize': 50, 'font-family': 'cursive', 'text-align': 'center',
                   'backgroundColor': '#311e73'}),
])


@app.callback(
    dash.dependencies.Output('line_polar', 'figure'),
    [dash.dependencies.Input('Country', 'value')])
def update_graph(Country):
    if Country == "Belgium":
        df_plot = data.copy()
    else:
        df_plot = data[data['Country'] == Country]
    trace = px.line_polar(df_plot, theta=data['Country'], r=data[Country], line_close=True, template="plotly_dark",
                          title='Summary of Factors (%)')
    return trace


app.title = 'Analysis of Life in Europe'

if __name__ == '__main__':
    app.run_server(debug=True)
