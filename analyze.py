import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

pd.options.mode.chained_assignment = None

data = pd.read_csv("~/Desktop/metis/project_luther/final_data_genre.csv")

""" HEADERS:
['movie_title', 'domestic_total_gross', 'runtime', 'budget',
'release_date', 'distributor', 'genre', 'actors', 'director',
'producers', 'rank_year', 'rank_history', 'number_theaters',
'close_date', 'imdb_rating', 'metascore_rating', 'rt_critics',
'rt_audience', 'video_sales']
"""

def make_sets(data_df, test_portion):
    import random as rnd

    tot_ix = range(len(data_df))
    test_ix = sorted(rnd.sample(tot_ix, int(test_portion * len(data_df))))
    train_ix = list(set(tot_ix) ^ set(test_ix))

    test_df = data_df.ix[test_ix]
    train_df = data_df.ix[train_ix]

    return train_df, test_df

data.drop_duplicates(inplace=True)
data, test = make_sets(data, 0.25)

data.budget[889] = 6000000
data.genre[667] = 'Romantic'

# newdf = df[(df['column_one']>2004) & (df['column_two']==9)]

data = data[~((data['genre'] == 'Comedy') & (data['rt_critics'] < 70))]


data['budget'] = data['budget'].convert_objects(convert_numeric=True)
data['rt_critics'] = data['rt_critics'].convert_objects(convert_numeric=True)
data['rt_audience'] = data['rt_audience'].convert_objects(convert_numeric=True)
data['rank_year'] = data['rank_year'].convert_objects(convert_numeric=True)
data['video_sales'] = data['video_sales'].convert_objects(convert_numeric=True)


data['agg_rating'] = (data['rt_audience'] + data['rt_critics'])/float(2)

data['gross_to_budget'] = data['domestic_total_gross']/data['budget']

data['log_gross'] = np.log(data['domestic_total_gross'])
data['log_g_b'] = np.log(data['gross_to_budget'])

sorted_by_ratio = data.sort(columns='gross_to_budget', ascending=False)

show = sorted_by_ratio[['movie_title', 'genre', 'rt_critics', 'gross_to_budget']]

print show.head(50)


# r2 = sm.ols(formula="gross_to_budget ~ distributor + rt_critics", data=data)
# res2 = r2.fit()
# print res2.summary()

r = sm.ols(formula="np.log(gross_to_budget) ~ C(genre) + number_theaters + rt_critics", data=data)
result = r.fit()
#print result.params
print result.summary()

plt.hist(result.resid, bins=20)
plt.ylabel('Box Office Gross to Bugdet Ratio')
plt.xlabel('Residuals (ϵ)')
plt.show()
# plt.scatter(data['gross_to_budget'], data['rt_critics'])
# plt.show()
