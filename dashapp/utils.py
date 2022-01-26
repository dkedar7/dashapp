"""
Utility functions
"""
import inspect
from dash import html
import dash_bootstrap_components as dbc


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

# Input utils


def get_input_names_from_callback_fn(callback_fn):
    """
    Returns the names of function arguments as a list of strings
    """
    signature = inspect.signature(callback_fn)
    parameters = signature.parameters
    parameter_list = list(parameters)

    return parameter_list


def assign_ids_to_inputs(inputs, callback_fn):
    """
    Modify the 'id' property of inputs.
    """
    if not isinstance(inputs, list):
        inputs = [inputs]

    inputs_with_ids = []

    for input_, parameter_name in zip(inputs, get_input_names_from_callback_fn(callback_fn)):
        input_.id = parameter_name
        inputs_with_ids.append(input_)

    return inputs_with_ids


def make_input_groups(inputs_with_ids):

    input_groups = []

    input_groups.append(html.H2('Input'))

    for input_ in inputs_with_ids:
        input_groups.append(
            dbc.Col(
                [
                    dbc.Label(input_.id.replace(
                        '_', ' ').upper(), align='end'),
                    input_
                ],
                align='center'
            )
        )

    button_row = html.Div(
        [
            dbc.Button("Reset", outline=True, color="primary",
                       className="me-1", id='reset_inputs', n_clicks=0),
            dbc.Button("Submit", color="warning", className="me-1",
                       id='submit_inputs', n_clicks=0)
        ]
    )

    input_groups.append(button_row)

    return input_groups


# Output utils
def assign_ids_to_outputs(outputs):
    """
    Modify the 'id' property of inputs.
    """
    if not isinstance(outputs, list):
        outputs = [outputs]

    outputs_with_ids = []

    for idx, output_ in enumerate(outputs):
        output_.id = f'output-{idx + 1}'
        outputs_with_ids.append(output_)

    return outputs_with_ids


def make_output_groups(outputs):

    output_groups = []
    n_outputs = len(outputs)

    output_groups.append(html.H2('Output'))

    for idx, output_ in enumerate(outputs):
        label = f'Output {idx + 1}' if output_.label_ is None else output_.label_
        label = label.replace('_', ' ').upper()
        output_groups.append(
            dbc.Col(
                [
                    dbc.Label(label, align='end'),
                    output_
                ],
                align='center'
            )
        )

    return output_groups