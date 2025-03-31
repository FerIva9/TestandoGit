#!/usr/bin/python3

""" Gerador de lero-lero.
Gera frases de efeito sem significado real."""

import random

# Cada frase é composra por três partes aleatórias; aqui,
# listas de possibilidades para cada uma das partes,

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Escolha a lingua: 1 - portugues; 2 - ingles\n"))

if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []


# Combina as partes aleatoriamente
print(random.choice(parte1), random.choice(parte2), random.choice(parte3))


