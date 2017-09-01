from decimal import Decimal, ROUND_HALF_UP
from time import strftime
import tkinter as tk
import datetime



class TimeClockApp(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.hours_worked = 0.00
        self.dtlbl = tk.Label(self.master, text="Current Date-Time: {} ~ {}".format(datetime.date.today(),strftime("%H:%M:%S")))
        self.dtlbl.grid(row=0, column=0, columnspan=2)
        
        self.lbl1 = tk.Label(self.master, text="Hours worked").grid(row=1, column=0, columnspan=2)

        self.lbl2 = tk.Label(self.master, text="Monday: ", anchor = "e").grid(row=2, column=0, sticky="e")
        self.lbl3 = tk.Label(self.master, text="Tuesday: ", anchor = "e").grid(row=3, column=0, sticky="e")
        self.lbl4 = tk.Label(self.master, text="Wednesday: ", anchor = "e").grid(row=4, column=0, sticky="e")
        self.lbl5 = tk.Label(self.master, text="Thursday: ", anchor = "e").grid(row=5, column=0, sticky="e")
        self.lbl6 = tk.Label(self.master, text="Friday: ", anchor = "e").grid(row=6, column=0, sticky="e")
        
        self.lbl7 = tk.Label(self.master, text="Total Hours worked:").grid(row=7, column=0, sticky="e")
        self.lbl8 = tk.Label(self.master, text="00h 0m")
        self.lbl8.grid(row=7, column=1, sticky="w")
        
        self.lbl9 = tk.Label(self.master, text="Hours left to 40:").grid(row=8, column=0, sticky="e")
        self.lbl10 = tk.Label(self.master, text="40h 0m")
        self.lbl10.grid(row=8, column=1, sticky="w")
        
        self.entry1 = tk.Entry(self.master, width=7)
        self.entry1.grid(row=2, column=1, sticky="w")
        self.entry2 = tk.Entry(self.master, width=7)
        self.entry2.grid(row=3, column=1, sticky="w")
        self.entry3 = tk.Entry(self.master, width=7)
        self.entry3.grid(row=4, column=1, sticky="w")
        self.entry4 = tk.Entry(self.master, width=7)
        self.entry4.grid(row=5, column=1, sticky="w")
        self.entry5 = tk.Entry(self.master, width=7)
        self.entry5.grid(row=6, column=1, sticky="w")
        self.entry1.bind("<Key>", lambda x: self.master.after(500, self.hours_left_update))
        self.entry2.bind("<Key>", lambda x: self.master.after(500, self.hours_left_update))
        self.entry3.bind("<Key>", lambda x: self.master.after(500, self.hours_left_update))
        self.entry4.bind("<Key>", lambda x: self.master.after(500, self.hours_left_update))
        self.entry5.bind("<Key>", lambda x: self.master.after(500, self.hours_left_update))
        
        
        
        self.status_clock()
        
    def status_clock(self):
        self.dtlbl.config(text ="Current Date-Time: {} ~ {}".format(datetime.date.today(),strftime("%H:%M:%S")))
        self.dtlbl.after(200, lambda: self.status_clock())

    def hours_left_update(self):
        for entry in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5]:
            if entry != "":
                try:
                    #print(Decimal(entry.get()).quantize(Decimal("0.01"), ROUND_HALF_UP))
                    self.hours_worked += float(entry.get())
                except:
                    pass
        x = str(Decimal(str(self.hours_worked)).quantize(Decimal("0.01"), ROUND_HALF_UP)).split('.')
        m60 = "00"
        
        if int(x[1]) != 0:
            m60 = Decimal(str(60 * float("0.{}".format(x[1])))).quantize(Decimal("1"))

        self.lbl8.config(text="{}h {}m".format(x[0], m60))
        
        var = 40 - int(x[0])
        print(var)
        if int(x[1]) != 0:
            var = 39 - int(x[0])
            
        self.lbl10.config(text="{}h {}m".format(var,60 - Decimal(str(60 * float("0.{}".format(x[1])))).quantize(Decimal("1"))))
        
        
        
        self.hours_worked = 0.00


if __name__ == "__main__":
    root = tk.Tk()
    app = TimeClockApp(root)
    root.mainloop()
