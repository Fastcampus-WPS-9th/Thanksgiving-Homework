import random
from .Player_Pokemon import *
from main import *


class Legendary:

    def __init__(self):
        self.name = 'no'
        self.level = 0
        self.max_hp = 0
        self.current_hp = self.max_hp
        self.type = 'random'
        self.attack = 0
        self.defense = 0
        self.catcha = 10
        self.turn = 0
        self.player_pokemon = 'no'

    def attack_player(self, skill_name, pow):
        self.player_pokemon.current_hp = self.player_pokemon.current_hp - (pow - self.player_pokemon.defense)
        print(
            f'{self.name}이 {skill_name}을 사용했다.\n'
            f'{self.player_pokemon.name}에게 {pow - self.player_pokemon.defense}의 데미지를 입혔다.\n'
            f'{self.player_pokemon.name}의 현재 체력 {self.player_pokemon.current_hp}!'
        )

    def debuff_player(self, skill_name, debuff_type, pow):
        if debuff_type == 'atk':
            self.player_pokemon.attack -= pow
            print(
                f'{self.name}이 {skill_name}을 사용했다.\n'
                f'{self.player_pokemon.name}의 atk가 {pow}만큼 떨어졌다.\n'
                f'{self.player_pokemon.name}의 현재 atk {self.player_pokemon.attack}!'
            )

        else:
            self.player_pokemon.defense -= pow
            print(
                f'{self.name}이 {skill_name}을 사용했다.\n'
                f'{self.player_pokemon.name}의 def가 {pow}만큼 떨어졌다.\n'
                f'{self.player_pokemon.name}의 현재 def {self.player_pokemon.defense}!'
            )

    def buff_legendary(self, skill_name, buff_type, pow):
        if buff_type == 'atk':
            self.attack += pow
            print(
                f'{self.name}이 {skill_name}을 사용했다.\n'
                f'{self.name}의 atk가 {pow}만큼 상승했다.\n'
                f'{self.name}의 현재 atk {self.attack}!'
            )

        else:
            self.defense += pow
            print(
                f'{self.name}이 {skill_name}을 사용했다.\n'
                f'{self.name}의 def가 {pow}만큼 상승했다.\n'
                f'{self.name}의 현재 def {self.defense}!'
            )

    def poke_info(self):
        print('{name}\n{hp}\n{attack}\n{defense}\n\n'.format(
            name=f'이름 : {self.name}',
            hp=f'HP : {self.current_hp} / {self.max_hp}',
            attack=f'ATK : {self.attack}',
            defense=f'DEF : {self.defense}'
        ))


class Articuno(Legendary):
    # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.name = '프리져'
        self.max_hp = 207
        self.current_hp = self.max_hp
        self.catcha = 10
        self.turn = 0
        self.level = 50
        self.type = 'ice,fly'
        self.attack = 10
        self.defense = 5
        self.player_pokemon = 'no'

    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'프리져({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            f'지속적으로 atk/def 버프/디버프를 사용하는 전설의 포켓몬입니다.\n'
        )

    def __str__(self):
        return self.name

    # 해당 전설의 포켓몬의 기술 메서드를 설정한다. 3개
    def gust(self):
        skill_name = '바람 일으키기'
        power = 2 * self.attack
        if 'grass' in self.player_pokemon.type:
            power *= 2
        elif 'earth' or 'electric' in self.player_pokemon.type:
            power *= 0.5
        self.attack_player(skill_name, power)

    def freeze_beam(self):
        power = 5 * self.attack
        debuff = 3
        debuff_type = 'def'
        skill_name = '냉동빔'
        if 'fire' and 'fly' in self.player_pokemon.type:
            power = power
        elif 'fire' in self.player_pokemon.type:
            power *= 0.5
        elif 'grass' or 'earth' or 'fly' in self.player_pokemon.type:
            power *= 2
        self.attack_player(skill_name, power)
        self.debuff_player(skill_name, debuff_type, debuff)

    def reflector(self):
        debuff_type = 'atk'
        buff_type = 'def'
        power = 2
        skill_name = '리플렉터'
        self.debuff_player(skill_name, debuff_type, power)
        self.buff_legendary(skill_name, buff_type, power)

    def mist(self):
        buff_type = 'atk'
        power = 3
        skill_name = '흰 안개'
        self.buff_legendary(skill_name, buff_type, power)

    def Do_attack(self):
        self.turn += 1
        skill = random.choices(population=[self.gust, self.freeze_beam, self.reflector, self.mist],
                               weights=[0.35, 0.35, 0.15, 0.15], k=1)
        return skill[0]()


