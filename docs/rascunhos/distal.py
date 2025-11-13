import random

dados = '''carlos:x:1037:1037:Carlos Mateus de Carvalho Gonçalves:/home/carlos:/bin/zsh
  felipe:x:1038:1038:Felipe Alison Jeronimo de Lima:/home/felipe:/bin/zsh
  gabrielm:x:1039:1039:Gabriel Araujo Maia da Silva:/home/gabrielm:/bin/zsh
  gabrielf:x:1040:1040:Gabriel Franco Montenegro:/home/gabrielf:/bin/zsh
  guilherme:x:1041:1041:Guilherme do Nascimento Cavalcanti:/home/guilherme:/bin/zsh
  jackson:x:1042:1042:Jackson Marques de Oliveira:/home/jackson:/bin/zsh
  jefferson:x:1043:1043:Jefferson Matheus Ferreira de Lima:/home/jefferson:/bin/zsh
  joaovitor:x:1044:1044:Joao Vitor da Silva:/home/joaovitor:/bin/zsh
  jonathan:x:1045:1045:Jonathan Freire Bezerra:/home/jonathan:/bin/zsh
  kaua:x:1046:1046:Kaua Henrique Almeida Salvador:/home/kaua:/bin/zsh
  leticia:x:1047:1047:Letícia Geovana Lopes dos Santos:/home/leticia:/bin/zsh
  lourival:x:1048:1048:Lourival Dantas da Silva Neto:/home/lourival:/bin/zsh
  lucas:x:1049:1049:Lucas Denner Hilláryo da Silva:/home/lucas:/bin/zsh
  poliana:x:1050:1050:Maria Poliana Pinheiro de Paiva:/home/poliana:/bin/zsh
  matheus:x:1051:1051:Matheus Eduardo da Silva Carneiro:/home/matheus:/bin/zsh
  rayssa:x:1052:1052:Rayssa de Oliveira Lima:/home/rayssa:/bin/zsh
  samuel:x:1053:1053:Samuel Teotonio da Costa:/home/samuel:/bin/zsh
  sofia:x:1054:1054:Sofia Barros Silva:/home/sofia:/bin/zsh
  yuri:x:1055:1055:Yuri Fabio Alves Ferreira:/home/yuri:/bin/zsh'''.splitlines()

usuarios = [linha.split(':')[0] for linha in dados]

random.shuffle(usuarios)
random.shuffle(usuarios)
random.shuffle(usuarios)

for i,u in enumerate(usuarios, start=2):
    print(f'PC-{i:02d}: {u.title()}')

