class Player:
    def __init__(self, name, archetype, Qatk, Patk, Sett, Serve, Receive, Block, Save, Awr, Str, AtkTech, Reflex, Spirit, DefTech):
        self.name = name
        self.ratingg = (Qatk + Patk + Sett + Serve) * (1 + AtkTech) + (Receive + Block + Save) * (1 + DefTech)
        self.archetype = archetype
        self.Qatk = Qatk
        self.Patk = Patk
        self.Sett = Sett
        self.Serve = Serve
        self.Awr = Awr
        self.Str = Str
        self.AtkTech = AtkTech
        self.Receive = Receive
        self.Block = Block
        self.Save = Save
        self.Reflex = Reflex
        self.Spirit = Spirit
        self.DefTech = DefTech

    def rating(self):
        return self.ratingg
    
    def basic_total(self):
        return self.Qatk + self.Patk + self.Sett + self.Serve + self.Receive + self.Block + self.Save
    
    def basic_atk(self):
        return self.Qatk + self.Patk + self.Sett + self.Serve

    def basic_def(self):
        return self.Receive + self.Block + self.Save

class Memory:
    def __init__(self, name, serve, power, sett, receive, block, save):
        self.name = name
        self.serve = serve
        self.power = power
        self.sett = sett
        self.receive = receive
        self.block = block
        self.save = save

oikawa_Qatk = 212 + 650
oikawa_Patk = 1533 + 2233
oikawa_Sett = 1627 + 2570
oikawa_Serve = 1705 + 1680
oikawa_Receive = 1378 + 1090
oikawa_Block = 1530 + 1231
oikawa_Save = 1290 + 1200
oikawa_Awr = 0.05 + 0.032
oikawa_Str = 0 + 0.128
oikawa_AtkTech = 0 + .036
oikawa_Reflex = 0 + 0.032
oikawa_Spirit = 0
oikawa_DefTech = 0 + 0.012
oikawa_Stam = 120

# playerList = [oikawa, ushi, korai, nishi, tendo, tana, tsuki, iwai, kage, kono, kuro, kenji, koga, komi, daichi, kyo]

ushi = Player("Ushijima Wakatoshi", ["Serve", "Power Attack"], 236 + 760, 1707 + 2309, 1368 + 863, 1626 + 2202, 1537 + 1742, 1459 + 1693, 1367 + 1322, 0.05 + 0.15, 0 + 0.16, 0 + 0.036, 0, 0, 0 + 0.012)
ushi_player_rating = 21360
# print(ushi.rating())

# oikawa = Player("Oikawa Toru", ["Power Attack", "Serve", "Setter"], oikawa_Qatk, oikawa_Patk, oikawa_Sett, oikawa_Serve, oikawa_Receive, oikawa_Block, oikawa_Save, oikawa_Awr, oikawa_Str, oikawa_AtkTech, oikawa_Reflex, oikawa_Spirit, oikawa_DefTech)
oikawa = Player("Oikawa Toru", ["Power Attack", "Serve", "Setter"], 212, 1533, 1627, 1705, 1378, 1530, 1290, 0.05, 0, 0, 0, 0, 0)
oikawa_player_rating = 20927
# print(oikawa.rating())

starting_team_rating = 20890 + 19007 + 13241 + 13971 + 21367 + 18790 + 21360
team_rating = 137089 # Starting Players Rating + Deployment Bond + School Bond + Cheer

print("Oikawa Stats:")
print("Real Rating:\t\t", oikawa_player_rating)
print("Calculated Rating:\t", oikawa.rating())
print("Calculated Difference:\t", oikawa_player_rating - oikawa.rating())
print("Base to Real Difference:", oikawa_player_rating - oikawa.basic_total())
print("Calc Multiplier:\t", ((oikawa_player_rating - oikawa.rating()) / oikawa.rating()) * 100)
print("Base Multiplier:\t", ((oikawa_player_rating - oikawa.basic_total()) / oikawa.basic_total()) * 100)


print("\nUshijima Stats:")
print("Real Rating:\t\t", ushi_player_rating)
print("Calculated Rating:\t", ushi.rating())
print("Calculated Difference:\t", ushi_player_rating - ushi.rating())
print("Base to Real Difference:", ushi_player_rating - ushi.basic_total())
print("Calc Multiplier:\t", ((ushi_player_rating - ushi.rating()) / ushi.rating()) * 100)
print("Base Multiplier:\t", ((ushi_player_rating - ushi.basic_total()) / ushi.basic_total()) * 100)