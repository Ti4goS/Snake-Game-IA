# Snake-Game-IA

## Instalação
Para executar o Código em um ambiente virtual siga esse tutoral:

#### Criar Venv

Execute esse código na pasta Raiz desse repositório

```python3 -m venv env```

Após isso, para ativar o ambiente virtual utilize o seguinte comando:

#### Windows
```env\Scripts\activate.bat```

#### Mac OS
```source env/bin/activate```

#### Desativar Venv

```deactivate```

#### Instalando Bibliotecas

```pytohn3 -m pip install -r requirements.txt```


## O Algoritmo A*

- snake_Head -> Guarda a posição X e Y de onde está a cabeça da cobra
- snake_List -> Guarda todas as posições em que a cobra está presente, incluindo a cabeça
- food_coordinates -> Guarda a posição X e Y de onde está a Maça (Objetivo)

#### Informações

1. A maça é gerada aleatóriamente e é garantido que essa posição nunca será um valor inválido (Corpo da cobra ou fora dos limites da janela)

2. Quando a borda está na quina do tabulero ela só tem 2 possibilidades de jogada:

##### Canto superior esquerdo (0,0)

'''
 successors = [
   (i,j+20), #Down
   (i+20,j)  #Right
]
'''

##### Canto superior direito (600,0)

'''
 successors = [
   (i,j+20), #Down
   (i-20,j)  #Left
]
''''

##### Canto inferior esquerdo (0,600)

'''
 successors = [
   (i,j-20), #Up
   (i+20,j)  #Right
]
'''

##### Canto inferior direito (400,600)

'''
 successors = [
   (i,j-20), #Up
   (i-20,j)  #Left
]
'''
3. Quando a Cobra estiver em outra posição ela tem 4 jogadas possiveis

'''
 successors = [
   (i,j-20), #Up
   (i,j+20), #Down
   (i-20,j), #Left
   (i+20,j)  #Right
]
'''

#### Para cada um desses sucessores deve ser verificado, se:

- O Sucessor está dentro do vetor snake_list, ou seja, se é de onde a cobra está vindo;
- O Sucessor está dentro do tabuleiro do jogo:

'''
 Se Sucessor X é maior ou igual a 0 ou é menor que 600
 Se Sucessor Y é maior ou igual a 0 ou é menor que 400
'''

#### Funções

- Heuristica -> A função Heuristica deve ser calculada usando os 2 pontos:
    
    1. a localização da cabeça da cobra
    2. a localização da maça

ela será calculada utilizando o teorema de pitágoras (distancia em linha reta): 

'''
    import math
    
    x_axis_delta = math.pow(snake_x_coordinate - food_x_coordinate,2) 
    y_axis_delta = math.pow(snake_y_coordinate - food_y_coordinate,2)

    function_h = math.sqrt(
        x_axis_delta + y_axis_delta
    )

'''

- Função G

Essa conta o deslocamento, todo deslocamento será, padrão e terá o valor de 1

'''
    function_g = 1
'''
