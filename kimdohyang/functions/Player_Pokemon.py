import random
from time import sleep
from .Legendary_Pokemon import *
from main import *


class Challenger:
    def __init__(self):
        self.name = 'no'
        self.level = 0
        self.max_hp = 0
        self.current_hp = self.max_hp
        self.type = 'random'
        self.attack = 0
        self.defense = 0
        self.legendary_pokemon = 'no'

    def attack_legendary(self, skill_name, pow):
        self.legendary_pokemon.current_hp = self.legendary_pokemon.current_hp - (pow - self.legendary_pokemon.defense)
        print(
            f'{self.name}이 {skill_name}을 사용했다.\n'
            f'{self.legendary_pokemon.name}에게 {pow - self.legendary_pokemon.defense}의 데미지를 입혔다.\n'
            f'{self.legendary_pokemon.name}의 현재 체력 {self.legendary_pokemon.current_hp}!'
        )

    def debuff_legendary(self, skill_name, debuff_type, pow):
        if debuff_type == 'atk':
            self.legendary_pokemon.attack -= pow
            print(
                f'{self.name}이 {skill_name}을 사용했다.\n'
                f'{self.legendary_pokemon.name}의 atk가 {pow}만큼 떨어졌다.\n'
                f'{self.legendary_pokemon.name}의 현재 atk {self.legendary_pokemon.attack}!'
            )

        else:
            self.legendary_pokemon.defense -= pow
            print(
                f'{self.name}이 {skill_name}을 사용했다.\n'
                f'{self.legendary_pokemon.name}의 def가 {pow}만큼 떨어졌다.\n'
                f'{self.legendary_pokemon.name}의 현재 def {self.legendary_pokemon.defense}!'
            )

    def buff_player(self, skill_name, buff_type, pow):
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

    def Do_turn(self, turn_choice):
        if turn_choice == '1':
            self.Do_attack()

        elif turn_choice == '2':
            catchcatch = Catch_Monster()
            ball = catchcatch.choice_ball()
            result = catchcatch.catch(ball, self.legendary_pokemon)

            if result:
                print(
                    f'{Player}가 {self.legendary_pokemon}을 {self.legendary_pokemon.turn}만에 잡았습니다!\n'
                    f'===================GAME CLEAR!!!====================\n'
                    )
                write_rank()
                print_rank()
                sleep(5)
                quit()

            elif result == False:
                if Catch_Monster.totalppp == 0:
                    print(
                        f'{Player}의 모든 몬스터볼이 소진되었습니다. 다시 도전하세요!\n'
                        f'===================GAME END====================\n'
                        f'잠시 후 게임이 종료됩니다.'
                    )
                    quit()

                else:
                    print(f'{self.legendary_pokemon}을 잡지 못했습니다!')

            else:
                print('잘못 입력하셨습니다. 다시 선택해주세요.')
                turn_choice = input()
                self.Do_turn(turn_choice)

    def poke_info(self):
        print('{name}\n{hp}\n{attack}\n{defense}\n\n'.format(
            name=f'이름 : {self.name}',
            hp=f'HP : {self.current_hp} / {self.max_hp}',
            attack=f'ATK : {self.attack}',
            defense=f'DEF : {self.defense}'
        ))


class Catch_Monster:
    def __init__(self):
        self.monsterppp = 3
        self.hyperppp = 1
        self.totalppp = 4

    def choice_ball(self):
        print(
            f'. 던질 몬스터볼을 정해주세요.\n'
            f'1: 몬스터볼\n2: 하이퍼볼\n'
        )
        select_ball = input()
        if select_ball == '1':
            if self.monsterppp > 0:
                ball_score = 10
                self.monsterppp -= 1
                self.totalppp -= 1
            else:
                print('몬스터볼이 다 떨어졌습니다. 다른 볼을 골라주세요.')
                self.choice_ball()

        elif select_ball == '2':
            if self.hyperppp > 0:
                ball_score = 20
                self.hyperppp -= 1
                self.totalppp -= 1
            else:
                print('하이퍼볼이 다 떨어졌습니다. 다른 볼을 골라주세요.')
                self.choice_ball()

        return ball_score

    def catch(self, ball, legendary_pokemon):
        catch_prob = (ball + legendary_pokemon.catcha) / 100
        if legendary_pokemon.current_hp > 100:
            catch_prob -= 0.18
        elif legendary_pokemon.current_hp <= 100 and legendary_pokemon.current_hp > 60:
            catch_prob -= 0.1
        elif legendary_pokemon.current_hp <= 60 and legendary_pokemon.current_hp > 40:
            pass
        elif legendary_pokemon.current_hp <= 40 and legendary_pokemon.current_hp > 20:
            catch_prob += 0.1
        elif legendary_pokemon.current_hp <= 20:
            catch_prob += 0.2
        print(f'가라! {ball}!')
        sleep(2)
        return random.choices(population=[True, False], weights=[catch_prob, 1 - catch_prob], k=1)[0]


