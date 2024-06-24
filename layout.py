import dash_bootstrap_components as dbc
from dash import dcc, html


def create_layout():
    return dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    html.H1("XML File Extractor"),
                    width={"size": 6, "offset": 3},
                    className="text-center mt-5",
                )
            ),
            dbc.Row(
                dbc.Col(
                    html.P("Upload your XML files below to extract and process data:"),
                    width={"size": 6, "offset": 3},
                    className="text-center",
                )
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Dropdown(
                        id="process-dropdown",
                        options=[
                            {"label": "Stage 1", "value": "Stage 1"},
                            {"label": "Stage 2", "value": "Stage 2"},
                        ],
                        value="Stage 1",
                    ),
                    width={"size": 6, "offset": 3},
                ),
                className="mt-3",
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Upload(
                        id="upload-data",
                        children=html.Div(
                            ["Drag and Drop or ", html.A("Select Files")]
                        ),
                        style={
                            "width": "100%",
                            "height": "60px",
                            "lineHeight": "60px",
                            "borderWidth": "1px",
                            "borderStyle": "dashed",
                            "borderRadius": "5px",
                            "textAlign": "center",
                            "margin": "10px",
                        },
                        multiple=True,
                    ),
                    width={"size": 6, "offset": 3},
                ),
                className="mt-3",
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(id="output-data-upload"),
                    width={"size": 8, "offset": 2},
                    className="mt-3",
                )
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Button("Clear All", id="clear-all", n_clicks=0, color="danger"),
                    width={"size": 2, "offset": 5},
                    className="text-center mt-3",
                )
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(id="download-button-container"),
                    width={"size": 2, "offset": 5},
                    className="text-center mt-3",
                )
            ),
            dcc.Download(id="download-dataframe-csv"),
        ],
        fluid=True,
    )
