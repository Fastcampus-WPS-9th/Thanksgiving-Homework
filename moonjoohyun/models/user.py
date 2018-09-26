class User:
    def __init__(self, name):
        self.name = name
        self.probability = 0
        self.equip_sword = None
        self.sword_list = []
        
    @property
    def show_sword_list(self):
        return '소유목록\n{item}'.format(
            item = ' '.join([f'{index}. {sword.name}' for index, sword in enumerate(self.sword_list, start=1)])
            )
        
    def buy_sword(self, sword):
        self.sword_list.append(sword)
        if self.equip_sword == None:
            self.equip_sword = sword
            
    def equiped(self):
        print('장비할 아이템 선택')
        print(show_sword_list)
        self.equip_sword = sword_list[0]
