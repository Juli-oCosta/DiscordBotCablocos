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

Cablocos online, fiot! 🌪️
