import os
import json
import importlib

class Routes:
    PATH_TO_JSON = "apps/backend/config/routes/"
    __resources = []

    def __init__(self, api, db):
        self.__api = api
        self.__db  = db
        self.__getResourcesFromJsonFile()

    def __getResourcesFromJsonFile(self):
        json_files = [json_file for json_file in os.listdir(self.PATH_TO_JSON) if json_file.endswith('.json')]

        for json_name_file in json_files:
            with open(os.path.join(self.PATH_TO_JSON, json_name_file)) as json_file:
                self.__resources += json.load(json_file)

    def initializeRoutes(self):
        for resource in self.__resources:
            controller = self.__importClassFromString(resource['module'], resource["controller"])

            if resource['dependency']:
                application = self.__importClassFromString(
                    resource['application']['module'], 
                    resource['application']['class']
                )
                repository = self.__importClassFromString(
                    resource['repository']['module'], 
                    resource['repository']['class']
                )

                self.__api.add_resource(
                    controller, 
                    resource['route'], 
                    resource_class_kwargs={resource['kwargs']: application(repository(self.__db.session))}
                )
            else:
                self.__api.add_resource(controller, resource['route'])

    def __importClassFromString(self, module: str, className: str):
        resourceModule = importlib.import_module(module)
        resourceClass  = getattr(resourceModule, className)

        return resourceClass
