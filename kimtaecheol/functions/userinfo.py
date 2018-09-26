class UserInfo:
    level = 1
    money = 1000

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @property
    def show_info(self):
        return '캐릭터명: {}\n레    벨: {}\n페    나: {:,}\n============'.format(self.name, UserInfo.level, UserInfo.money)
