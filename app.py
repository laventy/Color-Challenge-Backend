import json

from flask import Flask
from flask_restx import Api, Resource

from generator import ColorGenerator

app = Flask(__name__)
api = Api(app, version='1.0', title='Color Space API',
          description='A simple random-color-space code generator API',
          )

ns = api.namespace('colors', description='colors operations')


@ns.route("/")
class Colors(Resource):
    '''Shows a list of colors'''
    @ns.doc('list_colors')
    def get(self):
        with open('color_spaces_def.json', 'r') as f:
            return ColorGenerator(json.load(f)).generate(color_num=3)


if __name__ == '__main__':
    app.run(debug=True)
