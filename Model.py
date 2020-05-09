#name 1)malhar mane 2)parth korat 3)hengxi liang
# ucinetid 1)mmane 2)pkorat 3)hengxil
'''This is the model and is the back bone of the program. It does all the
calculations.'''
class Model:
    '''This model class has methods that deal with the calculations.'''
    def __init__(self):
        '''We initiate some variables that will be used throughout
        the program.'''
        self.list = ['%', 'CE', 'C', '<-', '÷', '√', '7', '8', '9', '×',
                     'x²', '4', '5', '6', '-', 'x³', '1', '2', '3', '+',
                     '1/x', '+/-', '0', '.', '=']
        self.current_number = '0'
        self.storage_number = '0'
        self.current_operation = None

    def _mouse_action(self, pos, pygame):
        """Function to check if use using a button."""
        surface = pygame.display.get_surface()

        width = surface.get_width()
        height = surface.get_height()
        # get window size

        button_width = width / 5
        button_height = height / 6
        # calculate button size

        pixel_x, pixel_y = pos
        # get user interact position

        # check which button that user interact
        # all the conditional statements deal with what the user selects
        # on the screen. There are 25 buttons and hence that many conditional
        # statements
        if 0 < pixel_x < button_width and\
                button_height < pixel_y < 2 * button_height:
            return self.list[0]
        elif button_width < pixel_x < 2 * button_width and\
                button_height < pixel_y < 2 * button_height:
            return self.list[1]
        elif 2 * button_width < pixel_x < 3 * button_width and\
                button_height < pixel_y < 2 * button_height:
            return self.list[2]
        elif 3 * button_width < pixel_x < 4 * button_width and\
                button_height < pixel_y < 2 * button_height:
            return self.list[3]
        elif 4 * button_width < pixel_x < 5 * button_width and\
                button_height < pixel_y < 2 * button_height:
            return self.list[4]
        elif 0 < pixel_x < button_width and\
                2 * button_height < pixel_y < 3 * button_height:
            return self.list[5]
        elif button_width < pixel_x < 2 * button_width and\
                2 * button_height < pixel_y < 3 * button_height:
            return self.list[6]
        elif 2 * button_width < pixel_x < 3 * button_width and\
                2 * button_height < pixel_y < 3 * button_height:
            return self.list[7]
        elif 3 * button_width < pixel_x < 4 * button_width and\
                2 * button_height < pixel_y < 3 * button_height:
            return self.list[8]
        elif 4 * button_width < pixel_x < 5 * button_width and\
                2 * button_height < pixel_y < 3 * button_height:
            return self.list[9]
        elif 0 < pixel_x < button_width and\
                3 * button_height < pixel_y < 4 * button_height:
            return self.list[10]
        elif button_width < pixel_x < 2 * button_width and\
                3 * button_height < pixel_y < 4 * button_height:
            return self.list[11]
        elif 2 * button_width < pixel_x < 3 * button_width and\
                3 * button_height < pixel_y < 4 * button_height:
            return self.list[12]
        elif 3 * button_width < pixel_x < 4 * button_width and\
                3 * button_height < pixel_y < 4 * button_height:
            return self.list[13]
        elif 4 * button_width < pixel_x < 5 * button_width and\
                3 * button_height < pixel_y < 4 * button_height:
            return self.list[14]
        elif 0 < pixel_x < button_width and\
                4 * button_height < pixel_y < 5 * button_height:
            return self.list[15]
        elif button_width < pixel_x < 2 * button_width and\
                4 * button_height < pixel_y < 5 * button_height:
            return self.list[16]
        elif 2 * button_width < pixel_x < 3 * button_width and\
                4 * button_height < pixel_y < 5 * button_height:
            return self.list[17]
        elif 3 * button_width < pixel_x < 4 * button_width and\
                4 * button_height < pixel_y < 5 * button_height:
            return self.list[18]
        elif 4 * button_width < pixel_x < 5 * button_width and\
                4 * button_height < pixel_y < 5 * button_height:
            return self.list[19]
        elif 0 < pixel_x < button_width and\
                5 * button_height < pixel_y < 6 * button_height:
            return self.list[20]
        elif button_width < pixel_x < 2 * button_width and\
                5 * button_height < pixel_y < 6 * button_height:
            return self.list[21]
        elif 2 * button_width < pixel_x < 3 * button_width and\
                5 * button_height < pixel_y < 6 * button_height:
            return self.list[22]
        elif 3 * button_width < pixel_x < 4 * button_width and\
                5 * button_height < pixel_y < 6 * button_height:
            return self.list[23]
        elif 4 * button_width < pixel_x < 5 * button_width and\
                5 * button_height < pixel_y < 6 * button_height:
            return self.list[24]

    def _command(self, text):
        """Fucntion that run the command of each button with button name."""
        # function for each button
        if text == self.list[0]:
            # button %
            self.current_number = str(float(self.current_number) / 100)
        elif text == self.list[1]:
            # button CE
            self.current_number = '0'
            self.storage_number = '0'
            self.current_operation = None
        elif text == self.list[2]:
            # button C
            self.current_number = '0'
        elif text == self.list[3]:
            # button <-
            self.current_number = self.current_number[:-1]
            if self.current_number == '':
                self.current_number = '0'
        elif text == self.list[4]:
            # button ÷
            self._command_operation(self.list[4])
        elif text == self.list[5]:
            # button √
            self.current_number = str(float(self.current_number)**(1/2))
        elif text == self.list[6]:
            # button 7
            self._command_number(self.list[6])
        elif text == self.list[7]:
            # button 8
            self._command_number(self.list[7])
        elif text == self.list[8]:
            # button 9
            self._command_number(self.list[8])
        elif text == self.list[9]:
            # button ×
            self._command_operation(self.list[9])
        elif text == self.list[10]:
            # button  x²
            self.current_number = str(float(self.current_number)**2)
        elif text == self.list[11]:
            # button 4
            self._command_number(self.list[11])
        elif text == self.list[12]:
            # button 5
            self._command_number(self.list[12])
        elif text == self.list[13]:
            # button 6
            self._command_number(self.list[13])
        elif text == self.list[14]:
            # button +
            self._command_operation(self.list[14])
        elif text == self.list[15]:
            # button x³
            self.current_number = str(float(self.current_number)**3)
        elif text == self.list[16]:
            # button 1
            self._command_number(self.list[16])
        elif text == self.list[17]:
            # button 2
            self._command_number(self.list[17])
        elif text == self.list[18]:
            # button 3
            self._command_number(self.list[18])
        elif text == self.list[19]:
            # button -
            self._command_operation(self.list[19])
        elif text == self.list[20]:
            # button 1/x
            self.current_number = str(1 / float(self.current_number))
        elif text == self.list[21]:
            # button +/-
            if self.current_number[0] == '-':
                self.current_number = self.current_number[1:]
            else:
                self.current_number = '-' + self.current_number
        elif text == self.list[22]:
            # button 0
            self._command_number(self.list[22])
        elif text == self.list[23]:
            # button .
            self._command_number(self.list[23])
        elif text == self.list[24]:
            # button =
            self._command_equal()


    def _command_number(self, number):
        """Function for all number button"""
        if number == '.':
            # check if the number is a float
            if '.' in self.current_number:
                return
            self.current_number = self.current_number + number
        elif self.current_number == '0':
            # check if the number is 0
            # if it is, replace it
            self.current_number = number
        else:
            # else we add number after the current number
            self.current_number = self.current_number + number

    def _command_operation(self, operation):
        """Function for all operations"""
        if self.current_number != '0' and\
                (self.current_operation is not None) and\
                self.storage_number != '0':
            # check if user already selected a operation
            # if it is, do the equal function once and display
            # the resolve
            self._command_equal()
            self.current_operation = operation
        else:
            # else storage the operation
            self.storage_number = self.current_number
            self.current_operation = operation
            self.current_number = '0'

    def _command_equal(self):
        """Function for equal button."""
        if self.current_operation is None:
            # check if user selected a operation
            return
        elif self.current_operation == self.list[4]:
            # check operation if is ÷
            self.current_number = str(
                float(self.storage_number) /
                float(self.current_number))
        elif self.current_operation == self.list[9]:
            # check operation if is ×
            self.current_number = str(
                float(self.storage_number) *
                float(self.current_number))
        elif self.current_operation == self.list[14]:
            # check operation if is -
            self.current_number = str(
                float(self.storage_number) -
                float(self.current_number))
        elif self.current_operation == self.list[19]:
            # check operation if is +
            self.current_number = str(
                float(self.storage_number) +
                float(self.current_number))

        self.current_operation = None
        # reset the storage of operation
