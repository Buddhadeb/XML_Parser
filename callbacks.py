from dash.dependencies import Input, Output, State
from dash import html, no_update, dcc

import pandas as pd
from utils import parse_contents
import dash_bootstrap_components as dbc


def register_callbacks(app):
    @app.callback(
        Output("output-data-upload", "children"),
        Output("download-button-container", "children"),
        Input("upload-data", "contents"),
        State("upload-data", "filename"),
        State("process-dropdown", "value"),
    )
    def update_output(list_of_contents, list_of_names, process):
        if list_of_contents is not None:
            all_data = []
            for contents, filename in zip(list_of_contents, list_of_names):
                data = parse_contents(contents, filename, process)
                all_data.append(data)

            if all_data:
                df = pd.DataFrame(all_data)
                # Ensure all column names are strings
                df.columns = df.columns.astype(str)
                download_button = dbc.Button(
                    "Download data as CSV",
                    id={"type": "btn_csv", "index": 0},
                    color="success",
                )
                return (
                    html.Div(
                        [
                            html.H5("Extracted Data:"),
                            dbc.Table.from_dataframe(
                                df,
                                striped=True,
                                bordered=True,
                                hover=True,
                                responsive=True,
                            ),
                        ]
                    ),
                    download_button,
                )

        return html.Div("No files uploaded"), None

    @app.callback(Output("upload-data", "contents"), Input("clear-all", "n_clicks"))
    def clear_all(n_clicks):
        if n_clicks > 0:
            return None

    @app.callback(
        Output("download-dataframe-csv", "data"),
        Input({"type": "btn_csv", "index": 0}, "n_clicks"),
        State("upload-data", "contents"),
        State("upload-data", "filename"),
        State("process-dropdown", "value"),
    )
    def download_csv(n_clicks, list_of_contents, list_of_names, process):
        if n_clicks:
            all_data = []
            for contents, filename in zip(list_of_contents, list_of_names):
                data = parse_contents(contents, filename, process)
                all_data.append(data)

            if all_data:
                df = pd.DataFrame(all_data)
                # Ensure all column names are strings
                df.columns = df.columns.astype(str)
                return dcc.send_data_frame(
                    df.to_csv, "output.csv", quoting=2, index=False
                )

        return no_update
