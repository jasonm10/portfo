from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/resources/seo.html')
def resources():
    return render_template('/resources/seo.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        category = data['category']
        message = data['message']
        file = database.write(f'\n{email}, {name}, {category}, {message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thank-you.html')
    else:
        return 'something went wrong'
