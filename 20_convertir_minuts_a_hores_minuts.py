minuts_totals = int(input("Introdueix el nombre total de minuts: "))
hores = minuts_totals // 60
minuts_restants = minuts_totals % 60
print(f"{minuts_totals} minuts són {hores} hores i {minuts_restants} minuts.")