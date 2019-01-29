import time

def inverse_dict(diction,value):
	key_list = list(diction.keys())
	index_to_search = 0
	try:
		index_to_search = list(diction.values()).index(value)
	except Exception as e:
		index_to_search = -1

	if index_to_search == -1:
	 	return value
	else: 
		return key_list[index_to_search] 
	
def en_gre(input_str):
	en_gre =	{
	  "q": ";",
	  "w": "ς",
	  "e": "ε",
	  "r": "ρ",
	  "t": "τ",
	  "y": "υ",
	  "u": "θ",
	  "i": "ι",
	  "o": "ο",
	  "p": "π",
	  "a": "α",
	  "s": "σ",
	  "d": "δ",
	  "f": "φ",
	  "g": "γ",
	  "h": "η",
	  "j": "ξ",
	  "k": "κ",
	  "l": "λ",
	  "z": "ζ",
	  "x": "χ",
	  "c": "ψ",
	  "v": "ω",
	  "b": "β",
	  "n": "ν",
	  "m": "μ",
	  #Uppercase
	  "Q": ":",
	  "W": "ς",
	  "E": "Ε",
	  "R": "Ρ",
	  "T": "Τ",
	  "Y": "Υ",
	  "U": "Θ",
	  "I": "Ι",
	  "O": "Ο",
	  "P": "Π",
	  "A": "Α",
	  "S": "Σ",
	  "D": "Δ",
	  "F": "Φ",
	  "G": "Γ",
	  "H": "Η",
	  "J": "Ξ",
	  "K": "Κ",
	  "L": "Λ",
	  "Z": "Ζ",
	  "X": "Χ",
	  "C": "Ψ",
	  "V": "Ω",
	  "B": "Β",
	  "N": "Ν",
	  "M": "Μ"
	}
	gre_phonienta = {
		"α": "ά",
		"ε": "έ",
		"η": "ή",
		"ι": "ί",
		"ο": "ό",
		"υ": "ύ",
		"ω": "ώ",
		#Uppercase
		"Α": "Ά",
		"Ε": "Έ",
		"Η": "Ή",
		"Ι": "Ί",
		"Ο": "Ό",
		"Υ": "Ύ",
		"Ω": "Ώ"	
	}

	result = ""

	i = len(input_str)-1
	#iterate two at a time except the last one
	while i >= 0:
		if i==1:
			if input_str[i] in en_gre:
				result = en_gre[input_str[i]] + result
			else:
				result = inverse_dict(en_gre,input_str[i]) + result
			i = i - 1	
			continue
		
		if input_str[i-1] == ";":
			if input_str[i] in en_gre:
				if en_gre[input_str[i]] in gre_phonienta:
					result = gre_phonienta[en_gre[input_str[i]]] + result
					i = i - 2
					continue
				else: 
					result = en_gre[input_str[i]] + result
			else:
				result = inverse_dict(en_gre,input_str[i]) + result	
				
		else:
			if input_str[i] in en_gre:
				result = en_gre[input_str[i]] + result
			else:
				result = inverse_dict(en_gre,input_str[i]) + result				
		i = i - 1

	return result

try:
	input_str = clipboard.get_selection()
	time.sleep(0.2)
	result = en_gre(input_str)

	clipboard.fill_clipboard(result)
	keyboard.send_keys('<ctrl>+v')

except Exception as e:
    dialog.info_dialog(title='No text selected', message=e) 