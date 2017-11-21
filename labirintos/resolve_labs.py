# Maze solver, uses DFS

def acha_caminho(inicio, fim, ultimo = []):
    t_min = tam*round(tam/2+0.1)+ tam - round(tam/2+0.1)
    caminho = None
    l_ultimo = ultimo[:] + [inicio]
    if inicio == fim:
        return [fim]
    for op in dictc[str(inicio)]:
        if op in l_ultimo:
            continue
        res = acha_caminho(op, fim, l_ultimo)
        if res == None:
            continue
        if res[-1] == fim and len(res)+1<t_min:
            caminho = [inicio] + res
            t_min = len(caminho)
    return caminho

print("Introduza o nome do ficheiro que contém o labirinto:")
nfic = raw_input()

with open(nfic + ".txt", "r") as f:
    l = [[int(car) for car in linha if car != "\n"] for linha in f]

tam = len(l)

l_util = [(i, j) for i in range(tam) for j in range(tam) if l[i][j]]

dictc = {}
for i, j in l_util:
    l_ligacoes = []
    for x in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
        if x in l_util:
            l_ligacoes.append(x)
    dictc[str((i, j))] = l_ligacoes

print("Introduza as coordenadas do ponto inicial:")
strinput = raw_input()
p_inicio = (int(strinput[strinput.find("(")+1:strinput.find(",")]), int(strinput[strinput.find(",")+1:strinput.find(")")]))

print("Introduza as coordenadas do ponto final:")
strinput = raw_input()
p_fim = (int(strinput[strinput.find("(")+1:strinput.find(",")]), int(strinput[strinput.find(",")+1:strinput.find(")")]))

caminho = acha_caminho(p_inicio, p_fim)

if caminho is None:
    print("Labirinto impossível!")
else:
    l_esc = [linha[:] for linha in l]

    for i, j in caminho:
        l_esc[i][j] = "X"

    with open(nfic[:-4] + "_sol.txt", "w") as f:
        for i in range(tam):
            str_n = ""
            for j in range(tam):
                f.write(str(l[i][j]))
                str_n += str(l_esc[i][j])
            f.write("\t--->\t"+ str_n+ "\n")
    print("Resolvido!")