class Groudon(Legendary):
    # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.name = '그란돈'
        self.max_hp = 255
        self.current_hp = self.max_hp
        self.catcha = 10
        self.turn = 0
        self.level = 55
        self.type = 'fire,earth'
        self.attack = 3
        self.defense = 12
        self.stack = 1
        self.player_pokemon = 'no'

    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'그란돈({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            f'기술을 통해 파워 스택을 쌓아 점점 강력해지는 전설의 포켓몬입니다.\n'
        )

    def __str__(self):
        return self.name

    # 해당 전설의 포켓몬의 기술 메서드를 설정한다. 3개
    def earthquake(self):
        skill_name = '지진'
        power = 3 * (self.attack + self.stack)
        if 'fire' or 'electric' in self.player_pokemon.type:
            power *= 2
        elif 'grass' or 'water' in self.player_pokemon.type:
            power *= 0.5
        self.attack_player(skill_name, power)
        self.stack += 1
        print('파워스택이 1 증가했다!')

    def volcano(self):
        power = 12 * (self.attack + self.stack)
        skill_name = '분화'
        if 'grass' or 'ice' in self.player_pokemon.type:
            power *= 2
        elif 'water' in self.player_pokemon.type:
            power *= 0.5
        self.attack_player(skill_name, power)
        self.stack = 1
        self.current_hp -= (self.attack + self.stack)
        self.attack += 3
        self.defense += 3
        print('파워 스택이 초기화되지만 atk와 def가 3씩 증가합니다.')

    def ancient_power(self):
        skill_name = '원시의 힘'
        self.stack += 2
        buff_type = 'def'
        power = -1
        self.buff_legendary(skill_name, buff_type, power)
        print('방어력을 -1잃고 2 파워 스택을 쌓았다!')

    def sleeping(self):
        stack_hp = 4 * self.stack
        if (self.current_hp + stack_hp) > self.max_hp:
            self.current_hp = self.max_hp
        else:
            self.current_hp += stack_hp
        self.stack -= 2
        self.defense += 1
        print(
            f'{self.name}이 잠자고 있습니다.\n'
            f'체력이 {stack_hp}만큼 회복되고, 방어력이 1만큼 상승하나 2 파워 스택을 잃습니다.\n'
            f'현재 체력 {self.current_hp}, 방어력 {self.defense}'
        )

    def Do_attack(self):
        self.turn += 1
        skill = random.choices(population=[self.earthquake, self.volcano, self.ancient_power, self.sleeping],
                               weights=[0.6, 0.1, 0.15, 0.15], k=1)
        return skill[0]()


class Mewtwo(Legendary):
    # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.name = '뮤츠'
        self.max_hp = 200
        self.current_hp = self.max_hp
        self.catcha = 10
        self.turn = 0
        self.level = 60
        self.type = 'esp'
        self.attack = 0
        self.defense = 0
        self.player_pokemon = 'no'

    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'뮤츠({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            f'서로의 atk/def를 뒤바꾸고 강력한 무상성 공격을 구사하는 전설의 포켓몬입니다.\n'
            f'공격시 계속해서 체력을 회복하며, 초과 회복시 MAX HP가 증가합니다.\n'
        )

    def __str__(self):
        return self.name

    # 해당 전설의 포켓몬의 기술 메서드를 설정한다. 3개
    def psychic(self):
        skill_name = '사이코키네시스'
        power = 25 + (7 * self.attack)
        self.attack_player(skill_name, power)
        self.current_hp += 15
        if self.max_hp < self.current_hp:
            max_hp = self.current_hp
        print('뮤츠는 15의 체력을 회복했다.')

    def psystrike(self):
        power = self.player_pokemon.current_hp / 2
        skill_name = '사이코브레이크'
        self.attack_player(skill_name, power)
        self.current_hp += 40
        if self.max_hp < self.current_hp:
            self.max_hp = self.current_hp
        print('뮤츠는 40의 체력을 회복했다.')

    def power_swap(self):
        self.attack, self.player_pokemon.attack = self.player_pokemon.attack, self.attack
        self.current_hp = self.current_hp / 2
        print(
            f'뮤츠는 파워스왑을 사용해 서로의 공격력을 뒤바꾸었다!\n'
            f'뮤츠의 atk는 이제 {self.attack}이다!\n'
            f'Player의 atk는 {self.player_pokemon.attack}가 되었다!\n'
            f'대신 뮤츠의 체력은 절반이 되었다!'
        )

    def guard_swap(self):
        self.current_hp, self.player_pokemon.current_hp = self.player_pokemon.current_hp, self.current_hp
        self.defense, self.player_pokemon.defense = self.player_pokemon.defense, self.defense
        print(
            f'뮤츠는 가드스왑을 사용해 서로의 방어를 뒤바꾸었다!\n'
            f'뮤츠의 체력은 이제 {self.current_hp}이다!\n'
            f'Player의 체력은 {self.player_pokemon.current_hp}가 되었다!\n'
            f'뮤츠의 def는 {self.defense}가 되었다!\n'
            f'Player의 def는 {self.player_pokemon.defense}가 되었다!'
        )

    def Do_attack(self):
        self.turn += 1
        skill = random.choices(population=[self.psychic, self.psystrike, self.power_swap, self.guard_swap],
                               weights=[0.35, 0.3, 0.25, 0.1], k=1)
        return skill[0]()