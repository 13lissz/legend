print("""

  ___                                   __       ___                            
 |   \ _  _ _ _  __ _ ___ ___ _ _  ___ / _|___  |   \ _ _ __ _ __ _ ___ _ _  ___
 | |) | || | ' \/ _` / -_) _ \ ' \(_-< > _|_ _| | |) | '_/ _` / _` / _ \ ' \(_-<
 |___/ \_,_|_||_\__, \___\___/_||_/__/ \_____|  |___/|_| \__,_\__, \___/_||_/__/
                |___/                                         |___/             

""")
print ("Welcome to Dungeons & Dragon")

player_name=input("What is your name, Adventure : ")

health = 100
damage = 20

print('\nwelcome, ' + player_name + '! you have ' + str(health) + ' health and can do damage ' + str(damage))

print("You came across a dragon!! what will you do")
print('1. Fight')
print('2. Run')
dragon_health=1000
dragon_damage=50

choice=int(input("Enter either 1 or 2 : "))


if choice ==1:
    print("\nYou attack the dragon and deal",str(damage),"damage to the dragon.")
    dragon_health-=20
    print("The Dragon current Health is",dragon_health)
elif choice ==2:
    print("\nYou run away from the dragon, the dragon chase you!")
    print("The dragon strike you and deal",str(dragon_damage),"damage to you.")
    health-=50
    print("Your current Health is",health)
elif choice ==3:
    print("You choose the hidden move. \nYou become friend with the dragon")
else :
    print("\nYou choose the invalid move, the dragon eat you alive..")
print("Thank for playing")