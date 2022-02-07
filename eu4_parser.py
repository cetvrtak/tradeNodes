def parse(string):
	db = {}
	currentRecord = ''
	oCntr = 0
	cCntr = 0

	for line in string:
		print(line)
		currentRecord += line
		oCntr += line.count('{')
		cCntr += line.count('}')

		if oCntr == cCntr:
			print('Loading', currentRecord[0:currentRecord.find('=')])
			db[currentRecord[0:currentRecord.find('=')]] = currentRecord
			currentRecord = ''
			oCntr = 0
			cCntr = 0

	return db