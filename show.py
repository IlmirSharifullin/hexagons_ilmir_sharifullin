import plotly.express as px

from consts import vfunc


def show(hex_data, hex_idxs):
    colors = vfunc(hex_data[:, 3])

    fig = px.scatter_3d(
        hex_data,
        x=hex_data[:, 0],
        y=hex_data[:, 1],
        z=hex_data[:, 2],
        hover_name=hex_idxs,
        color=colors,
        color_discrete_sequence=["#387C44", "gray", "#3EA99F", 'maroon'],
    )
    fig.show()

