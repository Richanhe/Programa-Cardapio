cardapio = {}

while True:
    entrada = input()

    if entrada == "add":
        categoria = input("Qual a categoria do item? ")
        item = input("Qual o item? ")
        produto = input("Qual o produto? ")
        preço = input("Qual o preço? ")
        if len(cardapio) == 0:
            cardapio[categoria] = {}
        if len(cardapio[categoria]) == 0:
            cardapio[categoria][item] = {}
        cardapio[categoria][item][produto] = preço
    #elif separada[0] == "rmv":

    #elif separada[0] == "edt":

    #elif separada[0] == "src":

    elif entrada == "all":
        print(cardapio)

    elif entrada == "stop":
        break 