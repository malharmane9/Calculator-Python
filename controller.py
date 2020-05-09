import view
import View_pygame

class Control:
    def __init__(self):
        self.x = view.View()
        self.y = View_pygame.View()

    def run(self):
        self.x.selection()
        if self.x.work == 0:
            self.x.manual()
            self.x.open_window()
        elif self.x.work == 1:
            self.y.run()

if __name__ == '__main__':
    x = Control()
    x.run()
