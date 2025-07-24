from Stack import *

pagina_atual = None
pagina_antiga = Stack()
proxima_pagina = Stack()

def exibir_estado():
    print(f"\nPágina Atual: {pagina_atual}")
    print(f"\nVoltar: {pagina_antiga}")
    print(f"\nAvançar: {proxima_pagina}")

def acessar_pagina(nova_pagina):
    global pagina_atual
    if pagina_atual is not None:
        pagina_antiga.push(pagina_atual)
    pagina_atual = nova_pagina
    proxima_pagina = Stack()
    return proxima_pagina
    

def avancar():
    global pagina_atual
    if not proxima_pagina.is_Empty():
        pagina_antiga.push(pagina_atual)
        pagina_atual = proxima_pagina.pop()
    else:
        print("\n======================")
        print("Pagina não encontrada")
        print("======================")

def voltar():
    global pagina_atual
    if not pagina_antiga.is_Empty():
        proxima_pagina.push(pagina_atual)
        pagina_atual = pagina_antiga.pop()
    else:
        print("\n======================")
        print("Pagina não encontrada")
        print("======================")
        
while True:
    print("\n\t---NAVEGADOR---")
    print("1 - Acessar nova página")
    print("2 - Voltar")
    print("3 - Avançar")
    print("4 - Exibir pagina atual")
    print("0 - Encerrar")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        site = input("Digite o endereço da nova página: ")
        acessar_pagina(site)
    elif opcao == '2':
        voltar()
    elif opcao == '3':
        avancar()
    elif opcao == '4':
        exibir_estado()
    elif opcao == '0':
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
