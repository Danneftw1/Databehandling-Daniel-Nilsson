import plotly_express as px
gapminder = px.data.gapminder()

fig = px.scatter(
    gapminder,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    log_x=True, # log_x räknar logaritmiskt istället
    size_max=70, # storleken på bubblorna
    color="country",
    animation_frame="year", #animerar alla år
    animation_group="country",
    title="Gapminder",
    range_y=[25, 90], 
    range_x=[100, 100_000],

)  
#fig.show()

fig.write_html("2.2_gapminder.html", auto_open = True)