from flask import abort
from flask_restful import Resource
from hexagonal.src.services.domain.service_id import ServiceId
from hexagonal.src.services.domain.service_not_exist import ServiceNotExist
from hexagonal.src.services.application.find.service_finder import ServiceFinder

class ServiceGetController(Resource):
    def __init__(self, finder: ServiceFinder):
        self.__finder = finder

    def get(self, id):
        
        try:
            response = self.__finder.run(ServiceId(id));

            return {
                "id": response.id(),
                "code": response.code(),
                "name": response.name(),
            }
        except ServiceNotExist as err:
            abort(400, err.message)
