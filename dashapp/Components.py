from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

theme_color_code = "#ffffff"  # Indigo


class DefaultLayout():

    def __init__(self, inputs=None,
                 outputs=None,
                 title=None,
                 title_image_path=None,
                 subtext=None,
                 github_url=None,
                 linkedin_url=None,
                 twitter_url=None):

        self.inputs = inputs
        self.outputs = outputs
        self.title = title
        self.title_image_path = title_image_path
        self.subtext = subtext
        self.github_url = github_url
        self.linkedin_url = linkedin_url
        self.twitter_url = twitter_url

        # Bring all containers together
        self.navbar_container = self.generate_navbar_container()
        self.header_container = self.generate_header_container()
        self.io_container = self.generate_io_container()
        self.footer_container = self.generate_footer_container()

        self.layout = dbc.Container(
            [
                self.navbar_container,
                self.header_container,
                self.io_container,
                self.footer_container
            ],
            fluid=True
        )

    def generate_navbar_container(self):

        # 1. Navbar
        social_media_navigation = []
        if self.github_url is not None:
            social_media_navigation.append(dbc.NavItem(dbc.NavLink(
                html.I(className="fa-2x fab fa-github", style={'color': '#ffffff'}), href=self.github_url, target="_blank")))

        if self.linkedin_url is not None:
            social_media_navigation.append(dbc.NavItem(dbc.NavLink(html.I(
                className="fa-2x fab fa-linkedin", style={'color': '#ffffff'}), href=self.linkedin_url, target="_blank")))

        if self.twitter_url is not None:
            social_media_navigation.append(dbc.NavItem(dbc.NavLink(html.I(
                className="fa-2x fab fa-twitter-square", style={'color': '#ffffff'}), href=self.twitter_url, target="_blank")))

        navbar = dbc.NavbarSimple(
            children=[dbc.NavItem(dbc.NavLink("About", href="#"))
                      ] + social_media_navigation,
            brand=self.title,
            color="primary",
            dark=True,
            fluid=True,
            fixed='top'
        )

        navbar_container = dbc.Container(
            [
                navbar
            ],
            fluid=True
        )

        return navbar_container

    def generate_header_container(self):

        header_children = []

        if self.title is not None:
            header_children.append(
                dbc.Row(
                    html.H1(self.title, style={'textAlign': 'center'}),
                    style={"padding": "8% 0% 2% 0%"}
                )
            )

        if self.title_image_path is not None:
            header_children.append(
                dbc.Row(
                    dbc.Row(
                        html.Img(src=self.title_image_path,
                                 style={
                                     'width': '250px'
                                 }),
                        justify='center'
                    )
                )
            )

        if self.subtext is not None:
            header_children.append(
                dbc.Row(
                    dbc.Row(
                        html.H4(
                            html.I(self.subtext), style={'textAlign': 'center'}),
                        style={"padding": "2% 0% 2% 0%"}
                    )
                )
            )

        header_container = dbc.Container(
            header_children
        )

        return header_container

    def generate_io_container(self):

        input_output_components = dbc.Row(
            [
                dbc.Col(self.inputs,
                        style={"padding": "2% 1% 1% 2%",
                               'lineHeight': '60px',
                               'borderWidth': '1px',
                               'borderRadius': '5px',
                               "background-color": "#F2F2F2"},
                        width=5,
                        xs=12,
                        sm=12,
                        md=5,
                        lg=5,
                        xl=5,
                        xxl=5),
                dbc.Col(self.outputs,
                        id="output-group",
                        style={"padding": "2% 1% 1% 2%",
                               'lineHeight': '60px',
                               'borderWidth': '1px',
                               'borderRadius': '5px',
                               "background-color": "#F2F2F2"},
                        width=5,
                        xs=12,
                        sm=12,
                        md=5,
                        lg=5,
                        xl=5,
                        xxl=5)
            ],
            justify='evenly',
            style={"padding": "2% 1% 10% 2%"}
        )

        io_container = dbc.Container(
            [
                input_output_components
            ],
            fluid=True
        )

        return io_container

    def generate_footer_container(self):

        footer = dbc.NavbarSimple(
            brand='Made with Dash',
            color="primary",
            dark=True,
            fluid=True,
            fixed='bottom'
        )

        footer_container = dbc.Container(
            [
                footer
            ],
            fluid=True
        )

        return footer_container

    def refresh_layout(self):

        layout = dbc.Container(
            [
                self.navbar_container,
                self.header_container,
                self.io_container,
                self.footer_container
            ],
            fluid=True
        )

        self.layout = layout


######
# Define default input components
######

class TextInput(dbc.Input):
    """
    Extends dbc.Input
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'value'


class UploadInput(dcc.Upload):
    """
    Extends dcc.Upload
    """

    def __init__(self, label='Click to upload', **kwargs):
        super().__init__(children=dbc.Col(
            [label]),
            style={
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center'
        }, **kwargs)
        self.attributable_property = 'contents'


class SliderInput(dcc.Slider):
    """
    Extends dbc.Input
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'value'


######
# Define default output components
######

class TextOutput(dbc.Input):
    """
    Extends dbc.Input
    """

    def __init__(self, label_=None, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'value'
        self.placeholder = None
        self.label_ = label_


class ImageOutput(html.Img):
    """
    Extends dbc.CardImg
    """

    def __init__(self, label_=None, **kwargs):
        super().__init__(**kwargs, style={'max-width': '100%'})
        self.attributable_property = 'src'
        self.placeholder = None
        self.label_ = label_


class GraphOutput(dcc.Graph):
    """
    Extends dcc.Graph
    """

    def __init__(self, label_=None, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'figure'
        self.placeholder = go.Figure().\
            update_yaxes(visible=False, showticklabels=False).\
            update_xaxes(visible=False, showticklabels=False)

        self.label_ = label_
