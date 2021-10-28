import numpy as np
import altair as alt
import pandas as pd

alt.themes.enable("latimes")
bad = np.hstack(
    [
        ["losers, probably"] * 10,
        "dweebs",
        "fools",
        "goobers",
        "goofballs",
        "dorks",
        "nerds",
        "bumpkins",
    ]
)
good = np.hstack(
    [["cool"] * 10, "l33t", "awesome", "deserves a raise", "chill", "spiffy"]
)


def make_plot(n=100, err=0.3):
    x = np.exp(np.linspace(1, 6, n) + np.random.normal(0, err, size=n))
    y = np.exp(np.linspace(1, 6, n) + np.random.normal(0, err, size=n))
    source = pd.DataFrame(np.vstack([x, y]).T, columns=["x", "y"])
    source["who"] = ""
    source.loc[int(n - n / 5) + 1, "who"] = "me"
    source["coolness"] = "basic"
    source.loc[: int(n / 4), "coolness"] = np.random.choice(bad)
    source.loc[n - int(n / 5) :, "coolness"] = np.random.choice(good)

    dom = [source.loc[0, "coolness"], "basic", source.loc[n - 1, "coolness"]]
    rng = ["red", "black", "green"]

    chart = (
        alt.Chart(source)
        .mark_circle(size=40)
        .encode(
            x=alt.X(
                "x",
                scale=alt.Scale(type="log"),
                axis=alt.Axis(title="How much Fortnite you play"),
            ),
            y=alt.Y(
                "y",
                scale=alt.Scale(type="log"),
                axis=alt.Axis(
                    title="How Cool My Friends Think\nYou Are [Apparent Magnitude]"
                ),
            ),
            color=alt.Color("coolness", scale=alt.Scale(domain=dom, range=rng)),
        )
        .properties(
            title="Objective Predictor of Coolness, should be used to determine all future friends."
        )
    )

    point = (
        alt.Chart(source[int(n - n / 5) + 1 : int(n - n / 5) + 1 + 1])
        .mark_point(size=100)
        .encode(
            x=alt.X("x", axis=alt.Axis(title="How much Fortnite you play")),
            y=alt.Y(
                "y",
                axis=alt.Axis(
                    title="How Cool My Friends Think\nYou Are [Apparent Magnitude]"
                ),
            ),
            color=alt.Color(
                "coolness",
                legend=alt.Legend(title="Coolness"),
                scale=alt.Scale(scheme="set1"),
            ),
        )
    )
    text = (
        alt.Chart(source.loc[int(n - n / 5) + 1 : int(n - n / 5) + 1 + 1])
        .mark_text(dy=-15, color="black")
        .encode(x=alt.X("x"), y=alt.Y("y"), text=alt.Text("who"))
    )

    return (chart + point + text).interactive()


plot = make_plot(int(np.random.normal(100, 50)), err=np.random.uniform(0.3, 0.8))
plot.save("objective.json")
plot.interactive()
