from decimal import Decimal

from accounting.transaction.models import Transaction, Collection


class CollectionService:
    collection = None

    def __init__(self):
        self.collection = None

    def create(self, name: str, type_: str):
        self.collection = Collection(name, type_)

    def get(self, name):
        return self.collection

class ResourceService:
    def __init__(self):
        self.collection_service = CollectionService()
        self.transaction = None

    def create(self, amount: Decimal, collection_name: str, type_: str, note: str, resource: str):
        CollectionService().create(collection_name, type_)

        self.resource = Transaction(amount, collection, note, resource)




