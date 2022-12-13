import tkinter as tk
from tkinter import *
import math

b_to_a_stones = 765000
a_to_s_stones = 4356000
s_to_sr_stones = 14586000
sr_to_ssr_stones = 75150000
#b_to_a_level = 300
#a_to_s_level = 720
#s_to_sr_level = 1320
b_max_level = 50
a_max_level = 120
s_max_level = 220
sr_max_level = 500

class App:
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.rank_value = tk.IntVar(self.master, 0)
        self.reward_value = tk.IntVar(self.master, 0)
        self.stones_value = tk.IntVar(self.master, 0)
        self.atk_value = tk.IntVar(self.master, 0)
        self.skill_value = tk.IntVar(self.master, 0)
        self.boss_value = tk.IntVar(self.master, 0)
        self.bskatk_value = tk.IntVar(self.master, 0)
        self.hlth_value = tk.IntVar(self.master, 0)
        self.bskcrt_value = tk.IntVar(self.master, 0)

        self.as_label = tk.Label(root, text="Awakening Stone Reward:", padx=3, pady=3)
        self.as_label.grid(column=1,row=1,sticky=tk.W)
        self.as_entry = tk.Entry(root, textvariable=self.reward_value, width=6)
        self.as_entry.grid(column=2,row=1,sticky=tk.W)

        self.currentstones_label = tk.Label(root, text="Current Number of Stones:", padx=3, pady=3)
        self.currentstones_label.grid(column=1,row=2,sticky=tk.W)
        self.currentstones_entry = tk.Entry(root, textvariable=self.stones_value,width=6)
        self.currentstones_entry.grid(column=2,row=2,sticky=tk.W)

        self.atk_label = tk.Label(root, text="Attack Level:", padx=3, pady=3)
        self.atk_label.grid(column=1,row=3,sticky=tk.W)
        self.atk_entry = tk.Entry(root, textvariable=self.atk_value, width=3)
        self.atk_entry.grid(column=2,row=3,sticky=tk.W)
       
        self.skldmg_label = tk.Label(root, text="Skill Damage Level:", padx=3, pady=3)
        self.skldmg_label.grid(column=1,row=4,sticky=tk.W)
        self.skldmg_entry = tk.Entry(root, textvariable=self.skill_value, width=3)
        self.skldmg_entry.grid(column=2,row=4,sticky=tk.W)
        
        self.bsdmg_label = tk.Label(root, text="Boss Damage Level:", padx=3, pady=3)
        self.bsdmg_label.grid(column=1,row=5,sticky=tk.W)
        self.bsdmg_entry = tk.Entry(root, textvariable=self.boss_value, width=3)
        self.bsdmg_entry.grid(column=2,row=5,sticky=tk.W)
        
        self.bskatk_label = tk.Label(root, text="Berserk Attack Level:", padx=3, pady=3)
        self.bskatk_label.grid(column=1,row=6,sticky=tk.W)
        self.bskatk_entry = tk.Entry(root, textvariable=self.bskatk_value, width=3)
        self.bskatk_entry.grid(column=2,row=6,sticky=tk.W)

        self.hlth_label = tk.Label(root, text="Health Level:", padx=3, pady=3)
        self.hlth_label.grid(column=1,row=7,sticky=tk.W)
        self.hlth_entry = tk.Entry(root, textvariable=self.hlth_value, width=3)
        self.hlth_entry.grid(column=2,row=7,sticky=tk.W)

        self.bsctdmg_label = tk.Label(root, text="Berserk Critical Damage Level:", padx=3, pady=3)
        self.bsctdmg_label.grid(column=1,row=8,sticky=tk.W)
        self.bsctdmg_entry = tk.Entry(root, textvariable=self.bskcrt_value, width=3)
        self.bsctdmg_entry.grid(column=2,row=8,sticky=tk.W)

        self.rank_label = tk.Label(root, text="Rank: ", padx=3, pady=3)
        self.rank_label.grid(column=1, row=9,sticky=tk.W)
        self.rank_b = tk.Radiobutton(root, text="B", variable=self.rank_value, value=0)
        self.rank_b.place(x=40,y=200)
        self.rank_a = tk.Radiobutton(root, text="A", variable=self.rank_value, value=1)
        self.rank_a.place(x=80,y=200)
        self.rank_s = tk.Radiobutton(root, text="S", variable=self.rank_value, value=2)
        self.rank_s.place(x=120,y=200)
        self.rank_sr = tk.Radiobutton(root, text="SR", variable=self.rank_value, value=3)
        self.rank_sr.place(x=160,y=200)
        
        self.button = tk.Button(self.master, text="Calculate", padx=3, pady=3, command=self.calckeys)
        self.results = tk.Label(self.master, text="0")

        self.button.grid(column=1,columnspan=3, row=10,padx=3,pady=3)
        self.results.grid(column=1, columnspan=2, row=11)

    def calckeys(self):

        try:
            input_value = self.atk_value.get() + self.skill_value.get() + self.boss_value.get() + self.bskatk_value.get() + self.hlth_value.get() + self.bskcrt_value.get()
        except tk.TclError:
            self.results['text'] = "Invalid Inputs"
        if self.rank_value.get() == 0:
            atkstones = self.calcstones(self.atk_value.get(), b_max_level)
            skillstones = self.calcstones(self.skill_value.get(), b_max_level)
            bossstones = self.calcstones(self.boss_value.get(), b_max_level)
            bskatkstones = self.calcstones(self.bskatk_value.get(), b_max_level)
            healthstones = self.calcstones(self.hlth_value.get(), b_max_level)
            bskcrtstones = self.calcstones(self.bskcrt_value.get(), b_max_level)
            
            total_b_stones = atkstones + skillstones + bossstones + bskatkstones + healthstones + bskcrtstones

            totalkeys = (total_b_stones - int(self.currentstones_entry.get())) / int(self.as_entry.get())
            self.results['text'] = math.ceil(totalkeys)
            
        elif self.rank_value.get() == 1:
            atkstones = self.calcstones(self.atk_value.get(), a_max_level)
            skillstones = self.calcstones(self.skill_value.get(), a_max_level)
            bossstones = self.calcstones(self.boss_value.get(), a_max_level)
            bskatkstones = self.calcstones(self.bskatk_value.get(), a_max_level)
            healthstones = self.calcstones(self.hlth_value.get(), a_max_level)
            bskcrtstones = self.calcstones(self.bskcrt_value.get(), a_max_level)
            
            total_a_stones = atkstones + skillstones + bossstones + bskatkstones + healthstones + bskcrtstones
            
            totalkeys = (total_a_stones - int(self.currentstones_entry.get())) / int(self.as_entry.get())
            self.results['text'] = math.ceil(totalkeys)
        
        elif self.rank_value.get() == 2:
            atkstones = self.calcstones(self.atk_value.get(), s_max_level)
            skillstones = self.calcstones(self.skill_value.get(), s_max_level)
            bossstones = self.calcstones(self.boss_value.get(), s_max_level)
            bskatkstones = self.calcstones(self.bskatk_value.get(), s_max_level)
            healthstones = self.calcstones(self.hlth_value.get(), s_max_level)
            bskcrtstones = self.calcstones(self.bskcrt_value.get(), s_max_level)
            total_s_stones = atkstones + skillstones + bossstones + bskatkstones + healthstones + bskcrtstones
            totalkeys = (total_s_stones - int(self.currentstones_entry.get())) / int(self.as_entry.get())
            self.results['text'] = math.ceil(totalkeys)
        
        elif self.rank_value.get() == 3:
            atkstones = self.calcstones(self.atk_value.get(), sr_max_level)
            skillstones = self.calcstones(self.skill_value.get(), sr_max_level)
            bossstones = self.calcstones(self.boss_value.get(), sr_max_level)
            bskatkstones = self.calcstones(self.bskatk_value.get(), sr_max_level)
            healthstones = self.calcstones(self.hlth_value.get(), sr_max_level)
            bskcrtstones = self.calcstones(self.bskcrt_value.get(), sr_max_level)
            total_sr_stones = atkstones + skillstones + bossstones + bskatkstones + healthstones + bskcrtstones
            totalkeys = (total_sr_stones - int(self.currentstones_entry.get())) / int(self.as_entry.get())
            self.results['text'] = math.ceil(totalkeys)

    def calcstones(self, awk_level, max_level): #Calculates Number of Stones Remaining for Awakening Skill
        n = 1
        input_value = (awk_level * 100) + 100
        totalstones = 0

        for i in range(awk_level, max_level, n):
            totalstones = (input_value + totalstones)
            input_value = input_value + 100
            #print(totalstones)
        return totalstones
    def start(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('250x300')
    root.title("Idle Berserker Key Calc")
    app = App(root)
    app.start()