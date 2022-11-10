import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
import plotly.graph_objects as go

def sns_line_plot(x, y, title):
    ax = plt.axes()
    sns.lineplot(x = x, y = y, ax = ax)
    ax.set(title = title)
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))

def double_sns_lineplot(x1, y1, x2, y2, title):
    ax = plt.axes()
    sns.lineplot(x = x1, y = y1, ax = ax)
    sns.lineplot(x = x2, y = y2, ax = ax)    
    ax.set(title = title)
    ax.set_yscale("log") # y-axis set to logarithmic which makes it easier to compare and read
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))

def plotly_bar_plot(df, x, y, title, save_file_title):

    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title
    )
    fig.show()
    fig.write_html("../Labb_1/Visualiseringar/"+save_file_title+".html")

def plotly_bar_plot_with_labels_sublabels (x, y, title, labels, sublabels, file_name_save):

    fig = px.bar(
        x=x,
        y=y,
        barmode= 'group', # groups the bars next to eachother instead of stacking on eachother
        labels=labels,
        title=title
    )
    newnames = sublabels
    # To be able to change the sub titles for 'Antal doser' without changing the data source,
    # you can switch the legendgroups name with a dict and map it onto existing subtitle names.
    # I had to do this since I couldn't change it through 'labels=' like the other titles
    # source: https://stackoverflow.com/questions/64371174/plotly-how-to-change-variable-label-names-for-the-legend-in-a-plotly-express-li
    fig.for_each_trace(lambda t: t.update(name=newnames[t.name]))

    # angles the provinces in order the read more easily
    fig.update_xaxes(tickangle=40)
    fig.show()

    fig.write_html("../Labb_1/Visualiseringar/"+file_name_save+".html")

def log_plotly_bar_with_df_title_labels(df, y, x, title, labels, save_file):
    fig = px.bar(
        df,
        y=y,
        x=x,
        barmode="group",  # groups the bars next to eachother instead of stacking on eachother
        labels=labels,
        title=title,
        log_y=True,  # easier to read, makes y-axes logarithmic
    )

    fig.show()
    fig.write_html("../Labb_1/Visualiseringar/" + save_file + ".html")

def continent_total(variable_name, continent_name):
    variable_name = worldcoviddata[(worldcoviddata["country"] == continent_name)].sort_values(by='cumulative_count', ascending=False).head()
    print(variable_name['cumulative_count'].head(1))