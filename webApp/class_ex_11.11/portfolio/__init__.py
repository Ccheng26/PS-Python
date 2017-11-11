from flask import Flask, render_template, request
# CREATES APP AND ASSIGNS NAME
app= Flask('portfolio')
# FROM CURRENT DIRECTORY IMPORT VIEWS
from . import views
# STORE INFO IN VIEWS