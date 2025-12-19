class Bond:
    def __init__(self, name, level, bond_buff):
        self.name = name
        self.level = level
        self.bond_buff = bond_buff
    
    def active(self):
        return self.bond_buff[self.level - 1]
    
    def get_modifier(self, stat, base):
        active = self.active()
        addition = 0
        
        if "Basic%" in active:
            addition += base * active["Basic%"]
        if stat + "%" in active:
            addition += base * active[stat + "%"]
        if stat in active:
            addition += active[stat]
        return addition