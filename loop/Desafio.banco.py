senha_correta=123456
iteracao=3
while iteracao>0:
    print("Voce tem {iteracao} tentativas")
    senha=int(input("Digite sua Senha: "))
    if senha!= senha_correta:
      print("Senha incorreta")
      itercao=1
    else:
        print("Senha correta")
        print(f"Olá Marcos. Sejá Bem vindo ao nosson Banco!")
        break
    if iteracao==0:
       print('Sua senha foi Bloqueada! Por favor Dirija-se a um dos nossos Caixas')