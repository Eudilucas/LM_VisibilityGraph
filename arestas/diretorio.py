import os

diretorio = "/home/eude/Desktop/IC/caos/arestas/LM_p1/"

# Lista todos os arquivos do diretório com a extensão .txt
arquivos_txt = [arquivo for arquivo in os.listdir(diretorio)]

#print(arquivos_txt)

for arquivo in arquivos_txt:
	caminho_completo = os.path.join(diretorio, arquivo)#concateno os valores de 
	print(caminho_completo)
'''    
    with open(caminho_completo, "r") as arquivo_aberto:
        conteudo = arquivo_aberto.read()
        
    print(f"Conteúdo de {arquivo}:")
    print(conteudo)
    print("-" * 20)  # Separador entre os arquivos
'''
