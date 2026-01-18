class Bond:
    def __init__(self, name, level, bond_buff):
        self.name = name
        self.level = level
        self.bond_buff = bond_buff
    
    def active(self):
        if self.level > 0:
            return self.bond_buff[self.level - 1]
        else:
            return {}
    
    def get_bonus(self, base, active):
        addition = 0
        
        for bonus in active.keys():
            if "%" in bonus:
                addition += base * active[bonus]
            else:
                addition += active[bonus]
        return addition