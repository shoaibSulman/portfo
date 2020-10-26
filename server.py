from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
# print(__name__)


@app.route('/')
def render():
    return render_template('index.html')


@app.route('/<string:page_id>')
def page(page_id):
    return render_template(page_id)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']

        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database2.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

        ########################
        # @app.route('/')
        # def homePage():
        #     return render_template('index.html')

        # @app.route('/index.html')
        # def index():
        #     return render_template('index.html')

        # @app.route('/works.html')
        # def works():
        #     return render_template('works.html')

        # @app.route('/about.html')
        # def about():
        #     return render_template('about.html')

        # @app.route('/contact.html')
        # def contact():
        #     return render_template('contact.html')

        ####################################

        # @app.route('/blog')
        # def blog():
        #     return render_template('index2.html')

        # @app.route('/<username>/<int:post_id>')
        # def name(username=None, post_id=None):
        #     return render_template('index.html', name=username, post_id=post_id)
