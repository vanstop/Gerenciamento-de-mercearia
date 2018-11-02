#Criado por: Gabriel de Oliveira Belarmino
#Funções do estoque, armazenar a quantidade e os preços dos produtos e alterar a quantidade dos produtos ja existentes

Products = [] 
_estadoEstoque = 1;

def NewProduct(code, name, price, amount):
  #TODO verificar se o código ou o nome ja existem
  Product = {
  "Code": code,
  "Name": name,
  "Price": float(price),
  "Amount": int(amount)
  }

  Products.append(Product)

NewProduct("155", "Leite", 3.50, 10)
NewProduct("156", "Cafe", 4.20, 7)

def ChangeAmount(code, difference):
  #TODO verificar se a nova quantidade é valida.
  for p in Products:
    if p.get("Code") == code:
      p["Amount"] += difference #pamount = pamount + diference
      print("Quantidade do produto alterada, a nova quantidade é %s. \n" %(p.get("Amount")))

def ProductExist(code):
  for p in Products:
    if p["Code"] == code:
      return True
    
  return False
'''
while _estadoEstoque != 0 :

  print("\n"*100)

  _estadoEstoque = int(input("Digite:\n [1] Para adicionar ou remover produtos do estoque\n [2] Para consultar o estoque\n [3] Para adicionar um novo produto ao estoque\n [0] Para sair do estoque\n"))
  print("\n"*100)

  if _estadoEstoque == 1:
    _codeToModify = input("Digite o código do produto que deseja alterar: \n")
    print("\n"*100)

    if(ProductExist(_codeToModify)):
      for p in Products:
          if p["Code"] == _codeToModify:
            print(p)

            _amountToChange = int(input("\nDigite o quanto deseja alterar a quantidade deste produto:\n\nNumeros Positivos: para adicionar produtos\nNumeros Negativos: para subitrair produtos\n"))
            print("\n"*100)

            ChangeAmount(_codeToModify, _amountToChange)

            input("\nAperte [Enter] para sair")
    else:
      print("Código invalido.")
      input("\nAperte [Enter] para sair")
  
  if _estadoEstoque == 2:
    _codeToConsult = input("Digite o código do produto a ser consultado ou digite [0] para ver todo o estoque: \n")
    print("\n"*100)

    if _codeToConsult == "0":
      for p in Products:
        print(p)
      input("\nAperte [Enter] para sair")
    else:
      if(ProductExist(_codeToConsult)):
        for p in Products:
          if p["Code"] == _codeToConsult:
            print(p)
            input("\nAperte [Enter] para sair")
      else:
        print("Código invalido.")
        input("\nAperte [Enter] para sair")

  if _estadoEstoque == 3:
    _code = input("Digite o código para o novo produto: \n")

    if(ProductExist(_code)):
      print("\n"*100)
      print("Esse código ja esta em uso.")
      input("\nAperte [Enter] para sair")
    else:
      _name = input("Digite o nome para o novo produto: \n")
      _price = input("Digite o preço para o novo produto: \n")
      _amount = int(input("Digite a quantidade para o novo produto: \n"))

      NewProduct(_code, _name, _price, _amount)

  if _estadoEstoque == 0:
    print("\nObrigado por usar Tabajara Sistemas.")
'''