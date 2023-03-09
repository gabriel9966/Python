class Evento:
    def Altera_nome_evento(self,Novo_nome):
        print("Alterando nome do evento")
        self.nome = Novo_nome
    pass#a classe acaba aqui

ev = Evento()
ev.nome = "Aula de python"
print(ev.nome)

#self referência, self = this

ev.Altera_nome_evento("Aula de javascript")
print(ev.nome)