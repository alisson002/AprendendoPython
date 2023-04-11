class Carros:
    def __init__(self, fabricante, modelo, ano):#esta parte do construtor ja esta sebdi feita como se fosse o SET, pois ja esta de uma forma que da pra alterar
        #diferente do q foi feito no exemplo do notebook, que deixava valores fixos aqui e fazia um SET "isolado" para altera-los
        self.fabricante = fabricante
        self.modelo = modelo   
        self.ano = ano
        self.odometro = 0
        self.combustivel = 100
        
    def descricao_nome(self):
        nome_longo = str(self.ano)+ ' ' + str(self.fabricante)+ ' ' + str(self.modelo)
        return nome_longo.title()
    
    def leia_odometro(self):
        #exibe a frase que mostra o valor do odometro do carro
        print('o carro tem ' + str(self.odometro)+ ' Km rodados')
        
    def altera_odometro(self, novo_odometro):#SET
        #alterar o odometro pelo valor usado como argumento
        self.odometro = novo_odometro
        
    def incrementa_odometro(self, novo_odometro):#para contar a kilometragem total do carro em 'altera_odometro' so altera o valor
        #incrementa um determinado valor ao odometro
        #self.odometro = self.odometro + novo_odometro
        self.odometro += novo_odometro
        
    def tanque_de_gasolina(self):
        #exibe a quantidade, em %, de gasolina no tanque
        print('o tanque está ' + str(self.combustivel) + '% cheio.')
        
carro = Carros('honda', 'civic', 2015)
carro.tanque_de_gasolina()


class Bateria():
    def __init__(self, bateria = 100):
        '''inicializa os atributos da bateria'''
        self.bateria = bateria
        
    def eltera_bateria(self, novo_valor):
        '''altera o valor da bateria'''
        self.bateria = novo_valor
        
        
class CarrosEletricos(Carros):#classe filha de Carros
    #representas aspectos de um carro especifico
    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        '''o super serve pra chamar o metodo construtor la da classe pai'''
        '''é uma maneira de não sobreescrever os métodos da classe pai'''
        '''The super() function is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class.'''
        self.bateria = Bateria()
        '''recebe a classe bateria e vai ter q ser chamada de forma diferente'''
        
    def tanque_de_gasolina(self):
        '''vai sobrecarregar o metodo da classe pai e vai executar so oq tem aqui para criações da classe filha'''
        print('carros eletricos nao usam gasolina')
        
carro_eletrico = CarrosEletricos('tesla', 'model s', 2016)
print(carro_eletrico.descricao_nome())
carro_eletrico.tanque_de_gasolina()

print('\npara a classe Carros (normal)')
carro.tanque_de_gasolina()



#HERANÇA2 CONTINUAÇÃO
class Bateria():
    def __init__(self, bateria = 100):
        '''inicializa os atributos da bateria'''
        self.bateria = bateria
        
    def altera_bateria(self, novo_valor):
        '''altera o valor da bateria'''
        self.bateria = novo_valor
        
    def mostrar_bateria(self):
        print('a bateria está ' + str(self.bateria) + '% cheia.')
        
        
    
bateria = Bateria()
'''#não coloquei nada dentro pq já esta definido na classe, já começa com 100'''

print(bateria.bateria)
print(bateria.altera_bateria(80))
print(bateria.bateria)

meu_carro5 = CarrosEletricos('ford', 'k', 2022)
print(meu_carro5.bateria.bateria)
'''chamando dessa forma pq é um metodo de outra classe'''
'''Usando o odometro como exemplo... se eu chamase ele, so precisaria de meu_carro5.odometro, pq já é algo q pertence a classe'''

meu_carro5.bateria.altera_bateria(56)
print(meu_carro5.bateria.bateria)

meu_carro5.bateria.mostrar_bateria()

