# class GameRole:
#     _vitality: int
#     _attack: int
#     _defense: int
    
#     def set_vitality(self,val):
#         self._vitality = val

#     def get_vitality(self):
#         return self._vitality
    
#     def set_attack(self,val):
#         self._attack = val
    
#     def get_attack(self):
#         return self._attack

#     def set_defense(self,val):
#         self._defense = val
    
#     def get_defense(self):
#         return self._defense
    
#     def state_display(self):
#         print("腳色當前狀態")
#         print(f"體力:{self._vitality}")
#         print(f"攻擊:{self._attack}")
#         print(f"防禦:{self._defense}")  

#     def get_init_state(self):
#         self._vitality = 100
#         self._attack = 100
#         self._defense = 100
    
#     def fight(self):
#         self._vitality = 0
#         self._attack = 0
#         self._defense = 0

# if __name__ == "__main__":
#     role = GameRole()
#     role.get_init_state()
#     role.state_display()
#     backup = GameRole()
#     backup.set_vitality(role.get_vitality())
#     backup.set_attack(role.get_attack())
#     backup.set_defense(role.get_defense())
#     #大戰後
#     role.fight()
#     role.state_display()
#     #恢復數據
#     role.set_vitality(backup.get_vitality())
#     role.set_attack(backup.get_attack())
#     role.set_defense(backup.get_defense())
#     role.state_display()
#     #以上程式碼暴露太多細節

#---------------------- 更改後 ----------------------#
class GameRoleMemo:

    def __init__(self, vit, att, defense) -> None:
        self.vit = vit
        self.att = att
        self.defense = defense

    def set_vitality(self,val):
        self.vit = val

    def get_vitality(self):
        return self.vit
    
    def set_attack(self,val):
        self.att = val
    
    def get_attack(self):
        return self.att

    def set_defense(self,val):
        self.defense = val
    
    def get_defense(self):
        return self.defense

class RoleStateCareTaker:
    memo : GameRoleMemo

    def get_memento(self):
        return self.memo

    def set_memento(self, val: GameRoleMemo):
        self.memo = val

class GameRole:
        
    _vitality: int
    _attack: int
    _defense: int

    def save_state(self):
        return GameRoleMemo(self._vitality,self._attack,self._defense)    

    def restore_state(self, val: GameRoleMemo):
        self._vitality = val.get_vitality()
        self._attack = val.get_attack()
        self._defense = val.get_defense()

    def state_display(self):
        print("腳色當前狀態")
        print(f"體力:{self._vitality}")
        print(f"攻擊:{self._attack}")
        print(f"防禦:{self._defense}")  

    def set_init_state(self):
        self._vitality = 100
        self._attack = 100
        self._defense = 100
    
    def fight(self):
        self._vitality = 0
        self._attack = 0
        self._defense = 0
    
if __name__ == "__main__":
    game = GameRole()        
    game.set_init_state()
    game.state_display()
    
    care_taker = RoleStateCareTaker()
    care_taker.set_memento(game.save_state())
    game.fight()
    game.state_display()
    game.restore_state(care_taker.get_memento())
    game.state_display()


