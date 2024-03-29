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
 - Filo
 - Classe
 - Ordem

O usuário pode criar um grafo aleatório, informando quantas espécies (vértices) e relações (arestas) existirão.

Ele pode ainda criar uma espécie individual, ao inserir os dados necessários, e dizer a relação entre duas espécies.

Com espécies criadas, o usuário pode fazer uma busca, que retornará as informações da espécie caso seja encontrada.

Além das informações sobre espécies, o usuário pode ver informações sobre o grafo, como:
 - Quantidade de nós
 - Quantidade de arestas
 - Se o grafo é conectado ou não

O usuário pode então comparar os métodos de busca existentes (BFS e DFS) no grafo atual ou em grafos aleatórios

Se quiser, o usuário pode gerar uma imagem sobre a cadeia alimentar