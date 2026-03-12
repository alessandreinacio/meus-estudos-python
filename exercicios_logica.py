# Exercício simples de lógica

def verificar_paridade(numero):
    return "Par" if numero % 2 == 0 else "Ímpar"

numeros = [10, 15, 22, 33, 40]

for n in numeros:
    print(f"O número {n} é {verificar_paridade(n)}")
