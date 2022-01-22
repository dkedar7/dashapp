import os

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import flask
from flask import request

import base64
from .Components import set_layout_skeleton, TextInput
from .Callbacks import process_inputs
from .utils import get_input_names_from_callback_fn, assign_ids_to_inputs, make_input_groups

from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.YETI,
"https://use.fontawesome.com/releases/v5.9.0/css/all.css"]


class App(object):

    def __init__(self, 
                callback_fn=None, 
                inputs=None, 
                output=None, 
                title=None, 
                title_image_path=None, 
                subheader=None, 
                github_url=None,
                linkedin_url=None,
                twitter_url=None):

        self.callback_fn = callback_fn
        self.inputs = inputs
        self.output = output

        if output is None:
            self.output = TextInput()

        self.output.id = 'output-component'

        self.title = title
        self.title_image_path = title_image_path
        self.subtext = subheader
        self.github_url = github_url
        self.linkedin_url = linkedin_url
        self.twitter_url = twitter_url

        self.inputs_with_ids = assign_ids_to_inputs(self.inputs, self.callback_fn)
        self.kwargs = get_input_names_from_callback_fn

        server = flask.Flask(__name__)

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
        

    def run(self):
        self.app.server.run(port=8080)#int(os.environ.get('PORT', 8889)))


    def set_layout(self):

        if self.inputs is not None:
            input_groups = make_input_groups(self.inputs_with_ids)

        self.app.layout = set_layout_skeleton(inputs=input_groups, 
                                            outputs=self.output,
                                            title=self.title,
                                            title_image_path=self.title_image_path, 
                                            subtext=self.subtext, 
                                            github_url=self.github_url, 
                                            linkedin_url=self.linkedin_url, 
                                            twitter_url=self.twitter_url)


    def register_callback_fn(self):
        @self.app.callback(
            Output(component_id=self.output.id, component_property=self.output.attributable_property),
            [Input(component_id=input_.id, component_property=input_.attributable_property) for input_ in self.inputs_with_ids])
        def process_input(*args):
            return self.callback_fn(*args)