class Charizard(Challenger):
    # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.level = 40
        self.max_hp = 118
        self.name = '리자몽'
        self.current_hp = self.max_hp
        self.type = 'fire,fly'
        self.attack = 4
        self.defense = 0
        self.ppp = 0
        self.legendary_pokemon = 'no'

    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'리자몽({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            '적의 def를 떨어뜨리는 딜러 포켓몬입니다. 유리대포입니다.'
        )

    def __str__(self):
        return self.name

    # 해당 포켓몬의 기술 메서드를 설정한다. 3개
    def airslash(self):
        skill_name = '에어슬래시'
        power = 5 * self.attack
        debuff_type = 'def'
        debuff = 2
        if 'grass' in self.legendary_pokemon.type:
            power *= 2
        elif 'earth' or 'electric' in self.legendary_pokemon.type:
            power *= 0.5
        self.attack_legendary(skill_name, power)
        self.debuff_legendary(skill_name, debuff_type, debuff)

    def flare_blitz(self):
        if self.ppp == 0:
            power = 10 * self.attack
            debuff = 8
            debuff_type = 'def'
            skill_name = '플레어 드라이브'
            if 'grass' or 'ice' in player_pokemon.type:
                power *= 2
            elif 'water' or 'earth' in player_pokemon.type:
                power *= 0.5
            self.attack_legendary(skill_name, power)
            self.debuff_legendary(skill_name, debuff_type, debuff)
            self.current_hp -= 20
            self.ppp += 1
        else:
            print('이미 1회 스킬을 사용하셨습니다.\n')
            self.Do_attack()

    def fire_fang(self):
        buff_type = 'atk'
        power = 3
        skill_name = '불꽃엄니'
        self.buff_player(skill_name, buff_type, power)
        self.defense -= 3
        print(f'방어력이 3 떨어졌습니다. 현재 방어력 {self.defense}!\n')

    def skill_info(self):
        skill_docs = [
            '에어슬래시 - 5 * attack의 데미지를 주고 방어력을 2 깎습니다.',
            '플레어 드라이브 - 10 * attack의 데미지를 주고 방어력을 8 깎습니다. 충격으로 자신의 hp가 20 떨어집니다. 1회만 사용 가능합니다.',
            '불꽃 엄니 - 자신의 atk를 3만큼 올리는 대신 방어력이 3 떨어집니다.'
        ]
        print('\n\n'.join([f'{index}:{skill}' for index, skill in enumerate(skill_docs, start=1)]))

    def Do_attack(self):
        self.skill_info()
        skill_list = [self.airslash, self.flare_blitz, self.fire_fang]
        select_skill = input('사용할 스킬을 선택해주세요.')
        skill_list[int(select_skill) - 1]()


