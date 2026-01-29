from dataclasses import dataclass


class TabName:
    LOANS = "Loans"
    OWNED = "Trucks"
    STORE = "Store"
    BANK = "Bank"
    ORDERS = "Orders"


class TruckCategory:
    LOCAL = "Local"
    LORRY = "Lorry"
    OFFORAD = "Offroad"


class BankName:
    PRIVAT = "Privat Bank"
    RAIFFEISEN = "Raiffeisen Bank"
    CREDIT_AGRICOLE = "Crédit Agricole"
    UNIVERSAL = "Universal Bank"
    UKR_GAS_BANK = "Ukrgasbank"


@dataclass
class ITruck:
    name: str
    category: TruckCategory
    price: int
    picture: str


@dataclass
class ILoan:
    amount: int
    duration: int
    bank: BankName


@dataclass
class IOrder:
    price: int
    location: str
    coordinates: tuple[float, float]
