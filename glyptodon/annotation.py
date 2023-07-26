# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_annotation.ipynb.

# %% auto 0
__all__ = ['createAnnotationTextArea', 'createPageSelector', 'createAnnotationFigure']

# %% ../nbs/04_annotation.ipynb 5
from dash import dcc, html
import plotly.express as px
import cv2

# %% ../nbs/04_annotation.ipynb 7
def createAnnotationTextArea():
    return dcc.Textarea(id="annotation",value="Enter transcription text here!",style={"width":"100%","height":285})

# %% ../nbs/04_annotation.ipynb 10
def createPageSelector():
    return dcc.Dropdown(id="page-selector")

# %% ../nbs/04_annotation.ipynb 13
def createAnnotationFigure(path):
    img = cv2.imread(path)
    # This reorders the color channels (the first two indices relate to the intensity values of individual colors while the last index indicates what
    img = img[:,:,::-1]
    fig = px.imshow(img)
    fig.update_layout(dragmode='drawrect',
                  # style of new shapes
                  newshape=dict(line_color='grey',
                                opacity=0.6))
    return fig
