class Estoque:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, validade, quantidade):
        self.itens.append({'nome': nome, 'validade': validade, 'quantidade': quantidade})

    def excluir_item(self, nome):
        self.itens = [item for item in self.itens if item['nome'] != nome]

    def ver_validade_quantidade(self, nome):
        for item in self.itens:
            if item['nome'] == nome:
                return f"Validade: {item['validade']}, Quantidade: {item['quantidade']}"
        return "Item não encontrado no estoque."

    def organizar_por_nome(self):
        self.itens = sorted(self.itens, key=lambda x: x['nome'])

    def organizar_por_validade(self):
        self.itens = sorted(self.itens, key=lambda x: x['validade'])

    def mostrar_estoque(self):
        for item in self.itens:
            print(f"Nome: {item['nome']}, Validade: {item['validade']}, Quantidade: {item['quantidade']}")


estoque = Estoque()

while True:
    print("\n=== MENU ===")
    print("1. Adicionar Item")
    print("2. Excluir Item")
    print("3. Ver Validade e Quantidade de um Item")
    print("4. Organizar por Nome")
    print("5. Organizar por Validade")
    print("6. Mostrar Estoque")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do item: ")
        validade = input("Validade do item: ")
        quantidade = input("Quantidade do item: ")
        estoque.adicionar_item(nome, validade, quantidade)
        print("Item adicionado ao estoque.")

    elif opcao == '2':
        nome = input("Nome do item a ser excluído: ")
        estoque.excluir_item(nome)
        print("Item excluído do estoque.")

    elif opcao == '3':
        nome = input("Nome do item: ")
        print(estoque.ver_validade_quantidade(nome))

    elif opcao == '4':
        estoque.organizar_por_nome()
        print("Estoque organizado por nome.")

    elif opcao == '5':
        estoque.organizar_por_validade()
        print("Estoque organizado por validade.")

    elif opcao == '6':
        print("\n=== ESTOQUE ===")
        estoque.mostrar_estoque()

    elif opcao == '7':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
