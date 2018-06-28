#code generator
import relation as rel
import attribute as atr
import schema as sch
from nltk.corpus import stopwords
def queryGenerator(tagged,keywords,numerals,query):
	table = []
	attribute = []
	special = []
	
	#Create table[] , attribute[], special[]
	for word in tagged:
		if word[0] in rel.relationList:
			table.append(rel.relationList[word[0]])
		elif word[0] in atr.attributeList:
			for temp in atr.attributeList[word[0]]:
				attribute.append(temp)
		elif word[0] not in numerals:
			special.append(word[0])
			
	for attr in attribute:
		table.append(sch.tableAttributeList[attr])
	table = list(set(table))
	
	#if no attribute is found, all attibutes to be selected	
	if(len(attribute)==0):
		attribute.append('*')
	else:
		attribute = list(set(attribute))
		
		
	print("Table Attribute Special List CodeGenerator.py ")
	print(table)
	print(attribute)
	print(special)
	print("x_x")
	
	
	#join condition if >1 tables
	joinCond = ''
	if(len(table)>1):
		joinCond = 'department.dId=student.dId '
		
	boolean = ['or','and']
	booleanDict = {}
	
	#Numeral processing and relational operation
	relOpn={'greater than' : '>', 'less than': '<' , 'more than' : '>'}
	numAttrList={}
	numOp={}
	for num in numerals:
		#relational operation for each numeral
		numIndex=query.index(num)
		if (numIndex+1)<len(query) and query[numIndex+1] in boolean:
			booleanDict[num] = query[numIndex+1]
		temp = ' '.join([query[numIndex-2], query[numIndex-1]]).lower()
		temp.strip(' ')
		if temp in relOpn:
			numOp[num]=relOpn[temp]
		else:
			numOp[num]='='
		
		#attribute for each numeral
		for i in range(1,5):
			identified=False
			if numIndex-i>-1 :
				if query[numIndex-i] in atr.attributeList:
					print(query[numIndex-i])
					numAttrList[num]=atr.attributeList[query[numIndex-i]]
					identified=True
			if identified==True:
				break		
	print('relational operation for each numeral')
	print(numOp)
	print('num attribute list')
	print(numAttrList)
	print("x_x")
	
	#mysql code for numerical condition
	numCond=[]
	for item in numAttrList:
		temp=numAttrList[item][0]+numOp[item]+item
		if item in booleanDict:
			temp = temp + ' ' + booleanDict[item]
		numCond.append(temp)
	print('Numeral conditions')
	print(numCond)
	
	stopw = ['need','i','fetch','give','all','find','display','greater','less','more','than','list', 'show','select', 'out', 'number','select',',','get','retrieve','print','tell','having','whose','details'] + stopwords.words('english')
	
	
	#condition list for non numeric attributes
	condList = {}
	for item in special:
		if item not in stopw:
			itemIndex = query.index(item)
			if (itemIndex+1)<len(query) and query[itemIndex+1] in boolean:
				booleanDict[item] = query[itemIndex+1]		
			identified = False
			for i in range(1,3):	
				if(itemIndex-i>=0):
					if query[itemIndex-i] in atr.attributeList:
						if item not in condList:
							condList[item] = atr.attributeList[query[itemIndex-i]]
				if(itemIndex+i<len(query)):
					if query[itemIndex+i] in atr.attributeList:
						if item not in condList:
							condList[item] = atr.attributeList[query[itemIndex+i]]
	
	print('Condition list')
	print(condList)
	
	#where clause involving 'and' and 'or' with numeral and string attributes
	whereClause = []
	for item in condList:
		temp = ''
		print(item)
		if(len(condList[item])>1):
			temp += ' ( '
			for attr in condList[item]:
				temp = temp+attr+'="'+item+'" or '
			temp = temp[:len(temp)-3]
			temp += ' ) '
			if item in booleanDict:
				temp = temp + ' ' + booleanDict[item]
			whereClause.append(temp)
			
		else:
			temp = condList[item][0]+'="'+item+'"'
			if item in booleanDict:
				temp = temp + ' ' + booleanDict[item]
			whereClause.append(condList[item][0]+'="'+item+'"')
		
	
	print('Where Clause List ')
	print(whereClause)
	print('x_x')
	
	selectAll = ['details','records','record','detail']
	for word in selectAll:
		if word in query:	
			attribute = ['*']
	
	#final where clause with attributes ,'or' and 'and' condition in proper order
	finalWhereclause=[]
	temp=[]
	for item in whereClause:
		if(item[len(item)-1]=='r' and item[len(item)-2]=='o'):
			finalWhereclause.append(item)
		if(item[len(item)-1]=='d' and item[len(item)-2]=='n'):
			finalWhereclause.append(item)	
		else:
			temp.append(item)
	for item in numCond:
		if(item[len(item)-1]=='r' and item[len(item)-2]=='o'):
			finalWhereclause.append(item)
		if(item[len(item)-1]=='d' and item[len(item)-2]=='n'):
			finalWhereclause.append(item)	
		else:
			temp.append(item)
			
	if(len(temp)>0):
		finalWhereclause.append(temp[0])
	print('finalWhereclause')
	print(finalWhereclause)
	
	execQuery='SELECT '
	
	#inserting attributes
	for index in range(0,len(attribute)-1):
		execQuery+=attribute[index]+', '
	execQuery+=attribute[len(attribute)-1]
	execQuery+=' FROM '
	
	#inserting tables
	for index in range(0,len(table)-1):
		execQuery+=table[index]+', '
	execQuery+=table[len(table)-1]
	
	if(len(joinCond)>0 or len(finalWhereclause)>0):
		execQuery+=' WHERE '
	#join condition
	execQuery+=joinCond
	
	if len(finalWhereclause)>0 and len(joinCond)>0:
		execQuery+=' and '
		
	for item in finalWhereclause:
		execQuery+=item+' '
		
	execQuery+=';'
	
	print('Final Query')
	print(execQuery)
	return execQuery
