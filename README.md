# 🎮 Runner Star - Linguagem de Programação Aplicada

**Nome:** José Everaldo de Barros
**RU:** 4972245
**Repositório GitHub:** https://github.com/EveraldoBarros/Linguagem-de-Programa-o-Aplicada.git

---

## 📌 Descrição

Este projeto consiste em um jogo 2D desenvolvido em Python utilizando a biblioteca **Pygame**, como atividade prática da disciplina de Linguagem de Programação Aplicada.

O jogo foi evoluído para uma versão mais completa, incluindo sprites, efeitos sonoros, power-ups e um menu interativo com botões clicáveis.

---

## 🖼️ Screenshot

![Screenshot do jogo](assets/screenshot.png)

---

## 🎯 Objetivo do jogo

Sobreviver o máximo de tempo possível desviando dos obstáculos e coletando power-ups que ajudam durante a partida.

---

## 🎮 Controles

* **← / A** → mover para a esquerda
* **→ / D** → mover para a direita
* **SPACE** → pular
* **P** → pausar/despausar
* **ENTER** → iniciar/reiniciar o jogo
* **ESC** → sair

---

## ▶️ Como executar (Recomendado)

Execute o arquivo:

```bash
main.exe
```

👉 Não é necessário instalar nada.

---

## 🧩 Mecânicas implementadas

* Jogabilidade estilo runner com desvio e pulo
* Sistema de vidas
* Power-ups:

  * Escudo (invencibilidade temporária)
  * Slow motion
* Diferentes tipos de obstáculos
* Pontuação baseada no tempo de sobrevivência
* Música de fundo e efeitos sonoros
* Menu inicial com botões clicáveis
* Sistema de pausa
* Tela de game over
* Transições entre telas

---

## 🛠️ Tecnologias utilizadas

* Python 3.11
* Pygame 2.6
* PyInstaller (para gerar o executável)

---

## ⚙️ Executar via Python (Opcional)

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o jogo:

```bash
python main.py
```

---

## 📦 Estrutura do projeto

```bash
main.exe
assets/
main.py
player.py
obstacle.py
utils.py
assets.py
README.md
requirements.txt
```

---

## ⚙️ Gerar executável (.exe) [Opcional]

Caso queira gerar o executável manualmente:

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Execute o comando:

```bash
python -m PyInstaller --onefile --noconsole main.py
```

3. O executável será gerado na pasta `dist/`

---

## 📌 Observações

* O jogo é uma versão demo jogável conforme solicitado no trabalho.
* O projeto foi desenvolvido de forma autoral.
* Os assets utilizados são de uso livre.
* O executável incluído permite rodar o jogo sem necessidade de instalar dependências.

---

## 👨‍💻 Autor

**José Everaldo de Barros**
RU: 4972245