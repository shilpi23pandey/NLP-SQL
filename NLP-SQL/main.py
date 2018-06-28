import wordIdentifier as wI
import codeGenerator as cG

def processQuery(query):
	#query=input("Enter the Query :")
	#print(query)
	query=query.lower()
	
	#wordIdentifier tokenizes sentences and tags words and segregates into numerals,keywords etc.,  
	tokens,keywords,tagged,numerals=wI.wordIdentifier(query)
	
	#queryGenerator forms the Sql query 
	sqlQuery = cG.queryGenerator(tagged,keywords,numerals,tokens)
	return sqlQuery	
	
