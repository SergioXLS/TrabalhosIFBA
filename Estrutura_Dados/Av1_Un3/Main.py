from Stack import *

pagina_atual = None
pagina_voltar = Stack()
pagina_avancar = Stack()

def exibir_estado():
    print(f"\nPágina Atual: {pagina_atual}")
    print(f"\nVoltar: {pagina_voltar}")
    print(f"\nAvançar: {pagina_avancar}")

def acessa_pagina(nova_pagina):
    global pagina_atual
    if pagina_atual is not None:
        pagina_voltar.push(pagina_atual)
        pagina_atual = nova_pagina

def avancar():
    global pagina_atual
    if pagina_avancar.isEmpty():
        pagina_voltar = pagina_atual
        pagina_atual = pagina_avancar.pop()

def voltar():
    global pagina_atual
    if not pagina_voltar.isEmpty():
        pagina_avancar = pagina_atual
        pagina_atual = pagina_voltar.pop()
