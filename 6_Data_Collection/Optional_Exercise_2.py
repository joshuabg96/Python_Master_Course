# In the develop of a videogame you have to configure and balance each character class jubale
# Starting with the base that the stadistic is 2, you have to meet following conditions
# Knight: Has 2 times life and defense of the warrior
# Warrior: Has 2 times attack and reach of the knight
# Archer: Has same life and attack of the warrior but haft of defense and 2 times reach

Knight = {'life':2, 'attack':2, 'defense':2, 'reach':2}
Warrior = {'life':2, 'attack':2, 'defense':2, 'reach':2}
Archer = {'life':2, 'attack':2, 'defense':2, 'reach':2}

Knight['life'] = Warrior['life'] * 2
Knight['defense'] = Warrior['defense'] * 2

Warrior['attack'] = Knight['attack'] * 2
Warrior['reach'] = Knight['reach'] * 2

Archer['life'] = Warrior['life']
Archer['attack'] = Warrior['attack']
Archer['defense'] = Warrior['defense'] / 2
Archer['reach'] = Warrior['reach'] * 2

print("Knight\t", Knight )
print("Warrior\t", Warrior)
print("Archer\t", Archer)
