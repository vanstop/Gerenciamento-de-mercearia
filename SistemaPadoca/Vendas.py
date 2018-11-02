#Criado por: Gabriel de Oliveira Belarmino
#Funções do sistema de vendas, registrar produtos a serem comprados, remover produtos da compra, receber em dinheiro e/ou cartão e armazenar a quantidade de dinheiro em cada.

import SistemaPadoca.Estoque

#Variaveis
ProdutosSendoVendidos = []
PreçoTotal = 0
PreçoRecebidoTotal = 0

estadoDaVenda = 1

Dinheiro = {
  "Dinheiro": 0,
  "Cartão": 0
}

print("\nSistema De Compras Iniciado ...\n")
print("------ NOVA COMPRA ------\n")


while estadoDaVenda != 0:

  if estadoDaVenda == 1:
    codigo = input("\nPor favor digite o código do produto: \n[finalizar] para finalizar a compra:\n")

    if codigo == "finalizar":
      estadoDaVenda = 2
    else:
      quantidade = int(input("\nDigite a quantidade: \n"))
      print("\n"*100)

      for p in SistemaPadoca.Estoque.Products:
          if p["Code"] == codigo:
            if p["Amount"] - quantidade >= 0:
              ProdutosSendoVendidos.insert(0, p.copy())
              ProdutosSendoVendidos[0]["Amount"] = quantidade
              p["Amount"] -= quantidade
            else:
              print("\nNão temos essa quantidade do produto")
      
      print("\n      ----------- Lista de compras atual -----------      \n")
      
      print("Code:", " Name:", " Price:", " Amount:")
      PreçoTotal = 0
      for p in ProdutosSendoVendidos:
        print(p["Code"],"  ", p["Name"]," $" + str(p["Price"]), "  ", p["Amount"])
        PreçoTotal += p["Price"] * p["Amount"]
      print("\nTotal: $", PreçoTotal)

  if estadoDaVenda == 2:
    while PreçoRecebidoTotal <= PreçoTotal:
      print("\n"*100)
      print("Valor recebido: ", PreçoRecebidoTotal, "\nValor restante: ", PreçoTotal - PreçoRecebidoTotal)
      metodoDePagamento = input("\nDigite: \n[c] Para pagar com cartão:\n[d] Para pagar com dinheiro:\n")
      PreçoRecebido = int(input("Digite a quantidade a ser paga:\n"))
      PreçoRecebidoTotal += PreçoRecebido
      
      if metodoDePagamento == "c":
        Dinheiro["Cartão"] += PreçoRecebido
      elif metodoDePagamento == "d":
        Dinheiro["Dinheiro"] += PreçoRecebido
      print("\n"*100)

    print("♥ Pagamento Concluido ♥\nTroco: ", PreçoRecebidoTotal - PreçoTotal)
    input("Digite [ENTER] para continuar")
    estadoDaVenda = 3

  if estadoDaVenda == 3:
    #Reseta valores para uma nova compra
    ProdutosSendoVendidos = []
    PreçoTotal = 0
    PreçoRecebidoTotal = 0

    print("\n"*100)
    print("------ NOVA COMPRA ------")

    estadoDaVenda = 1

