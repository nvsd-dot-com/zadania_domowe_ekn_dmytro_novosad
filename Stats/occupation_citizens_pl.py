import pandas as pd # Biblioteka Pandas dla analizy danych

# Student: Dmytro Novosad
# Nr albumu: 188066

# 1. Definicja danych z tabeli
# Przyjmujemy środki przedziałów (midpoints) do obliczenia średniej:
# "poniżej 25": zakładamy przedział 15-24 lata -> środek = (15+24)/2 = 19.5
# "25-34": środek = (25+34)/2 = 29.5
# "35-44": środek = (35+44)/2 = 39.5
# "45-54": środek = (45+54)/2 = 49.5
# "55 i więcej": zakładamy przedział 55-64 lata -> środek = (55+64)/2 = 59.5

data = {
    'Grupa wiekowa': ['poniżej 25', '25-34', '35-44', '45-54', '55 i więcej'],
    'Środek przedziału (x_i)': [19.5, 29.5, 39.5, 49.5, 59.5],
    'Kobiety [tys.] (f_k)': [524.3, 455.1, 382.8, 132.0, 13.1],
    'Mężczyźni [tys.] (f_m)': [471.7, 369.6, 346.3, 152.2, 43.5]
}

df = pd.DataFrame(data)

# Dodanie kolumny z łączną liczbą bezrobotnych (kobiety + mężczyźni)
df['Ogółem [tys.] (f_o)'] = df['Kobiety [tys.] (f_k)'] + df['Mężczyźni [tys.] (f_m)']

# --- a) Porównanie przeciętnego wieku bezrobotnych kobiet i mężczyzn ---
# Wzór na średnią z szeregu rozdzielczego: x_śr = suma(x_i * f_i) / suma(f_i)

suma_kobiety = df['Kobiety [tys.] (f_k)'].sum()
srednia_kobiety = (df['Środek przedziału (x_i)'] * df['Kobiety [tys.] (f_k)']).sum() / suma_kobiety

suma_mezczyzni = df['Mężczyźni [tys.] (f_m)'].sum()
srednia_mezczyzni = (df['Środek przedziału (x_i)'] * df['Mężczyźni [tys.] (f_m)']).sum() / suma_mezczyzni

print("\na) Przeciętny wiek bezrobotnych kobiet i mężczyzn")
print(f"Przeciętny wiek bezrobotnych kobiet:   {srednia_kobiety:.2f} lat")
print(f"Przeciętny wiek bezrobotnych mężczyzn: {srednia_mezczyzni:.2f} lat")

if srednia_kobiety > srednia_mezczyzni:
    print("Wniosek: Przeciętny wiek bezrobotnych kobiet był wyższy niż mężczyzn.")
else:
    print("Wniosek: Przeciętny wiek bezrobotnych mężczyzn był wyższy niż kobiet.")
print("\n")


# --- b) Przeciętny wiek wszystkich bezrobotnych zarejestrowanych w Polsce 31.12.1993 r. ---
suma_ogolem = df['Ogółem [tys.] (f_o)'].sum()
srednia_ogolem = (df['Środek przedziału (x_i)'] * df['Ogółem [tys.] (f_o)']).sum() / suma_ogolem

print("b) Przeciętny wiek wszystkich bezrobotnych")
print(f"Przeciętny wiek (ogółem): {srednia_ogolem:.2f} lat\n")

input("Naciśnij Enter, aby zakończyć program...")
