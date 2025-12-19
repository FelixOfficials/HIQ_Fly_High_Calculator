from calculator import Player, Training, Skill, SkillRes, Bond, Potential, Memory

# playerList = [oikawa, ushi, korai, nishi, tendo, tana, tsuki, iwai, kage, kono, kuro, kenji, koga, komi, daichi, kyo]

# ushi = Player("Ushijima Wakatoshi", ["bsc_serve", "Power Attack"], 236 + 760, 1707 + 2309, 1368 + 863, 1626 + 2202, 1537 + 1742, 1459 + 1693, 1367 + 1322, 0.05 + 0.15, 0 + 0.16, 0 + 0.036, 0, 0, 0 + 0.012)
# ushi_player_rating = 21360
# print(ushi.rating())

def main():
    oikawa_training = Training("Oikawa Toru", 7, ["Power", "Serve", "Set%", "Block", "Set", "Serve%", "Court Commander"], [250, 250, 0.065, 250, 250, 0.065, 0.1])
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
    oikawa_bonds = [bond1, bond2, bond3, bond4]
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

if __name__ == "__main__":
    main()