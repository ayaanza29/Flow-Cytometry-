#import subprocess
#subprocess.call ("/usr/bin/Rscript --vanilla C:/Users/Zuhayr/Documents/GitHub/Flow-Cytometry-/functions.r", shell = True)

"""
import rpy2 #.robjects as robjects

"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\R\R x64 4.1.1.lnk"
"C:\Program Files\R\R-4.1.1/bin/x64"
"""


from flask import Flask, flash, request, redirect, url_for, render_template
import datetime
import os
import subprocess
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "C:/Users/rkhan/Desktop/Z Research Programming"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'fcs'}

app = Flask(__name__, static_url_path='/static')
app.config["Upload_Folder"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template('index.html')