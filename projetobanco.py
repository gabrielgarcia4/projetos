class Cliente:
    def __init__(self,nome,CPF,endereço,cidade,estado,telefone):
        self._nome=nome
        self._CPF=CPF
        self._endereço=endereço
        self._cidade=cidade
        self._estado=estado
        self._telefone=telefone
    def exibir_dados(self):
        print(f'Dados sobre o cliente:\nNome: {self._nome}\nCPF: {self._CPF}'
    f'\nEndereço: {self._endereço}\ncidade: {self._cidade}\nestado: {self._estado}'
    f'\ntelefone: {self._telefone}\n')
#usando input para registras as contas
def cad_cliente():
    nome=input('Insira seu nome: ')
    CPF=input('Insira seu CPF: ')
    endereço=input('Insira seu endereço: ')
    cidade=input('Insira sua cidade: ')
    estado=input('Insira seu estado: ')
    telefone=input('Insira seu telefone: ')
    return nome,CPF,endereço,cidade,estado,telefone
nome,CPF,endereço,cidade,estado,telefone=cad_cliente()
cliente_3=Cliente(nome,CPF,endereço,cidade,estado,telefone)


cliente_1=Cliente('Luciano','123456789','Rua das flores','Poá','SP','987654321')
cliente_2=Cliente('Brenner','987654321','Rua Carlota Cardinale','Belo Horizonte','MG','963852741')

class Conta:
    def __init__(self,número,Cliente,saldo):
        self.número=número
        self.Cliente=Cliente
        self.saldo=float(saldo)
    def exibir_conta(self):
        self.Cliente.exibir_dados()
        print(f'Dados sobre a conta:\nNúmero da conta: {self.número}\nSaldo: R$ {self.saldo}')
    def depósito(self):
        valor=float(input('Insira o valor para depositar na conta: R$'))
        self.saldo=self.saldo+valor
        print(f'Foi efetuado um depósito de R${valor} na sua conta\nseu saldo atual é: R${self.saldo}')
    def sacar(self):
        saque=float(input('Insira um valor para sacar da sua conta: '))
        if saque>self.saldo:
            print('O valor excede o seu saldo atual, operação negada. Não oferecemos cheque especial. :(')
        else:
            self.saldo=self.saldo-saque
            print(f'Foi efetuado um saque de R${saque} de sua conta\nseu saldo atual é: R${self.saldo}')

conta_1 = Conta('1010', cliente_1, 1000)
conta_2 = Conta('2020', cliente_2, 2000)

#usando input para registrar conta
def cad_conta():
    número=input('Insira um número de 4 digitos para sua conta: ')
    contas.append(número)
    saldo=float(input('Insira o seu saldo'))
    return número,saldo
número,saldo=cad_conta()
conta_3=Conta(número,cliente_3,saldo)
print('-------------------SEU CADASTRO--------------')
conta_3.exibir_conta()
print('-------------------OUTROS CLIENTES CADASTRADOS-------------------')
conta_2.exibir_conta()
conta_1.exibir_conta()
print('------EFETUANDO UM EXEMPLO DE DEPOSITO, SAQUE E TRANSFERENCIA------------')
conta_3.depósito()
conta_3.sacar()


def transferencia():
    teste = input('voce deseja fazer uma transferencia ? [sim/não] ')
    if teste == 'sim' :
        quem_envia = input('qual o numero da sua conta ?')
        if quem_envia == conta_3.número:
            print('olá', cliente_3._nome, ' seu saldo é de ', conta_3.saldo,)
            valor_trans = float(input('qual o valor que deseja tranferir ?'))
            if valor_trans > conta_3.saldo: 
                print('valor inserido é maior que o saldo :(')
            else:
                num_conta = input('qual o numero da conta que voce deseja transferir ?')
                if num_conta == conta_1.número:
                    conta_3.saldo = conta_3.saldo - valor_trans
                    conta_1.saldo = conta_1.saldo + valor_trans
                    print('voce tranferiu ', valor_trans, 'para ', cliente_1._nome, '. Seu saldo atual é de:', conta_3.saldo)
                elif num_conta == conta_2.número:
                    conta_3.saldo = conta_3.saldo - valor_trans
                    conta_2.saldo = conta_2.saldo + valor_trans
                    print('voce tranferiu ', valor_trans, 'para ', cliente_2._nome, '. Seu saldo atual é de:', conta_3.saldo)
        elif quem_envia == conta_1.número:
                 print('olá', cliente_1._nome, ' seu saldo é de ', conta_1.saldo,)
                 valor_trans = float(input('qual o valor que deseja tranferir ?'))
                 if  valor_trans > conta_1.saldo:
                        print('valor inserido é maior que o saldo :(')
                 else:
                        num_conta = input('qual o numero da conta que voce deseja transferir ?')
                        if num_conta == conta_3.número :
                            conta_1.saldo = conta_1.saldo - valor_trans
                            conta_3.saldo = conta_3.saldo + valor_trans
                            print('voce tranferiu ', valor_trans, 'para ', cliente_3._nome, '. Seu saldo atual é de:', conta_1.saldo)
                        elif num_conta == conta_2.número:
                            conta_1.saldo = conta_1.saldo - valor_trans
                            conta_2.saldo = conta_2.saldo + valor_trans
                            print('voce tranferiu ', valor_trans, 'para ', cliente_2._nome, '. Seu saldo atual é de:', conta_1.saldo)
        elif quem_envia == conta_2.número:
                 print('olá', cliente_2._nome, ' seu saldo é de ', conta_2.saldo,)
                 valor_trans = float(input('qual o valor que deseja tranferir ?'))
                 if  valor_trans > conta_2.saldo:
                        print('valor inserido é maior que o saldo :(')
                 else:
                        num_conta = input('qual o numero da conta que voce deseja transferir ?')
                        if num_conta == conta_3.número :
                            conta_2.saldo = conta_2.saldo - valor_trans
                            conta_3.saldo = conta_3.saldo + valor_trans
                            print('voce tranferiu ', valor_trans, 'para ', cliente_3._nome, '. Seu saldo atual é de:', conta_2.saldo)
                        elif num_conta == conta_1.número:
                            conta_2.saldo = conta_2.saldo - valor_trans
                            conta_1.saldo = conta_1.saldo + valor_trans
                            print('voce tranferiu ', valor_trans, 'para ', cliente_1._nome, '. Seu saldo atual é de:', conta_2.saldo)
    else:
        print('operação encerrada :)')                


transferencia()
print('O banco VGA agradece a sua preferencia ;)')