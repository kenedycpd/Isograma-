
def is_isogram(palavra):
     if not isinstance (palavra, str):
             raise TypeError ("insira uma palavra")
     if not palavra:
             isogram = False
     else:
             isogram = len(palavra) == len(set(palavra.lower()))
     return(palavra, isogram)
    
if __name__ == '__main__': 
	print(is_isogram("Machine"))
	print(is_isogram("GeeksforGeeks"))
