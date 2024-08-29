# myapp/repositories.py

from abc import ABC, abstractmethod
from .models import Weapon

class IWeaponRepository(ABC):
    @abstractmethod
    def get_weapon(self, weapon_id: int) -> Weapon:
        pass

    @abstractmethod
    def save_weapon(self, weapon: Weapon) -> None:
        pass

class WeaponRepository(IWeaponRepository):
    def get_weapon(self, weapon_id: int) -> Weapon:
        return Weapon.objects.get(id=weapon_id)

    def save_weapon(self, weapon: Weapon) -> None:
        weapon.save()