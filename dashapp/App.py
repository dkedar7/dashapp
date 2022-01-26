import os

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import flask
from flask import request

import base64
from .Components import TextInput
from .utils import (
    assign_ids_to_inputs, 
    make_input_groups, 
    make_output_groups, 
    set_layout_skeleton, 
    assign_ids_to_outputs
)

from dash.dependencies import Input, Output


class App(object):

    def __init__(self,
                 callback_fn=None,
                 inputs=None,
                 outputs=None,
                 title=None,
                 title_image_path=None,
                 subheader=None,
                 github_url=None,
                 linkedin_url=None,
                 twitter_url=None):

        self.callback_fn = callback_fn
        self.inputs = inputs
        self.outputs = outputs

        if outputs is None:
            self.outputs = [TextInput()]

        self.output_state = [None] * len(self.outputs)

        # self.output.id = 'output-component'

        self.title = title
        self.title_image_path = title_image_path
        self.subtext = subheader
        self.github_url = github_url
        self.linkedin_url = linkedin_url
        self.twitter_url = twitter_url

        self.inputs_with_ids = assign_ids_to_inputs(
            self.inputs, self.callback_fn)

        self.outputs_with_ids = assign_ids_to_outputs(
            self.outputs)

        server = flask.Flask(__name__)

        external_stylesheets = [dbc.themes.YETI,
                                "https://use.fontawesome.com/releases/v5.9.0/css/all.css"]
        self.app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                             server=server,
                             meta_tags=[{'name': 'viewport',
                                         'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.8, minimum-scale=0.5,'}]
                             )
        # cache = Cache(self.app.server)
        self.app.title = title

        # Intialize layout
        self.set_layout()

        # Register callbacks
        self.register_callback_fn()

        # Keep track of the number of clicks
        self.submit_clicks = 0
        self.reset_clicks = 0

    def run(self):
        self.app.server.run(port=8080)  # int(os.environ.get('PORT', 8889)))

    def set_layout(self):

        if self.inputs is not None:
            input_groups = make_input_groups(self.inputs_with_ids)

        if self.outputs is not None:
            output_groups = make_output_groups(self.outputs_with_ids)

        self.app.layout = set_layout_skeleton(inputs=input_groups,
                                              outputs=output_groups,
                                              title=self.title,
                                              title_image_path=self.title_image_path,
                                              subtext=self.subtext,
                                              github_url=self.github_url,
                                              linkedin_url=self.linkedin_url,
                                              twitter_url=self.twitter_url)

    def register_callback_fn(self):
        @self.app.callback(
            [Output(component_id=output_.id, component_property=output_.attributable_property) for output_ in self.outputs_with_ids],
            [Input(component_id=input_.id, component_property=input_.attributable_property) for input_ in self.inputs_with_ids] +
            [Input(component_id='reset_inputs', component_property='n_clicks'),
             Input(component_id='submit_inputs', component_property='n_clicks')])
        def process_input(*args):

            reset_button = args[-2]
            submit_button = args[-1]

            if submit_button > self.submit_clicks:
                self.submit_clicks = submit_button
                output_state = self.callback_fn(*args[:-2])
                if isinstance(output_state, tuple):
                    return output_state

                return [self.output_state]

            elif reset_button > self.reset_clicks:
                self.reset_clicks = reset_button
                self.output_state = [None]*len(self.outputs)
                return self.output_state

            else:
                return self.output_state