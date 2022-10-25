import matplotlib.pyplot as plt
import seaborn as sns


def bar_plot(dataframe):
    missingrows = dataframe.isnull().sum()
    sf = missingrows.loc[lambda x : x > 0]
    sns.barplot(x= sf.index, y=sf.values)