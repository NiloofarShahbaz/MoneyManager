from enum import Enum

from tortoise import fields, models


class _ResourceType(Enum):
    BANK = 'bank'
    CASH = 'cash'


class Resource(models.Model):
    TYPES = _ResourceType

    name = fields.CharField(max_length=225, unique=True)
    amount = fields.DecimalField(max_digits=40, decimal_places=2)
    type = fields.CharEnumField(TYPES, max_length=4)
