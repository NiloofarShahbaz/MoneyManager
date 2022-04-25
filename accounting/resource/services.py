from decimal import Decimal

from accounting.resource.models import Resource


class ResourceService:
    def __init__(self):
        self.resource = None

    def create(self, name: str, amount: Decimal, type_: str):
        self.resource = Resource(name, amount, type_)




