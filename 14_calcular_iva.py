preu_base = float(input("Introdueix el preu del producte (sense IVA): "))
iva = preu_base * 0.21
preu_final = preu_base + iva
print(f"Preu base: {preu_base}€")
print(f"IVA (21%): {iva}€")
print(f"Preu total: {preu_final}€")