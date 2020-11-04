"""program to plot graph of simple number line"""
import pygame, sys
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

root = Tk()
class Main:
    def __init__(self):
        root.title("INPUT")
        root.geometry('300x250')
        root.resizable (False, False)
        self.root = root
        self.Input()
        self.root.mainloop()

    def Input(self):
        showinfo("About and Help", "This program is to plot a simple number line graph for visualizing the inequalities of x, \nuse the combobox widget to select the particular symbol pertaining to the value range \nof 'x', i.e '>' for greater tha, '<' for less than, '<=' for less than or equal to and '>=' for greater than or equal to \nand then input the number (the object of x (the number range with respect to the symbol for the combobox)) \n then click submit in order to see the graph plotted. Made by: Praise James (www.github.com/Trojancipher/)")
        global  selected, Entry
        banner = Label(self.root, text = "INPUT THE STATEMENT", bg = "black", fg = "white").pack()
        x = Label(self.root, text = "X", fg = "green", font = ("Calibri", 20, "bold"))
        x.pack(pady = 16, padx = 10)
        inequality_symbol = StringVar()
        selected = ttk.Combobox(self.root, width = 9, textvariable = inequality_symbol, state = 'readonly')
        selected['values'] = ('<', '>', '<=', '>=')
        selected.pack(pady = 16, padx = 15)
        Entry = Spinbox(root, from_ = -2, to = 12, width  = 8, bd = 6)
        Entry.pack(pady = 16, padx = 25)
        Btn = Button(self.root, text = "SUBMIT", command = lambda: self.Submit()).pack()

        
    def Submit(self):
        self.draw()
        self.plot(Entry.get())
        root.destroy()

    def draw(self):
        global screen
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Numline plot')
        bg = pygame.image.load("abstract.jpg")
        screen.blit(bg, [0, 0])
        font = pygame.font.SysFont('Helvetica', 15)
        BLUE = (80, 80, 255)
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, (130, 360, 520, 58))
        X = 130
        for i in range(3):
            pygame.draw.circle(screen, WHITE, (X, 389), 30)
            X += 529
        pygame.draw.rect(screen, BLUE, (150, 380, 490, 8))
        x = 170
        n = -12
        x1 = 160
        for i in range(24):
            pygame.draw.rect(screen, BLUE, (x, 380, 2, 13))
            x += 20
        for i in range(3):
            screen.blit(font.render(str(n), True, BLUE), (x1, 390))
            n += 1
            x1 += 20
        N = -9
        x2 = 223
        for i in range(9):
            screen.blit(font.render(str(N), True, BLUE), (x2, 390))
            N += 1
            x2 += 20
        n_ = 0
        x3 = 407
        for i in range(12):
            screen.blit(font.render(str(n_), True, BLUE), (x3, 390))
            n_ += 1
            x3 += 20
        pygame.draw.rect(screen, BLUE, (410, 380, 2, 20))
        pygame.display.update()
        
    def plot(self, statement):
        RED = (255, 0, 0)
        dict_ = {-12: 160, -11: 180, -10: 200, -9:223, -8:243, -7:263, -6:283, -5:303, -4:326, -3:346, -2:366, -1:386, 0:407, 1:427, 2:447, 3:467, 4:487, 5:507, 6:527, 7:547, 8:567, 9:587, 10:607, 11:627, 12:647}
        _dict = range(-12, 12)
        num = int(statement)
        print(num)
        for i in _dict:
            if num == i:
                x = dict_[num]
                if selected.get() == ">=":
                    pygame.draw.circle(screen, RED, (x, 380), 7)
                    pygame.draw.line(screen, RED, (x, 380), (640, 380), 3)
                elif selected.get() == "<=":
                    pygame.draw.circle(screen, RED, (x, 380), 7)
                    pygame.draw.line(screen, RED, (150, 380), (x, 380), 3)
                elif selected.get() == "<":
                    pygame.draw.circle(screen, RED, (x, 380), 7, 1)
                    pygame.draw.line(screen, RED, (150, 380), (x, 380), 3)
                elif selected.get() == ">":
                    pygame.draw.circle(screen, RED, (x, 380), 7, 1)
                    pygame.draw.line(screen, RED, (x, 380), (640, 380), 3)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            pygame.display.update()

if __name__=='__main__':
    Main()
