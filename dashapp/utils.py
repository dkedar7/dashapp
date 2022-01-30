"""
Utility functions
"""
import inspect
from dash import html
import dash_bootstrap_components as dbc


# Input component utils
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

    button_row = html.Div(
        [
            dbc.Button("Clear", outline=True, color="primary",
                       className="me-1", id='reset_inputs', n_clicks=0)
        ]
    )

    output_groups.append(button_row)

    return output_groups
