while True:
    sex = input("Digite o sexo (M/F): ").strip().upper()
    if sex != 'M' and sex != 'F':
        continue
    else:
        break

print("Sexo", "masculino" if sex == "M" else "feminino")
