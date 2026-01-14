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
        
        self.add_stats = {
            Stat.QUICK: self._stat_addition(Stat.QUICK),
            Stat.POWER: self._stat_addition(Stat.POWER),
            Stat.SET: self._stat_addition(Stat.SET),
            Stat.SERVE: self._stat_addition(Stat.SERVE),
            
            Stat.RECEIVE: self._stat_addition(Stat.RECEIVE),
            Stat.BLOCK: self._stat_addition(Stat.BLOCK),
            Stat.SAVE: self._stat_addition(Stat.SAVE),
            
            Stat.AWARENESS: self._stat_addition(Stat.AWARENESS),
            Stat.STRENGTH: self._stat_addition(Stat.STRENGTH),
            Stat.ATTACKTECHNIQUE: self._stat_addition(Stat.ATTACKTECHNIQUE),
            
            Stat.REFLEX: self._stat_addition(Stat.REFLEX),
            Stat.SPIRIT: self._stat_addition(Stat.SPIRIT),
            Stat.DEFENSETECHNIQUE: self._stat_addition(Stat.DEFENSETECHNIQUE),
        }

    def stat_base(self, stat):
        return self.base_stats[stat]

    def rating(self):
        if self.base_stats[Stat.QUICK] > self.base_stats[Stat.POWER]:
            use_stat = Stat.QUICK
        else:
            use_stat = Stat.POWER
        rating_order =[use_stat, Stat.SET, Stat.SERVE, Stat.RECEIVE, Stat.BLOCK, Stat.SAVE]
        return sum(self.base_stats[stat] + self.add_stats[stat] for stat in rating_order)
    
    def basic_total(self):
        return sum(self.base_stats.values())

    
    
    def _stat_addition(self, stat):
        base = self.base_stats[stat]
        addition = 0

        addition += self.training.get_modifier(stat, base)

        for skill in self.skills:
            if stat != "Serve":
                addition += skill.get_modifier(stat, base)
        
        addition += self.skillres.get_modifier(stat, base)
            
        for bond in self.bonds:
            addition += bond.get_modifier(stat, base)
                
        return addition
    
    def update_stat_addition(self, stat):
        self.add_stats[stat] = self._stat_addition(stat)
        
    def stat_total(self, stat):
        base = self.base_stats[stat]
        added = self.add_stats[stat]
        return base + added



    def __repr__(self):
        return f"Object {self.name}..."
    
    def __str__(self):
        return f"""{self.name} - Player Rating:\t{self.rating()}
\033[4mBasic Attack Stats\033[0m
Quick Attack:\t{self.base_stats[Stat.QUICK]} + {round(self.add_stats[Stat.QUICK], 1)}\t{round(self.stat_total(Stat.QUICK))}
Power Attack:\t{self.base_stats[Stat.POWER]} + {round(self.add_stats[Stat.POWER], 1)}\t{round(self.stat_total(Stat.POWER))}
Set:\t\t{self.base_stats[Stat.SET]} + {round(self.add_stats[Stat.SET], 1)}\t{round(self.stat_total(Stat.SET))}
Serve:\t\t{self.base_stats[Stat.SERVE]} + {round(self.add_stats[Stat.SERVE], 1)}\t{round(self.stat_total(Stat.SERVE))}
                    
\033[4mBasic Defense Stats\033[0m
Receive:\t{self.base_stats[Stat.RECEIVE]} + {round(self.add_stats[Stat.RECEIVE], 1)}\t{round(self.stat_total(Stat.RECEIVE))}
Block:\t\t{self.base_stats[Stat.BLOCK]} + {round(self.add_stats[Stat.BLOCK], 1)}\t{round(self.stat_total(Stat.BLOCK))}
Save:\t\t{self.base_stats[Stat.SAVE]} + {round(self.add_stats[Stat.SAVE], 1)}\t{round(self.stat_total(Stat.SAVE))}"""