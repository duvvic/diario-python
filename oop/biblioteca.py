class Livro:
    def __init__(self, id, titulo, ano_publi):
        self.id = id
        self.titulo = titulo
        self.ano_publi = ano_publi
        self.status = "disponível"

    def __str__(self):
        return f"[{self.id}] {self.titulo} ({self.ano_publi}) - {self.status}"


class Membro:
    def __init__(self, nome_completo, registro_membro):
        self.nome_completo = nome_completo
        self.registro_membro = registro_membro
        self.historico_de_livros_emprestados = []

    def __str__(self):
        return f"{self.nome_completo} (Reg: {self.registro_membro})"


class Biblioteca:
    def __init__(self):
        self.lista_de_membros = []
        self.catalogo_de_livros = []

    def adicionar_livro(self):
        id = int(input("ID do livro: "))
        titulo = input("Título: ")
        ano = int(input("Ano de publicação: "))
        self.catalogo_de_livros.append(Livro(id, titulo, ano))
        print("📚 Livro adicionado com sucesso!")

    def adicionar_membro(self):
        nome = input("Nome completo: ")
        registro = input("Registro do membro: ")
        self.lista_de_membros.append(Membro(nome, registro))
        print("👤 Membro registrado com sucesso!")

    def emprestar_livro(self):
        id_livro = int(input("ID do livro para emprestar: "))
        registro_membro = input("Registro do membro: ")

        livro = next((l for l in self.catalogo_de_livros if l.id == id_livro), None)
        membro = next((m for m in self.lista_de_membros if m.registro_membro == registro_membro), None)

        if livro and membro:
            if livro.status == "disponível":
                livro.status = "emprestado"
                membro.historico_de_livros_emprestados.append(livro.titulo)
                print(f"✅ Livro '{livro.titulo}' emprestado para {membro.nome_completo}.")
            else:
                print("❌ Livro já está emprestado.")
        else:
            print("❌ Livro ou membro não encontrado.")

    def devolver_livro(self):
        id_livro = int(input("ID do livro para devolver: "))
        livro = next((l for l in self.catalogo_de_livros if l.id == id_livro), None)

        if livro:
            if livro.status == "emprestado":
                livro.status = "disponível"
                print(f"📦 Livro '{livro.titulo}' devolvido com sucesso!")
            else:
                print("❌ Esse livro já está disponível.")
        else:
            print("❌ Livro não encontrado.")

    def listar_livros(self):
        if self.catalogo_de_livros:
            print("\n📚 Catálogo de Livros:")
            for livro in self.catalogo_de_livros:
                print(livro)
        else:
            print("Nenhum livro cadastrado.")

    def listar_membros(self):
        if self.lista_de_membros:
            print("\n👥 Lista de Membros:")
            for membro in self.lista_de_membros:
                print(membro)
        else:
            print("Nenhum membro registrado.")

    def historico_membro(self):
        registro = input("Registro do membro: ")
        membro = next((m for m in self.lista_de_membros if m.registro_membro == registro), None)
        if membro:
            print(f"\n📜 Histórico de livros de {membro.nome_completo}:")
            if membro.historico_de_livros_emprestados:
                for livro in membro.historico_de_livros_emprestados:
                    print(f"- {livro}")
            else:
                print("Nenhum livro emprestado ainda.")
        else:
            print("❌ Membro não encontrado.")


# =========================
# MENU INTERATIVO
# =========================
biblioteca = Biblioteca()

while True:
    print("\n=== 📖 MENU DA BIBLIOTECA ===")
    print("1. Adicionar livro")
    print("2. Adicionar membro")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Listar livros")
    print("6. Listar membros")
    print("7. Histórico de membro")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        biblioteca.adicionar_livro()
    elif opcao == "2":
        biblioteca.adicionar_membro()
    elif opcao == "3":
        biblioteca.emprestar_livro()
    elif opcao == "4":
        biblioteca.devolver_livro()
    elif opcao == "5":
        biblioteca.listar_livros()
    elif opcao == "6":
        biblioteca.listar_membros()
    elif opcao == "7":
        biblioteca.historico_membro()
    elif opcao == "0":
        print("👋 Encerrando o sistema...")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")
