class ItemLista:
  def __init__(self, data=0, nextItem=None):
    self.data = data
    self.next = nextItem

  def __repr__(self):
    return '%s => %s' % (self.data, self.next)
  


class ListaEncadeada:
  def __init__(self):
    self.head = None

  def __repr__(self):
    return "%s" % (self.head) 
  
  def insere(lista, data):
    # cria um objeto para armazenar um novo item da lista
    item = ItemLista(data)
    # o head é apontado como próximo item
    item.next = lista.head
    # o item atual se torna o head
    lista.head = item

  def insere_no_fim(lista, data):
    # 1. Cria um objeto para armazenar o novo item da lista
    novo_item = ItemLista(data)

    # 2. CASO ESPECIAL: A lista está vazia?
    if lista.head is None:
        # Se estiver, o novo item se torna o head e a função termina.
        lista.head = novo_item
        return # return para sair da função aqui mesmo

    # 3. Se a lista NÃO está vazia, precisamos percorrê-la.
    # Começamos com uma variável temporária no head.
    ultimo = lista.head

    # Loop: "Enquanto o próximo do 'ultimo' não for nulo, continue andando"
    while ultimo.next:
        ultimo = ultimo.next

    # 4. Quando o loop termina, 'ultimo' é uma referência para o último nó da lista.
    # Agora, fazemos o 'next' do último nó apontar para o nosso novo item.
    ultimo.next = novo_item

  # Supondo as mesmas classes ItemLista (Node) e ListaEncadeada
  def insere_na_posicao(lista, data, posicao):
      """
      Insere um novo item em uma posição específica na lista encadeada.
      A posição 0 é o início da lista.
      """
      # --- Validação de Entrada ---
      if posicao < 0:
          print("Erro: Posição não pode ser negativa.")
          return

      # --- Caso 1: Inserção no início ---
      if posicao == 0:
          novo_item = ItemLista(data)
          novo_item.next = lista.head
          lista.head = novo_item
          return

      # --- Caso 2: Inserção no meio ou fim ---
      novo_item = ItemLista(data)
      atual = lista.head
      contador = 0

      # Loop para encontrar o nó ANTERIOR à posição de inserção.
      # Por isso, o loop vai até 'posicao - 1'.
      while contador < posicao - 1:
          # Se 'atual' se tornar None antes de acharmos a posição,
          # significa que a posição é inválida (maior que o tamanho da lista).
          if atual is None:
              print(f"Erro: Posição {posicao} é inválida. A lista é menor.")
              return

          atual = atual.next # 2
          contador += 1

      # --- Verificação final após o loop ---
      # Se 'atual' for None aqui, significa que a lista era vazia e a posicao > 0,
      # ou a posição é exatamente uma a mais que o tamanho da lista.
      if atual is None:
          print(f"Erro: Posição {posicao} é inválida.")
          return

      # --- Lógica de Inserção ---
      # 1. O 'next' do novo item aponta para o antigo 'next' do nó atual.
      novo_item.next = atual.next # o next do novo_item será 1 (que antes era next do 2)
                        
      # 2. O 'next' do nó atual agora aponta para o novo item.
      atual.next = novo_item # o next do atual (2) será o nosso item (antes era 1, que virou next do nosso item)
        
  def buscar_elemento(lista, data):
      """
      Busca por um elemento na lista e retorna seu índice se encontrado.
      Retorna None se o elemento não estiver na lista.
      """
      ponteiro_atual = lista.head
      indice = 0

      while ponteiro_atual is not None:
          if ponteiro_atual.data == data:
              # Encontramos o elemento, retornamos sua posição
              return indice
          
          # Se não for o elemento, avançamos para o próximo
          ponteiro_atual = ponteiro_atual.next
          indice += 1

      # Se o loop terminar, o elemento não está na lista
      return None
    # Supondo as mesmas classes ItemLista (Node) e ListaEncadeada
  def buscar_elemento_por_indice(lista, indice):
        """
        Busca por um nó na lista baseado em seu índice.
        Retorna o Nó se encontrado, ou None se o índice for inválido.
        """
        # 1. Validação básica inicial
        if indice < 0:
            print("Erro: Índice não pode ser negativo.")
            return None

        ponteiro_atual = lista.head
        contador = 0

        # 2. Loop que percorre a lista E verifica se não chegou ao fim
        while contador < indice and ponteiro_atual is not None:
            ponteiro_atual = ponteiro_atual.next
            contador += 1

        # 3. Verificação final após o loop
        # Se o ponteiro for None, significa que o índice era maior que o tamanho da lista.
        # Também verificamos se o contador realmente chegou ao índice desejado.
        if ponteiro_atual is None:
            print(f"Erro: Índice {indice} fora do alcance da lista.")
            return None
        
        # Se chegamos aqui, o ponteiro está no nó correto
        return ponteiro_atual.data # Retorna o objeto Nó inteiro

  def remover_elemento(lista, data):
    """
    Remove o primeiro nó que contém o dado especificado.
    Retorna True se o elemento foi removido, False caso contrário.
    """
    atual = lista.head
    anterior = None

    # Loop para encontrar o nó a ser removido
    while atual is not None and atual.data != data:
        anterior = atual
        atual = atual.next

    # Se 'atual' é None, o elemento não foi encontrado na lista
    if atual is None:
        return False

    # Agora, vamos "remover" o nó 'atual'
    if anterior is None:
        # CASO ESPECIAL: O nó a ser removido é o head (anterior nunca foi atualizado)
        lista.head = atual.next
    else:
        # CASO GERAL: O nó está no meio ou no fim
        # O 'next' do anterior pula o 'atual' e aponta para o 'next' do 'atual'
        anterior.next = atual.next
    
    return True



l = ListaEncadeada()
l.insere(10)
l.insere_no_fim(20)
l.insere_no_fim(40)
l.insere(0)
l.insere_na_posicao(30,3)
l
