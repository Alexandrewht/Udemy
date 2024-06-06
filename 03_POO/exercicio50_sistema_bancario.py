'''
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e 
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrent) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente Obs. Pode solicitar emprestimo para completar a quantia.
    ContaPoupanca Obs. Não pode ficar negativo.

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco Obs. O banco só precisa checa se existe o cliente.
    Banco -> Cliente 
    Banco -> Conta

Dicas:
 1. Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (agregação da classe ContaCorrente ou ContaPoupanca)

 2. Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas deve ter médotos para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e 
    Polimorfismo - as subclasses que implementam o método sacar)

 3. Criar classe Banco para AGREGAR classes de cliente e de contas (agregação)
 
 4. Banco será responsável autenticar o cliente e as contas da seguinte maneira
    Banco tem contas e clientes (agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

 5. Só será possível sacar se passar na autenticação do banco (descrita acima).
 
 6. Banco autentica por um método.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.contas = []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class Conta(Cliente):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        
class Conta_Poupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            print(f'Tentativa de sacar {valor}R$')
            self.saldo -= valor
            print(valor, 'R$, Sacado com sucesso.')
        else:
            print('Saldo insuficiente.'
                  f' Você tentou sacar {valor}R$.'
                  f' O seu saldo é de {self.saldo}R$.')
            
    def depositar(self, valor):
        self.saldo += valor
        print(f'{valor}R$, Depositado com sucesso.')
    
class Conta_Corrente(Conta):
    def __init__(self, agencia, numero, saldo, limite_extra=1000):
        super().__init__(agencia, numero, saldo)
        self.limite_extra = limite_extra

    def sacar(self, valor):
        saldo_total = self.saldo + self.limite_extra
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'{valor} R$, Sacado com sucesso, '
                  f'Saldo atual: {self.saldo} R$')
        elif valor <= saldo_total:
            print('Saldo insuficiente. Gostaria de usar o seu limite extra? ')
            opcao = input('S/N: ').upper().strip()[0]
            if opcao == 'S':
                self.saldo -= valor
                if self.saldo < 0:
                    self.limite_extra += self.saldo
                    self.saldo = 0
                print(f'{valor} R$, Sacado com sucesso.' 
                      f' Saldo atual: {self.saldo}R$'
                      f' Limite extra disponível: {self.limite_extra}R$')
            else:
                print('Operação cancelada.')
        else:
            print('Saldo insuficiente, incluindo o limite extra.')
            
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
        
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
    def autenticar_cliente(self, cliente, conta):
        if cliente in self.clientes and conta in self.contas:
            return True
        else:
            return False
        
    def autenticar_conta(self, conta):
        if conta in self.contas:
            return True
        else:
            return False

# Criando as Pessoas
pessoa1 = Pessoa('Alexandre', 25)
pessoa2 = Pessoa('Maria', 35)
pessoa3 = Pessoa('Valéria', 26)

# Criando os Bancos
banco1 = Banco('Caixa')
banco2 = Banco('Nubank')

# Adicionando Cliente no Banco
cliente1_caixa = banco1.adicionar_cliente(pessoa1)
cliente1_nubank = banco1.adicionar_cliente(pessoa1)

cliente2_caixa = banco1.adicionar_cliente(pessoa2)
cliente2_nubank = banco2.adicionar_cliente(pessoa2)

cliente3_caixa = banco1.adicionar_cliente(pessoa3)
cliente3_nubank = banco2.adicionar_cliente(pessoa3)

# Criando as Contas Correntes (Agencia, saldo e limite especial)
conta_corrente1 = Conta_Corrente('001', 500, 1000)
conta_corrente2 = Conta_Corrente('002', 600, 1000)
conta_corrente3 = Conta_Corrente('003', 700, 1000)

# Criando as Contas Poupancas (Agencia, numero e saldo)
conta_poupanca1 = Conta_Poupanca('001', '12345-0', 500)
conta_poupanca2 = Conta_Poupanca('002', '67890-1', 600)
conta_poupanca3 = Conta_Poupanca('003', '24680-3', 700)

# Adicionando as Contas nos Bancos
banco1.adicionar_conta(conta_corrente1)
banco1.adicionar_conta(conta_corrente2)
banco1.adicionar_conta(conta_corrente3)

banco2.adicionar_conta(conta_poupanca1)
banco2.adicionar_conta(conta_poupanca2)
banco2.adicionar_conta(conta_poupanca3)

# Fazendo Depositos e Saques
print('--- Saldo + Deposito ---')
# saldo inicial
print(f'O Saldo da conta poupança é: {conta_poupanca1.saldo}RS')  
conta_poupanca1.depositar(500)  # depositando 500

print('--- Tentativa de saque ---')
print(f'O Saldo da conta poupança é: {conta_poupanca1.saldo}RS')
conta_poupanca1.sacar(1100)

print('--- Saldo final ---')
# mostrando o saldo
print(f'O Saldo da conta poupança é: {conta_poupanca1.saldo}RS')  

print('-' * 20)
print('--- Saque Conta Corrente ---')
print(conta_corrente1.saldo)  # saldo inicial
# vai pra sacar, e o saldo é insuficiente e usar o limite especial
print(conta_corrente1.sacar(1100))  

# mostrando o saldo
print(f'O Saldo da conta corrente é: {conta_corrente1.saldo} R$')
