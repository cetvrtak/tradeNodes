def parse(string):
	db = []
	currentRecord = ''
	oCntr = 0
	cCntr = 0

	for line in string:
		currentRecord += line
		oCntr += line.count('{')
		cCntr += line.count('}')

		if oCntr == cCntr:
			db.append(currentRecord)
			currentRecord = ''
			oCntr = 0
			cCntr = 0

	return db