import random

def do_enchant(user):
    pb_list = [0, 0, 0, 0, 0, 0, 0.3, 0.3, 0.3, 0.5, 0.5, 0.7, 0.7, 0.85, 0.85, 0.9]
    wepon_broken = [True, False]
    success_probability = random.randrange(1, 101)
    sword = user.equip_sword
    sword.probability = 100 - (100 * pb_list[sword.enchant_level])+user.probability

    if success_probability <= sword.probability:
        sword.enchant_level += 1
        print(f'[+{sword.enchant_level} {sword.name}] 강화에 성공했습니다')
        sword.probability = 100 - (100 * pb_list[sword.enchant_level])

    else:
        print(f'[+{sword.enchant_level} {sword.name}] 강화에 실패했습니다.')
        if sword.enchant_level <= 5:
            print(f'+{sword.enchant_level} {sword.name} 아무 일도 일어나지 않습니다')
                
        elif sword.enchant_level <= 8:
            print(f'+{sword.enchant_level} {sword.name} 강화도가 1 하락합니다')
            sword.enchant_level -= 1
                
        elif sword.enchant_level <= 10:
            drop_enchant_level = [1, 2]
            selected = random.choice(drop_enchant_level)
            print(f'+{sword.enchant_level} {sword.name} 강화도가 {selected} 하락합니다')
            sword.enchant_level -= selected
            
        elif sword.enchant_level <= 12:
            sword.broken = random.choice(wepon_broken)
            if sword.broken:
                drop_enchant_level = [1, 2, 3]
                selected = random.choice(drop_enchant_level)
                print(f'+{sword.enchant_level} {sword.name} 강화도가 {selected} 하락합니다')
                sword.enchant_level -= selected
            else:
                print(f'{sword.name} 증발 됐습니다')
                user.sword_list.remove(user.equip_sword)
                user.equip_sword = None
            
        elif sword.enchant_level < 15:
            sword.broken = random.choice(wepon_broken)
            if sword.broken:
                drop_enchant_level = [1, 2, 3]
                selected = random.choice(drop_enchant_level)
                print(f'+{sword.enchant_level} {sword.name} 강화도가 {selected} 하락합니다')
                sword.enchant_level -= selected
            else:
                print(f'{sword.name} 증발 됐습니다.')
                user.sword_list.remove(user.equip_sword)
                user.equip_sword = None
            
    return sword.probability
