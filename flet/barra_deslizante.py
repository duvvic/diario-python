import flet as ft

def principal(page: ft.Page):
    slider = ft.Slider(min=0, max=100, value=10)
    page.add(slider)

ft.app(target=principal)