import flet as ft

def principal(page: ft.Page):


    texto = ft.Text(value="Esse é um texto de exemplo.")
    page.add(texto)

ft.app(target=principal)