class Dragonite(Challenger):
    # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.level = 40
        self.max_hp = 146
        self.name = '망나뇽'
        self.current_hp = self.max_hp
        self.type = 'dragon'
        self.attack = 5
        self.defense = 2
        self.dragon_stack = 0
        self.ppp = 0
        self.legendary_pokemon = 'no'

    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'망나뇽({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            '무상성 딜러 포켓몬입니다. 분노 스택 관리가 중요합니다.'
        )

    def __str__(self):
        return self.name

    # 해당 포켓몬의 기술 메서드를 설정한다. 3개
    def dragon_dance(self):
        skill_name = '용춤'
        power = (3 * self.attack) + self.dragon_stack
        self.attack_legendary(skill_name, power)
        self.current_hp += (2 * self.dragon_stack)
        self.dragon_stack -= 2
        print(
            f'{2 * self.dragon_stack}만큼 hp가 회복됩니다.\n'
            f'대신 분노 스택이 2만큼 떨어집니다. 현재 분노 스택 {self.dragon_stack}!\n'
        )

    def hyper_beam(self):
        if self.ppp == 0:
            power = (2 * self.attack) + (7 * self.dragon_stack)
            skill_name = '파괴광선'
            self.attack_legendary(skill_name, power)
            self.current_hp -= self.dragon_stack
            print(
                f'스트레스로 {self.dragon_stack}만큼 hp가 떨어집니다.\n'
            )
            self.dragon_stack = 0
            print(
                f'분노 스택이 초기화됩니다. 현재 분노 스택 {self.dragon_stack}\n!'
            )
            self.ppp += 1
        else:
            print('이미 1회 스킬을 사용하셨습니다.\n')
            self.Do_attack()

    def dragon_rage(self):
        self.dragon_stack += 4
        skill_name = '용의 분노'
        self.current_hp -= (self.dragon_stack + 6)
        print(f'스트레스로 {self.dragon_stack + 6}만큼 hp가 떨어집니다.\n')

    def skill_info(self):
        skill_docs = [
            '용춤 - 3 * attack + 1 * 분노 스택 데미지를 주고 분노 스택 *2 만큼 체력을 회복합니다. 대신 분노 스택이 2만큼 떨어집니다.',
            '파괴광선 - 2 * attack + 7 * 분노 스택의 데미지를 주고 자신의 hp가 분노 스택만큼 떨어집니다. 1회만 사용 가능합니다.',
            '용의 분노 - 자신의 체력을 분노스택 + 6 만큼 소모하여 분노 스택을 4 올립니다.'
        ]
        print('\n\n'.join([f'{index}:{skill}' for index, skill in enumerate(skill_docs, start=1)]))

    def Do_attack(self):
        self.skill_info()
        skill_list = [self.dragon_dance, self.hyper_beam, self.dragon_rage]
        select_skill = input('사용할 스킬을 선택해주세요.')
        skill_list[int(select_skill) - 1]()

class Snorlax(Challenger):
    # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.level = 40
        self.max_hp = 228
        self.name = '잠만보'
        self.current_hp = self.max_hp
        self.type = 'grass,earth'
        self.attack = 8
        self.defense = 12
        self.sleep_stack = 0
        self.legendary_pokemon = 'no'

    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'잠만보({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            '오로지 탱킹을 위해 모든걸 바친 포켓몬입니다. 체력 초과회복 보너스가 있습니다.'
        )

    def __str__(self):
        return self.name

    def Snorlax_over_hp(self):
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
            self.attack += 1
            self.defense += 1
            print(
                f'체력을 초과회복했으므로 atk와 def가 1씩 증가합니다.\n'
                f'현재 atk {self.attack} def {self.defense}!\n'
            )
        else:
            pass

    # 해당 포켓몬의 기술 메서드를 설정한다. 3개
    def tackle(self):
        skill_name = '몸통박치기'
        power = self.attack
        self.attack_legendary(skill_name, power)

    def deep_sleep(self):
        buff = 1 + (self.sleep_stack)
        buff_type = 'def'
        skill_name = '잠자기'
        self.buff_player(skill_name, buff_type, buff)
        self.current_hp += 13 + (2 * self.sleep_stack)
        print(
            f'잠자기로 체력을 {13 + (2 * self.sleep_stack)}만큼 회복합니다!\n'
            f'현재 체력 {self.current_hp}!\n'
        )
        self.sleep_stack += 1
        print(f'꿀잠 스택이 1 증가합니다. 현재 꿀잠 스택 {self.sleep_stack}!\n')
        self.Snorlax_over_hp()

    def snore(self):
        debuff_type = 'atk'
        power = 1
        skill_name = '코골기'
        self.debuff_legendary(skill_name, debuff_type, power)
        self.current_hp += 10
        print(
            f'코골기로 체력을 10만큼 회복합니다!\n'
            f'현재 체력 {self.current_hp}!\n'
        )
        self.Snorlax_over_hp()

    def skill_info(self):
        skill_docs = [
            '몸통박치기 - 평범한 몸통박치기로 attack만큼 데미지를 줍니다.',
            '잠자기 - 13 + (2*꿀잠 스택)만큼 체력을 회복하고 방어력도 (1+꿀잠스택)만큼 상승합니다.',
            '코골기 - 코골기로 자신의 체력을 10만큼 회복하고 상대의 atk를 2만큼 떨어뜨립니다.'
        ]
        print('\n\n'.join([f'{index}:{skill}' for index, skill in enumerate(skill_docs, start=1)]))

    def Do_attack(self):
        self.skill_info()
        skill_list = [self.tackle, self.deep_sleep, self.snore]
        select_skill = input('사용할 스킬을 선택해주세요.')
        skill_list[int(select_skill) - 1]()


