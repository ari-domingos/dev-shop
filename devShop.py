import os
vendas = []

def calcularTotal(valorDoProduto, estado, tipoDoFrete):
    if estado == 'SP' or estado == 'RJ':
        valorImposto = valorDoProduto * 1.10
    else:
        valorImposto = valorDoProduto * 1.07

    if tipoDoFrete == 1:
        frete = 20
    else:
        frete = 50

    if valorDoProduto > 1000:
        frete = 0

    totalFinal = valorImposto + frete
    return totalFinal

def registrarVendas():
    print("\n===== REGISTRAR VENDA =====")
    idPedido = int(input('ID: '))
    nomeDoProduto = input('Produto: ').capitalize()
    valorDoProduto = float(input('Preço do produto: R$')) 
    estado = input('Estado de destino: ').upper()
    
    print('\n==== TIPO DE FRETE ====')
    print("1. Padrão (R$ 20,00)\n2. Express (R$ 50,00)")
    print('-------------------')
    
    tipoDoFrete = int(input("Frete (1 ou 2): "))
    if tipoDoFrete == 1:
        freteTexto = 'Padrão'
    elif tipoDoFrete == 2:
        freteTexto = 'Express'
    else:
        print('Escolha entre 1 - 2')
        return  
    
    totalFinal = calcularTotal(valorDoProduto, estado, tipoDoFrete)
    
    status = 'Aguardando Pagamento'
    
    novaVenda = {
        'id': idPedido,              
        'produto': nomeDoProduto,    
        'valor': valorDoProduto,
        'estado': estado,
        'frete': freteTexto,
        'status': status,
        'total': totalFinal         
    }
    
    vendas.append(novaVenda)
    print(f'\nVenda ID:{idPedido} registrada com sucesso!')

def exibirRelatorio():
    print("\n===== VENDAS CADASTRADAS =====")
    
    for venda in vendas:  
        print(f"\nID: {venda['id']}")
        print(f"Produto: {venda['produto']}")
        print(f"Valor: R$ {venda['valor']:.2f}")
        print(f"Estado: {venda['estado']}")
        print(f"Frete: {venda['frete']}")
        print(f"Total: R$ {venda['total']:.2f}")  
        print(f"Status: {venda['status']}")

while True:
    print('\n======== DEVSHOP MANAGER =======')
    print('')
    print('1. Registrar nova venda')
    print('2. Calcular preço final')
    print('3. Exibir relatório de vendas')
    print('4. Confirmar pagamento')
    print('5. Sair')
    print('-------------------------')
    opcaoDoMenu = int(input('Digite sua opção: '))

    if opcaoDoMenu == 1:
        os.system('cls')
        registrarVendas()
        input("\nPressione Enter para continuar...")
        os.system('cls')

    elif opcaoDoMenu == 2:
        os.system('cls')
        print("\n===== CALCULADORA =====")
        valor = float(input("Valor do produto R$: "))
        estado = input("Estado de destino: ").upper()
        print("1. Padrão (R$ 20,00)\n2. Express (R$ 50,00)")
        frete = int(input("Frete (1 ou 2): "))
        resultado = calcularTotal(valor, estado, frete)
        print(f"\nTotal: R$ {resultado:.2f}")
        
        input("\nPressione Enter para continuar...")
        os.system('cls')

    elif opcaoDoMenu == 3:
        os.system('cls')
        exibirRelatorio()

        input("\nPressione Enter para continuar...")
        os.system('cls')

    elif opcaoDoMenu == 4:
        os.system('cls')
        print("\n===== CONFIRMAR PAGAMENTO =====")
        idBusca = int(input("ID do pedido: "))
            
        for venda in vendas:
            if venda['id'] == idBusca:
                print(f"\nPedido encontrado: {venda['produto']}")
                print(f"Status atual: {venda['status']}")                    
                opcaoDoPagamento = input("Confirmar pagamento? (s/n): ").lower()
                    
                if opcaoDoPagamento == 's':
                    venda['status'] = 'Pago/Enviado'
                    print("Pagamento confirmado!")
                else:
                    print("Aguardando Pagamento")
                    break
            else:
                print(f"Pedido ID:{idBusca} não encontrado.")
            
        input("\nPressione Enter para continuar...")
        os.system('cls')

    elif opcaoDoMenu == 5:
        os.system('cls')
        print('\n-----------------------------')
        print('     Saindo do Sistema...')
        print('')
        break

    else:
        os.system('cls')
        print('\n-----------------------------')
        print('Digite um número entre 1 - 5')
        input("\nPressione Enter para continuar...")
        os.system('cls')