agenda = []   #Cria lista vazia

#Procedimento que cria novo ctt

def novo():
    global agenda    #Definindo variável como global
    nome = p_nome()
    celular = input("Celular....: ")
    email = input("E-mail.....: ")
    agenda.append([nome, celular, email])   #Add dados na agenda
    print(
   "-------------------------"

"Registro gravado com sucesso!!!"
        "-----------------------------")


#Procedimento que lê um nome
def p_nome():
    return(input("nome.......: "))


#Procedimento que lista um registro
def listar_dados(nome, celular, email):
    print("Nome: %s\nCelular: %s\nEmail: %s" % (nome, celular, email))
    print("------------------------------")
    


#Procedimento que lista todos os registros da matriz
def listar():     #função para mostrar lisa de ctt
    print("\nCONTATOS DA AGENDA################\n")
    for e in agenda:
        listar_dados(e[0], e[1], e[2])
    print("\nFIM DA AGENDA################\n")



#Esta função pesquisa um ctt pelo nome
def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(agenda):    #percorrer toda a matriz
        if e[0].lower() == name:  #Procurar nome desejado
            return d  #retorna o indice do nome encontrado
    return None   #retornar vazio se não encontrar nada


#Procedimento exibe o registro ou mensagem de insucesso
def pesquisar():
    p = pesquisa(p_nome())   #entrada de dados
    if p != None:
        print("Registro encontrado!")
        #atualiza as variáveis se encontrar
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        #mostra o registro
        listar_dados(nome, celular, email)
    else:
        print("\nNome não encontrado!!!")


#Procedimento que apaga ctts
def apagar():
    global agenda
    nome = p_nome()
    #retornar o índice do nome ou vazio
    p = pesquisa(nome)
    if p != None:  #se encontrou o ctt
        del agenda[p]  #excluir ctt
        print("\n----------------------------"
        "\nRegistro APAGADO com sucesso!!"
        "-----------------------------")
    else:
        #não encontrou o registro para excluir
        print("Nome não encontrado.")


#Procedimento para editar um ctt
def editar():
    p = pesquisa(p_nome())  #entrada de dados
    #se encontrou
    if p != None:
        #mostrar o nome e pedir a edição dos demais
        nome = agenda[p][0]
        print("Nome........:", nome)
        celular = input("Celular....:")
        email = input("E-mail.....:")
        agenda[p] = [nome, celular, email]  #armazenar os novos dados
        print("\n-------------------------"
        "\nRegistro gravado com sucesso!!!"
        "-----------------------------")
    else:
        print("Nome não encontrado.")   #executa caso a condição seja falsa
    

#Função que valida se o item digitado foi valido
def validar(pergunta, inicio, fim):  #validar numeros inteiros
    while True:  #loop infinito
        try:   #condição
            valor = int(input(pergunta))  #entrada de dados
            if inicio <= valor <= fim:  #determinando condição
                return (valor)   #executar caso vdd
            else:
                return (0)
        except ValueError:  #executa caso falso
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))


#função que retorna o item do menu ou 0 para inválida
def menu():  #exibe menu de opções
    print("""
   1 - Adicionar novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Lista de contatos
   5 - Apagar um contato
   6 - Sair
""")
    return validar("Escolha uma opção:", 1, 6)


#PROGRAMA PRINCIPAL
while True: #loop infinito
    opcao = menu()
    if opcao == 0:
        print("Opcao inválida!")
    elif opcao == 6:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()

