# gif和plotly的结合

import random
import plotly.graph_objects as go
import pandas as pd
import gif

df = pd.DataFrame({
    't': list(range(10)) * 10,
    'x': [random.randint(0, 100) for _ in range(100)],
    'y': [random.randint(0, 100) for _ in range(100)]
})

@gif.frame
def plot(i):
    d = df[df['t'] == i]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=d["x"],
        y=d["y"],
        mode="markers"
    ))
    fig.update_layout(width=500, height=300)
    return fig

frames = []
for i in range(10):
    frame = plot(i)
    frames.append(frame)

gif.save(frames, 'gif-plotly.gif', duration=100)