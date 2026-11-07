import numpy as np
from scipy.stats import linregress

# Student: Dmytro Novosad
# Nr albumu: 188066

# Wprowadzenie danych z tabeli
# X - Volume (wielkość produkcji)
# Y - Cost (całkowity koszt)
volume = np.array([400, 450, 550, 600, 700, 750])
cost = np.array([4000, 5000, 5400, 5900, 6400, 7000])

# Obliczenie regresji liniowej metodą najmniejszych kwadratów
slope, intercept, r_value, p_value, std_err = linregress(volume, cost)

# a. Równanie regresji (Estimated regression equation)
print("\na. Szacowane równanie regresji ---")
# y = b0 + b1*x, gdzie b0 to intercept (wyraz wolny), a b1 to slope (współczynnik kierunkowy)
print(f"Równanie: Wyliczony Koszt (y) = {intercept:.2f} + {slope:.2f} * Wielkość Produkcji (x)\n")

# b. Zmienny koszt na jednostkę (Variable cost per unit)
print("b. Zmienny koszt na jednostkę ---")
# Koszt zmienny to współczynnik kierunkowy (slope) z naszego równania
print(f"Zmienny koszt wyprodukowania jednej jednostki wynosi: ${slope:.2f}\n")

# c. Współczynnik determinacji (Coefficient of determination, R^2)
print("c. Współczynnik determinacji (R^2) ---")
r_squared = r_value ** 2
percentage_explained = r_squared * 100
print(f"Współczynnik determinacji R^2: {r_squared:.4f}")
print(f"Wielkość produkcji wyjaśnia {percentage_explained:.2f}% wariancji całkowitego kosztu.\n")

# d. Przewidywanie kosztu dla 500 jednostek
print("d. Przewidywany całkowity koszt dla 500 jednostek ---")
production_target = 500
predicted_cost = intercept + slope * production_target
print(f"Szacowany koszt dla produkcji {production_target} jednostek wynosi: ${predicted_cost:.2f}")

input("\nNaciśnij Enter, aby zakończyć program...")
