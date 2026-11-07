import pandas as pd # Pandas dla analizy danych

# Student: Dmytro Novosad
# Nr albumu: 188066

# Dane z tabeli
data = {
    'Company': [
        'Procter & Gamble', 'Comcast', 'AT&T', 'Ford', 'Verizon', "L'Oreal",
        'American Express', 'General Motors', 'Toyota', 'Fiat Chrysler', 
        'Walt Disney Company', 'J.P. Morgan'
    ],
    'Advertising ($billions)': [
        5.00, 3.08, 2.91, 2.56, 2.44, 2.34,
        2.19, 2.15, 2.09, 1.97, 1.96, 1.88
    ]
}

df = pd.DataFrame(data)

# Wyodrębnienie kolumny z wydatkami dla wygody
spending = df['Advertising ($billions)']

# a. Średnia (mean)
mean_spending = spending.mean()
print(f"a. Średnia kwota wydana na reklamę: ${mean_spending:.3f} mld")

# b. Mediana (median)
median_spending = spending.median()
print(f"b. Mediana kwoty wydanej na reklamę: ${median_spending:.3f} mld")

# c. Pierwszy i trzeci kwartyl (Q1, Q3)
# Używamy interpolation='midpoint', aby naśladować standardowe obliczenia statystyczne dla parzystej liczby elementów
q1 = spending.quantile(0.25, interpolation='midpoint')
q3 = spending.quantile(0.75, interpolation='midpoint')

print(f"\nc. Wydatki Q1: ${q1:.3f} mld")
print(f"   Wydatki Q3: ${q3:.3f} mld")

input("\nNaciśnij Enter, aby zakończyć program...")
