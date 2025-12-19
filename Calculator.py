class Player:
    def __init__(self, name, archetype, bsc_quick, bsc_power, bsc_set, bsc_serve, bsc_receive, bsc_block, bsc_save, bsc_awareness, bsc_strength, bsc_atk_tech, bsc_reflex, bsc_spirit, bsc_def_tech, training, skills, skillres, bonds):
        self.name = name
        self.archetype = archetype
        
        self.bsc_quick = bsc_quick
        self.bsc_power = bsc_power
        self.bsc_set = bsc_set
        self.bsc_serve = bsc_serve
        
        self.bsc_receive = bsc_receive
        self.bsc_block = bsc_block
        self.bsc_save = bsc_save
        
        self.bsc_awareness = bsc_awareness
        self.bsc_strength = bsc_strength
        self.bsc_atk_tech = bsc_atk_tech
        
        self.bsc_reflex = bsc_reflex
        self.bsc_spirit = bsc_spirit
        self.bsc_def_tech = bsc_def_tech
        
        self.training = training.active()
        self.skills = skills
        self.skillres = skillres.active()
        self.skillres_unlocked = skillres.skillres_unlocked
        self.bonds = bonds
        
        #Could do 1 check by making a loop here and passing bond as argument
        self.add_quick = self._quick_addition()
        self.add_power = self._power_addition()
        self.add_set = self._set_addition()
        self.add_serve = self._serve_addition()
        
        self.add_receive = self._receive_addition()
        self.add_block = self._block_addition()
        self.add_save = self._save_addition()
        


    def rating(self):
        return self.quick_total() + self.power_total() + self.set_total() + self.serve_total() + self.receive_total() + self.block_total() + self.save_total()
    
    
    
    def basic_total(self):
        return self.bsc_quick + self.bsc_power + self.bsc_set + self.bsc_serve + self.bsc_receive + self.bsc_block + self.bsc_save

    def basic_atk(self):
        return self.bsc_quick + self.bsc_power + self.bsc_set + self.bsc_serve

    def basic_def(self):
        return self.bsc_receive + self.bsc_block + self.bsc_save
    
    
    
    def _quick_addition(self):
        addition = 0
        
        for skill in self.skills:
            if skill.affected_stat == "Quick":
                addition += self.bsc_quick * skill.addition_percentage()
        
        for bond in self.bonds:
            if "Quick Attack" in bond:
                addition += bond["Quick Attack"]
            if "Quick Attack%" in bond:
                addition += self.bsc_quick * bond["Quick Attack%"]
            if "Basic%" in bond:
                addition += self.bsc_quick * bond["Basic%"]
    
        if "Basic%" in self.skillres:
            addition += self.bsc_quick * self.skillres["Basic%"]        
        if "Quick Attack" in self.training:
            addition += self.training["Quick Attack"]
        if "Quick Attack%" in self.training:
            addition += self.bsc_quick * self.training["Quick Attack%"]
        return addition
    
    def update_quick_addition(self):
        self.add_quick = self._quick_addition()
        
    def quick_total(self):
        return self.bsc_quick + self.add_quick



    def _power_addition(self):
        addition = 0
        
        for skill in self.skills:
            if skill.affected_stat == "Power":
                addition += self.bsc_power * skill.addition_percentage()
                
        for bond in self.bonds:
            if "Power Attack" in bond:
                addition += bond["Power Attack"]
            if "Power Attack%" in bond:
                addition += self.bsc_power * bond["Power Attack%"]
            if "Basic%" in bond:
                addition += self.bsc_power * bond["Basic%"]
        
        if "Basic%" in self.skillres:
            addition += self.bsc_power * self.skillres["Basic%"]        
        if "Power Attack" in self.training:
            addition += self.training["Power Attack"]
        if "Power Attack%" in self.training:
            addition += self.bsc_power * self.training["Power Attack%"]
        return addition
    
    def update_power_addition(self):    
        self.add_power = self._power_addition()
        
    def power_total(self):
        return self.bsc_power + self.add_power



    def _set_addition(self):
        addition = 0
        
        for skill in self.skills:
            if skill.affected_stat == "Set":
                addition += self.bsc_set * skill.addition_percentage()
        
        for bond in self.bonds:
            if "Set" in bond:
                addition += bond["Set"]
            if "Set%" in bond:
                addition += self.bsc_set * bond["Set%"]
            if "Basic%" in bond:
                addition += self.bsc_set * bond["Basic%"]
        
        if "Basic%" in self.skillres:
            addition += self.bsc_set * self.skillres["Basic%"]
        if "Set" in self.training:
            addition += self.training["Set"]
        if "Set%" in self.training:
            addition += self.bsc_set * self.training["Set%"]
        return addition
    
    def update_set_addition(self):  
        self.add_set = self._set_addition()
        
    def set_total(self):
        return self.bsc_set + self.add_set


  
    def _serve_addition(self):
        addition = 0
        
        for bond in self.bonds:
            if "Serve" in bond:
                addition += bond["Serve"]
            if "Serve%" in bond:
                addition += self.bsc_serve * bond["Serve%"]
            if "Basic%" in bond:
                addition += self.bsc_serve * bond["Basic%"]

        if "Basic%" in self.skillres:
            addition += self.bsc_serve * self.skillres["Basic%"]        
        if "Serve" in self.training:
            addition += self.training["Serve"]
        if "Serve%" in self.training:
            addition += self.bsc_serve * self.training["Serve%"]
        return addition
    
    def update_serve_addition(self):  
        self.add_serve = self._serve_addition()
        
    def serve_total(self):
        return self.bsc_serve + self.add_serve

  
  
    def _receive_addition(self):
        addition = 0
        
        for skill in self.skills:
            if skill.affected_stat == "Receive":
                addition += self.bsc_receive * skill.addition_percentage()
        
        for bond in self.bonds:
            if "Receive" in bond:
                addition += bond["Receive"]
            if "Receive%" in bond:
                addition += self.bsc_receive * bond["Receive%"]
            if "Basic%" in bond:
                addition += self.bsc_receive * bond["Basic%"]

        if "Basic%" in self.skillres:
            addition += self.bsc_receive * self.skillres["Basic%"]        
        if "Receive" in self.training:
            addition += self.training["Receive"]
        if "Receive%" in self.training:
            addition += self.bsc_receive * self.training["Receive%"]
        return addition
    
    def update_receive_addition(self):  
        self.add_receive = self._receive_addition()
    def receive_total(self):
        return self.bsc_receive + self.add_receive

  
  
    def _block_addition(self):
        addition = 0
        
        for skill in self.skills:
            if skill.affected_stat == "Block":
                addition += self.bsc_block * skill.addition_percentage()
        
        for bond in self.bonds:
            if "Block" in bond:
                addition += bond["Block"]
            if "Block%" in bond:
                addition += self.bsc_block * bond["Block%"]
            if "Basic%" in bond:
                addition += self.bsc_block * bond["Basic%"]

        if "Basic%" in self.skillres:
            addition += self.bsc_block * self.skillres["Basic%"]        
        if "Block" in self.training:
            addition += self.training["Block"]
        if "Block%" in self.training:
            addition += self.bsc_block * self.training["Block%"]
        return addition
    
    def update_block_addition(self):  
        self.add_block = self._block_addition()
    def block_total(self):
        return self.bsc_block + self.add_block


  
    def _save_addition(self):
        addition = 0
        
        for skill in self.skills:
            if skill.affected_stat == "Save":
                addition += self.bsc_save * skill.addition_percentage()
        
        for bond in self.bonds:
            if "Save" in bond:
                addition += bond["Save"]
            if "Save%" in bond:
                addition += self.bsc_save * bond["Save%"]
            if "Basic%" in bond:
                addition += self.bsc_save * bond["Basic%"]
        
        if "Basic%" in self.skillres:
            addition += self.bsc_save * self.skillres["Basic%"]        
        if "Save" in self.training:
            addition += self.training["Save"]
        if "Save%" in self.training:
            addition += self.bsc_save * self.training["Save%"]
        return addition
    
    def update_save_addition(self):  
        self.add_save = self._save_addition()
        
    def save_total(self):
        return self.bsc_save + self.add_save


    
    def __repr__(self):
        return f"Object {self.name}..."
    
    def __str__(self):
        return f"""{self.name} - Player Rating:\t{self.rating()}
\033[4mBasic Attack Stats\033[0m
Quick Attack:\t{self.bsc_quick} + {round(self.add_quick, 1)}\t{round(self.quick_total())}
Power Attack:\t{self.bsc_power} + {round(self.add_power, 1)}\t{round(self.power_total())}
Set:\t\t{self.bsc_set} + {round(self.add_set, 1)}\t{round(self.set_total())}
Serve:\t\t{self.bsc_serve} + {round(self.add_serve, 1)}\t{round(self.serve_total())}
                    
\033[4mBasic Defense Stats\033[0m
Receive:\t{self.bsc_receive} + {round(self.add_receive, 1)}\t{round(self.receive_total())}
Block:\t\t{self.bsc_block} + {round(self.add_block, 1)}\t{round(self.block_total())}
Save:\t\t{self.bsc_save} + {round(self.add_save, 1)}\t{round(self.save_total())}"""



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
                return (self.skill_numbers[self.level] - 1) / (self.cooldown / 2)
            else:
                return (self.skill_numbers[self.level] - 1)
        
    
        
      
      
        
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



