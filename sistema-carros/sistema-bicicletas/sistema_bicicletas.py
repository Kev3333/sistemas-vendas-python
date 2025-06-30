
#ENTRADA DE DADOS
#CONSTANTES 
CNPJ="00.348.003/0116-60"
NOME="Bike Plus"
#ENTRADA DE LISTAS E VARIAVEIS 
produtos=[]
valores=[]
total=0
brinde=0

quantidade=int(input("Digite a quantidade de compras que deseja cadastrar (digite 0 para sair): "))

#PROCESSAMENTO 
while quantidade != 0:
    #ZERANDO LISTAS 
    bicicletas=[]
    valores=[]

    if quantidade < 0:
        print("\n ======== SISTEMA ENCERRADO ========")

    for i in range (0,quantidade):
        produtos.append(str(input(f"Digite o {i+1} produto: ")))
        valores.append(float(input(f"Digite o {i+1} preço: ")))
    #ZERANDO VARIAVEL 
    total=0

    for valor in valores:
        total = total + valor
    #CONDICIONAIS PARA DETERMINAR BRINDES 
    if total < 999.99:
        brinde="Kit de iluminação"
    else:
        if total < 1999.99:
            brinde="Capacete"
        else:
            if total < 2999.99:
                brinde="Trava antifurto"
            else:
                brinde="Cupom 50% por 3 meses para cada mês em uma compra!"
    #IMPRESSÃO DE DADOS 
    print("\n========= NOTA FISCAL ==========")
    print(f"EMPRESA: {NOME}")
    print(f"CNPJ: {CNPJ}")
    print("=================================")
    for i in range(0,quantidade):
        print(f".{i+1} R$ {valores [i]:.2f}")
    print(f"O valor total foi de: {total}")
    print(f"O brinde contemplado foi: \n {brinde}")
    print("=================================")

    #CONTINUAÇÃO DO LOOPING 
    quantidade=int(input("Digite a quantidade de compras que deseja cadastrar (digite 0 para sair)"))

print("\n ======== SISTEMA ENCERRADO ========")

