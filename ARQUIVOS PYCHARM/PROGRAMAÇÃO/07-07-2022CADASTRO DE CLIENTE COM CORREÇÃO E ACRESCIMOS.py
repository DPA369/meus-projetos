#SENAC 190 DILTON ARGOLO
#Cadastro de clientes

cliente=input("informe nome do cliente")
CPF=input("informe nome do CPF")
#QUANDO SE TRATA DE UM NOME COMPOSTO USE UNDERLINE
data_de_nascimento=input("informe data de nascimento")
endereco=input("informe seu endereço")
profissao=input("qual sua profissao")
#O PRINT VAI EXIBIR NA TELA AS INFORMAÇÕES OBTIDAS
#PRINT SIMPLE SÓ COM AS VARIÁVEIS
print(cliente,CPF,data_de_nascimento,profissao,endereco)
#COM ESSE PRINT, VOCÊ PULA UMA LINHA NA EXIBIÇÃO DO CÓDIGO print("\n")
#PRINT COM TEXTOS ADCIONAIS, COLOCANDO O f FORA DAS ""
#E DENTRO DAS CHAVES{} COLOCA O NOME DA VARIÁVEL QUE VOCÊ QUER EXIBIR
print(f"nome do cliente:{cliente},CPF:{CPF} nascimento{data_de_nascimento}, tem o endereço)
#PRIN COM TEXTOS ADICIONAIS, COLOCANDO O f fora das ""
# E DENTRO DAS {} COLOCA O NOME DA VARIÁVEL QUE VOCÊ QUER DEIXAR
print(f"nome do cliente:{cliente},CPF:{CPF}nascimento{data_de_nascimento},tem o endereço{endereço}, profissao{profissao}")