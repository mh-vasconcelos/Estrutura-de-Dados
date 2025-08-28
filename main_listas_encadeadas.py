from listas_encadeadas import ItemLista, ListaEncadeada


l = ListaEncadeada()
l.insere(10) # insere no início
l.insere_no_fim(20) # insere na última posição
l.insere_no_fim(40)
l.insere(0)
l.insere_na_posicao(30,3) # insere em uma posição específica
print(l)