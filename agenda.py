agendaTelefones = {}

def incluirContato(nome, telefone):
    if nome in agendaTelefones:
        print('Já existe um contato com esse nome!')
    else:
        agendaTelefones[nome] = telefone
        print('Contato adicionado com sucesso!')

def alterarContato(nome, telefone):
    if nome in agendaTelefones:
        agendaTelefones[nome] = telefone
        print('Telefone alterado com sucesso!')

    else:
        pergunta = int(input('O nome informado não está na lista, deseja adicionar? \n 1 - Sim \n 2 - Não \n Opção:'))
        if pergunta == 1:
                incluirContato(nome, telefone)

        else:
            print('Contato não adicionado, nenhuma alteração foi feita')

def excluirContato(nome):
    if nome in agendaTelefones:
        del agendaTelefones[nome]
        print('Contato excluido com sucesso!')
    else:
        print('O nome informado não está na lista')

def consultarContato(nome):
    if nome in agendaTelefones:
        print(nome + ' - ' + agendaTelefones[nome])
    else:
        print('O nome informado não está na lista')

def consultarContatos():
    if len(agendaTelefones) == 0:
        print('A agenda está vazia')
    else:
        for i in(agendaTelefones):
            print(i, " - ", agendaTelefones.get(i))


def limparContatos():
    if len(agendaTelefones) == 0:
        print('A agenda já está vazia')
    else:
        agendaTelefones.clear()
        print('Agenda vazia')

while True:
    opcao = int(input("Informe uma opção: \n 1 - Incluir contato \n 2 - Alterar contato \n 3 - Excluir contato \n 4 - Consultar contato \n 5 - Consultar contatos \n 6 - Limpar contatos \n 7 - Sair \nOpção: "))

    if opcao == 1:
        nome = str(input('Informe o nome do novo contato: '))
        telefone = int(input('Informe o telefone do novo contato: '))
        incluirContato(nome, telefone)
    
    elif opcao == 2:
        nome = str(input('Informe o nome do contato que deseja alterar: '))
        telefone = int(input('Informe o novo telefone do contato: '))
        alterarContato(nome, telefone)
    
    elif opcao == 3:
        nome = str(input('Informe o nome do contato para excluir: '))
        excluirContato(nome)

    elif opcao == 4:
        nome = str(input('Informe o nome do contato para consulta: '))
        consultarContato(nome)

    elif opcao == 5:
        consultarContatos()

    elif opcao == 6:
        limparContatos()

    elif opcao == 7:
        break

    else:
        print('Opção inválida!')