import flet as ft

def principal(page: ft.Page):
    grupo_opcoes = ft.RadioGroup(content=ft.column([
        ft.Radio(value="vermelho", label="Vermelho"),
        ft.Radio(value="verde", label="Verde"),
        ft.Radio(value="azul", label="Azul")
    ]))

    page.add(grupo_opcoes)



ft.app(target=principal)    