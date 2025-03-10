

from tabulate import tabulate

dados = [
    ["nome", "idade", "Profissao"],
    ["Guilherme", 21, "analista de dados"],
    ["Joao", 20, "dev front-end"],
    ["Eduardo", 20, "deb back-end"],
]

tabela = tabulate(dados, headers="firstrow", tablefmt="grid")

print(tabela)