#Menu que será apresentado ao usuário
Menu ="""
    [a] Adicionar produto 
    [r] Remover Produto
    [l] Listar produtos

    => """

#Lista Nascendo Vázia
lista_mercado = []
#Lista onde será armazenado os dados Onde o usuário irá digitar
lista_adicionado = []

#Loop do tipo True
while True:
    #Input onde será apresentado o menu
    produto_digitado = input(Menu)

    if produto_digitado == "a":
        produto = str(input("Digite o produto: "))

        if len(produto) > 0 :

            lista_mercado +=(produto) 

            lista_adicionado.append(produto)
            print(f"Sua lista de Marcado é: {lista_adicionado}")
        else:
            print("[ERROS], O campo não pode estar vázio !")
   
    elif produto_digitado == "r":
        produto = str(input("Digite o Nome do produto que deseja remover: "))
        
        if len(produto) > 0:
            
            lista_adicionado.remove(produto)

            print(f"Seu produto {produto}, Foi removido com sucesso!!!")

        else :
                print("[ERROS], O campo não pode estar vázio !")
    elif produto_digitado == "l":

        print("\n######## Lista de mercado ###########")
        print(f"\nLista: {lista_adicionado}")a
        print("\n##########Fim da Lista ###########")

    