""" 
fil'my, zaly, miscja
"""


class Konstanty:
    import os

    POTOCHNA_TEKA: str = os.path.dirname(os.path.abspath(__file__))


class Menju:
    def __init__(self):
        print("Slava ISUSU HRYSTU!")


class User:
    jmennja: str
    parol: str

    def __init__(self, jmennja: str, parol: str):
        self.jmennja = jmennja
        self.parol = parol


test_user = User("test", "test")
print(test_user.jmennja)
