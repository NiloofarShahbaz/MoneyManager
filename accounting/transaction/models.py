from tortoise import fields, models
from enum import Enum


class _TransactionType(Enum):
    INCOME = 'in'
    EXPENSE = 'ex'


class Collection(models.Model):
    TYPES = _TransactionType

    name = fields.TextField()
    type = fields.CharEnumField(TYPES, max_length=2)


class Transaction(models.Model):
    TYPES = _TransactionType

    amount = fields.DecimalField(max_digits=40, decimal_places=2)
    collection = fields.ForeignKeyField("transaction.Collection", on_delete=fields.SET_NULL)
    note = fields.TextField()
    resource = fields.ForeignKeyField('resource.Resource', on_delete=fields.SET_NULL)
