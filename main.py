import os

def ordenar_arquivo_txt(nome_arquivo):
    # Separa o nome do arquivo da sua extensão (ex: 'lista' e '.txt')
    nome_base, extensao = os.path.splitext(nome_arquivo)
    
    # Cria o nome do novo arquivo
    novo_nome = f"{nome_base} em ordem alfabética{extensao}"
    
    try:
        # Abre o arquivo original para leitura (usando utf-8 para acentos funcionarem bem)
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê todas as linhas e remove quebras de linha vazias no final
            linhas = arquivo.readlines()
            
        # Ordena a lista em ordem alfabética
        # key=str.casefold ajuda a ignorar diferenças entre maiúsculas e minúsculas
        linhas_ordenadas = sorted(linhas, key=str.casefold)
        
        # Cria e escreve no novo arquivo
        with open(novo_nome, 'w', encoding='utf-8') as novo_arquivo:
            novo_arquivo.writelines(linhas_ordenadas)
            
        print(f"✅ Sucesso! O arquivo '{novo_nome}' foi criado com as linhas ordenadas.")
        
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{nome_arquivo}' não foi encontrado. Verifique o nome e tente novamente.")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

# --- Como usar ---
# Coloque o nome do seu arquivo txt aqui embaixo
nome_do_seu_arquivo = "lista-convidados.txt" 
ordenar_arquivo_txt(nome_do_seu_arquivo)