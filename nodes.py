import re
from eu4_parser import parse
from node import Node

with open('D:/source/repos/tradeNodes/eu4_save.eu4') as file:
	save = file.read()
file.close()

tradeBeg = save.find('trade={\n')
tradeEnd = save.find('\n}', tradeBeg)

tradeFile = open('D:/source/repos/tradeNodes/trade_file.txt', 'w')
tradeFile.write(save[tradeBeg:tradeEnd + 2])
tradeFile = open('D:/source/repos/tradeNodes/trade_file.txt')

for rec in parse(tradeFile):
	print(rec)
tradeFile.close()