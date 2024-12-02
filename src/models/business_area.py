from enum import Enum


class BusinessArea(Enum):
    """Business area of an account"""

    CHARITABLE_ACTIVITIES = "Ideeller Bereich"
    ASSET_MANAGEMENT = "Vermögensverwaltung"
    PURPOSE_RELATED_BUSINESS = "Zweckbetrieb"
    COMMERCIAL_OPERATIONS = "Wirtschaftlicher Geschäftsbetrieb"
