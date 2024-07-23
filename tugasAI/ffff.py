def bahu_kanan(a,b,x):
    if x <= a:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif x > b:
        return 1

def bahu_kiri(a,b,x):
    if x <= a:
        return 1
    elif a < x <= b:
        return (b - x) / (b - a)
    elif x > b:
        return 0

def segitiga(a, b, c, x):
    if x <= a or x >= c:
        return 0
    if x > a and x <= b:
        return (x - a) / (b - a)
    if x > b and x < c:
        return (c - x) / (c - b)

def fDA(x):
    return {
        "rendah": bahu_kiri(40, 60, x),
        "sedang": segitiga(40, 60, 70, x),
        "tinggi": bahu_kanan(60, 80, x)
    }

def fIH(x):
    return {
        "rendah": bahu_kiri(40, 60, x),
        "sedang": segitiga(40, 60, 70, x),
        "tinggi": bahu_kanan(60, 80, x)
    }

class ZValue:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def turun(self, x):
        a = self.a
        b = self.b
        return b - (x * (b - a))

    def naik(self, x):
        a = self.a
        b = self.b
        return (x * (b - a)) + a

def defuzzify(alpha, z):
    numerator = 0
    denominator = 0
    for value in range(len(alpha)):
        numerator += alpha[value]["alpha"] * z[value]
        denominator += alpha[value]["alpha"]
    return numerator / denominator

def klik_proses(DA_val, IH_val):
    DA = fDA(DA_val) #[0.1][1]
    IH = fIH(IH_val)

    alphaLam = [
        {"alpha": min(DA["rendah"], IH["rendah"]), "out": "turun"},
        {"alpha": min(DA["rendah"], IH["sedang"]), "out": "turun"},
        {"alpha": min(DA["rendah"], IH["tinggi"]), "out": "naik"},
        {"alpha": min(DA["sedang"], IH["rendah"]), "out": "turun"},
        {"alpha": min(DA["sedang"], IH["sedang"]), "out": "naik"},
        {"alpha": min(DA["sedang"], IH["tinggi"]), "out": "naik"},
        {"alpha": min(DA["tinggi"], IH["rendah"]), "out": "naik"},
        {"alpha": min(DA["tinggi"], IH["sedang"]), "out": "naik"},
        {"alpha": min(DA["tinggi"], IH["tinggi"]), "out": "naik"}
    ]


    z = ZValue(0, 100)

    zLam = []
    for rule in alphaLam:
        zLam.append(z.turun(rule["alpha"]) if rule["out"] == "turun" else z.naik(rule["alpha"]))


    Lam = defuzzify(alphaLam, zLam)

    return Lam

if __name__ == "__main__":
    DA_val = float(input("Masukkan volume lalu lintas (0-100): "))
    IH_val = float(input("Masukkan kepadatan lalu lintas (0-100): "))

    Lam = klik_proses(DA_val, IH_val)

    print("Durasi lampu hijau yang direkomendasikan:", round(Lam) , "detik")
