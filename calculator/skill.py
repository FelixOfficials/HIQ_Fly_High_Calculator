from .stat import Stat

class Skill:
    def __init__(self, name, level, cooldown, skill_numbers, affected_stat):
        self.name = name
        self.level = level
        self.max_level = len(skill_numbers)
        self.cooldown = cooldown
        self.skill_numbers = skill_numbers
        self.affected_stat = self._stat_conversion(affected_stat)
        self.tag = self.skill_type()
    
    def _stat_conversion(self, affected_stat):
        for stat in Stat:
            if stat.value == affected_stat:
                return stat
    
    def skill_type(self):
        return "Active" if self.cooldown > 1 else "Passive"
    
    def addition_percentage(self):
        if self.level <= self.max_level:
            skill_bonus = self.skill_numbers[self.level - 1]
            
            if self.cooldown != 1:
                cooldown_calc = self.cooldown / 2
                return 1/cooldown_calc * (skill_bonus)
            else:
                return (skill_bonus)
    
    def get_modifier(self, stat, base):
        if self.affected_stat != stat:
            return 0
        return base * self.addition_percentage()
    
    # Fix this part