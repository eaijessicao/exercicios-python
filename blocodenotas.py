import tkinter as tk

def salvar():
    texto = caixa_texto.get("1.0", "end-1c") # Pega o conteúdo da caixa de texto
    with open("bloco_de_notas.txt", "w") as arquivo: # Cria ou abre o arquivo em modo de escrita
        arquivo.write(texto) # Escreve o conteúdo no arquivo

janela = tk.Tk()
janela.title("Bloco de Notas")

caixa_texto = tk.Text(janela)
caixa_texto.pack()

botao_salvar = tk.Button(janela, text="Salvar", command=salvar)
botao_salvar.pack()

janela.mainloop()
