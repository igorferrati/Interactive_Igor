from time import sleep
from datetime import date
from Funções import frase, titulo

contagem = 0
idade = date.today().year - (1993 + 1)  #aniversário em fev, 28 anos.
# PROGRAMA
titulo('Currículo Interativo', 6)

# BANCO DE DADOS
dados_pessoais = {'Nome:': 'Igor Ferrati Leite',
                  'Idade:': f'{idade} anos',
                  'Contatos:': '(11) 97181 4739 | ferrati.igor@gmail.com',
                  'GitHub:': 'https://github.com/igorferrati',
                  'LinkedIn:': 'https://www.linkedin.com/in/igor-ferrati-leite-b5212422a/'
                  }
experiencia_prof = {'empresa6': ['Assistente de Projetos', 'PHL Construções a Seco', 'Fev.2020/Jul.2021'],
                    'empresa5': ['Vendedor Sênior', 'Decathlon Brasil', 'Set.2018/Fev.2020'],
                    'empresa4': ['Desenhista Cadista', 'CEPLAM Engenharia', 'Mai.2017/Set.2018'],
                    'empresa3': ['Projetista CAD', 'PA Engenharia', 'Jul.2016/Mai.2017'],
                    'empresa2': ['Estagiário de Projetos', 'Prefeitura de São Paulo', 'Jul.2014/Jul.2016'],
                    'empresa1': ['Estagio', 'Instituto Florestal', 'Jul.2013/Mai.2014'],
                    }
formacao = {'Udemy': {'Python, Projetos Avançados':
                          ['-Tratativas de erros',
                           '- Boas práticas e organização de código',
                           '- Manipulação de funções,listas,dicionários,tuplas,sets',
                           '- Git/GitHub',
                           'Conclusão: 2021.']
                      },

            'FIAP': {'Programação Python':
                         ['-Lógica de programação',
                          '-Tratamento de dados',
                          '-Orientação ao Objeto',
                          'Conclusão: 2021.']
                     },

            'ESE - SEBRAE': {'Custumer Success':
                                 ['Importância custumer success',
                                  'Beneficíos e definições',
                                  'Métricas e indicadores',
                                  'Análise e retorno de informações',
                                  'Conclusão: 2021.']
                             },
            'Udemy ': {'Lógica de Pogramação':
                           ['Introdução a linguagens e IDE;',
                            'Desenvolvimento de exercícios básico e lógicos;',
                            'Programação básica: Java, C e Python;',
                            'Conclusão: 2021.'],
                       },

            'SENAI': {'Excel':
                          ['Formatações;',
                           'Formulas e funções',
                           'Interpolação, organização e apresentação de dados;',
                           'Conclusão: 2021.']
                      },

            'FAAP': {'Dimensionamento de Design Naval':
                         ['Ambientes funcionais;',
                          'Máxima funcionalidade e aproveitamento de espaços;',
                          'Soluções de problema atípicos;',
                          'Conclusão: 2017.']
                     },

            'UNICSUL': {'Universidade Cruzeiro do Sul - 2016':
                            ['Bacharelado em Arquitetura e Urbanismo, 2012-2016.']
                        },

            'Melies': {'Modelagem de Ambientes Virtuais':
                           ['Aplicação de projetos arquitetônicos em softwares 3D;',
                            'Manipulação de arquivos, familias;',
                            'Pós-produção de imagens;',
                            'Modelagem 3D;',
                            'Conclusão: 2015.']
                       }
            }

while True:
    frase('Processando', 6)
    resp = validaint('Digite uma opção: ')
    if resp == 1:
        for k, v in dados_pessoais.items():
            print('\033[7:40m', end='')
            print(f'{k:.<13} {v:.<80}')
    elif resp == 2:
        print('\033[7:40m', end='')
        print(f'{"Empresas:":.<}{"Cargo/Func.": >32}{"Período:":>43}')
        for ke, ve in experiencia_prof.items():
            sleep(0.5)
            print(f'{ve[1]:.<30}{ve[0]:.<30}{ve[2]:.>33}')
    elif resp == 3:
        print('\033[7:40m', end='')
        print(f'{" Objetivos ! ":_^94} ')
        print('Adquitir experiência profissional no campo da tecnologia, ingressar no mercado como'
              'desenvolvedor,\nprogramador e/ou áreas relacionadas.Foco em dados, bigdata, learnmachine, BI, etc.')
        print('_'*94)
        print('Pontos de desenvolvimento para obejtivo:')
        sleep(1)
        print('[1] - Estudo no âmbito da tecnologia')
        sleep(0.5)
        print('[2] - Desenvolver próprios códigos')
        sleep(0.5)
        print('[3] - Experiência profissional')
        sleep(0.5)
        print('[4] - Iniciar uma pós-graduação')
    elif resp == 4:
        print('\033[7:40m', end='')
        print(f'{"Graduação completa: Arquitetura e Urbanismo - 2016":<94}')
        print(f'{"Formações / Cursos":.^94}')
        for form_k, form_v in formacao.items():
            print(f'{form_k}', end=' - ')
            for dados_k, dados_v in form_v.items():
                print(f'{dados_k}')
                for topicos in dados_v:
                    print(topicos)
                print('_' * 94)
                sleep(1)
    elif resp == 5:
        second = 0
        print('\033[7:40m', end='')
        print(f'{"Saindo":_^94}')
        print(' .  .  . ', end='')
        sleep(0.5)
        while second < 4:
            print(' . ',end='')
            sleep(0.5)
            second += 1
        print()
        print(f'{"* * * Programa Finalizado * * *":^94}')
        break
    else:
        print('\033[7:40m', end='')
        print('Erro, digite uma opção válida.')

