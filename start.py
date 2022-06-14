import sys, time #importa o módulo sys e time
from src.banner import banner #importa o banner do programa
from src.cls import cls

cart =[]

def menu():
    option = 0 #variável que armazena a opção escolhida pelo usuário

    while option != "4": #enquanto a opção escolhida não for 4, o programa continua
        cls()
        banner() #imprime o banner do programa
        option = input("\n1 - Adicionar um produto ao carrinho \n2 - Remover um produto do carrinho \n3 - Visualizar carrinho \n4 - Finalizar compra\nDigite a opção desejada: ")
        if option == "1":
            add_product()
        elif option == "2":
            remove_product()
        elif option == "3":
            list_products()
        elif option == "4":
            list_products()
            print("\nFinalizando sua compra, aguarde...")
            time.sleep(5)
            print("\nCompra finalizada com sucesso!\n")
            time.sleep(2)
            cls()
            sys.exit()
        else:
            print("\nOpção inválida, tente novamente\n")
            time.sleep(2)

def add_product():
    print("\nAdicionando um produto ao carrinho...")
    product_name = input("Digite o nome do produto: ")

    cart.append(product_name)
    print("\nProduto adicionado ao carrinho com sucesso!\n")
    time.sleep(2)
    menu()

def remove_product():
    print("\nRemovendo um produto do carrinho...")
    product_name = input("Digite o nome do produto: ")

    if product_name in cart:
        cart.remove(product_name)
        print("\nProduto removido com sucesso!\n")
    else:
        print("\nProduto não encontrado no carrinho!\n")
    time.sleep(2)
    menu()

def list_products():
    print("\nListando os produtos do carrinho...")
    time.sleep(2)
    if len(cart) == 0:
        print("\nO carrinho está vazio!\n")
    else:
        print("\nProdutos no carrinho:")
        for product in cart:
            print(product) 
        time.sleep(2)
menu()