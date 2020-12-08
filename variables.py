import pandas as pd

euro_stats_data = pd.read_csv("datasets/euro_stats.csv")

# Economy
gdp_data = pd.read_csv("datasets/gdp.csv")
low_savings_data = pd.read_csv("datasets/low_savings.csv")
median_income_data = pd.read_csv("datasets/median_income.csv")
population_data = pd.read_csv("datasets/population.csv")

# Employment
job_satisfaction_data = pd.read_csv('datasets/job_satisfaction.csv')
unemployment_data = pd.read_csv('datasets/unemployment.csv')

# Legal
crime_data = pd.read_csv('datasets/crime.csv')

# Health
health_data = pd.read_csv('datasets/perceived_health.csv')
life_expectation_data = pd.read_csv('datasets/life_expectancy.csv')

# Politics
close_relations = pd.read_csv('datasets/close_relations.csv')
