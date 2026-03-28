# Linguagem de Programação Aplicada

Nome: José Everaldo de Barros
RU: 4972245
Repositório GitHub: https://github.com/EveraldoBarros/Linguagem-de-Programa-o-Aplicada.git

Este repositório contém o trabalho prático da disciplina de Linguagem de Programação Aplicada.
O projeto foi ampliado para uma versão mais completa, com sprites, efeitos sonoros, power-ups e menu clicável.

## Visão geral do jogo
`Runner Star` é um jogo 2D de sobrevivência em que o jogador deve desviar de obstáculos, coletar power-ups e manter o personagem vivo o máximo possível.

![Screenshot do jogo](assets/screenshot.png)

## Mecânicas implementadas
- Jogabilidade de corredor com pulo, desvio e fase contínua
- Menu inicial com botões clicáveis
- Sistema de vidas
- Escudo temporário (invencibilidade)
- Slow motion por alguns segundos
- Diferentes tipos de obstáculos
- Pontuação por tempo de sobrevivência
- Música de fundo e efeitos sonoros de pulo, colisão e power-up
- Transição entre telas (menu, jogo, pausa e fim de jogo)
- Código organizado em módulos: `main.py`, `player.py`, `obstacle.py`, `utils.py`, `assets.py`

## O que está no projeto
- `main.py` — arquivo principal do jogo
- `player.py` — classe de lógica do personagem
- `obstacle.py` — classes de obstáculos e power-ups
- `utils.py` — funções de interface, botões e carregamento de assets
- `assets.py` — geração e caminho dos arquivos de imagem e som
- `assets/` — imagens e arquivos de som usados pelo jogo
- `requirements.txt` — dependências necessárias
- `build.ps1` — build automático para Windows (PowerShell)
- `build.bat` — build automático para Windows (CMD)
- `README.md` — instruções completas
- `trabalho.zip` — pacote final de entrega com `main.exe` e `README.md`

## Tecnologias usadas
- Python 3.11
- Pygame 2.6
- PyInstaller para gerar o `.exe`

## Requisitos para executar
1. Windows 10 ou superior
2. Python 3.11 instalado
3. Acesso ao terminal PowerShell ou CMD

## Passo a passo de instalação
1. Abra o terminal (PowerShell ou CMD).
2. Vá até a pasta do projeto:
   `cd C:\Linguagem-de-Programa-o-Aplicada`
3. Verifique se o Python 3.11 está instalado:
   `py -3.11 --version`
4. Instale as dependências do projeto no Python 3.11:
   `py -3.11 -m pip install -r requirements.txt`

## Como executar o jogo
1. No terminal, estando na pasta do projeto:
   `py -3.11 main.py`
2. O menu do jogo aparecerá automaticamente.
3. Controles do jogo:
   - `←` / `A`: mover para a esquerda
   - `→` / `D`: mover para a direita
   - `SPACE`: pular
   - `P`: pausar/despausar
   - `ENTER`: iniciar o jogo ou reiniciar após fim de jogo
   - `ESC`: sair do jogo

## Observação importante
- Este projeto foi testado com Python 3.11 e `pygame` instalado via `py -3.11`.
- Em sistemas com várias versões de Python, use sempre `py -3.11` para instalar dependências e executar o jogo.

## Como gerar o executável Windows (.exe)
### Opção 1: usar o script PowerShell
1. Abra o PowerShell na pasta do projeto.
2. Execute:
   `./build.ps1`
3. O script irá gerar o executável e criar o arquivo `trabalho.zip`.

### Opção 2: usar o script CMD
1. Abra o Prompt de Comando na pasta do projeto.
2. Execute:
   `build.bat`
3. O script irá gerar o executável e criar o arquivo `trabalho.zip`.

### Opção 3: gerar manualmente com PyInstaller
1. Instale o PyInstaller:
   `py -3.11 -m pip install pyinstaller`
2. Execute o build:
   `py -3.11 -m PyInstaller --onefile --noconsole --add-data "assets;assets" main.py`
3. O executável ficará em `dist\main.exe`.
4. Copie `dist\main.exe` para o pacote de entrega ou use o `trabalho.zip`.

## Entrega final
- O arquivo `trabalho.zip` final contém:
  - `dist\main.exe`
  - `README.md`
  - `main.py`
  - `player.py`
  - `obstacle.py`
  - `utils.py`
  - `assets.py`
  - `requirements.txt`

## Observações finais
- O jogo agora tem visual e mecânicas avançadas para uma entrega caprichada.
- O código foi organizado em módulos para facilitar manutenção e leitura.
- A versão atual foi testada com Python 3.11 e Pygame 2.6.
