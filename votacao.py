import hashlib
import os
import sqlite3

dirpath = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(dirpath, 'dados.db')
con = sqlite3.connect(data)
c = con.cursor()

print("""
Candidato 1 = 01
Candidato 2 - 02
Candidato 3- 03
""")

print("")
nome = input("Insira seu nome: ")
cpf = input("Insira seu CPF: ")
print("")
voto = input("Insira seu Voto: ")

codename = nome.encode('utf-8')
codecpf = cpf.encode('utf-8')

hashname = hashlib.sha1(codename)
hashcpf = hashlib.sha1(codecpf)

digname = hashname.hexdigest()
digcpf = hashcpf.hexdigest()

c.execute("SELECT 1 FROM eleitores WHERE CPF = ?", (digcpf,))
inspecao = c.fetchone()
if inspecao:
    print('Voto negado! Você já votou.')
elif voto == '01':
    c.execute("INSERT INTO eleitores (nome, CPF, voto) VALUES (?, ?, ?)", (digname, digcpf, voto))
    con.commit()
    c.execute("UPDATE candidatos SET votos = (votos + 1) WHERE nome = 'Candidato 1'")
    con.commit()
    print('Voto Confirmado')
elif voto == '02':
    c.execute("INSERT INTO eleitores (nome, CPF, voto) VALUES (?, ?, ?)", (digname, digcpf, voto))
    con.commit()
    c.execute("UPDATE candidatos SET votos = (votos + 1) WHERE nome = 'Candidato 2'")
    con.commit()
    print('Voto confirmado')
elif voto == '03':
    c.execute("INSERT INTO eleitores (nome, CPF, voto) VALUES (?, ?, ?)", (digname, digcpf, voto))
    con.commit
    c.execute("UPDATE candidatos SET votos = (votos + 1) WHERE nome = 'Candidato 3'")
    print("Voto confirmado")
else:
    c.execute("INSERT INTO eleitores (nome, CPF, voto) VALUES (?, ?, ?)", (digname, digcpf, 'Branco/Nulo'))
    con.commit
    c.execute("UPDATE candidatos SET votos = (votos + 1) WHERE nome = 'Branco/Nulo'")
    print("Voto confirmado")


con.close()