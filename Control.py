#name 1)malhar mane 2)parth korat 3)hengxi liang
# ucinetid 1)mmane 2)pkorat 3)hengxil
'''This is the ocntrol model and it acts as a communicator
between view and model.'''
import View_pygame
import Model
import pygame
import view


class control:
    '''The control class in an intermediary between view and model.'''
    def __init__(self):
        '''We initiate and set variables to call different modules.'''
        self.pygame = pygame
        self.x = view.View()
        self.view = View_pygame.View()
        self.model = Model.Model()
        self.running = True

    def selection(self):
        '''This method checks if the user wants the gui 1 or gui 2.'''
        self.x.selection()
        # If the user selects Gui 1, the tkinter view is initiated
        if self.x.work == 0:
            self.x.manual()
            self.x.open_window()
        # If the user selects gui 2, the pygame view is initiated
        elif self.x.work == 1:
            self.run()
        

    def run(self):
        '''The Function to star the whole program.'''
        self.pygame.init()

        self.view._create_window(self.pygame,
                                 (600, 600),
                                 self.model.current_number)

        while self.running:
            self.event()

        self.pygame.quit()

    def event(self):
        '''Function handel user action.'''
        surface = pygame.display.get_surface()

        width = surface.get_width()
        height = surface.get_height()
        # get the winodow size

        for event in self.pygame.event.get():
            if event.type == pygame.QUIT:
                # for event when user quit
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                # for even when user change window size
                self.view._create_window(self.pygame,
                                         event.size,
                                         self.model.current_number)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # for even when user interact with buttons
                self.model._command(self.model._mouse_action(event.pos, self.pygame))

                self.view._create_window(self.pygame, (width, height), self.model.current_number)
                # refresh the window


if __name__ == '__main__':
    '''We run the control to run everything.'''
    x = control()
    x.selection()
