from enum import Enum


class RecordType(Enum):
    """Type of the accounting record"""

    DEBIT = "Soll"
    CREDIT = "Haben"
