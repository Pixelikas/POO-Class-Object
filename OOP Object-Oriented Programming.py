
# Vetor para armazenar objetos
pessoas = []

# Classe padrão para instanciar objetos
class Pessoa:

  # Function com atributos para criação de objeto
  def __init__(self, nome: str, idade: int, altura: float):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  # Método para apresentar no idade e altura da Pessoa
  def dizer_ola(self):
    print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
    f'anos e minha altura é {self.altura}m.\n')

  # Método para apresentar receita que está sendo cozinhada
  def cozinhar(self, receita: str):
    print(f'Estou cozinhando um(a): {receita}.\n')

  # Método para apresentar distância do passeio
  def andar(self, distancia: float):
    print(f'Saí para andar. Volto quando completar {distancia} metros.\n')

# Criação de objeto (instância)
novaPessoa = Pessoa(nome='Oberti', idade=28, altura=1.75)

# Chamada de métodos
novaPessoa.dizer_ola()
novaPessoa.cozinhar('rabada')
novaPessoa.andar(10.5)

# dados = str(f'Nome: {novaPessoa.nome}\nIdade: {novaPessoa.idade}\nAltura: {novaPessoa.altura}')
# print(dados)

