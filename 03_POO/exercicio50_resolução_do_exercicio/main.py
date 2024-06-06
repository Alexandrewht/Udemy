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

import contas

class Transacoes:
    def __init__(self):
        self.extrato = []
        self.saldo = 0
    
    def deposito(self):
        deposito = float(input('Quanto quer depositar:'))
        self.saldo += deposito
        self.extrato.append(f'+ R${deposito:.2f}')
        return f'O valor de R${deposito:.2f} foi depositado em sua conta.'
    
    def saque(self):
        saque = float(input('Quanto quer sacar?'))
        if saque > self.saldo:
            print('Você não possui saldo suficiente para este saque.')
        elif saque > 1500:
            print('Para um saque maior que 1500, favor comparecer a agência.')
        else:
            print(f'Foi sacado um valor de {saque:.2f}')
            self.saldo -= saque
            self.extrato.append(f'- R${saque:.2f}')
    
    def ver_extrato(self):
        return self.extrato
    
    def ver_saldo(self):
        return self.saldo

x = Transacoes()
y = Transacoes()
print(x.deposito())
print(y.deposito())
print(y.ver_extrato())
print(x.ver_saldo())
print(y.ver_saldo())
