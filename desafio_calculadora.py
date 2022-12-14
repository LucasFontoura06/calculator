import sys

def lin():
  print('')

def lin2():
  print('-'*35)

def menu1():
  lin()
  print("Bem vindo a calculadora!")
  lin()
  print("Digite: sim / não")
  lin()
  resp = input("Vamos começar? ")
  if resp == "sim":
    lin()
    respostaDoUsuario()
  elif resp == "não":
    lin()
    lin2()
    print("Programa Finalizado!")
    lin()
    print("Que pena, quem sabe da próxima vez!\n\n")
    lin()
    sys.exit()

def respostaDoUsuario():
  lin2()
  print("Opções:\n\n 1 - Soma\n", "2 - Subtração\n", "3 - Multiplicação\n", "4 - Divisão\n")
  resposta = input("Digite sua opção: ")
  lin()
  if resposta == "1":
    calculadoraSoma()
  elif resposta == "2":
    calculadoraSubtracao()
  elif resposta == "3":
    calculadoraMultiplicacao()
  elif resposta == "4":
    calculadoraDivisao()
  else:
    print("Opção Inválida!")
    lin()
    print("Programa Finalizado! Volte sempre.")
    lin()
    sys.exit()

def calculadoraSoma():
  lin2()
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  lin()
  print("Resultado:", num1 + num2)
  lin()
  lin2()
  resp = input("Deseja escolher outro operador? ")
  if resp == "sim":
    lin()
    respostaDoUsuario()
  elif resp == "não":
    lin()
    print("Programa Finalizado! Volte sempre.")
    lin()
    sys.exit()

def calculadoraSubtracao():
  lin2()
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  lin()
  print("Resultado", num1 - num2)
  lin()
  lin2()
  resp = input("Deseja escolher outro operador? ")
  if resp == "sim":
    lin()
    respostaDoUsuario()
  elif resp == "não":
    lin()
    print("Programa Finalizado! Volte sempre.")
    lin()
    sys.exit()

def calculadoraMultiplicacao():
  lin2()
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  lin()
  print("Resultado:", num1 * num2)
  lin()
  lin2()
  resp = input("Deseja escolher outro operador? ")
  if resp == "sim":
    lin()
    respostaDoUsuario()
  elif resp == "não":
    lin()
    print("Programa Finalizado! Volte sempre.")
    lin()
    sys.exit()

def calculadoraDivisao():
  lin2()
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  lin()
  print("Resultado:", num1 / num2)
  lin()
  lin2()
  resp = input("Deseja escolher outro operador? ")
  if resp == "sim":
    lin()
    respostaDoUsuario()
  elif resp == "não":
    lin()
    print("Programa Finalizado! Volte sempre.")
    lin()
    sys.exit()

def main():
  menu1()
  respostaDoUsuario()
  calculadoraSoma()
  calculadoraSubtracao()
  calculadoraDivisao()
  calculadoraMultiplicacao()

main()
