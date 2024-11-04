from flask import Flask, send_from_directory

"""
Przed uruchomieniem zainstaluj pakiet flask
"""


app = Flask(__name__)

@app.route('/')
def main():
    return send_from_directory('htmldocs', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
