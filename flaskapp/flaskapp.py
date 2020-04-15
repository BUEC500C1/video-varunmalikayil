from flask import Flask, request, send_file
from flask_restful import Resource, Api


app = Flask(__name__)
@app.route('/download')
def download():
    return send_file('test.avi')

if __name__ == '__main__':
  app.run()