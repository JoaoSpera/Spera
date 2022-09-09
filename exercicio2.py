"""
Algoritimo que recebe uma senha
e retorna se está logado ou que a senha está incorreta
Autor: João Pedro de OLiveira Spera
"""
sc = 'Senha123@'
while True:
    
    s = str(input("qual é a senha:"))

    if s == 'Senha123@':
        print("Senha correta, você está logado")
        break

    else:
        print("Senha incorreta, digite novamente")
    
    
