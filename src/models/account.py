from models.account_type import AccountType
from models.business_area import BusinessArea
from models.cost_center import CostCenter
from models.record import Record


class Account:

    def __init__(
        self,
        number: int,
        description: str,
        group_number: int,
        group_description: str,
        class_number: int,
        class_description: str,
        type: AccountType,
        cost_center: CostCenter,
        business_area: BusinessArea,
        estimated_annual_amount: float = 0,
    ) -> None:
        self.number = number
        self.description = description
        self.group_number = group_number
        self.group_description = group_description
        self.class_number = class_number
        self.class_description = class_description
        self.type = type
        self.estimated_annual_amount = estimated_annual_amount
        self.cost_center = cost_center
        self.business_area = business_area
        self.records: list[Record] = []
