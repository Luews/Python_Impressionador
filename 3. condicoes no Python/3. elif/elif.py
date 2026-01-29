# Exemplo:

# Vamos criar um algoritmo para analisar as bonificacoes dos funcionarios

# se a pessoa vendeu abaixo do meta ela não ganha bônus.
# se a pessoa vendeu acima da meta, ela ganha um bônus de 3%.
# se a pessoa vendeu o dobro da meta, ela ganha um bônus de 7%.

meta = 20000
vendas = int(input("Quantos R$ você fez de faturamento esse mês?: "))

if vendas < meta:
    print("Meta não batida, infelizmente sem bonificação")
elif vendas >= (meta*2):
    bonus = 0.07 * vendas
    print(f"Parabéns, meta dobrada com sucesso! e uma bonificação de R$ {bonus: .2f}")
else:
    bonus = 0.03 * vendas
    print(f"Parabéns, meta alcançada com sucesso e uma bonificação de R${bonus: .2f}")