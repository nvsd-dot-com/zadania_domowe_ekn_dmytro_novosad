import pandas as pd # pandas dla anaizy danych
import matplotlib.pyplot as plt # matplotlib narysuje histogram

# Student : Dmytro Novosad
# Nr albumu : 188066

# Dane lotnisk
data = {
    'Airport': [
        'Boston Logan (BOS)', 'Charlotte Douglas (CLT)', 'Chicago O’Hare (ORD)', 
        'Dallas/Ft. Worth (DFW)', 'Denver (DEN)', 'Detroit Metropolitan (DTW)', 
        'Hartsfield-Jackson Atlanta (ATL)', 'Houston George Bush (IAH)', 
        'Las Vegas McCarran (LAS)', 'Los Angeles (LAX)', 'Miami (MIA)', 
        'Minneapolis/St. Paul (MSP)', 'New York John F. Kennedy (JFK)', 
        'Newark Liberty (EWR)', 'Orlando (MCO)', 'Philadelphia (PHL)', 
        'Phoenix Sky Harbor (PHX)', 'San Francisco (SFO)', 
        'Seattle-Tacoma (SEA)', 'Toronto Pearson (YYZ)'
    ],
    'Passengers': [
        36.3, 44.4, 78.0, 65.7, 58.3, 34.4, 104.2, 41.6, 47.5, 80.9, 
        44.6, 37.4, 59.1, 40.6, 41.9, 36.4, 43.3, 53.1, 45.7, 44.3
    ]
}

df = pd.DataFrame(data)

#  a. Znalezienie najbardziej i najmniej zajętego lotniska
print("a -> Analiza skrajnych wartości")

busiest = df.loc[df['Passengers'].idxmax()]
least_busy = df.loc[df['Passengers'].idxmin()]

print(f"Najbardziej zajęte lotnisko: {busiest['Airport']} ({busiest['Passengers']} mln)")
print(f"Najmniej zajęte lotnisko: {least_busy['Airport']} ({least_busy['Passengers']} mln)\n")


# b. Tabela rozkładu częstości
print("b -> Rozkład częstości")
# Tworzenie przedziałów co 10 jednostek, jak w zadaniu
bins = [30, 40, 50, 60, 70, 80, 90, 100, 110] # granice przedziałów
labels = ['30–39.9', '40–49.9', '50–59.9', '60–69.9', '70–79.9', '80–89.9', '90–99.9', '100–109.9']

# Podział danych na klasy, używamy prawostronnego otwarcia przedziału, aby odpowiadało zapisowi z polecenia
# PANDAS cut() funkcja tworzy kategorie na podstawie przedziałów
df['Class'] = pd.cut(df['Passengers'], bins=bins, labels=labels, right=False)
frequency_distribution = df['Class'].value_counts().sort_index()

print("Klasa (mln)\tCzęstość")
for klasa, czestosc in frequency_distribution.items():
    print(f"{klasa}\t\t{czestosc}")
print("\n")


# c. Wygenerowanie histogramu
print("c -> Rysowanie histogramu ")
print("**Wykres otworzy się w nowym oknie.**")

plt.figure(figsize=(10, 6))

# Rysowanie histogramu (krawędzie słupków oparte o przygotowane przedziały) (zm. bins)
plt.hist(df['Passengers'], bins=bins, color='skyblue', edgecolor='black', zorder=2)

plt.title('Histogram ruchu pasażerskiego na lotniskach w Ameryce Północnej (2018)')
plt.xlabel('Całkowita liczba pasażerów (Miliony)')
plt.ylabel('Częstość (Liczba lotnisk)')
plt.xticks(bins)
plt.yticks(range(0, 12, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)

# Wyświetlamy wykresu
plt.show()

# Interpretacja histogramu
print("\nInterpretacja histogramu:")
print("- Rozkład jest prawoskośny (ang. right-skewed / positively skewed).")
print("- Większość lotnisk (najwyższy słupek) obsługuje ruch w przedziale 40-49.9 mln pasażerów rocznie.")
print("- Istnieją lotniska będące wartościami odstającymi na prawym końcu wykresu (np. ATL obsługujące ponad 100 mln), które znacząco odstają od reszty grupy.")

input("Naciśnij Enter, aby zakończyć program...")