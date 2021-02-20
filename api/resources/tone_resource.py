from flask_restful import Resource, reqparse

class ToneResource(Resource):
    def get(self):
         parser = reqparse.RequestParser()

         import code; code.interact(local=dict(globals(), **locals()))
