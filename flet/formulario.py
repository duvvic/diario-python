import flet as ft
import time

def main(page: ft.Page):
    page.title = "App Completa em Flet"
    page.scroll = "auto"

    # ========== 1. FORMULÁRIO DE CADASTRO COM VALIDAÇÃO ==========

    nome = ft.TextField(label="Nome")
    email = ft.TextField(label="E-mail")
    idade = ft.TextField(label="Idade", keyboard_type="number")
    mensagem_form = ft.Text()

    def enviar_dados(e):
        if not nome.value or not email.value or not idade.value:
            mensagem_form.value = "Todos os campos devem ser preenchidos."
        elif not idade.value.isdigit() or int(idade.value) < 0:
            mensagem_form.value = "Idade inválida. Insira um número positivo."
        else:
            mensagem_form.value = f"Cadastro realizado com sucesso, {nome.value}!"
        page.update()

    botao_enviar = ft.ElevatedButton(text="Cadastrar", on_click=enviar_dados)

    formulario = ft.Column([
        ft.Text("Formulário de Cadastro", size=20, weight="bold"),
        nome,
        email,
        idade,
        botao_enviar,
        mensagem_form
    ])

    # ========== 2. CONTADOR REGRESSIVO ==========

    texto_contador = ft.Text(value="Pronto para iniciar a contagem!", size=18)
    
    def iniciar_contagem(e):
        for i in range(10, -1, -1):
            texto_contador.value = f"Contagem: {i}"
            page.update()
            time.sleep(1)
        texto_contador.value = "Contagem finalizada!"
        page.update()

    botao_contador = ft.ElevatedButton(text="Iniciar Contagem Regressiva", on_click=iniciar_contagem)

    contador = ft.Column([
        ft.Text("Contador Regressivo", size=20, weight="bold"),
        texto_contador,
        botao_contador
    ])

    # ========== 3. QUIZ COM VALIDAÇÃO ==========

    pergunta = ft.Text("Qual é a capital do Brasil?", size=18)
    resultado_quiz = ft.Text()

    def verificar_resposta(e):
        if e.control.text == "Brasília":
            resultado_quiz.value = "✅ Resposta correta!"
        else:
            resultado_quiz.value = "❌ Resposta incorreta. Tente novamente."
        page.update()

    opcoes = ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"]
    botoes_quiz = [ft.ElevatedButton(text=opcao, on_click=verificar_resposta) for opcao in opcoes]

    quiz = ft.Column([
        ft.Text("Quiz de Geografia", size=20, weight="bold"),
        pergunta,
        *botoes_quiz,
        resultado_quiz
    ])

    # ========== ADICIONAR TUDO NA PÁGINA ==========
    page.add(formulario, ft.Divider(), contador, ft.Divider(), quiz)


ft.app(target=main)
