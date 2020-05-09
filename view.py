#name 1)malhar mane 2)parth korat 3)hengxi liang
# ucinetid 1)mmane 2)pkorat 3)hengxil
'''This module deals with tkinter view.'''
from tkinter import *
import math


class View:
    '''this class deals with the tkinter view functions.'''
    def __init__(self):
        '''We initiate with a list.'''
        x = []

    def manual(self):
        '''This creates the windiow with all buttons.'''
        self.window = Tk()
        self.display = ''
        self.num = StringVar()
        
        self.display_num = Entry(self.window, textvariable = self.num, font=('Verdana',25))
        self.display_num.grid(columnspan=5, ipadx = 90, sticky=N+S+E+W)
        Grid.columnconfigure(self.window, 0, weight=1)
        # we create all buttons
        button_percentage = self.create_button('%', 1, 0)
        button_CE = self.create_button('CE', 1, 1)
        button_C = self.create_button('C', 1, 2)
        button_back = self.create_button('<-', 1, 3)
        button_divide = self.create_button('/', 1, 4)

        button_squ_root = self.create_button('√', 2, 0)
        button_7 = self.create_button('7', 2, 1)
        button_8 = self.create_button('8', 2, 2)
        button_9 = self.create_button('9', 2, 3)
        button_multiple = self.create_button('*', 2, 4)

        button_squ = self.create_button('x²', 3, 0)
        button_4 = self.create_button('4', 3, 1)
        button_5 = self.create_button('5', 3, 2)
        button_6 = self.create_button('6', 3, 3)
        button_subtract = self.create_button('-', 3, 4)

        button_cube = self.create_button('x³', 4, 0)
        button_1 = self.create_button('1', 4, 1)
        button_2 = self.create_button('2', 4, 2)
        button_3 = self.create_button('3', 4, 3)
        button_add = self.create_button('+', 4, 4)

        button_half = self.create_button('1/x', 5, 0)
        button_negative = self.create_button('+/-', 5, 1)
        button_0 = self.create_button('0', 5, 2)
        button_dot = self.create_button('.', 5, 3)
        button_equal = self.create_button('=', 5, 4)

    def create_button(self, text, row, col):
        '''
        creates a button type that can be used for in the calculator
        '''
        button = Button(self.window, text=text, height=3, width=9, font=('Verdana',13), 
                        command= lambda: self.create_command(text))
        return button.grid(row=row, column=col, sticky=N+S+E+W)

    def create_command(self, text):
        '''
        creates the commands that are used for each operator
        '''
        operators = ['1','2','3','4','5','6','7','8','9','0',
                     '+', '-', '/', '*']
        # we manage all commands here
        if text in operators:
            self.display = self.display + str(text)
            self.num.set(self.display)
        elif text == '=':
            try:
                self.display = str(eval(self.display))
                self.num.set(self.display)
            except:
                self.num.set('Error')
                self.display = ''
        elif text == 'C':
            self.display = ''
            self.num.set(self.display)
        elif text == '<-':
            self.display = self.display[:-1]
            self.num.set(self.display)
        elif text == '√':
            self.display = str(math.sqrt(float(self.display)))
            self.num.set(self.display)
        elif text == '1/x':
            self.display = str(1/float(self.display))
            self.num.set(self.display)
        elif text == '+/-':
            self.display = str(-(float(self.display)))
            self.num.set(self.display)
        elif text == 'x²':
            self.display = str(float(self.display)*float(self.display))
            self.num.set(self.display)
        elif text == 'x³':
            self.display = str(float(self.display)*float(self.display))
            self.display = str(float(self.display)*float(self.display))
            self.num.set(self.display)
        elif text == 'CE':
            self.display = ''
            self.num.set(self.display)
        elif text == '%':
            self.display = str(float(self.display)/100)
            self.num.set(self.display)

    def open_window(self):
        '''
        keeps the window running
        '''
        # This deals with window expansion
        for column in range(5):
            Grid.columnconfigure(self.window, column, weight=1)
        for row in range(6):
            Grid.rowconfigure(self.window, row, weight=1)

        self.window.mainloop()

    def selection(self):
        '''We select the Gui window here.'''
        self.sel = Tk()
        button1 = Button(self.sel, text='GUI1', command = self.GUI1)
        button1.pack()
        button2 = Button(self.sel, text='GUI2', command = self.GUI2)
        button2.pack()
        self.sel.mainloop()

    def GUI1(self):
        # For gui 1 
        self.work = 0
        self.sel.destroy()

    def GUI2(self):
        # for gui 2
        self.work = 1
        self.sel.destroy()
        


