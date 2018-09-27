from . import ran, status
game_status = ''
def versus():
    boss_hp = status.boss_hp
    boss_attack = status.boss_attack
    boss_defence = status.boss_defence
    hp = status.hp
    attack = status.attack
    defence = status.defence
    if boss_attack > defence:
        damage_for_me = boss_attack - defence
    else:
        damage_for_me = 1
    if attack > boss_defence:
        damage_for_boss = attack - boss_defence
    else:
        damage_for_boss = 1

    while True:
        boss_hp -= damage_for_boss
        hp -= damage_for_me
        if boss_hp < 0:
            break
        elif hp < 0:
            break
    global game_status
    if boss_hp > hp:
        game_status = 'lose'
    else:
        game_status = 'win'
