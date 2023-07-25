from flask_restful import Resource

class HealthCheckGetController(Resource):
    def get(self):
        return {'backend': 'ok', 'number': 1}