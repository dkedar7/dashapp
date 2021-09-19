import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import base64

theme_color_code = "#ffffff" #Indigo


def set_layout_skeleton(title_image_path, subtext, github_url, final_text):

    image_filename = title_image_path # replace with your own image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8") if image_filename else ''
    
    # 1. Navbar placeholder (currently black row)
    navbar = dbc.Row()

    # 2. Mosaic icon image
    icon_image = dbc.Row(
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image),
                        style={'width':'250px'}),
                        justify='center'
    )


    ### 3. Body title
    subtext = '' if not subtext else subtext
    body_paragraph = dbc.Row(
        [
            dbc.Col(
                    [
                        html.Br(),
                        html.H5(subtext,
                            style={'text-align':'center', "color":"darkgray", "font-family": "Verdana; Gill Sans"})
                    ],
                    style ={"padding":"1% 1% 3% 0%", "background-color":theme_color_code}
                )
        ],
        style = {'text-align':'center', "padding":"1% 1% 1% 0%", "background-color":theme_color_code}
    )

    ### 4. Github logo
    github_url = '_blank' if not github_url else github_url
    github_logo = dbc.Row(
                html.A(
                    html.I(className = "fa-2x fab fa-github", style={'color':'#000000'}),
                    href = github_url, target="_blank",
                    className="mr-3"
            ),
            justify='center'
    )

    ### 5. Upload button
    upload_button = dbc.Col(
        [
            dcc.Upload(id='upload-image',
                    children = dbc.Col(
                        [
                            'Click to upload an image'
                        ]
                    ),
                    style={
                        'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                    }
                ),
            ]
    )


    ### 7. Display original and processed images
    images = dbc.Row(
        [
            dbc.Col(dbc.CardImg(id='original-image'), style = {"padding" : "2% 1% 1% 2%", 
                                                                'lineHeight': '60px',
                                                                'borderWidth': '1px',
                                                                'borderStyle': 'dashed',
                                                                'borderRadius': '5px',
                                                                'margin': '10px'}),
            dbc.Col(html.P(id='processed-text'), style = {"padding" : "2% 1% 1% 2%", 
                                                            'lineHeight': '60px',
                                                            'borderWidth': '1px',
                                                            'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'margin': '10px'}
                        )
        ]
    )

    ### 8. Footer
    final_text = '' if not final_text else final_text
    footer = dbc.Row(
        dbc.Col(
            html.Div(
            [
                final_text,
                html.A("GitHub repository", 
                        href = github_url,
                        target = "_blank"),
                ' to learn more.'
            ],
        ),
        width={"size": 10}
    ), 
        justify='center',
        align='center',
        style={'margin-bottom': "10%"}
    )

    ### Bring it together
    top = dbc.Container(
        [
            dcc.Store(id='memory-output', storage_type='memory'),
            navbar,
            icon_image,
            body_paragraph,
            github_logo
        ],
        fluid = False
    )

    middle = dbc.Container(
        [
            upload_button,
            images
        ],
        fluid = False
    )

    bottom = dbc.Container(
        [   
            footer
        ],
        fluid = False
    )

    layout = dbc.Container(
        [
            top, 
            middle,
            bottom
        ]
    )

    return layout