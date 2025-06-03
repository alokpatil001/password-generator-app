from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Modern Calculator")
        master.geometry('370x480+500+150')
        master.config(bg='#2f3542')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_Value = ''


        Entry(master, width=15, bg='#dfe4ea', fg='black', font=('Helvetica', 28), 
              textvariable=self.equation, justify='right', bd=10, relief='sunken').place(x=10, y=20)


        btn_cfg = {'width': 8, 'height': 2, 'bg': '#57606f', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'bd': 0}
        op_cfg = {'width': 8, 'height': 2, 'bg': '#ff7f50', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'bd': 0}
        action_cfg = {'width': 8, 'height': 2, 'bg': '#1e90ff', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'bd': 0}


        Button(master, text='(', command=lambda: self.show('('), **btn_cfg).place(x=10, y=90)
        Button(master, text=')', command=lambda: self.show(')'), **btn_cfg).place(x=100, y=90)
        Button(master, text='%', command=lambda: self.show('%'), **btn_cfg).place(x=190, y=90)
        Button(master, text='C', command=self.clear, bg='#ff4757', fg='white', font=('Helvetica', 12, 'bold'), width=8, height=2, bd=0).place(x=280, y=90)


        Button(master, text='7', command=lambda: self.show(7), **btn_cfg).place(x=10, y=160)
        Button(master, text='8', command=lambda: self.show(8), **btn_cfg).place(x=100, y=160)
        Button(master, text='9', command=lambda: self.show(9), **btn_cfg).place(x=190, y=160)
        Button(master, text='/', command=lambda: self.show('/'), **op_cfg).place(x=280, y=160)


        Button(master, text='4', command=lambda: self.show(4), **btn_cfg).place(x=10, y=230)
        Button(master, text='5', command=lambda: self.show(5), **btn_cfg).place(x=100, y=230)
        Button(master, text='6', command=lambda: self.show(6), **btn_cfg).place(x=190, y=230)
        Button(master, text='x', command=lambda: self.show('*'), **op_cfg).place(x=280, y=230)


        Button(master, text='1', command=lambda: self.show(1), **btn_cfg).place(x=10, y=300)
        Button(master, text='2', command=lambda: self.show(2), **btn_cfg).place(x=100, y=300)
        Button(master, text='3', command=lambda: self.show(3), **btn_cfg).place(x=190, y=300)
        Button(master, text='-', command=lambda: self.show('-'), **op_cfg).place(x=280, y=300)


        Button(master, text='0', command=lambda: self.show(0), **btn_cfg).place(x=10, y=370)
        Button(master, text='.', command=lambda: self.show('.'), **btn_cfg).place(x=100, y=370)
        Button(master, text='=', command=self.solve, bg='#2ed573', fg='white', font=('Helvetica', 12, 'bold'), width=8, height=2, bd=0).place(x=190, y=370)
        Button(master, text='+', command=lambda: self.show('+'), **op_cfg).place(x=280, y=370)

    def show(self, value):
        self.entry_Value += str(value)
        self.equation.set(self.entry_Value)

    def clear(self):
        self.entry_Value = ''
        self.equation.set('')

    def solve(self):
        try:
            result = eval(self.entry_Value)
            self.equation.set(result)
            self.entry_Value = str(result)
        except:
            self.equation.set("Error")
            self.entry_Value = ''


root = Tk()
Calculator(root)
root.mainloop()
