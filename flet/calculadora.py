import flet as ft

def  principal(page: ft.Page):
    # Criar campos de texto para os dois numeros
    numero1 = ft.TextField(label="Número 1")
    numero2 = ft.TextField(label="Número 2")
    txt_resultado = ft.Text('') # Campo para mostrar o resultado

    def somar(evento):
        n1 = float(numero1.value)
        n2 = float(numero2.value)
        resultado = n1 + n2
        txt_resultado.value = f'Resultado: {resultado}'
        page.update()

    def subtrair(evento):
        n1 = float(numero1.value)
        n2 = float(numero2.value)
        resultado = n1 - n2
        txt_resultado.value = f'Resultado: {resultado}'
        page.update()

    def multiplicar(evento):
        n1 = float(numero1.value)
        n2 = float(numero2.value)
        resultado = n1 * n2
        txt_resultado.value = f'Resultado: {resultado}'
        page.update()

    def dividir(evento):
        n1 = float(numero1.value)
        n2 = float(numero2.value)
        if n2 == 0:
            txt_resultado.value = 'Erro: Divisão por zero'
        else:
            resultado = n1 / n2
            txt_resultado.value = f'Resultado: {resultado}'
        page.update()  

    # Criar os botões para as operações
    btn_soma = ft.ElevatedButton(text='+', on_click=somar) 
    btn_subtracao = ft.ElevatedButton(text='-', on_click=subtrair)
    btn_multiplicacao = ft.ElevatedButton(text='*', on_click=multiplicar)
    btn_divisao = ft.ElevatedButton(text='/', on_click=dividir)         

    # Adicionar os campos de texto á pagina
    page.add(numero1, numero2, txt_resultado,btn_soma, btn_subtracao, btn_multiplicacao, btn_divisao)


ft.app(target=principal)    