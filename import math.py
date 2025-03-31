import math

def calcular_potencias(pu, eficiencia, fator_potencia):
    """
    Calcula as potências ativa, aparente e reativa de um motor.

    Args:
      pu: Potência útil do motor (em kW).
      eficiencia: Rendimento do motor (em decimal, ex: 0.85).
      fator_potencia: Fator de potência do motor (em decimal, ex: 0.92).

    Returns:
      Uma tupla contendo as potências ativa, aparente e reativa (em kW, kVA e kVAr, respectivamente).
    """
    pa = pu / eficiencia
    s = pa / fator_potencia
    pr = math.sqrt(s**2 - pa**2)
    return pa, s, pr

# Receber dados dos motores
motores = []
num_motores = int(input("Digite o número de motores: "))

for i in range(num_motores):
    print(f"\nMotor {i+1}:")
    pu = float(input("Digite a potência útil (Pu) em kW: "))
    eficiencia = float(input("Digite o rendimento (η): "))
    fator_potencia = float(input("Digite o fator de potência (FP): "))
    motores.append({"pu": pu, "eficiencia": eficiencia, "fator_potencia": fator_potencia})

# Calcular e exibir resultados
for i, motor in enumerate(motores):
    pa, s, pr = calcular_potencias(motor["pu"], motor["eficiencia"], motor["fator_potencia"])
    print(f"\nMotor {i+1}:")
    print(f"  Potência Ativa (Pa): {pa:.3f} kW")
    print(f"  Potência Aparente (S): {s:.3f} kVA")
    print(f"  Potência Reativa (Pr): {pr:.3f} kVAr")