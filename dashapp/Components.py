import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import base64

theme_color_code = "#ffffff"  # Indigo


class TextInput(dbc.Input):
    """
    Extends dbc.Input
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'value'


class Upload(dcc.Upload):
    """
    Extends dcc.Upload
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'contents'


class Slider(dcc.Slider):
    """
    Extends dbc.Input
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'value'


# class Text


def set_layout_skeleton(inputs=None, 
                        outputs=None, 
                        title=None, 
                        title_image_path=None, 
                        subtext=None, 
                        github_url=None, 
                        linkedin_url=None, 
                        twitter_url=None):


    # 1. Navbar placeholder
    social_media_navigation = []
    if github_url is not None:
        social_media_navigation.append(dbc.NavItem(dbc.NavLink(
            html.I(className="fa-2x fab fa-github", style={'color': '#ffffff'}), href=github_url, target="_blank")))

    if linkedin_url is not None:
        social_media_navigation.append(dbc.NavItem(dbc.NavLink(html.I(
            className="fa-2x fab fa-linkedin", style={'color': '#ffffff'}), href=linkedin_url, target="_blank")))

    if twitter_url is not None:
        social_media_navigation.append(dbc.NavItem(dbc.NavLink(html.I(
            className="fa-2x fab fa-twitter-square", style={'color': '#ffffff'}), href=twitter_url, target="_blank")))

    # 1. Navbar
    navbar = dbc.NavbarSimple(
        children=[dbc.NavItem(dbc.NavLink("About", href="#"))
                  ] + social_media_navigation,
        brand=title,
        color="primary",
        dark=True,
        fluid=True,
        fixed='top'
    )

    # 2. Top container
    top_container_children = []

    if title is not None:
        top_container_children.append(
            dbc.Row(
                html.H1(title, style={'textAlign': 'center'}),
                style={"padding": "8% 0% 2% 0%"}
            )
        )

    if title_image_path is not None:
        top_container_children.append(
            dbc.Row(
                dbc.Row(
                    html.Img(src=title_image_path,
                             style={
                                    'width': '250px'
                                    }),
                    justify='center'
                )
            )
        )

    if subtext is not None:
        top_container_children.append(
            dbc.Row(    
                dbc.Row(
                    html.H4(
                        html.I(subtext), style={'textAlign': 'center'}),
                        style={"padding": "2% 0% 2% 0%"}
                )
            )
        )

    # 3. Body title
    subtext = '' if not subtext else subtext
    body_paragraph = dbc.Row(
        [
            dbc.Col(
                [
                    html.Br(),
                    html.H5(subtext,
                            style={'text-align': 'center', "color": "darkgray", "font-family": "Verdana; Gill Sans"})
                ],
                style={"padding": "1% 1% 3% 0%",
                       "background-color": theme_color_code}
            )
        ],
        style={'text-align': 'center', "padding": "1% 1% 1% 0%",
               "background-color": theme_color_code}
    )


    # 5. Upload button
    upload_button = dbc.Row(
        dbc.Col(
            [
                dcc.Upload(id='upload-image',
                           children=dbc.Col(
                               [
                                   'Click to upload an image'
                               ]
                           ),
                           style={
                               'lineHeight': '60px',
                               'borderWidth': '1px',
                               'borderStyle': 'dashed',
                               'borderRadius': '5px',
                               'textAlign': 'center'
                           }
                           ),
            ],
            width=6,
            xs=12,
            sm=12,
            md=12,
            lg=10,
            xl=6,
            xxl=6
        ),
        justify="center"
    )

    # 7. Display original and processed images
    input_output_components = dbc.Row(
        [
            dbc.Col(inputs,
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
            dbc.Col(outputs,
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

    # 8. Footer
    footer = dbc.NavbarSimple(
        brand='Made with Dash',
        color="primary",
        dark=True,
        fluid=True,
        fixed='bottom'
    )

    # Bring it together
    navbar_container = dbc.Container(
        [
            navbar
        ],
        fluid=True
    )

    top = dbc.Container(
            top_container_children
    )

    middle = dbc.Container(
        [
            # upload_button,
            input_output_components
        ],
        fluid=True
    )

    bottom = dbc.Container(
        [
            footer
        ],
        fluid=True
    )

    layout = dbc.Container(
        [
            navbar_container,
            top,
            middle,
            bottom
        ],
        fluid=True
    )

    return layout
