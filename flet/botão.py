import flet as ft

def principal(page: ft.Page):
    def click_botao(evento):
        texto_botao=ft.Text("Você clicou no botão!")
        page.add(texto_botao)

    texto = ft.Text("Olá a todos, estou desenvolvendo com Flet!")
    botao = ft.ElevatedButton(text="Esse botão agora é clicavel", on_click=click_botao)
    page.add(texto,botao)

ft.app(target=principal)