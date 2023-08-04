# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_information.ipynb.

# %% auto 0
__all__ = ['labeledInput', 'createInputObjects', 'createCenturiesSlider', 'createUploadObjects', 'createInformationInfo',
           'createSaveNContinue', 'createInformationLayout']

# %% ../nbs/03_information.ipynb 5
from dash import dcc, html
import dash_bootstrap_components as dbc

# %% ../nbs/03_information.ipynb 7
def labeledInput(label, identity = None):
    lab = dbc.Label(children=label)
    inp = dbc.Input(placeholder=label, id=identity)

    return html.Div([lab, inp])

# %% ../nbs/03_information.ipynb 10
def createInputObjects():
    inputObjects = []
    metadata = ["Work", "Author", "Language", "Country", "City", "Institution"]

    for data in metadata:
        inputObjects.append(labeledInput(label = data, identity = data.lower()))

    return inputObjects

# %% ../nbs/03_information.ipynb 13
def createCenturiesSlider():
    centuries = [
        None,
        "1st",
        "2nd",
        "3rd",
    ] + [f"{i}th" for i in range(4, 21)]

    centuriesSlider = dcc.RangeSlider(
        min=1,
        max=20,
        step=1,
        value=[1, 20],
        id="centuries-slider",
        marks=None,
        tooltip={"placement": "bottom", "always_visible": True}
    )

    return centuries, html.Div([html.Label(children="Centuries"),centuriesSlider])

# %% ../nbs/03_information.ipynb 16
def createUploadObjects():
    uploadImages = dcc.Upload(
        children=dbc.Button("Upload Images"),
        multiple=True,
        id="upload-images",
    )

    uploadManuscripts = dcc.Upload(
        children=dbc.Button("Upload Transcripts"),
        multiple=True,
        id="upload-manuscripts",
    )

    return uploadImages, uploadManuscripts

# %% ../nbs/03_information.ipynb 19
def createInformationInfo():
    return dbc.Card(
        dbc.CardBody(
            [
                html.H1("Information"),
                html.P(
                    "This menu allows you to to modify information about current manuscripts as well as allowing you to upload images and transcripts for a new manuscript. "
                    "Once you have made your changes and uploaded the relevant files, click the Save and Continue button to save these changes and move to the next tab."
                )
            ]
        )
    )

# %% ../nbs/03_information.ipynb 22
def createSaveNContinue():
    return dbc.Button("Save and Continue", color="primary", id="save-and-continue")

# %% ../nbs/03_information.ipynb 24
def createInformationLayout():
    inputObjects = createInputObjects()
    centuries, centuriesSlider = createCenturiesSlider()
    uploaders = createUploadObjects()

    layout = html.Div(
        [
            createInformationInfo(),
            html.Br(),  # This is a temporary measure to make it more readable, true for following Br calls
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            inputObjects[0],
                            inputObjects[1],
                            inputObjects[2],
                            inputObjects[3],
                            inputObjects[4],
                            inputObjects[5],
                            centuriesSlider,
                            html.Br(),
                            html.Div(
                                dbc.ButtonGroup(
                                    [
                                        uploaders[0],  # uploadImages
                                        uploaders[1],  # uploadManuscripts
                                    ],
                                ),
                                id="uploader-container",
                            ),
                        ]
                    ),
                    createSaveNContinue(),
                ],
            ),
        ]
    )

    return centuries, layout
