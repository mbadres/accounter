from models.account_type import AccountType
from models.business_area import BusinessArea
from models.cost_center import CostCenter


class Account:

    def __init__(
        self,
        number: str,
        type: AccountType,
        description: str,
        estimated_annual_amount: float,
        cost_center: CostCenter,
        business_area: BusinessArea,
    ) -> None:
        self.number = number
        self.type = type
        self.description = description
        self.estimated_annual_amount = estimated_annual_amount
        self.cost_center = cost_center
        self.business_area = business_area
