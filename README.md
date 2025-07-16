# 🤖 Bot Cabloco - Discord

Um bot para Discord simples, criado como um projeto para passar o tempo e materializar uma piada interna entre amigos. A ideia principal é ter um bot que envia mensagens características em dias específicos da semana, com controle de estado para "ativar" ou "desativar" suas funções.

---

### 📜 Sobre o Projeto

Este bot nasceu de uma brincadeira e não possui um objetivo profissional. Foi desenvolvido como uma forma divertida de praticar a criação de bots com a biblioteca `discord.py`, além de explorar conceitos de persistência de dados.

O "lore" do bot é que os **cablocos** são entidades misteriosas que observam o servidor e se manifestam com mensagens enigmáticas — principalmente às quintas e sextas-feiras. O projeto funciona como um playground para testar ideias e interações com a API do Discord.

---

### ✨ Funcionalidades Atuais

- **`/ativar`** – "Acorda" os cablocos, permitindo que enviem mensagens automáticas.
- **`/desativar`** – Coloca os cablocos "de férias", desativando as mensagens.
- **`/status`** – Verifica se os cablocos estão ativos ou descansando.
- **Persistência de Estado** – O bot lembra seu estado (ativo/inativo) mesmo após reiniciar, salvando tudo em um arquivo `.json`.

---

### 🔮 Funcionalidades Futuras (O Core do Bot)

A lógica principal, a ser implementada em breve, será baseada em tarefas agendadas:

- **Mensagens de Quinta-feira:** Envio de mensagens aleatórias e enigmáticas anunciando a proximidade da sexta-feira.
- **Mensagens de Sexta-feira:** Comemorações automáticas informando que o grande dia chegou.
- **Aviso Especial:** A cada 3 sextas-feiras em que o bot estiver ativo, ele enviará uma mensagem especial numa quarta-feira, e o contador será reiniciado.

---

### 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Biblioteca Discord:** `discord.py` – Interação com a API do Discord
- **Variáveis de Ambiente:** `python-dotenv` – Segurança do token
- **Persistência de Dados:** Arquivo `.json` para gerenciamento de estado

---

### 🚀 Como Rodar o Projeto

*(Em breve será adicionado um guia de execução local e configuração do bot)*

---

### 📌 Objetivo Principal

- ✅ Praticar o desenvolvimento de bots para Discord com Python  
- ✅ Materializar uma piada interna de forma criativa e funcional  
- ✅ Aprender sobre persistência de dados simples com JSON  
- ✅ Explorar gerenciamento de estado e comandos personalizados  
- ⚠️ **Este não é um projeto sério!** É um espaço de aprendizado, teste e diversão.

---

📘 [English version below](#-bot-cabloco---discord-english-version)

---

# 🤖 Pal Bot - Discord

A simple Discord bot, created as a side project to bring a running joke between friends to life. The main idea is to have a bot that sends characteristic messages on specific days of the week, with a state control system to "activate" or "deactivate" its functions.

---

### 📜 About the Project

This bot was born from a joke and has no professional goal. It was developed as a fun way to practice building bots using the `discord.py` library and to explore data persistence concepts.

The "lore" behind the bot is that the **Pals** are mysterious entities who observe the server and manifest through cryptic messages — especially on Thursdays and Fridays. The project serves as a playground to test ideas and interactions with the Discord API.

---

### ✨ Current Features

- **`/activate`** – "Wakes up" the Pals, allowing them to send automatic messages.
- **`/deactivate`** – Gives the Pals some "time off", disabling message sending.
- **`/status`** – Checks whether the Pals are active or resting.
- **State Persistence** – The bot remembers its state (active/inactive) even after a restart, using a `.json` file for storage.

---

### 🔮 Future Features (The Core of the Bot)

The main logic, to be implemented next, will be based on scheduled tasks:

- **Thursday Messages:** The bot will send random and cryptic messages foreshadowing the arrival of Friday.
- **Friday Messages:** Celebration messages marking the arrival of the big day.
- **Special Warning:** A secret feature where, after 3 active Fridays, the bot will send a special warning message on a Wednesday and reset the counter.

---

### 🛠️ Technologies Used

- **Language:** Python 3  
- **Discord Library:** `discord.py` – Interaction with the Discord API  
- **Environment Variables:** `python-dotenv` – Secure token management  
- **Data Persistence:** JSON file to manage the bot's state  

---

### 🚀 How to Run the Project

*(A step-by-step guide on running the bot locally will be added soon)*

---

### 📌 Main Goals

- ✅ Practice Discord bot development using Python  
- ✅ Bring an inside joke to life in a creative and functional way  
- ✅ Learn simple data persistence with JSON  
- ✅ Explore state management and custom slash commands  
- ⚠️ **This is not a serious project!** It’s a fun space to learn, test, and enjoy coding.
