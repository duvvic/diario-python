import flet as ft

def principal(page: ft.Page):
    texto1=ft.Text("texto 1")
    texto2=ft.Text("texto2")

    # Adicionar textos á pagina alinhados no centro
    page.add(
        ft.Column(
            controls=[texto1,texto2],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=principal)

# Esse exemplo mostra como alinhar textos da pagina

# ft.MainAxisAlignment.START  ~ topo
# ft.MainAxisAlignment.CENTER   ~ centralizado
# ft.MainAxisAlignment.END   ~ final
# ft.MainAxisAlignment.SPACE_BETWEEN   ~ espaço entre os itens
# ft.MainAxisAlignment.SPACE_AROUND   ~ espaço ao redor dos itens
# ft.MainAxisAlignment.SPACE_EVENLY   ~ espaço igual entre os itens
