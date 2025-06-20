import flet as ft



def main(pagina: ft.Page):
    def enviar_formulario(event):
        email_usario = email.value
        mensagem_usuario = mensagem.value
        pagina.add(ft.Text(f"Email: {email_usario}", "mensagem: {mensagem_usuario}"))
        email.value = ""
        mensagem.value = ""
        pagina.update()

    def botao_enviar(event):
        if email.value == "" or mensagem.value == "":
            pagina.add(ft.Text("Por favor, preencha todos os campos."))
            return
        else:
            pagina.add(ft.Text("Formulário enviado com sucesso!"))
        pagina.update()


    titulo = ft.Text("Formulário de Contato", size=50)
    pagina.add(titulo)

    email = ft.TextField(hint_text="Digite seu email:")
    pagina.add(email)

    mensagem = ft.TextField(hint_text="Digite sua mensagem:")
    pagina.add(mensagem)

    enviar = ft.ElevatedButton("Enviar", on_click=botao_enviar)
    pagina.add(enviar)

    pagina.update()

ft.app(target=main)
