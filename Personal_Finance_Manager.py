import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Finance_Manager:
    def __init__(self,App):
        self.app=App

    def add_expense(self,master,E1,E2,E3,L4):
        des=E1.get()
        amount=E2.get()
        date=E3.get()
        if (des and amount and date):
            with open("expenses.txt", "a") as file:
                file.write(f"{des}|{amount}|{date}\n")

            E1.delete(0, tk.END)
            E2.delete(0, tk.END)
            E3.delete(0, tk.END)
            L4.configure(text="",bg="green")
            messagebox.showinfo('Success', 'Expense Added Successfully')
            master.destroy()
        else:
            L4.configure(text="Invalid Data", bg="red")
            L4.grid(row=4,column=1,padx=20)
        
    def set_budget(self, master,E1,E2,L3):
        cat=E1.get()
        amount=E2.get()
        if (cat and amount):
            with open("budgets.txt", "a") as file:
                file.write(f"{cat}|{amount}\n")
                
            L3.configure(bg="orange",text="")
            messagebox.showinfo('Success', 'Budget Set Successfully')
            master.destroy()
        else:
            L3.configure(text="Invalid Data",bg="red")
            L3.grid(row=4,column=1,padx=20)
     

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")
        self.root.geometry("600x500")
        self.root.config(bg='black')

        title = tk.Message(self.root, text="Personal Finance Manager", relief="raised", width=400,
                           padx=400, pady=0, fg="gray", bg="blue3", justify="center",
                           anchor="center", font=("Verdana", "25", "bold"))
        title.pack(side="top")
        
        self.b1 = tk.Button(self.root, text="Add Expenses", bg="green", activebackground="green",width=15,
                            command=self.add_expense_menu)
        self.b1.place(x=50,y=180)
        self.b2 = tk.Button(self.root, text="Set Budget", bg="orange", activebackground="orange",width=15,
                            command=self.set_budget_menu)
        self.b2.place(x=255,y=180)
        self.b3 = tk.Button(self.root, text="View Expenses", bg="yellow", activebackground="yellow",width=15,
                            command=self.view_expenses_menu)
        self.b3.place(x=455,y=180)
        self.b4 = tk.Button(self.root, text="View Budget", bg="blue", activebackground="blue",width=15,
                            command=self.view_budgets_menu)
        self.b4.place(x=130,y=320)
        self.b5 = tk.Button(self.root, text="Generate Expense Chart", bg="gray", activebackground="gray",width=20,
                            command=self.generate_expense_chart)
        self.b5.place(x=380,y=320)
        self.b6 = tk.Button(self.root, text="Exit", bg="red", activebackground="red",width=8,
                            command=self.root.destroy)
        self.b6.place(x=275,y=430)
        self.main_menu()
        self.Finance=Finance_Manager(self)
        

    def main_menu(self):
        def button_enter(event, bg_color, active_bg_color):
            event.widget.config(bg=active_bg_color, fg="white")

        def button_leave(event, bg_color, active_bg_color):
            event.widget.config(bg=bg_color, fg='black')

        self.b1.bind("<Enter>", lambda event, bg="green3", active_bg="green3": button_enter(event, bg, active_bg))
        self.b1.bind("<Leave>", lambda event, bg="green", active_bg="green3": button_leave(event, bg, active_bg))

        self.b2.bind("<Enter>", lambda event, bg="orang3", active_bg="orange3": button_enter(event, bg, active_bg))
        self.b2.bind("<Leave>", lambda event, bg="orange", active_bg="orange3": button_leave(event, bg, active_bg))

        self.b3.bind("<Enter>", lambda event, bg="yellow3", active_bg="yellow3": button_enter(event, bg, active_bg))
        self.b3.bind("<Leave>", lambda event, bg="yellow", active_bg="yellow3": button_leave(event, bg, active_bg))

        self.b4.bind("<Enter>", lambda event, bg="blue3", active_bg="blue3": button_enter(event, bg, active_bg))
        self.b4.bind("<Leave>", lambda event, bg="blue", active_bg="blue3": button_leave(event, bg, active_bg))

        self.b5.bind("<Enter>", lambda event, bg="gray3", active_bg="gray3": button_enter(event, bg, active_bg))
        self.b5.bind("<Leave>", lambda event, bg="gray", active_bg="gray3": button_leave(event, bg, active_bg))

        self.b6.bind("<Enter>", lambda event, bg="red3", active_bg="red3": button_enter(event, bg, active_bg))
        self.b6.bind("<Leave>", lambda event, bg="red", active_bg="red3": button_leave(event, bg, active_bg))

    def add_expense_menu(self):
        wn=tk.Tk()
        wn.title("Add Expense")
        wn.configure(bg="green")
        wn.geometry("280x180")

        L1=tk.Label(wn,text="Description: ")
        E1=tk.Entry(wn)
        L2=tk.Label(wn,text="Amount:")
        E2=tk.Entry(wn)
        L3=tk.Label(wn,text="Date: YYYY-MM-DD")
        E3=tk.Entry(wn)
        
        L4=tk.Label(wn)

        L1.grid(row=0,column=0,padx=10,pady=13)
        E1.grid(row=0,column=1)
        L2.grid(row=1,column=0,padx=13)
        E2.grid(row=1,column=1)
        L3.grid(row=2,column=0,padx=10,pady=13)
        E3.grid(row=2,column=1)

        B = tk.Button(wn, text="Add Expense", command=lambda: self.Finance.add_expense(wn,E1,E2,E3,L4))
        B.grid(row=3,column=1,padx=20)


    def set_budget_menu(self):
        wn=tk.Tk()
        wn.title("Set Budget")
        wn.configure(bg="orange")
        wn.geometry("230x130")

        L1=tk.Label(wn,text="Category: ")
        E1=tk.Entry(wn)
        L2=tk.Label(wn,text="Amount:")
        E2=tk.Entry(wn)

        L3=tk.Label(wn)

        L1.grid(row=0,column=0,padx=10,pady=13)
        E1.grid(row=0,column=1)
        L2.grid(row=1,column=0,padx=13)
        E2.grid(row=1,column=1)

        B = tk.Button(wn, text="Add Expense", command=lambda: self.Finance.set_budget(wn,E1,E2,L3))
        B.grid(row=3,column=1,padx=20)


    def view_expenses_menu(self):
        wn = tk.Tk()
        wn.title("Expenses")
        wn.geometry("350x350")
        wn.configure(bg="yellow")

        title = tk.Message(wn, text="Expenses", relief="raised", width=150,
                           padx=100, pady=0, fg="gray", bg="blue3", justify="center",
                           anchor="center", font=("Verdana", "19", "bold"))
        title.pack(side="top")

        # Create a scrolled text widget
        text_widget = scrolledtext.ScrolledText(wn, wrap=tk.WORD, width=35, height=10)
        text_widget.pack(pady=10)

        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    x, y, z = line.strip().split("|")
                    text_widget.insert(tk.END, f"  {z}: {x} ₹{y}\n\n")
                    
        except FileNotFoundError:
            pass
        b=tk.Button(wn,text="Close",command=lambda:wn.destroy())
        b.pack()

    def view_budgets_menu(self):
        wn = tk.Tk()
        wn.title("Budgets")
        wn.geometry("350x350")
        wn.configure(bg="yellow")

        title = tk.Message(wn, text="Budgets", relief="raised", width=150,
                           padx=100, pady=0, fg="gray", bg="blue3", justify="center",
                           anchor="center", font=("Verdana", "19", "bold"))
        title.pack(side="top")

        # Create a scrolled text widget
        text_widget = scrolledtext.ScrolledText(wn, wrap=tk.WORD, width=35, height=10)
        text_widget.pack(pady=10)

        try:
            with open("budgets.txt", "r") as file:
                for line in file:
                    x, y= line.strip().split("|")
                    text_widget.insert(tk.END, f"  {x} Budget: ₹{y}\n\n")


        except FileNotFoundError:
            pass
        b=tk.Button(wn,text="Close",command=lambda:wn.destroy())
        b.pack()

    def generate_expense_chart(self):
        chart_window = tk.Tk()
        chart_window.title("Expense Distribution Chart")
        chart_window.geometry("500x500")

        categories = {}
        
        with open('expenses.txt', 'r') as f:
            for line in f:
                des, amt, date = line.strip().split("|")
                if des in categories:
                    categories[des] += float(amt)
                else:
                    categories[des] = float(amt)

        # Create a list of categories and corresponding amounts
        category_labels = list(categories.keys())
        category_amounts = list(categories.values())

        
        # Create a Matplotlib figure
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(category_amounts, labels=category_labels, autopct='%1.1f%%', startangle=140)
        ax.set_title("Expense Distribution by Category")
        
        # Embed the Matplotlib figure in the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.get_tk_widget().pack()
        
        chart_window.protocol("WM_DELETE_WINDOW",lambda:self.close_chart_window(chart_window))

    def close_chart_window(self,master):
        plt.close()
        master.destroy()

if __name__ == "__main__":
    root=tk.Tk()
    app=App(root)
    root.mainloop()
