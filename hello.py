from flask import Flask, request, send_from_directory, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<page>')
def hello(page=None):
	return render_template('index.html', page=page, css_path=url_for('static', filename="cover.css"))

if __name__ == "__main__":
    app.run(debug=True)
