import itertools

def generate_codes():
    
    digits = '98765'
    letters = 'PQRWXYZ'
    special_chars = '_#&%'

    
    all_combinations = list(itertools.product(digits, repeat=3))
    all_combinations *= len(letters) * len(special_chars) 

    codes = []

    for digit_combination, letter, special_char in itertools.product(all_combinations, letters, special_chars):
        code = f'COD-{"".join(digit_combination)}{letter}{special_char}'
        codes.append(code)

    return codes


all_codes = generate_codes()
x=[]

for code in all_codes:
    print(code)


size_of_list = len(all_codes)
print(f"Tamaño de la lista de códigos: {size_of_list}")
