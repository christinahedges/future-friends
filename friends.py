import numpy as np
import altair as alt
import pandas as pd

n = 100
dom = ['losers, probably', 'basic', 'cool']
rng = ['red', 'black', 'green']
x = np.exp(np.linspace(1, 6, n) + np.random.normal(0, 0.3, size=n))
y = np.exp(np.linspace(1, 6, n) + np.random.normal(0, 0.3, size=n))
source = pd.DataFrame(np.vstack([x, y]).T, columns=['x', 'y'])
source['who'] = ''
source.loc[int(n-n/5), 'who'] = 'me'
source['coolness'] = 'basic'
source.loc[:int(n/4), 'coolness'] = 'losers, probably'
source.loc[n-int(n/5):, 'coolness'] = 'cool'
chart = alt.Chart(source).mark_circle(size=40).encode(
    x=alt.X('x', scale=alt.Scale(type='log'), axis=alt.Axis(title='How much Fortnite you play')),
    y=alt.Y('y', scale=alt.Scale(type='log'), axis=alt.Axis(title='How Cool My Friends Think\nYou Are [Apparent Magnitude]')),
    color=alt.Color('coolness', scale=alt.
                    Scale(domain=dom, range=rng))
).properties(
    title='Objective Predictor of Coolness, should be used to determine all future friends.'
)

point = alt.Chart(source[int(n-n/5):int(n-n/5) + 1]).mark_point(size=100).encode(
    x=alt.X('x', axis=alt.Axis(title='How much Fortnite you play')),
    y=alt.Y('y', axis=alt.Axis(title='How Cool My Friends Think\nYou Are [Apparent Magnitude]')),
    color=alt.Color('coolness', legend=alt.Legend(title="Coolness"), scale=alt.Scale(scheme='set1'))
)
text = (
    alt.Chart(source.loc[int(n-n/5):int(n-n/5)+1])
        .mark_text(dy=-15, color="black")
        .encode(x=alt.X("x"), y=alt.Y("y"), text=alt.Text("who"))
    )

(chart + point + text).save("objective.json")
