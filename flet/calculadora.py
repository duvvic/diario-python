import flet as ft 


def main(pagina:ft.Page):    #função principal que cria a pagina da calculadora
    def somar(event):
        valor_numero1 = numero1.value
        valor_numero2 = numero2.value

        resultados.value = int(valor_numero1) + int(valor_numero2)
        numero1.value = ""
        numero2.value = ""
        pagina.update()

    def subtrair(event):
        valor_numero1 = numero1.value
        valor_numero2 = numero2.value

        resultados.value = int(valor_numero1) - int(valor_numero2)
        numero1.value = ""
        numero2.value = ""
        pagina.update()

    def multiplicar(event):
        valor_numero1 = numero1.value
        valor_numero2 = numero2.value

        resultados.value = int(valor_numero1) * int(valor_numero2)
        numero1.value = ""
        numero2.value = ""
        pagina.update()

    def dividir(event): 
        valor_numero1 = numero1.value
        valor_numero2 = numero2.value

        if int(valor_numero2) == 0:
            resultados.value = "Erro: Divisão por zero"
        else:
            resultados.value = int(valor_numero1) / int(valor_numero2)
        numero1.value = ""
        numero2.value = ""
        pagina.update()

    pagina.title = "Calculadora Simples"
    


  

    numero1 = ft.TextField(hint_text="Digite o primeiro número:")
    numero2 = ft.TextField(hint_text="Digite o segundo número:")

    pagina.add(numero1,numero2)

    botao_somar = ft.ElevatedButton("+",on_click=somar)
    botao_subtrair = ft.ElevatedButton("-",on_click=subtrair)
    botao_multiplicar = ft.ElevatedButton("*",on_click=multiplicar)
    botao_dividir = ft.ElevatedButton("/",on_click=dividir)

    pagina.add(botao_somar, botao_subtrair, botao_multiplicar, botao_dividir)



    
    resultados = ft.Text()
    pagina.add(resultados)
    
ft.app(target=main)