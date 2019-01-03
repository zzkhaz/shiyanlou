from flask import Flask, render_template
import os
import json

app = Flask(__name__)
path = '/home/shiyanlou/files/'

@app.route('/')
def index():
	text_list = []
	for file in os.listdir(path):  
		text_list.append(os.path.splitext(file)[0])
	return render_template("index.html", text_list = text_list)

@app.route('/files/<filename>')
def file(filename):
	file_path = path + filename + '.json'
	if os.path.exists(file_path):
		f = open(file_path, encoding = 'utf-8')
		text_json = json.load(f)
		return render_template("file.html", text_json = text_json)
	else:
		print('err')
		return render_template("404.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
	app.run()
