# Abrindo os arquivos
entrada = open("bacteria.fasta").read()
saida = open("bacteria.html", "w")  # Corrigido para modo de escrita

# Inicializando o dicionário de contagem
cont = {}
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i + j] = 0

# Filtrando a entrada (remover cabeçalhos e caracteres inválidos)
linhas = entrada.splitlines()
sequencia = ""
for linha in linhas:
    if not linha.startswith(">"):  # Ignorar linhas de cabeçalho
        sequencia += linha.strip()  # Adicionar apenas a sequência de nucleotídeos

# Contando os pares de nucleotídeos
for k in range(len(sequencia) - 1):
    par = sequencia[k] + sequencia[k + 1]
    if par in cont:  # Apenas pares válidos
        cont[par] += 1

# Gerando o HTML
i = 1
for k in cont:
    transparencia = cont[k] / max(cont.values()) if max(cont.values()) > 0 else 0
    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; "
                "height:100px; float:left; background-color:rgba(0,0,0," + str(transparencia) + ")'>"
                + k + "</div>")

    if i % 4 == 0:
        saida.write("<div style='clear:both;'></div>")
    i += 1

saida.close()
