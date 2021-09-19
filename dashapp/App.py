import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask
from flask import request

import base64
from Components import set_layout_skeleton
import callbacks

from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.BOOTSTRAP,
"https://use.fontawesome.com/releases/v5.9.0/css/all.css"]


class App(object):

    def __init__(self, title, title_image_path, subtext, github_url, final_text, default_image_path):

        self.title_image_path = title_image_path
        self.subtext = subtext
        self.github_url = github_url
        self.final_text = final_text
        self.default_image_path = default_image_path

        server = flask.Flask(__name__)

        self.app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                        server=server,
                        meta_tags=[{'name': 'viewport',
                                    'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.8, minimum-scale=0.5,'}]
                        )
        cache = Cache(self.app.server)
        self.app.title = title
        

    def run(self):
        self.app.server.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


    def set_layout(self):
        self.app.layout = set_layout_skeleton(self.title_image_path, self.subtext, self.github_url, self.final_text)


    def define_callbacks(self):
        @self.app.callback(
            Output('original-image', 'src'),
            [Input('upload-image', 'contents')])
        def update_original_image(contents):
            if contents:
                return contents
            else:
                image_filename = self.default_image_path # replace with your own image
                encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8")
                default_image = 'data:image/png;base64,{}'.format(encoded_image)
                return default_image

        @self.app.callback(
            Output('processed-image', 'src'),
            [Input('original-image', 'src'),
            Input('passage_dropdown', 'value')]
        )
        def update_processed_image(contents, model):
            if contents:
                content_type, content_string = contents.split(',')
                processed_image_string = callbacks.stylize_image(content_string, model).decode("utf-8")
                processed_image_string = 'data:image/png;base64,{}'.format(processed_image_string)
                return processed_image_string

            else:
                image_filename = 'assets/processed_defaultimage.png' # replace with your own image
                encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8")
                default_image = 'data:image/png;base64,{}'.format(encoded_image)
                return default_image
