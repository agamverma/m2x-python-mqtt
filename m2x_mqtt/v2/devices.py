from m2x_mqtt.v2.resource import Resource
from m2x_mqtt.v2.streams import Stream


class Device(Resource):
    COLLECTION_PATH = 'devices'
    ITEM_PATH = 'devices/{id}'
    ITEMS_KEY = 'devices'

    def stream(self, name):
        return Stream(self.api, self, name=name)

    def create_stream(self, name, **params):
        return Stream.create(self.api, self, name, **params)

    def post_updates(self, **values):
        return self.api.post(self.subpath('/updates'), data=values)

    def update_location(self, **params):
        return self.api.put(self.subpath('/location'), data=params)
