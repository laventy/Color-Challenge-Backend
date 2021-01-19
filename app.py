import json

from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS

from src.generator import ColorGenerator
from src.config import COLOR_SPACE_DEF

app = Flask(__name__)
CORS(app)

api = Api(app, version='1.0', title='Color Space API',
          description='A simple random-color-space code generator API',
          )

ns = api.namespace('api/v1/colors', description='colors operations')


@ns.route("/")
class Colors(Resource):
    '''Shows a list of colors'''
    @ns.doc('list_colors')
    def get(self):
        return ColorGenerator(COLOR_SPACE_DEF).generate(color_num=5)


if __name__ == '__main__':
    app.run(debug=True)
