import flet as ft

def principal(page: ft.Page):
    texto = ft.TextField(label="Digite algo aqui")
    page.add(texto)



ft.app(target=principal)