"""
html.Div(
        [
            dcc.Dropdown(
                id="Country",
                options=[{
                    'label': i,
                    'value': i
                } for i in euro_stats_data['country']],
                value='European countries'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])


@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('Country', 'value')])
def update_graph(Country):
    if Country == "European countries":
        df_plot = euro_stats_data.copy()
    else:
        df_plot = euro_stats_data[euro_stats_data['country'] == Country]

    pv = pd.pivot_table(
        df_plot,
        index=['country'],
        columns=["prct_life_satis_high", "prct_life_satis_med"],
        values=['prct_life_satis_high', "prct_life_satis_med"],
        aggfunc=sum,
        fill_value=0)

trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')

return {
    'data': [trace1],
    'layout':
    go.Layout(
        title='Customer Order Status for {}'.format(Manager),
        barmode='stack')
}
"""