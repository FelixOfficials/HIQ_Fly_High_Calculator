class Skill:
    def __init__(self, name, level, cooldown, skill_numbers, affected_stat):
        self.name = name
        self.level = level
        self.max_level = len(skill_numbers)
        self.cooldown = cooldown
        self.skill_numbers = skill_numbers
        self.affected_stat = affected_stat
    
    def addition_percentage(self):
        if self.level <= self.max_level:
            if self.cooldown > 1:
                return (self.skill_numbers[self.level - 1] - 1) / (self.cooldown / 2)
            else:
                return (self.skill_numbers[self.level - 1])
    
    def get_modifier(self, stat, base):
        if self.affected_stat != stat:
            return 0
        return base * self.addition_percentage()
    
    # Fix this part