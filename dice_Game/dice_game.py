from iconservice import *
from .custom import RandomGenerateClass

TAG = 'DiceGame'

class DiceGame(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def diceRoll(self, name: str) -> int:
        return RandomGenerateClass(name, self.block.timestamp).random_generate()