class Blastoise(Challenger):
    # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.level = 40
        self.max_hp = 186
        self.name = '거북왕'
        self.current_hp = self.max_hp
        self.type = 'water'
        self.attack = 5
        self.defense = 4
        self.rage_stack = 0
        self.legendary_pokemon = 'no'

    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'거북왕({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            '분노 스택을 쌓아 스스로를 강화하는 딜탱 포켓몬입니다.'
        )

    def __str__(self):
        return self.name

    def Blastoise_rage(self):
        if self.current_hp <= 93:
            self.rage_stack += 10
            print(
                f'체력이 절반 이하로 떨어져 분노가 10상승합니다!\n'
                f'현재 분노 {self.rage_stack}!\n'
            )

        if self.rage_stack >= 13:
            self.rage_stack = 1 + (self.rage_stack - 12)
            self.attack += 8
            self.defense += 4
            print(
                f'분노가 최대치를 초과해 아드레날린이 분비되었습니다!\n'
                f'atk가 8, def가 4 증가합니다! 현재 atk {self.attack}, def{self.defense}!\n'
            )

    # 해당 포켓몬의 기술 메서드를 설정한다. 3개
    def hydro_pump(self):
        skill_name = '하이드로펌프'
        power = self.attack + (2 * self.rage_stack)
        if 'fire' or 'earth' in self.legendary_pokemon.type:
            power *= 2
        elif 'grass' or 'ice' in self.legendary_pokemon.type:
            power *= 0.5
        self.attack_legendary(skill_name, power)
        self.rage_stack += 1
        self.Blastoise_rage()

    def water_pulse(self):
        self.current_hp += 8 + self.rage_stack
        self.rage_stack += 3
        skill_name = '물의 파동'
        print(
            f'{self.name}이 {skill_name}을 사용합니다.\n'
            f'체력이 {10+self.rage_stack}만큼 회복되고, 3 분노 스택을 얻습니다. \n'
            f'현재 체력 {self.current_hp}, 분노 {self.rage_stack}\n'
        )
        self.Blastoise_rage()

    def withdraw(self):
        buff_type = 'def'
        power = self.rage_stack / 2
        skill_name = '껍질에 숨기'
        self.buff_player(skill_name, buff_type, power)
        self.current_hp += (5 + self.rage_stack)
        self.rage_stack -= 2
        print(
            f'껍질에 숨어 힘을 회복하여 체력이 {10 + self.rage_stack}만큼 회복됩니다.\n'
            f'분노 1 하락! 현재 분노 {self.rage_stack}\n'
        )

    def skill_info(self):
        skill_docs = [
            '하이드로 펌프 - (1*attack) + (2*분노)의 데미지를 주고 분노를 1 올립니다.',
            '물의 파동 - 10+분노 스택만큼 체력을 회복하고 분노가 3 증가합니다.',
            '껍질에 숨기 - 자신의 def를 분노/2만큼 올리고 체력을 5+분노만큼 회복합니다. 대신 분노가 2 떨어집니다.'
        ]
        print('\n\n'.join([f'{index}:{skill}' for index, skill in enumerate(skill_docs, start=1)]))

    def Do_attack(self):
        self.skill_info()
        skill_list = [self.hydro_pump, self.water_pulse, self.withdraw]
        select_skill = input('사용할 스킬을 선택해주세요.')
        skill_list[int(select_skill) - 1]()

