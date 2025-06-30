#ENTRADA DE DADOS

#ENTRADA DE CONSTANTES:
CNPJ = "12.345.678/0001-90"
NOME_EMPRESA = 'Mundo Car'

#LISTAS PARA OS DADOS
nome_carro=[]
precos=[]

#ZERANDO VARIÁVEIS
total=0

quantidade=int(input("Digite quantos carros deseja cadastrar(Digite 0 para sair):"))


#PROCESSAMENTO
while quantidade != 0:
   #ZERNADO AS LISTAS:
    nome_carro=[]
    precos=[]

    if quantidade < 0:
        print("\n====== Sistema encerrando ======")

    for i in range(0,quantidade):
        nome_carro.append((str(input(f"Digite o {i+1} carro: "))))
        precos.append(float(input(f"Digite o {i+1} preço: ")))
    #ZERANDO O TOTAL

    total=0


    for preco in precos:
            total = total + preco
    #BRINDES
    if total < 9999.99:
        brinde = "1 ano de garantia a mais!"
    else:
        if total < 1999.99:
            brinde= "1 vale de 1000 reais em produtos da loja"
        else:
            if total < 29999.99:
                brinde= "1 ano de vale combustivel de até 100 reais por 3 meses"
            else:
                if total < 39999.99:
                    brinde= "1 ano de vale combustivel de até 100 reais por 9 meses"
                else:
                    brinde= "1 ano de revisão de graça!"
    #IMPRESSÃO DOS DADOS
    print("\n========== NOTA FISCAL ==========")
    print(f"Empresa: {NOME_EMPRESA}")
    print(f"CNPJ: {CNPJ}")
    print("---------------------------------")


    #FOR PARA IMPRIMIR OS CARROS
    for i in range(0,quantidade):
        print(f"{i+1}. {nome_carro[i]} - R$ {precos [i]:.2f}")
    print("---------------------------------")
    print(f". O total da compra foi: {total}")
    print(f". O brinde contemplado foi:\n {brinde}")
    print("================================")

    quantidade=int(input("Digite quantos carros deseja cadastrar(Digite 0 para sair):"))

print("\n====== Sistema encerrando ======")