class Bond:
    def __init__(self, name, level, bond_buff):
        self.name = name
        self.level = level
        self.bond_buff = bond_buff
    
    def active(self):
        return self.bond_buff[self.level - 1]



class Potential:
    def __init__(self, name):
        self.name  



class Memory:
    def __init__(self, name, bsc_serve, power, bsc_set, bsc_receive, bsc_block, bsc_save):
        self.name = name
        self.bsc_serve = bsc_serve
        self.power = power
        self.bsc_set = bsc_set
        self.bsc_receive = bsc_receive
        self.bsc_block = bsc_block
        self.bsc_save = bsc_save

# playerList = [oikawa, ushi, korai, nishi, tendo, tana, tsuki, iwai, kage, kono, kuro, kenji, koga, komi, daichi, kyo]

# ushi = Player("Ushijima Wakatoshi", ["bsc_serve", "Power Attack"], 236 + 760, 1707 + 2309, 1368 + 863, 1626 + 2202, 1537 + 1742, 1459 + 1693, 1367 + 1322, 0.05 + 0.15, 0 + 0.16, 0 + 0.036, 0, 0, 0 + 0.012)
# ushi_player_rating = 21360
# print(ushi.rating())

oikawa_training = Training("Oikawa Toru", 7, ["Power Attack", "Serve", "Set%", "Block", "Set", "Serve%", "Court Commander"], [250, 250, 0.065, 250, 250, 0.065, 0.1])
oikawa_skillres = SkillRes("Oikawa Toru", 4, 4, ["Basic%", "Serve%", "Basic%", "Placeholder%", "Basic%"], [0.13, 0.18, 0.13, 0.15, 0.13])

