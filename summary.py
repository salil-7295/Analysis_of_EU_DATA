from variables import *

summary = pd.DataFrame(columns=['Country', 'Economy', 'Politics', 'Environment', 'Employment', 'Life Satisfaction', 'Legal', 'Health'])

summary['Country'] = euro_stats_data['country']
summary['Economy'] = (100. * (euro_stats_data['median_income'] + euro_stats_data['gdp']) / (euro_stats_data['median_income'] + euro_stats_data['gdp']).sum()) *6
summary['Politics'] = euro_stats_data['legal_trust_rating'] * 10
summary['Environment'] = euro_stats_data['prct_env_satis_high']
summary['Employment'] = 100 - euro_stats_data['unemp_rate']
summary['Life Satisfaction'] = euro_stats_data['prct_life_satis_high'] * 2
summary['Legal'] = euro_stats_data['legal_trust_rating'] * 10
summary['Health'] = euro_stats_data['prct_health_verygood'] * 2

summary.T.to_csv(r'datasets/summary.csv')

data = pd.read_csv('datasets/summary.csv')
new_header = data.iloc[0]
data = data[1:]
data.columns = new_header



