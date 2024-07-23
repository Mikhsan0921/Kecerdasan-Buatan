# Definisi fungsi keanggotaan secara manual
def fuzzy_membership(value, low, mid, high):
    low_membership = max(0, min((value - low) / (mid - low), 1))
    mid_membership = max(0, min((high - value) / (high - mid), 1))
    high_membership = max(0, min((value - mid) / (high - mid), 1))
    return low_membership, mid_membership, high_membership

# Fungsi untuk melakukan inferensi fuzzy
def fuzzy_inference(volume, density):
    # Definisi aturan fuzzy
    rules = [
        ('low', 'low', 'long'),
        ('low', 'mid', 'medium'),
        ('low', 'high', 'short'),
        ('mid', 'low', 'medium'),
        ('mid', 'mid', 'short'),
        ('mid', 'high', 'short'),
        ('high', 'low', 'short'),
        ('high', 'mid', 'short'),
        ('high', 'high', 'short')
    ]

    # Inisialisasi variabel hasil
    results = {'short': 0, 'medium': 0, 'long': 0}

    # Proses inferensi fuzzy
    for v, d, o in rules:
        v_low, v_mid, v_high = fuzzy_membership(volume, 30, 60, 100)
        d_low, d_mid, d_high = fuzzy_membership(density, 30, 60, 100)
        activation = min(v_low if v == 'low' else (v_mid if v == 'mid' else v_high),
                         d_low if d == 'low' else (d_mid if d == 'mid' else d_high))
        if o == 'short':
            results['short'] = max(results['short'], activation)
        elif o == 'medium':
            results['medium'] = max(results['medium'], activation)
        elif o == 'long':
            results['long'] = max(results['long'], activation)

    return results

# Fungsi untuk melakukan defuzzifikasi
def defuzzification(results):
    total_activation = sum(results.values())
    if total_activation == 0:
        return 0
    
    numerator = sum(float(k) * v for k, v in results.items())  
    return numerator / total_activation

# Masukkan volume dan kepadatan
volume_input = float(input("Masukkan volume lalu lintas (0-100): "))
density_input = float(input("Masukkan kepadatan lalu lintas (0-100): "))

# Proses inferensi fuzzy
fuzzy_result = fuzzy_inference(volume_input, density_input)

# Lakukan defuzzifikasi
output_duration = defuzzification(fuzzy_result)

# Output hasil
print("Durasi lampu hijau yang direkomendasikan:", output_duration)
