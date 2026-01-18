from calculator import Player, Training, Skill, SkillRes, Bond, Potential, Memory

def main():
    oikawa_training = Training("Oikawa Toru", 7, ["Power Attack", "Serve", "Set%", "Block", "Set", "Serve%", "Court Commander"], [250, 250, 0.065, 250, 250, 0.065, 0.1])
    oikawa_skillres = SkillRes("Oikawa Toru", 4, 4, ["Basic%", "Serve%", "Basic%", "Placeholder%", "Basic%"], [0.13, 0.18, 0.13, 0.15, 0.13])

    bond1 = Bond("Long-standing Rivals", 5, [{"Set": 5, "Set%": 0.01}, {"Set": 7, "Set%": 0.02}, {"Set": 9, "Set%": 0.03}, {"Set": 12, "Set%": 0.04}, {"Set": 15, "Set%": 0.05}])
    bond2 = Bond("Power of Trust", 3, [{"Block": 5, "Block%": 0.01}, {"Block": 7, "Block%": 0.02}, {"Block": 9, "Block%": 0.03}, {"Block": 12, "Block%": 0.04}, {"Block": 15, "Block%": 0.05}])
    bond3 = Bond("Perfect Chemistry", 4, [{"Placeholder": 5, "Placeholder%": 0.01}, {"Placeholder": 7, "Placeholder%": 0.02}, {"Placeholder": 9, "Placeholder%": 0.03}, {"Placeholder": 12, "Placeholder%": 0.04}, {"Placeholder": 15, "Placeholder%": 0.05}])
    bond4 = Bond("A Bit Higher!", 3, [{"Set": 5, "Set%": 0.01}, {"Set": 7, "Set%": 0.02}, {"Set": 9, "Set%": 0.03}, {"Set": 12, "Set%": 0.04}, {"Set": 15, "Set%": 0.05}])

    skill1 = Skill("Great King's Set", 1, 6, [1.2, 1.35, 1.5], "Set")
    skill2 = Skill("Great King's Dump", 1, 6, [1.15, 1.350, 1.45], "Set")
    skill3 = Skill("Court Commander", 1, 1, [0.1, 0.14, 0.18], "Awareness")
    skill4 = Skill("Great King's Jump Serve", 1, 8, [2.6, 2.75, 2.9, 3.05, 3.2], "Serve")

    oikawa_skills = [skill1, skill2, skill3, skill4]
    oikawa_bonds = [bond1, bond2, bond3, bond4]
    oikawa = Player("Oikawa Toru", ["Power Attack", "Serve", "Setter"], 212, 1533, 1627, 1705, 1378, 1530, 1290, 0.05, 0, 0, 0, 0, 0, oikawa_training, oikawa_skills, oikawa_skillres, oikawa_bonds)
    oikawa_player_rating = 20927
    print(oikawa)



    ushijima_training = Training("Wakatoshi Ushijima", 7, ["Receive", "Power Attack", "Serve%", "Block", "Serve", "Power Attack%", "Ace Style"], [250, 250, 0.065, 250, 250, 0.065, 0.015])
    ushijima_skillres = SkillRes("Wakatoshi Ushijima", 4, 4, ["Basic%", "Placeholder%", "Basic%", "Placeholder%", "Basic%"], [0.13, 0.18, 0.13, 0.15, 0.13])

    bond5 = Bond("Undisputed Ace VS The Freak Quick", 0, [{"Power Attack": 5, "Power Attack%": 0.01}, {"Power Attack": 7, "Power Attack%": 0.02}, {"Power Attack": 9, "Power Attack%": 0.03}, {"Power Attack": 12, "Power Attack%": 0.04}, {"Power Attack": 15, "Power Attack%": 0.05}])
    bond6 = Bond("Undisputed Aces", 0, [{"Power Attack": 5, "Power Attack%": 0.01}, {"Power Attack": 7, "Power Attack%": 0.02}, {"Power Attack": 9, "Power Attack%": 0.03}, {"Power Attack": 12, "Power Attack%": 0.04}, {"Power Attack": 15, "Power Attack%": 0.05}])
    bond7 = Bond("Lifelong Best Friends", 5, [{"Attack Technique%": 0.03}, {"Attack Technique%": 0.035}, {"Attack Technique%": 0.04}, {"Attack Technique%": 0.045}, {"Attack Technique%": 0.05}])
    bond8 = Bond("Ushijima and Benkei", 0, [{"Block": 5, "Block%": 0.01}, {"Block": 7, "Block%": 0.02}, {"Block": 9, "Block%": 0.03}, {"Block": 12, "Block%": 0.04}, {"Block": 15, "Block%": 0.05}])
    bond9 = Bond("Undisputed Ace and Shadow Setter", 0, [{"Placeholder": 5, "Placeholder%": 0.01}, {"Placeholder": 7, "Placeholder%": 0.02}, {"Placeholder": 9, "Placeholder%": 0.03}, {"Placeholder": 12, "Placeholder%": 0.04}, {"Placeholder": 15, "Placeholder%": 0.05}])

    skill5 = Skill("In The Groove", 1, 1, [0.08, 0.1, 1.2], "Awareness")
    skill6 = Skill("Dominating Serve", 1, 6, [1.25, 1.40, 1.55], "Serve")
    skill7 = Skill("Ace Style", 1, 1, [0.015, 0.02, 0.02], "Basic")
    skill8 = Skill("Undisputed Ace", 1, 8, [2.5, 2.65, 2.80, 2.95, 3.1], "Serve")

    ushijima_skills = [skill5, skill6, skill7, skill8]
    ushijima_bonds = [bond5, bond6, bond7, bond8, bond9]
    ushijima = Player("Wakatoshi Ushijima", ["Power Attack", "Serve", "Setter"], 236, 1707, 1368, 1626, 1537, 1459, 1367, 0.05, 0, 0, 0, 0, 0, ushijima_training, ushijima_skills, ushijima_skillres, ushijima_bonds)
    ushijima_player_rating = 20927
    # print(ushijima)

    starting_team_rating = 20890 + 19007 + 13241 + 13971 + 21367 + 18790 + 21360
    team_rating = 137089 # Starting Players Rating + Deployment Bond + School Bond + Cheer

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
    
    skill9 = Skill("Basic Spike", 1, 1, [0.05, 0.07], "Quick Attack")
    skill10 = Skill("Basic Receive", 1, 1, [0.05, 0.07], "Receive")
    skill11 = Skill("Basic Blocking", 1, 1, [0.05, 0.07], "Block")
    skill12 = Skill("Hearty Block", 1, 12, [1.50, 1.58, 1.65], "Block")
    
    kosuke_skills = [skill9, skill10, skill11, skill12]
    # kosuke_skills = []
    kosuke = Player("Kosuke Tashiro", ["Block"], 78, 54, 68, 72, 70, 82, 66, 0, 0, 0, 0.05, 0, 0, kosuke_training, kosuke_skills, kosuke_skillres, kosuke_bonds)

    # print(kosuke)

if __name__ == "__main__":
    main()