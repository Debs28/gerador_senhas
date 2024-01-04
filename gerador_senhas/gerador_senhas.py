import random
import string


class Api:
    def gerar_senha(self, tamanho_senha):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''
        tamanho_senha = int(tamanho_senha)
        for i in range(tamanho_senha):
            senha += random.choice(caracteres)
        return senha
