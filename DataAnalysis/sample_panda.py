import pandas as pd

metro = pd.read_csv('/Users/vinayreddy/Downloads/query_result_2018-08-09T13_16_31.754Z.csv', index_col=0)


bounce = metro.head(11000)

print(bounce)