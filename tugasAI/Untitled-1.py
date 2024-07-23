import time
import numpypip as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class AirFreyer:
    def _init_(self):
        self.suhu = 0
        self.timer = 0
        self.dayalistrik = False 

    def atur_suhu(self, suhu):
        if suhu < 0 or suhu > 200:
            print("Error: Suhu di luar rentang (0-200°C)")
        else:
            self.suhu = suhu

    def atur_timer(self, timer):
        if timer < 0 or timer > 60:
            print("Error: Timer di luar rentang (0-60 menit)")
        else:
            self.timer = timer

    def nyalakan(self):
        self.dayalistrik = True
        print("Airfreyer dinyalakan.")

    def matikan(self):
        self.dayalistrik = False
        print("Airfreyer dimatikan.")

    def memasak(self):
        if not self.dayalistrik:
            print("Error: Airfreyer tidak dinyalakan.")
        elif self.suhu == 0:
            print("Error: Suhu belum diatur.")
        elif self.timer == 0:
            print("Error: Timer belum diatur.")
        else:
            print(f"Memulai memasak pada suhu {self.suhu}°C selama {self.timer} menit.")
            start_time = time.time()
            while time.time() - start_time < self.timer * 60:
                print("Memasak...")
                time.sleep(1)
            print("Proses memasak selesai.")

def pilihan_makanan():
    print("Pilihan Makanan : ")
    print("1. Makanan beku (Timer: 5 menit, Suhu: 180°C)")
    print("2. Defrost (Timer: 10 menit, Suhu: 80°C)")
    print("3. Menghangatkan makanan (Timer: 3 menit, Suhu: 180°C)")
    print("4. Pengaturan suhu dan timer")
    print("5. Off ")
    while True:
        pilihan = input("Masukkan pilihan Anda (1/2/3/4/5): ")
        if pilihan in ['1', '2', '3', '4', '5']:
            return int(pilihan)
        else:
            print("Pilihan tidak valid, silahkan coba lagi.")

def input_suhu():
    while True:
        try:
            suhu = int(input("Masukkan suhu (0-200°C): "))
            return suhu
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def input_timer():
    while True:
        try:
            timer = int(input("Masukkan timer (0-60 menit): "))
            return timer
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

# Fuzzy Sugeno Model
suhu = ctrl.Antecedent(np.arange(0, 201, 1), 'suhu')
timer = ctrl.Antecedent(np.arange(0, 61, 1), 'timer')
output_suhu = ctrl.Consequent(np.arange(0, 201, 1), 'output_suhu', defuzzify_method='centroid')
output_timer = ctrl.Consequent(np.arange(0, 61, 1), 'output_timer', defuzzify_method='centroid')

# Membership functions
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 100])
suhu['sedang'] = fuzz.trimf(suhu.universe, [50, 100, 150])
suhu['panas'] = fuzz.trimf(suhu.universe, [100, 200, 200])

timer['singkat'] = fuzz.trimf(timer.universe, [0, 0, 30])
timer['sedang'] = fuzz.trimf(timer.universe, [15, 30, 45])
timer['panjang'] = fuzz.trimf(timer.universe, [30, 60, 60])

output_suhu['rendah'] = fuzz.trimf(output_suhu.universe, [0, 0, 100])
output_suhu['sedang'] = fuzz.trimf(output_suhu.universe, [50, 100, 150])
output_suhu['tinggi'] = fuzz.trimf(output_suhu.universe, [100, 200, 200])

output_timer['rendah'] = fuzz.trimf(output_timer.universe, [0, 0, 30])
output_timer['sedang'] = fuzz.trimf(output_timer.universe, [15, 30, 45])
output_timer['tinggi'] = fuzz.trimf(output_timer.universe, [30, 60, 60])

# Rules
rule1 = ctrl.Rule(suhu['dingin'] & timer['singkat'], [output_suhu['tinggi'].cen, output_timer['rendah'].cen])
rule2 = ctrl.Rule(suhu['dingin'] & timer['sedang'], [output_suhu['sedang'].cen, output_timer['sedang'].cen])
rule3 = ctrl.Rule(suhu['dingin'] & timer['panjang'], [output_suhu['rendah'].cen, output_timer['tinggi'].cen])

rule4 = ctrl.Rule(suhu['sedang'] & timer['singkat'], [output_suhu['tinggi'].cen, output_timer['rendah'].cen])
rule5 = ctrl.Rule(suhu['sedang'] & timer['sedang'], [output_suhu['sedang'].cen, output_timer['sedang'].cen])
rule6 = ctrl.Rule(suhu['sedang'] & timer['panjang'], [output_suhu['rendah'].cen, output_timer['tinggi'].cen])

rule7 = ctrl.Rule(suhu['panas'] & timer['singkat'], [output_suhu['tinggi'].cen, output_timer['rendah'].cen])
rule8 = ctrl.Rule(suhu['panas'] & timer['sedang'], [output_suhu['sedang'].cen, output_timer['sedang'].cen])
rule9 = ctrl.Rule(suhu['panas'] & timer['panjang'], [output_suhu['rendah'].cen, output_timer['tinggi'].cen])

# Control System
suhu_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
timer_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

# Simulation
suhu_sim = ctrl.ControlSystemSimulation(suhu_ctrl)
timer_sim = ctrl.ControlSystemSimulation(timer_ctrl)

# Input from user
air_freyer = AirFreyer()
air_freyer.nyalakan()
pilihan = pilihan_makanan()

if pilihan == 1:
    air_freyer.atur_suhu(180)
    air_freyer.atur_timer(5)
elif pilihan == 2:
    air_freyer.atur_suhu(80)
    air_freyer.atur_timer(10)
elif pilihan == 3:
    air_freyer.atur_suhu(180)
    air_freyer.atur_timer(3)
elif pilihan == 4:
    suhu = input_suhu()
    timer = input_timer()
    air_freyer.atur_suhu(suhu)
    air_freyer.atur_timer(timer)
elif pilihan == 5:
    air_freyer.matikan()

if pilihan != 5:
    suhu_sim.input['suhu'] = air_freyer.suhu
    timer_sim.input['timer'] = air_freyer.timer

    suhu_sim.compute()
    timer_sim.compute()

    optimal_suhu = suhu_sim.output['output_suhu']
    optimal_timer = timer_sim.output['output_timer']

    print(f"Optimal Suhu: {optimal_suhu}°C")
    print(f"Optimal Timer: {optimal_timer} menit")

    air_freyer.atur_suhu(optimal_suhu)
    air_freyer.atur_timer(optimal_timer)

    air_freyer.memasak()