from .stat import Stat
from .training import Training
from .skill import Skill
from .skill_resonance import SkillRes


class Player:
    def __init__(self, name, archetype, bsc_quick, bsc_power, bsc_set, bsc_serve, bsc_receive, bsc_block, bsc_save, bsc_awareness, bsc_strength, bsc_atk_tech, bsc_reflex, bsc_spirit, bsc_def_tech, training, skills, skillres, bonds):
        self.name = name
        self.archetype = archetype
        self.training = training
        self.skills = skills
        self.skillres = skillres
        self.skillres_unlocked = skillres.skillres_unlocked
        self.bonds = bonds
        
        self.base_stats = {
            Stat.QUICK: bsc_quick,
            Stat.POWER: bsc_power,
            Stat.SET: bsc_set,
            Stat.SERVE: bsc_serve,
            
            Stat.RECEIVE: bsc_receive,
            Stat.BLOCK: bsc_block,
            Stat.SAVE: bsc_save,

            Stat.AWARENESS: bsc_awareness,
            Stat.STRENGTH: bsc_strength,
            Stat.ATTACKTECHNIQUE: bsc_atk_tech,
            
            Stat.REFLEX: bsc_reflex,
            Stat.SPIRIT: bsc_spirit,
            Stat.DEFENSETECHNIQUE: bsc_def_tech,
        }
        
        self.bond_bonus = {
            stat: 0.0 for stat in Stat
        }
        
        self.training_bonus = {
            stat: 0.0 for stat in Stat
        }        
        
        self.passive_skill_bonus = {
            stat: 0.0 for stat in Stat
        }
        
        self.active_skill_bonus = {
            stat: 0.0 for stat in Stat
        }
        
        self.skillres_bonus = {
            stat: 0.0 for stat in Stat
        }

        self.potential_bonus = {
            stat: 0.0 for stat in Stat
        }
        
        self.memory_bonus = {
            stat: 0.0 for stat in Stat
        }    
        
        self.use_stat = Stat.QUICK if self.base_stats[Stat.QUICK] > self.base_stats[Stat.POWER] else Stat.POWER
        self._initial_run = False

    def stat_base(self, stat):
        return self.base_stats[stat]
    
    def passive_calc(self):
        for skill in self.skills:
            if skill.tag == "Passive":
                cur_stat = skill.affected_stat
                self.passive_skill_bonus[cur_stat] = skill.get_modifier(cur_stat, self.base_stats[cur_stat])
                
    def active_calc(self):
        for skill in self.skills:
            if skill.tag == "Active":
                cur_stat = skill.affected_stat
                self.active_skill_bonus[cur_stat] = skill.get_modifier(cur_stat, self.base_stats[cur_stat] + self.passive_skill_bonus[cur_stat])
                print(self.active_skill_bonus[cur_stat])
                
    def bond_calc(self):
        for bond in self.bonds:
            cur_active = bond.active()
            cur_stat = list(cur_active.keys())[0]
            self.bond_bonus[cur_stat] = bond.get_bonus(self.base_stats[cur_stat], cur_active)
            

    def rating(self):
        self.calculate()      
        total_rating = 0
        rating_order = [self.use_stat, Stat.SET, Stat.SERVE, Stat.RECEIVE, Stat.BLOCK, Stat.SAVE]
        for order in rating_order:
            total_rating += self.base_stats[order] + self.passive_skill_bonus[order] + self.active_skill_bonus[order]
        return total_rating
    
    def calculate(self):
        if self._initial_run == False:
            self.bond_calc()
            self.passive_calc()
            self.active_calc()
            self._initial_run = True
    
    def basic_total(self):
        return sum(self.base_stats.values())

    def _stat_addition(self, stat):
        base = self.base_stats[stat]
        addition = 0

        addition += self.training.get_modifier(stat, base)

        for skill in self.skills:
            addition += skill.get_modifier(stat, base)
        
        addition += self.skillres.get_modifier(stat, base)
            
        for bond in self.bonds:
            addition += bond.get_modifier(stat, base)
                
        return addition
    
    def update_stat_addition(self, stat):
        self.add_stats[stat] = self._stat_addition(stat)
        
    def stat_display(self, stat):
        base = self.base_stats[stat]
        passive = self.passive_skill_bonus[stat]
        return base + passive



    def __repr__(self):
        return f"Object {self.name}..."
    
    def __str__(self):
        return f"""{self.name} - Player Rating:\t{self.rating()}
\033[4mBasic Attack Stats\033[0m
Quick Attack:\t{self.base_stats[Stat.QUICK]} + {round(self.passive_skill_bonus[Stat.QUICK], 1)}\t{round(self.stat_display(Stat.QUICK))}
Power Attack:\t{self.base_stats[Stat.POWER]} + {round(self.passive_skill_bonus[Stat.POWER], 1)}\t{round(self.stat_display(Stat.POWER))}
Set:\t\t{self.base_stats[Stat.SET]} + {round(self.passive_skill_bonus[Stat.SET], 1)}\t{round(self.stat_display(Stat.SET))}
Serve:\t\t{self.base_stats[Stat.SERVE]} + {round(self.passive_skill_bonus[Stat.SERVE], 1)}\t{round(self.stat_display(Stat.SERVE))}
                    
\033[4mBasic Defense Stats\033[0m
Receive:\t{self.base_stats[Stat.RECEIVE]} + {round(self.passive_skill_bonus[Stat.RECEIVE], 1)}\t{round(self.stat_display(Stat.RECEIVE))}
Block:\t\t{self.base_stats[Stat.BLOCK]} + {round(self.passive_skill_bonus[Stat.BLOCK], 1)}\t{round(self.stat_display(Stat.BLOCK))}
Save:\t\t{self.base_stats[Stat.SAVE]} + {round(self.passive_skill_bonus[Stat.SAVE], 1)}\t{round(self.stat_display(Stat.SAVE))}"""