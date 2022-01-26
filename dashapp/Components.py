import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import base64

theme_color_code = "#ffffff"  # Indigo

## Define default input elements
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'contents'


class SliderInput(dcc.Slider):
    """
    Extends dbc.Input
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'value'


## Define default output elements
class TextOutput(dbc.Input):
    """
    Extends dbc.Input
    """
    def __init__(self, label_=None, **kwargs):
        super().__init__(**kwargs)
        self.attributable_property = 'value'
        self.label_ = label_