bond1 = Bond("Long-standing Rivals", 5, [{"Set": 5, "Set%": 0.01}, {"Set": 7, "Set%": 0.02}, {"Set": 9, "Set%": 0.03}, {"Set": 12, "Set%": 0.04}, {"Set": 15, "Set%": 0.05}])
bond2 = Bond("Power of Trust", 3, [{"Block": 5, "Block%": 0.01}, {"Block": 7, "Block%": 0.02}, {"Block": 9, "Block%": 0.03}, {"Block": 12, "Block%": 0.04}, {"Block": 15, "Block%": 0.05}])
bond3 = Bond("Perfect Chemistry", 4, [{"Placeholder": 5, "Placeholder%": 0.01}, {"Placeholder": 7, "Placeholder%": 0.02}, {"Placeholder": 9, "Placeholder%": 0.03}, {"Placeholder": 12, "Placeholder%": 0.04}, {"Placeholder": 15, "Placeholder%": 0.05}])
bond4 = Bond("A Bit Higher!", 3, [{"Set": 5, "Set%": 0.01}, {"Set": 7, "Set%": 0.02}, {"Set": 9, "Set%": 0.03}, {"Set": 12, "Set%": 0.04}, {"Set": 15, "Set%": 0.05}])

skill1 = Skill("Great King's Set", 1, 6, [1.2, 1.35, 1.5], "Set")
skill2 = Skill("Great King's Dump", 1, 6, [1.15, 1.350, 1.45], "Set")
skill3 = Skill("Court Commander", 1, 1, [0.1, 0.14, 0.18], "Placeholder")
skill4 = Skill("Great King's Jump Serve", 1, 8, [2.6, 2.75, 2.9, 3.05, 3.2], "Serve")

