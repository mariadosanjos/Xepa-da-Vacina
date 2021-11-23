from datetime import datetime
import random

class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Agendamento:
    def __init__(self):
        self._agendamento = []
        self._contemplados = []
        self._fabricante = []
        self._quantidade_doses = []
        self._qtd_doses = 0

  # Encapsulamento dos atributos

    @property
    def agendamento(self):
        return self._agendamento

    @agendamento.setter
    def agendamento(self, novo):
        self._agendamento = novo

    @property
    def contemplados(self):
        return self._contemplados

    @contemplados.setter
    def contemplados(self, novo):
        self._contemplados = novo
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    @property
    def quantidade_doses(self):
        return self._quantidade_doses

    @quantidade_doses.setter
    def quantidade_doses(self, quantidade):
        self._quantidade_doses = quantidade

  # Método para inserir o nome do fabricante.

    def inserir_fabricante(self, fabricante):
        self.fabricante.append(fabricante)
    
  # Método para inserir a quantidade de doses.

    def inserir_doses(self, quantidade):
      if quantidade > 0:
        self.quantidade_doses.append(quantidade)
      else:
        return ('\nQuantidade inválida! Por favor insira um número inteiro positivo.')
      
  # Método para imprirmir fabricante e a quantidade de suas doses, respectivamente.

    def quantidade_doses_fabricante(self):

        print('\nRelatório de ', end='')
        print(datetime.today().strftime('%d/%m/%Y'))
        for i in range(len(self.fabricante)):
          print(f'\nFabricante: {self.fabricante[i]}\nQuantidade: {self.quantidade_doses[i]}')

  # Método para retornar o número total de pessoas agendadas.

    def tamanho(self):
        return len(self.agendamento)

  # Método para apresentar na tela as pessoas agendadas.

    def visualizar_agendamento(self):
        if not self.agendamento:
            return ("\nNão existem pessoas agendadas.")
        else:
            return (f'\nLista de pessoas agendadas:\n\n{self.agendamento}')

  # Método para inserir uma pessoa na lista de agendamento.

    def inserir(self, nome):
        if nome in self.agendamento:
            raise ListaException('\nNome já cadastrado!')
        else:
            return self.agendamento.append(nome)

  # Método para inserir doses totais para o sorteio.

    def qtd_Doses(self, valor):
        if valor > 0:
            self._qtd_doses += valor
        else:
            raise ListaException(
                "\nValor inserido não foi um valor válido. Por favor insira um número inteiro positivo.")

  # Método para realizar o sorteio das vacinas e apresentar na tela o seu processo.

    def sorteio(self, k):

        if not self.agendamento:
            raise ListaException("\nImpossível realizar sorteio. Não há ninguém agendado para o sorteio.")

        elif self._qtd_doses == 0:
            raise ListaException('\nImpossível realizar sorteio. Não há doses disponíveis para o sorteio.')

        elif k <= 0:
          raise ListaException('\nValor inserido não foi um valor válido. Por favor, insira um número inteiro e que este seja positivo.')

        else:
            print('\nIniciando sorteio...')
            print(f'k escolhido: {k}')
            pointer = random.randint(1, self.tamanho())
            print(f'O pointer sorteado foi: {self.agendamento[pointer-1]}\n')

            while self._qtd_doses != 0 and self.tamanho() > 0:
                self._qtd_doses -= 1

                print(f'Lista: {self.agendamento}')
                print(f'Pointer -> {pointer} : {self.agendamento[pointer-1]}')
                ultimo = len(self.agendamento)
                contador = 0
                condicao = False
                while contador != k:
                    ultimo = len(self.agendamento)

                    if pointer == ultimo:
                        pointer = 1

                    else:
                        pointer += 1
                    contador += 1
                    if pointer == ultimo and contador == k:
                        condicao = True
                        aux = pointer
                        pointer = 1
                        print(f'Contemplado: {self.agendamento[aux-1]}')
                        self.contemplados.append(self.agendamento[aux-1])
                        self.agendamento.pop(aux-1)
                        print()
                        break

                if condicao == False:
                    print(f'Contemplado: {self.agendamento[pointer-1]}\n')
                    self.contemplados.append(self.agendamento[pointer-1])
                    self.agendamento.pop(pointer-1)
                    print()
     
    # Método para distribuir vacinas entre os contemplados.
    
    def vacinas_contemplados(self):
        vacinas_contemplados = []
        for i in self.fabricante:
            posicao_fabricante = self.fabricante.index(i)
            for posicao_fabricante in range(self.quantidade_doses[posicao_fabricante]):
                vacinas_contemplados.append(i)
        return vacinas_contemplados
          
    # Método para imprimir pessoas contempladas ou não para a vacinação.

    def imprimir(self):
        if self.tamanho() < self._qtd_doses and self._qtd_doses == 1:
            print(f'\nSobrou {self._qtd_doses} dose!')
        elif self.tamanho() < self._qtd_doses and self._qtd_doses > 1:
            print(f'\nSobraram {self._qtd_doses} doses!')
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print(f'\033[32m'+'Contemplados'+'\033[0;0m')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        lista_doses = self.vacinas_contemplados()
        for i in range(len(self.contemplados)):
            print(f'{self.contemplados[i]} - {lista_doses[i]}')
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('\033[31m'+'Não Contemplados'+'\033[0;0m')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        for i in range(len(self.agendamento)):
            print(self.agendamento[i])