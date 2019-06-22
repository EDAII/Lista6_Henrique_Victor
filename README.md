# LISTA 6 - ESTRUTURA DE DADOS 2 - 2019/1

### Henrique Martins de Messias - 17/0050394
### Victor Rodrigues Silva - 16/0019516

<br>

### Instalações necessárias
- No teminal, digite os seguinte comando para instalar as dependências:
  ```bash
    $ pip3 install -r requirements.txt
    $ sudo apt-get install python3-tk
  ```


### Instruções de uso

- No terminal, vá até o diretório do exercício, que contém, além de arquivos como o README, a pasta "src"
- Digite o seguinte comando:

  ```bash
    $ cd src
  ```

- Para executar o código, digite:

  ```bash
    $ python3 main.py
  ```

### Detalhes da Lista 6

O software deste repositório é sobre a <b>Cadeia Alimentar</b>.

Cada animal possui as seguintes informações:
 - Nome Popular
 - Nome Científico
 - Habitat

O usuário pode criar uma quantidade determinada de espécies de animais aleatórios, ou criar uma espécie individual, ao inserir os dados necessários.

A partir do momento em que houver espécies registrados, o usuário pode fazer a relação predador-presa entre eles, informando:
 - Quantas espécies farão parte da cadeia
 - Quantas relações existirão na cadeia

O usuário pode então usar os seguintes recursos, e compará-los entre si:
- DFS
- BFS

Se quiser, o usuário pode imprimir a cadeia alimentar