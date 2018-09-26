from .sword import Sword

class Shop:
    def __init__(self):
        self.item_list = ['나무목검', '박달나무목검', '숏소드', '롱소드', '레이피어', '싸울아비장검']
    
    @property
    def show_item_list(self):
        return '{item}'.format(
            item = ' '.join([f'{index}. {item}' for index, item in enumerate(self.item_list, start=1)])
            )
    
    def sell_item(self, item_number):
        sword = Sword(self.item_list[int(item_number)-1])
        return sword
