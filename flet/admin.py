import flet as ft 

cadastros = []

def main(pagina:ft.Page):
    def clicar_botao(event):
        pagina.add(ft.Text("Cadastro realizado com sucesso!"))
        nome_usuario = nome.value
        senha_usuario = senha.value
        cpf_usuario = cpf.value
        cadastros.append({
            "nome": nome_usuario,
            "senha": senha_usuario,
            "cpf": cpf_usuario
        })
        nome.value = ""
        senha.value = ""
        cpf.value = ""


        pagina.update()

    def botao_adm(event):
        if nome.value != "admin" or senha.value != "123":
            pagina.add(ft.Text("Acesso negado!"))
            return
        else:
            pagina.add(ft.Text("Acesso concedido!"))    
            for cadastro in cadastros:
                pagina.add(ft.Text(f"Nome: {cadastro['nome']}, CPF: {cadastro['cpf']}"))
        pagina.update()


    titulo = ft.Text("Formulário de Cadastro",size=50)
    pagina.add(titulo)

    nome = ft.TextField(hint_text="Digite seu nome:")

    pagina.add(nome)

    senha = ft.TextField(hint_text="Digite sua senha:",password=True)
    pagina.add(senha)

    cpf = ft.TextField(hint_text="Digite seu cpf")
    pagina.add(cpf)

    cadastrar = ft.ElevatedButton("Cadastrar",on_click=clicar_botao)
    pagina.add(cadastrar)

    listar = ft.ElevatedButton("Admin",on_click= botao_adm)
    pagina.add(listar)

ft.app(target=main)