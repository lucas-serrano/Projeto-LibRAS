# RAS-Libras

## Descrição do Projeto:

O projeto LibRAS é uma das atividade da RAS UNESP Bauru do segundo semestre de 2020. Ele tem como objetivo criar um aplicativo para computadores que ensine o básico da Língua Brasileira de Sinais (LIBRAS) para todos os usuários. Os movimentos errados são corrigidos através da webcam, utilizando rede neural, visão computacional e a linguagem de programação Python. A proposta do projeto é tornar o aprendizado em LIBRAS mais acessível a população brasileira, pretendendo aumentar a comunicação geral com surdos e mudos, bem como sua inclusão na sociedade.

## Bibliotecas usadas:

Programação utilizando a linguagem Python 3.8.6 com as seguintes bibliotecas:

Instalação do Tensorflow
```
pip install tensorflow==2.3.1
```
Instalação do Numpy
```
pip install numpy==1.19.2
```
Instalação do OpenCV
```
pip install opencv-python==4.4.0.40
```
Instalação do PyQt5
```
pip install PyQt5==5.15.1
```
Instalação da DateTime
```
pip install DateTime==4.3
```
## Instruções para a execução do programa:

Ao baixar os arquivos deste projeto execute o "Main.py", podendo ser diretamente pelo CMD do computador ou por um editor de códigos. Para que o programa funcione corretamente todos eles devem estar juntos em uma mesma pasta.

## Aprendendo LIBRAS:

No menu inicial há 4 botões: Aprender, Testar, Informações e Sair.
- Aprender: O usuário deverá escolher qual letra do alfabeto deseja aprender e selecionar a opção "Aprender" logo abaixo. Uma foto da letra a ser realizada será disponibilizada para consulta. Em seguida, ao repetir o movimento em frente a câmera, o botão "Fotografar" deverá ser selecionado para que o programa verifique se a execução está correta. Uma letra aparecerá no canto esquerdo, indicando qual a rede neural conseguiu identificar.
- Testar:
- Informações: Um breve texto explicará o intuito de cada um dos modos acima.
- Sair: O programa fechará por completo.
