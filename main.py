import os

email = input("Informe o inicio do seu email antes do @: ")
op = 0
email_final = ""

while(len(email) <= 5):
    email = input("Informe um email válido, com mais de 5 caracteres, até o @: ")

print("\nNome de email válido!\n")

while(op != 4):
    print("Dominio de Email:")
    print("""
    ---------------------------
    1 - @ifpr.edu.br
    2 - @gmail.com
    3 - @hotmail.com
    4 - Outro
    ---------------------------
""")
    op = int(input("Escolha uma opção: "))
    print("")
    if (op == 1):
        email_final = email + "@ifpr.edu.br"
        break
    elif(op == 2):
        email_final = email + "@gmail.com"
        break

    elif(op == 3):
        email_final = email + "@hotmail.com"
        break
    else:
        print("Informe o final do email, exemplo: @gmail.com")
        outro_email = input("Final do email: ")
        while(not("@" in outro_email and ".com" in outro_email)):
            outro_email = input("Email inválido, .com esperado no final, insira novamente: ")
        email_final = email + outro_email
        break

print(f"\nSeu email: {email_final}\n")

correto = input("Seu email está correto? (S) Sim ou Não (N)").upper()
while(correto != "S"):
    exit()

msg_commit = input("\nInforme a menssagem do seu commit: ")
while(len(msg_commit) <= 10):
    msg_commit= input("\nMensagem muito pequena, insira novamente uma mensagem mais detalhada de seu commit!\ncommit: ")


print(f"\nSeu email: {email_final}\nSua mensagem de commit: {msg_commit}\n")

print("Executando comandos......")

comando = f"git config user.email \"{email_final}\""
os.system(comando)
comando = f"git add *"
os.system(comando)
comando = f"git commit -m \"{msg_commit}\""
os.system(comando)
comando = f"git push"
os.system(comando)

print("Comandos executados com sucesso, programa finalizado.")