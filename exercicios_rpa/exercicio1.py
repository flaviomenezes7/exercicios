"""
1 - Crie um script que extraia todo o texto de um arquivo PDF e salve em um arquivo

"""
import PyPDF2

def extrair_texto_pdf(pdf_arquivo, txt_arquivo): # recebe como parametro o arquivo pdf e o arquivo txt
    with open(pdf_arquivo, 'rb') as pdf: # abre o arquivo pdf em modo leitura binaria por que o pdf é um arquivo binario
        leitor = PyPDF2.PdfReader(pdf) 
        texto = '' # inicia uma variavel vazia para armazenar o texto extraido do pdf
        for pagina in leitor.pages:
            texto += pagina.extract_text()
    
    # o arquivo será criado automaticamente se não existir
    with open(txt_arquivo, 'w', encoding='utf-8') as txt:
        txt.write(texto)
        
# gera o arquivo 'arquivo.txt' com o texto extraído do PDF
extrair_texto_pdf(r'C:\Users\mnzfl\exercicios\exercicios_rpa\cv_flavio.pdf', 'arquivo.txt')