#name 1)malhar mane 2)parth korat 3)hengxi liang
# ucinetid 1)mmane 2)pkorat 3)hengxil
'''This is the pygame view file which starst when the user selects
GUI 2.'''
class View:
    '''This class deals with the functions for pygame view.'''
    def __init__(self):
        '''We initiate with a list.'''
        self.list = ['%', 'CE', 'C', '<-', '÷', '√', '7', '8', '9', '×',
                     'x²', '4', '5', '6', '-', 'x³', '1', '2', '3', '+',
                     '1/x', '+/-', '0', '.', '=']

    def _create_window(self, pygame, size, current_number):
        '''A function that create window or refresh window.'''

        pygame.display.set_mode(size, pygame.RESIZABLE)
        # Create a pygame window with given size

        surface_1 = pygame.display.get_surface()
        surface_1.fill((211, 211, 211))
        # fill the window to color gray

        self._create_buttons(pygame)
        self._current_number(pygame, current_number)
        # run the function to create button and number display

        pygame.display.flip()
        # save the window

    def _create_buttons(self, pygame):
        '''A function that create line and text on the pygame window.'''
        surface_1 = pygame.display.get_surface()
        width = surface_1.get_width()
        height = surface_1.get_height()
        # Getting the window size

        button_width = width / 5
        button_height = height / 6
        # Calculate the button size base on the window size

        # Creating white line on the window
        pygame.draw.line(surface_1, (255, 255, 255),
                         (button_width, button_height),
                         (button_width, height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (2 * button_width, button_height),
                         (2 * button_width, height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (3 * button_width, button_height),
                         (3 * button_width, height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (4 * button_width, button_height),
                         (4 * button_width, height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (0, button_height), (width, button_height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (0, 2 * button_height),
                         (width, 2 * button_height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (0, 3 * button_height),
                         (width, 3 * button_height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (0, 4 * button_height),
                         (width, 4 * button_height))
        pygame.draw.line(surface_1, (255, 255, 255),
                         (0, 5 * button_height),
                         (width, 5 * button_height))

        column = 0

        for i in range(len(self.list)):
            # display all text of each button on the correct place
            if i % 5 == 0:
                column += 1

            font = pygame.font.SysFont(None, 48)
            text = font.render(self.list[i], True, (0, 0, 0))
            # set the font and text for each button placement

            textrect = text.get_rect()
            textrect.center = ((i % 5) * button_width + button_width / 2,
                               column * button_height + (button_height / 2))
            # get the position of each button text

            surface_1.blit(text, textrect)
            # place the text at the position

    def _current_number(self, pygame, current_number):
        '''A function display the current_number on the top of the window.'''
        surface = pygame.display.get_surface()
        width = surface.get_width()
        height = surface.get_height()
        # getting the width of the window

        font = pygame.font.SysFont(None, 48)
        text = font.render(current_number, True, (0, 0, 0))
        # set the font and text of the text

        text_rect = text.get_rect()
        text_rect.center = (0, height / 12)
        text_rect.right = width - 10
        # get the position of the text

        surface.blit(text, text_rect)
        # place the text at the position

