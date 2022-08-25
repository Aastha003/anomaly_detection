
from flask import Flask
import os
import sys
from config import cfg

folder = {}
folder['main'] = '/Users/caast/Downloads/RA_Anomaly_Detection/'
if folder['main'] == '':
    folder['main'] = os.getcwd()

sys.path.append(folder["main"])
#img_path = ''

cnf = cfg(folder["main"])
args = cnf.args

UPLOAD_FOLDER = args['video']

config_new = {}

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#import os
#import urllib.request
#from flask import Flask, flash, request, redirect, url_for, render_template
#from werkzeug.utils import secure_filename
#from config import cfg 
#from image_parser import img_parser
#import sys
#import subprocess

#app = Flask(__name__)


#from flask import Flask, render_template, request
#from werkzeug import secure_filename
#app = Flask(__name__)

#@app.route('/')
#def upload_file():
#   return render_template('videofile.html')

#@app.route('/', methods = ['GET', 'POST'])
#def process_file():
#    if request.method == 'POST':
#        f = request.files['file']
#        f.save(os.path.join(args['video'], filename))
#        #f.save(secure_filename(f.filename))
#        return 'file uploaded successfully'

#if __name__ == '__main__':
#   app.run()

#@app.route('/')
#def upload_form():
#    # rendering webpage
#    return render_template('videofile.html')

#@app.route('/', methods=['GET', 'POST'])
#def process_video():  
#    if 'file' not in request.files:
#        flash('No file part')
#        return redirect(request.url)
#    file = request.files['file']
#    if file.filename == '':
#        flash('No video selected for uploading')
#        return redirect(request.url)
#    else:
#        filename = file.filename
#        file.save(os.path.join(args['video'], filename))
        #print('upload_video filename: ' + filename)
#        flash('Video successfully uploaded')
#        process = subprocess.Popen(['python' , 'image_parser.py' ], stdout=subprocess.PIPE)
#        out, err = process.communicate()
#        print(out)
#        return render_template('videofile.html', filename=filename)

#@app.route('/display/<filename>')
#def display_video(filename):
#    #print('display_video filename: ' + filename)
#    tempname = os.path.splitext(filename)
#    output_file = tempname[0] + '_anomaly.avi'
#    video_path = args['video'] + output_file
#    return redirect(url_for('static', filename=video_path), code=301)

    
#if __name__ == '__main__':
    # defining server ip address and port
#    app.run()
