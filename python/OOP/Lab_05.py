from random import randint


class Character:
    def __init__(self, nick_name: str, player_class: str, hp: int, armour: int, damage: int, weapon: int):
        self.nick_name = nick_name
        self.player_class = player_class
        self.hp = hp
        self.armour = armour
        self.damage = damage
        self.weapon = weapon

    def attack_function(self):

        attack = self.damage

        result_critical_attack = attack + (attack * (randint(15, 21) / 100))
        critical_attack = int(result_critical_attack)

        return self.weapon + randint(attack, critical_attack)

    def health_increase_function(self):
        return self.hp + 1000

    def exit_function(self):
        print("The game is over...!\n"
              "You both are loser...!\n")


def main():

    player_1 = Character(nick_name=input('First Player Name: '), player_class='Warrior', hp=10000, armour=1400, damage=500, weapon=1500)
    player_2 = Character(nick_name=input('Second Player Name: '), player_class='Magician', hp=6000, armour=850, damage=2000, weapon=1500)
    print(f'Welcome {player_1.nick_name} and {player_2.nick_name}')

    while True:
        print('Menu\n'
              'Attack Button ==> a\n'
              f'Health Button for {player_1.nick_name} ==> h1\n'
              f'Health Button for {player_2.nick_name} ==> h2\n'
              'Exit ==> e\n')

        process = input("Let's begin! ").lower()

        if process == 'e':
            player_1 and player_2.exit_function()
            break
        elif process == 'a':
            player_1.hp -= player_2.attack_function() - player_1.armour
            player_2.hp -= player_1.attack_function() - player_2.armour

            print(f"{player_1.nick_name} life: {player_1.hp}\n"
                  f"{player_2.nick_name} life: {player_2.hp}\n"
                  f"---------------------------------------\n"
                  f"{player_1.nick_name} has inflicted {player_1.attack_function() - player_2.armour} on {player_2.nick_name}\n"
                  f"{player_2.nick_name} has inflicted {player_2.attack_function() - player_1.armour} on {player_1.nick_name}\n")

        elif process == 'h1':
            if player_1.hp >= 10000:
                print("You can't use this skill more...! ")
            elif player_1.hp < 10000:
                player_1.health_increase_function()
                print(f"{player_1.hp}")
        elif process == 'h2':
            if player_2.hp >= 6000:
                print("You can't use this skill more...! ")
            elif player_2.hp < 6000:
                player_2.health_increase_function()
                print(f"{player_2.hp}")

        else:
            print('Please choose a valid action...! ')

        if player_1.hp <= 0 <= player_2.hp:

            print(f"{player_2.nick_name} has won the fight...! ")
            print(f"{player_1.nick_name} is totally loser...! ")
            break

        elif player_2.hp <= 0 <= player_1.hp:

            print(f"{player_1.nick_name} has won the fight...! ")
            print(f"{player_2.nick_name} is totally loser...! ")
            break

        elif player_1.hp <= 0 and player_2.hp <= 0:
            print(f"Tied game...!")
            break


main()