class Pikachu(Challenger):
 # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.level = 40
        self.max_hp = 134
        self.name = '피카츄'
        self.current_hp = self.max_hp
        self.type = 'electric'
        self.attack = 10
        self.defense = 2
        self.legendary_pokemon = 'no'
        self.ppp = 0




    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'피카츄({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            '상대의 atk를 낮추는 디버프를 거는 포켓몬입니다.'
        )


    def __str__(self):
        return self.name


    # 해당 포켓몬의 기술 메서드를 설정한다. 3개
    def thunderbolt(self):
        skill_name = '10만 볼트'
        power = self.attack + 12
        if 'water' or 'ice' in self.legendary_pokemon.type:
            power *= 2
        elif 'earth' in self.legendary_pokemon.type:
            power *= 0.5

        debuff_type = 'atk'
        debuff = 1
        self.attack_legendary(skill_name, power)
        self.debuff_legendary(skill_name, debuff_type, power)


    def thunder_wave(self):
        skill_name = "전기자석파"
        power = 2
        debuff_type = 'atk'
        self.debuff_legendary(skill_name, debuff_type, power)


    def nuzzle(self):
        if self.ppp < 2:
            debuff_type = 'atk'
            buff_type = 'atk'
            power = 3
            skill_name = '볼부비부비'
            self.debuff_legendary(skill_name, debuff_type, power)
            self.buff_player(skill_name, buff_type, power)
            self.current_hp += 25
            print('체력을 30 회복합니다.\n')
        else:
            print('이미 2회 스킬을 사용하셨습니다.\n')
            self.Do_attack()

    def skill_info(self):
        skill_docs = [
            '10만 볼트 - attack+12의 데미지를 주고 atk를 1 깎습니다.',
            '전기자석파 - atk를 2 깎습니다.',
            '볼부비부비 - 자신의 atk를 3만큼 올리고 체력을 25 회복하며, 상대의 atk는 3 떨어집니다. 2회 사용 가능합니다.'
        ]
        print('\n\n'.join([f'{index}:{skill}' for index, skill in enumerate(skill_docs, start=1)]))


    def Do_attack(self):
        self.skill_info
        skill_list = [self.thunderbolt, self.thunder_wave, self.nuzzle]
        select_skill = input('사용할 스킬을 선택해주세요.')
        skill_list[int(select_skill) - 1]()

class Electrode(Challenger):
   # 기본값 설정, 이름과 레벨, hp, 타입을 설정
    def __init__(self):
        self.level = 40
        self.max_hp = 160
        self.name = '붐볼'
        self.current_hp = self.max_hp
        self.type = 'electric'
        self.attack = 10
        self.legendary_pokemon = 'no'
        self.defense = 3


    # repr, str을 설정해 예쁘게 출력되도록 하자.
    def __repr__(self):
        return (
            f'붐볼({self.name})\n'
            f'HP : {self.max_hp}\n'
            f'Type : {self.type}\n'
            '포획확률을 극대화시키는 포켓몬입니다. 공격 능력은 부족합니다.'
        )


    def __str__(self):
        return self.name


    # 해당 포켓몬의 기술 메서드를 설정한다. 3개
    def electro_ball(self):
        skill_name = '일렉트릭 볼'
        power = self.attack
        if 'water' or 'ice' in self.legendary_pokemon.type:
            power *= 2
        elif 'earth' in self.legendary_pokemon.type:
            power *= 0.5

        self.attack_legendary(skill_name, power)
        self.legendary_pokemon.catcha += 3
        print(
            f'붐볼이 포획 계수를 3 높입니다! \n'
            f'현재 포획계수 {self.legendary_pokemon.catcha}!\n'
        )


    def magent_rise(self):
        skill_name = "전자부유"
        self.defense -= 2
        self.legendary_pokemon.catcha += 5
        print(
            f'붐볼이 포획 계수를 5 높입니다! 대신 방어력이 2만큼 감소합니다.\n'
            f'현재 포획계수 {self.legendary_pokemon.catcha}!\n'
        )


    def self_destruct(self):
        skill_name = '자폭'
        self.legendary_pokemon.catcha *= 2
        self.current_hp = 0
        print(
            f'붐볼이 포획 계수를 2배로 높입니다! ...그리고 붐볼은 장렬히 산화했습니다...\n'
            f'현재 포획계수 {self.legendary_pokemon.catcha}!\n'
        )


    def skill_info(self):
        skill_docs = [
            '일렉트릭 볼 - attack만큼 데미지를 주고 포획계수를 3 올립니다.',
            '전자부유 - 자신의 방어력을 2 깎고 포획계수를 5 올립니다.',
            '자폭 - 포획계수를 2배로 높이고 붐볼이 쓰러집니다.'
        ]
        print('\n\n'.join([f'{index}:{skill}' for index, skill in enumerate(skill_docs, start=1)]))


    def Do_attack(self):
        self.skill_info()
        skill_list = [self.electro_ball, self.magent_rise, self.self_destruct]
        select_skill = input('사용할 스킬을 선택해주세요.')
        skill_list[int(select_skill) - 1]()