import random
from . import status
dice_count = 1
def dice():
    global dice_count
    dice_count += 1
    dice_result = random.randrange(1, 7)
    status.boss_hp += 2
    status.boss_attack += 2
    status.boss_defence += 1
    add_status = dice_result / 2
    status.attack += add_status
    status.defence += add_status
    print(
            f'주사위값은 {dice_result}가 나왔습니다.'
            f'공격력이 {add_status}만큼 증가하였습니다.'
            f'방어력이 {add_status}만큼 증가하였습니다.'
            )

if __name__ == '__main__':
    dice()
