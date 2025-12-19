class Training:
    def __init__(self, name, level, training_type, training_numbers):
        self.name = name
        self.level = level
        self.training_type = training_type
        self.training_numbers = training_numbers
    
    def active(self):
        active_dict = {}
        
        for i in range(self.level):
            if self.training_type[i] in active_dict:
                active_dict[self.training_type[i]] += self.training_numbers[i]
            else:
                active_dict[self.training_type[i]] = self.training_numbers[i]
        
        return active_dict
        
    def get_modifier(self, stat, base):
        active = self.active()
        addition = 0
        
        if stat + "%" in active:
            addition += base * active[stat + "%"]
        if stat in active:
            addition += active[stat]
        return addition