import pyautogui
import openpyxl
import pyperclip

workbook = openpyxl.load_workbook(
    r'/home/rose/portifólio/pa automacão de cadastro/.xlsx')
sheet_produtos = workbook['planilha']
for linha in sheet_planilha.iter_rows(min_row=2, max_row=501):
    produto = linha[0].value
    fornecedor = linha[1].value
    categoria = linha[2].value
    quantidade = linha[3].value
    valor_unitario = linha[4].value
    notificar_venda = linha[5].value

    pyautogui.click(x, y, duration=2)
    pyautogui.write(produto)

    pyautogui.click(x, y, duration=2)
    pyautogui.write(fornecedor)

    pyautogui.click(x, y, duration=2)
    pyperclip.copy(categoria)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(x, y, duration=2)
    pyperclip.copy(valor_unitario)
    pyautogui.hotkey('ctrl', 'v')

    if notificar_venda == "Sim":
        pyautogui.click(x, y, duration=2)
    elif notificar_venda == "Não":
        pyautogui.click(x, y, duration=2)

    pyautogui.click(x, y, duration=2)

    pyautogui.click(x, y, duration=2)
