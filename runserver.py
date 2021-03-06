import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
import copy
import base64
import random
import uuid
import requests
import mimetypes
from api_test import call_api_test
app = Flask(__name__)


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set([ 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
jinja_options = app.jinja_options.copy()

jinja_options.update(dict(
	variable_start_string='%%',
	variable_end_string='%%',
))
app.jinja_options = jinja_options

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_hash():
	return str(uuid.uuid4())

def classify( imgName ):
	if int_to_word_out[np.argmax(prediction)] =="handicap":
		return True
	else:
		return False

@app.route('/')
def root():
	return render_template('project-index.html')
	# url=request.form.get('url') ;


@app.route('/classifyUpload', methods=['GET', 'POST'] )
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file :
			filename = secure_filename(file.filename)
			filename+=get_hash()+filename
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))	
			handicap = classify( filename )
			if( handicap ):
				keywordList = ["speaker", "interpreter", "teacher", "singer", "food tester", "Design Thinker"]
				#keywordList = [ handicap keywords ]
				pass
			else:
				#keywordList = [ normal keywords ]
				pass
			jobs = call_api_test( keywordList )
			return jsonify(jobs)
			# return redirect('/')
			# return jobs
	return '404'

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug=True)

