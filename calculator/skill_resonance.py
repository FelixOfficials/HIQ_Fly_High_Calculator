class SkillRes:
    def __init__(self, name, level, skillres_first_threshold, skillres_type, skillres_numbers):
        self.name = name
        self.level = level
        self.skillres_type = skillres_type
        self.skillres_unlocked = (level - skillres_first_threshold)//2 + 1
        self.skillres_numbers = skillres_numbers
        
    def active(self):
        active_dict = {}
        
        for i in range(self.skillres_unlocked):
            if self.skillres_type[i] in active_dict:
                active_dict[self.skillres_type[i]] += self.skillres_numbers[i]
            else:
                active_dict[self.skillres_type[i]] = self.skillres_numbers[i]
        
        return active_dict
    
    def get_modifier(self, stat, base):
        active = self.active()
        addition = 0
        
        if "Basic%" in active:
            addition += base * active["Basic%"]
        if stat + "%" in active:
            addition += base * active[stat + "%"]
        return addition