oikawa_skills = [skill1, skill2, skill3, skill4]
oikawa_bonds = [bond1.active(), bond2.active(), bond3.active(), bond4.active()]
oikawa = Player("Oikawa Toru", ["Power Attack", "Serve", "Setter"], 212, 1533, 1627, 1705, 1378, 1530, 1290, 0.05, 0, 0, 0, 0, 0, oikawa_training, oikawa_skills, oikawa_skillres, oikawa_bonds)
oikawa_player_rating = 20927
# print(oikawa.rating())

starting_team_rating = 20890 + 19007 + 13241 + 13971 + 21367 + 18790 + 21360
team_rating = 137089 # Starting Players Rating + Deployment Bond + School Bond + Cheer

print(oikawa)
# print(12249 + (12249 * 0.0038))

raimu_training = Training("Raimu", 0, [], [])
raimu_skillres = SkillRes("Raimu", 4, 5, ["Basic%", "Basic%", "Basic%"], [0.02, 0.02, 0.02])
raimu_bonds = []
raimu_skills = []
raimu = Player("Raimu", ["Receive"], 56, 82, 66, 70, 78, 74, 66, 0.05, 0, 0, 0, 0, 0, raimu_training, raimu_skills, raimu_skillres, raimu_bonds)

# print(raimu)

mori_training = Training("mori", 0, [], [])
mori_skillres = SkillRes("mori", 4, 5, ["Basic%", "Basic%", "Basic%"], [0.02, 0.02, 0.02])
mori_bonds = []
mori_skills = []
mori = Player("mori", ["Receive"], 58, 183, 161, 166, 166, 195, 148, 0, 0, 0, 0.05, 0, 0, mori_training, mori_skills, mori_skillres, mori_bonds)

# print(mori)

kosuke_training = Training("Kosuke Tashiro", 0, [], [])
kosuke_skillres = SkillRes("Kosuke Tashiro", 4, 5, ["Basic%", "Basic%", "Basic%"], [0.02, 0.02, 0.02])
kosuke_bonds = []
kosuke_skills = []
kosuke = Player("Kosuke Tashiro", ["Block"], 78, 54, 68, 72, 70, 82, 66, 0, 0, 0, 0.05, 0, 0, kosuke_training, kosuke_skills, kosuke_skillres, kosuke_bonds)

# print(kosuke)

# print("Oikawa Stats:")
# print("Real Rating:\t\t", oikawa_player_rating)
# print("Calculated Rating:\t", oikawa.rating())
# print("Calculated Difference:\t", oikawa_player_rating - oikawa.rating())
# print("Base to Real Difference:", oikawa_player_rating - oikawa.basic_total())
# print("Calc Multiplier:\t", ((oikawa_player_rating - oikawa.rating()) / oikawa.rating()) * 100)
# print("Base Multiplier:\t", ((oikawa_player_rating - oikawa.basic_total()) / oikawa.basic_total()) * 100)


# print("\nUshijima Stats:")
# print("Real Rating:\t\t", ushi_player_rating)
# print("Calculated Rating:\t", ushi.rating())
# print("Calculated Difference:\t", ushi_player_rating - ushi.rating())
# print("Base to Real Difference:", ushi_player_rating - ushi.basic_total())
# print("Calc Multiplier:\t", ((ushi_player_rating - ushi.rating()) / ushi.rating()) * 100)
# print("Base Multiplier:\t", ((ushi_player_rating - ushi.basic_total()) / ushi.basic_total()) * 100)