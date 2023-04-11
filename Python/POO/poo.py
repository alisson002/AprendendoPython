class Computador():
    #propriedades da classe
    # marca = 'Samsung'
    # processador = 'intel'
    # usb = 3
    # ligado
    
    #NO PYTHON NÃO TEM DESTRUTOR
    def __init__(self):#construtor #AQUI AS INFORMAÇÕES SÃO FIXAS, DADAS DENTRO DA CLASSE MESMO (OUTRO EXEMPLO ABAIXO)
        #o ideal é que as prorpiedade sejam definidas aqui
        self.ligado = False
        self.marca = 'Samsung'
        self.processador = 'intel'
        self.usb = 3
    
    
    #metodo, vai mudar caracteristicas da classe
    def ligar_computador(self):#todo objeto que tem uma caracteristica interna da classe, deve ser referenciado como self
        #self referencia as variaveis internas da classe
        self.ligado = True
    
    def mudar_marca(self, marca):#SET: set_marca para alterar a marca
        self.marca = marca
        
    #o ideal é que não se tenha um acesso direto as propriedades
    def obter_marca(self):#GET: get_marca para obter a marca
        return self.marca
        

pc = Computador()#para instanciar a classe

print(pc.marca)
print(pc.processador)
print(pc.ligado)
pc.ligar_computador()
print(pc.ligado)

pc.mudar_marca('waio')
print(pc.marca)#isso aqui seria um acesso direto

print(pc.obter_marca())

#herança, classe filha
class Notebook(Computador):
    pass

print('herança'.upper())
pc2 = Notebook()#instanciar
print(pc2.obter_marca())#retorna samsung, ja que na herança são herdadas as propriedades/variaveis default da classe pai

#herança, classe filha
class Notebook2(Computador):
    #NO PYTHON NÃO TEM DESTRUTOR
    def __init__(self):#construtor
        #o ideal é que as prorpiedade sejam definidas aqui
        self.ligado = False
        self.marca = 'dell'
        self.processador = 'intel'
        self.usb = 3
        self.horas_ligado = 100#msm sendo uma classe filha eu posso criar novas prorpiedades nela

print('herança2'.upper())
pc3 = Notebook2()#instanciar
print(pc3.obter_marca())#retorna dell, ja que nesse caso eu fiz uma sobre carga do construtor

class Cachorro:#tentativa simple de modelar um cachorro
    def __init__(self, name, age): #DESTA FORMA AS INFORMAÇÕES SERÃO DEFINIDAS FORA DA CLASSE, COMO MOSTRADO ABAIXO
        #inicializa os atributos nome e idade
        self.name = name
        self.age = age
        
    def sentar(self):
        #simula um cachorro sentando em resposta a um comando
        print(self.name.title() + ' está sentando...')
        print(self.name.title() + ' está sentado.')
        
    def rolar(self):
        #simula um cachorro rolando em resposta a um comando
        print(self.name.title() + ' está rolando...')
        print(self.name.title() + ' está rolou.')
        
meu_Cachorro = Cachorro('Aquiles', 6)

meu_Cachorro.rolar()
meu_Cachorro.sentar()

meu_Cachorro2 = Cachorro('Big', 6)
meu_Cachorro2.rolar()
meu_Cachorro2.sentar()

#alterando atributos

class Carro:
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
        
        
    
meu_carro = Carro('audi', 'a4', 2016)
print(meu_carro.descricao_nome())
print(meu_carro.leia_odometro())#vai mostrar um none junto pq nao esta retornando nada
#mas se tirar do print, ja que ja tem um print la dentro, não mostra tb. mas pode ser adicionando a um variavel e retornando ela pra printar so aqui fora

print('\nmudando odometro')
meu_carro.odometro = 7
print(meu_carro.leia_odometro())#vai mostrar um none junto pq nao esta retornando nada

print('\nmudando odometro')
meu_carro.altera_odometro(10)
meu_carro.leia_odometro()

print('\nincrementando odometro')
meu_carro.incrementa_odometro(10)
meu_carro.leia_odometro()

print('\nincrementando odometro')
meu_carro.incrementa_odometro(3)
meu_carro.leia_odometro()
