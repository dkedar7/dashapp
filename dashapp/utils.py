"""
Utility functions
"""
import inspect
from dash import html
import dash_bootstrap_components as dbc

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
    Modify the id properties of inputs.
    """
    if not isinstance(inputs, list):
        inputs = [inputs]

    inputs_with_ids = []

    for input_, parameter_name in zip(inputs, get_input_names_from_callback_fn(callback_fn)):
        input_.id = parameter_name
        inputs_with_ids.append(input_)

    return inputs_with_ids


def make_input_groups(inputs_with_ids):

    # inputs_with_ids = assign_ids_to_inputs(inputs, callback_fn)
    input_groups = []

    input_groups.append(html.H2('Inputs'))

    for input_ in inputs_with_ids:
        input_groups.append(
            dbc.Col(
                [
                    dbc.Label(input_.id.replace('_', ' ').upper(), align='end'),
                    input_
                ],
                align='center'
            )
        )

    button_row = html.Div(
        [
            dbc.Button("Reset", outline=True, color="primary", className="me-1", id='reset_inputs'),
            dbc.Button("Submit", color="warning", className="me-1", id='submit_inputs')
        ]
    )

    input_groups.append(button_row)

    return input_groups