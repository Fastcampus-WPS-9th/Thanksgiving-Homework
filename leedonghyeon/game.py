import curses
import random
import pickle

max_width = 40
max_height = 20

class Body():
    def __init__(self, position, shape):
        self._position = position
        self._shape = shape
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def shape(self):
        return self._shape

class Apple():
    def __init__(self, window):
        self._window = window
        self._position = (0, 0)
    
    def create(self):
        x = random.randint(2, max_width - 2)
        y = random.randint(2, max_height - 2)

        self._position = (x, y)

    def draw(self):
        x = self._position[0]
        y = self._position[1]
        self._window.addstr(y, x, '@')

    @property
    def position(self):
        return self._position

class Snake():
    def __init__(self, position, window):
        self._position = position
        self._length = 5
        self._window = window
        self._direction = curses.KEY_RIGHT
        self._opposition_dir_map = {
            curses.KEY_RIGHT:curses.KEY_LEFT,
            curses.KEY_LEFT:curses.KEY_RIGHT,
            curses.KEY_DOWN:curses.KEY_UP,
            curses.KEY_UP:curses.KEY_DOWN
        }
        self._score = 0

        x = self._position[0] + 1
        y = self._position[1]

        self._body_list = [Body((x - i, y), '#') for i in range(self._length, 1, -1)]
        self._body_list.append(Body(self._position, 'O'))


    def move(self):
        new_body = self._body_list.pop(0)
        new_body.position = self._position
        self._body_list.insert(-1, new_body)

        if self._direction == curses.KEY_RIGHT:
            self._position = (self._position[0] + 1, self._position[1])
        if self._direction == curses.KEY_LEFT:
            self._position = (self._position[0] - 1, self._position[1])
        if self._direction == curses.KEY_UP:
            self._position = (self._position[0], self._position[1] - 1)
        if self._direction == curses.KEY_DOWN:
            self._position = (self._position[0], self._position[1] + 1)

        self._body_list[-1].position = self._position
    
    def change_dircetion(self, direction):
        if self._direction != direction and direction != self._opposition_dir_map[self._direction]:
            self._direction = direction
    
    def add_body(self):
        new_body = Body(self._body_list[0].position, '#')
        self._body_list.insert(0, new_body)

    def eat(self, apple: Apple):
            self._score += 1
            self.add_body()
            apple.create()

    def draw(self):
        for i in self._body_list:
            x = i.position[0]
            y = i.position[1]
            self._window.addstr(y, x, i.shape)
    
    def check_collision(self):
        x = self._position[0]
        y = self._position[1]

        if x <= 0 or x >= max_width - 1 or y <= 0 or y >= max_height - 1:
            return -1

        for i in self._body_list[:-1]:
            if i.position == self._position:
                return -1
    
    @property
    def position(self):
        return self._position

    @property
    def score(self):
        return self._score
        
class Ui:
    def __init__(self, ui, position, window, data = 0):
        self._ui = ui
        self._window = window
        self._position = position
        self._data = data
    
    def draw(self):
        self._window.addstr(self._position[1], self._position[0], self._ui)

    def draw_data(self):
        self.draw()
        for i in range(0, len(self._data)):
            self._window.addstr(self._position[1] + i + 1, self._position[0], str(self._data[i]))

    @property
    def ui(self):
        return self._ui

    @ui.setter
    def ui(self, ui):
        self._ui = ui

user_id = input('Player NickName: ')

curses.initscr()
curses.curs_set(0)

def loading(height, width):
    window = curses.newwin(height, max_width, 0, 0)
    window.timeout(150) # frame
    window.keypad(1)
    return window

window = 0
player = Snake((7, 5), window)
apple = Apple(window)
scene = 0

window = loading(3, max_width)
key_move_event = [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT]


title_str = '[1]Start [2]Ranking [3]Exit'
title_ui = Ui(title_str, (2,1), window)

ranking_str = ''
ranking_ui = Ui(ranking_str, (2,1), window)




while True:
    event = window.getch()

    window.clear()
    window.border()

    #title scene
    if scene == 0:
        title_ui.draw()

        # scene change
        if event == 49: # game loading    
            window.erase()
            window.refresh()
            window = loading(max_height, max_width)
            player = Snake((7, 5), window)
            apple = Apple(window)
            apple.create()

            scene = 1
        elif event == 50: # ranking loading
            window.erase()
            window.refresh()
            window = loading(15, max_width)

            line = {}

            try:
                with open('ranking.txt', 'rb') as f:
                    line = pickle.load(f)
            except Exception:
                pass

            ranking_str = '[AnyKey] title\n'
            

            ranking_ui = Ui(ranking_str, (2,1), window, list(line.items()))

            scene = 2
        elif event == 51: # exit
            break

    # game scene
    elif scene == 1:
        if event in key_move_event:
            player.change_dircetion(event)

        player.move()
        
        if player.position == apple.position: player.eat(apple)
        
                
        apple.draw()
        player.draw()

        # GameOver
        if player.check_collision() == -1:
            line = {}

            try:
                with open('ranking.txt', 'rb') as f:
                    line = pickle.load(f)
            except Exception:
                pass

            line[user_id] = player.score
            line = sorted(line.items() , key = lambda kv: kv[1], reverse = True)
            if len(line) > 10: line.pop()

            f = open('ranking.txt', 'wb')

            pickle.dump(dict(line), f)

            f.close()
            
            scene = 0
            player = 0
            apple = 0

            window.erase()
            window.refresh()
            window = loading(3, max_width)
            title_ui = Ui(title_str, (2,1), window)

    #ranking scene
    elif scene == 2:
        ranking_ui.draw_data()
        if event != -1:
            scene = 0
            window.erase()
            window.refresh()
            window = loading(3, max_width)
            title_ui = Ui(title_str, (2,1), window)

curses.endwin()
