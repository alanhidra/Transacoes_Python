import json
import tkinter as tk
from tkinter import ttk

def atualizar_saldos():
    transacao = float(entry_transacao.get())
    saldos["cliente"] -= transacao
    saldos["vendedor"] += transacao
    label_saldo_cliente["text"] = f"Novo saldo do cliente: {saldos['cliente']}"
    label_saldo_vendedor["text"] = f"Novo saldo do vendedor: {saldos['vendedor']}"
    
    # Salvar os saldos de volta no arquivo
    with open(nome_arquivo, "w") as file:
        json.dump(saldos, file)

# Nome do arquivo para armazenar os saldos
nome_arquivo = "saldos.json"

# Tente carregar os saldos do arquivo
try:
    with open(nome_arquivo, "r") as file:
        saldos = json.load(file)
except FileNotFoundError:
    # Se o arquivo não existir, crie saldos padrão
    saldos = {"cliente": 1000, "vendedor": 0}

# Criar a janela principal
root = tk.Tk()
root.title("Sistema de Transações")

# Criar widgets
label_transacao = ttk.Label(root, text="Digite o valor da transação:")
entry_transacao = ttk.Entry(root)
button_atualizar = ttk.Button(root, text="Atualizar Saldos", command=atualizar_saldos)
label_saldo_cliente = ttk.Label(root, text=f"Novo saldo do cliente: {saldos['cliente']}")
label_saldo_vendedor = ttk.Label(root, text=f"Novo saldo do vendedor: {saldos['vendedor']}")

# Organizar widgets na grade
label_transacao.grid(row=0, column=0, padx=10, pady=10)
entry_transacao.grid(row=0, column=1, padx=10, pady=10)
button_atualizar.grid(row=1, column=0, columnspan=2, pady=10)
label_saldo_cliente.grid(row=2, column=0, columnspan=2, pady=10)
label_saldo_vendedor.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()