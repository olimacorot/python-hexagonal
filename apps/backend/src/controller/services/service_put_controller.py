from flask import Response, request
from http import HTTPStatus
from flask_restful import Resource
from hexagonal.src.services.application.create.service_creator import ServiceCreator
from hexagonal.src.services.application.create.service_creator_request import ServiceCreatorRequest

class ServicePutController(Resource):
    def __init__(self, creator: ServiceCreator):
        self.__creator = creator

    def put(self, id):
        self.__creator.run(
            ServiceCreatorRequest(
                id,
                request.get_json()['code'],
                request.get_json()['name']
            )
        );

        return Response("", status=HTTPStatus.CREATED)