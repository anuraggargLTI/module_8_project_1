from dash import dcc
from dash import html


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url("Columbia_Logo.png"),
                            className="logo",
                        ),
                        href="https://www.columbia.edu/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Columbia's Portfolio Analyzer")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/Columbia_Portfolio_Analyzer/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/Columbia_Portfolio_Analyzer/overview",
                className="tab first",
            ),
            dcc.Link(
                "Stock Performance",
                href="/Columbia_Portfolio_Analyzer/stockPerformance",
                className="tab",
            ),
            dcc.Link(
                "Portfolio & Management",
                href="/Columbia_Portfolio_Analyzer/portfolio-management",
                className="tab",
            )
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table