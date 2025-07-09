import discord
from discord import app_commands
import os
from dotenv import load_dotenv

from utils.data_handler import carregar_estado, salvar_estado

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class Cabloco(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            intents = intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"Os {self.user} estão atentos.")

bot = Cabloco()

@bot.tree.command(name="ativar", description="Ativa o Bot.")
async def mensagem_ativacao(interaction:discord.Interaction):
    estado = carregar_estado()
    estado["ativado"] = True
    salvar_estado(estado)
    await interaction.response.send_message(
        f"Não se preocupe {interaction.user.mention}, nós, os cablocos estamos ativos sempre de olho."
    )

@bot.tree.command(name="desativar", description="Desativa o Bot")
async def mensagem_desativacao(interaction:discord.Interaction):
    estado = carregar_estado()
    estado["ativado"] = False
    salvar_estado(estado)
    await interaction.response.send_message(
        f"Nós cablocos também temos férias {interaction.user.mention}, estamos desativados para descansar."
    )

@bot.tree.command(name="status", description="Verifica qual o status do Bot.")
async def mensagem_status(interaction:discord.Interaction):
    mensagem = f"Aopa {interaction.user.mention}, no momento nós cablocos estamos"
    estado = carregar_estado()
    if estado["ativado"] == True:
        mensagem += " ativos."
    else:
        mensagem += " desativados."
    
    await interaction.response.send_message(
        mensagem
    )

bot.run(TOKEN)
