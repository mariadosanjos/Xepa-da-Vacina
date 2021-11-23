from SistemaVacinas import Agendamento
from SistemaVacinas import ListaException

sistema_vacinas = Agendamento()

while True:
        try:

            print('''
Sistema de Vacinas para Agendamentos e Sorteios

      (1) Agendar vacina
      (2) Cadastrar doses remanescentes
      (3) Iniciar sorteio das doses
      (4) Consultar agendamento
      (x) Sair do programa
            ''')

            opcao = input('Insira a opção desejada: ').lower()

            # Cadeia de ifs de acordo com as opções do menu

            # Opção para inserir o nome dos candidatos.

            if opcao == '1':
              try:
                nome = input('Informe seu nome: ')        
                    
                if nome.replace(" ","").isalpha():
                  sistema_vacinas.inserir(nome)
                  print (f'\n{nome}, seu agendamento foi realizado com sucesso!')

                else:
                  print("\nNome inserido inválido. Por favor, insira um nome apenas com letras.")

              except ListaException as e:
                print(e)

            # Opção para inserir os fabricantes e suas doses.

            elif opcao == '2':
                try:
                    fabricante = input('Informe o fabricante: ')
                    if fabricante.replace(" ","").isalpha():
                      
                      valor = int(input(f'\nInforme a quantidade de doses remanescentes do fabricante {fabricante}: '))
         
                      sistema_vacinas.inserir_doses(valor)
                      sistema_vacinas.qtd_Doses(valor)
                      sistema_vacinas.inserir_fabricante(fabricante)
                      print(f'\nFabricante {fabricante} e quantidade de doses cadastrados com sucesso!')
                    
                    else:
                      print("\nValor inserido não foi um valor válido.Por favor, insira um nome com apenas letras.")

                except ValueError:
                    print('\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro positivo.')

                except ListaException as e:
                  print(e)
            
            # Opção para realizar o sorteio.

            elif opcao == '3':
              try:
                k = int(input('Informe o valor de k: '))
                sistema_vacinas.sorteio(k)
                sistema_vacinas.quantidade_doses_fabricante()
                sistema_vacinas.imprimir()
                break

              except ValueError:
                print("\nValor inserido não foi um valor válido. Por favor, insira um número inteiro.")
              except ListaException as e:
                print (e)

            # Opção para encerrar o programa.

            elif opcao == '4':
                print(sistema_vacinas.visualizar_agendamento())

            elif opcao == 'x':
                print('Programa encerrado!')
                break

            # Estrutura de decisão para caso o usuário digite algum valor não referente a nenhuma opção no menu, fazendo com que o laço reinicie.

            else:
                print(
                    '\nOpção inválida. Por favor, insira um valor referente à uma das opções que estejam no menu. ')

            # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

        except KeyboardInterrupt:
            print('\n\nComando de teclas para encerrar pressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')