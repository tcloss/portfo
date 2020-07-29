from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/' )
def index():
	return render_template('index.html')

@app.route('/<string:page_name>.html' )
def content(page_name=None):
	return render_template(f'{page_name}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
		except: 
			return "did not save to database"
	return redirect('thankyou.html')


def write_to_file(data):
	with open('data.txt', mode='a') as file:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file.write(f'{email}\t{subject}\t{message}\n')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as csvfile:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])
