# (a) Oduzimanje 5.0 i 4.935
result_a = 5.0 - 4.935
print("Rezultat oduzimanja 5.0 i 4.935 (ocekivano):", 0.065)
print("Rezultat oduzimanja 5.0 i 4.935 (Python):", result_a)

# (b) Provjera jednakosti sume 0.1, 0.2 i 0.3 i broja 0.6
tolerance = 0.0001  # Tolerancija za usporedbu decimalnih brojeva

result_b = 0.1 + 0.2 + 0.3
expected_result_b = 0.6

print("\nRezultat:", result_b)
print("Ocekivani rezultat:", expected_result_b)

# Provjera jednakosti s tolerancijom
if abs(result_b - expected_result_b) < tolerance:
    print("Rezultat je u granicama tolerancije.")
else:
    print("Rezultat nije u granicama tolerancije.")