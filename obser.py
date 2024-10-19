import pandas as pd

local_csv_path = 'C:\\Users\\ll7nt\\SMNAMonitoringApp\\examples\\jo\\jo_table_series.csv'

dfs = pd.read_csv(local_csv_path, header=1, parse_dates=['Date'])

print(dfs.head())
