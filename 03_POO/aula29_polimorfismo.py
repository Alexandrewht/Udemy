'''
 Princípio da substituição de liskov
 Objetos de uma superclasse devem ser substituiveis
 por objetos de uma classe sem quebrar a aplicação.
 Sobrecarga de métodos (Overload) = errado
 Sobreposição de métodos (Override) = correto
'''
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: ...
    
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando:', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self)-> bool:
        print('SMS: enviando:', self.mensagem)
        return False
    
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print('Notificação enviada!')
    else:
        print('Notificação NÃO notificação!')

notificacao_email = NotificacaoEmail('Testando E-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)