import random
import string

# Função para gerar um código seguindo o padrão letras e números alternados
def generate_code():
    code = ""
    for i in range(8):
        if i % 2 == 0:
            code += random.choice(string.ascii_uppercase)  # Letras maiúsculas
        else:
            code += random.choice(string.digits)  # Números
    return code

# Gerando 5 novos códigos
new_codes = [generate_code() for _ in range(5)]
new_codes
print(new_codes)