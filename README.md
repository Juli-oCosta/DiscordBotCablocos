# 🤖 Bot Cabloco - Discord

Um bot para Discord simples, criado como um projeto para passar o tempo e materializar uma piada interna entre amigos. A ideia principal é ter um bot que envia mensagens características em dias específicos da semana, com um controle de estado para "ativar" ou "desativar" suas funções.

---

### 📜 Sobre o Projeto

Este bot nasceu de uma brincadeira e não possui um objetivo profissional. Ele foi desenvolvido como uma forma divertida de praticar a criação de bots com a biblioteca `discord.py` e explorar conceitos de persistência de dados.

O "lore" do bot é que os "cablocos" são entidades que observam o servidor e se manifestam com mensagens enigmáticas, principalmente às quintas e sextas-feiras. O projeto serve como um playground para testar ideias e interações com a API do Discord.

### ✨ Funcionalidades Atuais

* **/ativar:** "Acorda" os cablocos, permitindo que eles enviem as mensagens automáticas.
* **/desativar:** Coloca os cablocos "de férias", desativando as mensagens.
* **/status:** Verifica se os cablocos estão ativos ou descansando.
* **Persistência de Estado:** O bot lembra se está ativo ou inativo mesmo após ser reiniciado, salvando seu estado em um arquivo `JSON`.

### 🎯 Funcionalidades Futuras (O Core do Bot)

A lógica principal, a ser implementada a seguir, é baseada em tarefas agendadas:

* **Mensagens de Quinta-feira:** Durante as quintas, o bot enviará mensagens aleatórias e enigmáticas sobre a chegada da sexta-feira.
* **Mensagens de Sexta-feira:** Comemorações e anúncios de que o grande dia chegou.
* **Aviso Especial:** Uma funcionalidade secreta onde, a cada 3 sextas-feiras acumuladas, o bot envia uma mensagem de aviso especial em uma quarta-feira e zera o contador.

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** `Python 3`
* **Biblioteca Discord:** `discord.py` para toda a interação com a API do Discord.
* **Variáveis de Ambiente:** `python-dotenv` para gerenciar o token do bot de forma segura.
* **Persistência de Dados:** `JSON` para armazenar o estado de ativação do bot.

### 🚀 Como Rodar o Projeto (Adicionarei futuramente)

### 📌 Objetivo Principal

✅ Praticar o desenvolvimento de bots para Discord em Python.
✅ Materializar uma piada interna de forma criativa e funcional.
✅ Aprender sobre persistência de dados simples com JSON e gerenciamento de estado.
✅ **Não é um projeto sério!** É um espaço para aprender, testar e se divertir com programação.
