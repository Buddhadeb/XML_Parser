import dash
from dash import html
import dash_bootstrap_components as dbc
from layout import create_layout
import callbacks
from waitress import serve

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.title = "XML_Parser"
app.layout = create_layout()


# Register callbacks
callbacks.register_callbacks(app)

if __name__ == "__main__":
    serve(app.server, port=8000)
