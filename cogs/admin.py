import discord
from discord import app_commands
from discord.ext import commands
from utils.data_handler import carregar_estado, salvar_estado

class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ativar", description="Ativa o Bot.")
    async def mensagem_ativacao(self, interaction:discord.Interaction):
        estado = carregar_estado()
        estado["ativado"] = True
        salvar_estado(estado)

        await interaction.response.send_message(
            f"Não se preocupe {interaction.user.mention}, nós, os cablocos estamos ativos sempre de olho."
        )

    @app_commands.command(name="desativar", description="Desativa o Bot")
    async def mensagem_desativacao(self, interaction:discord.Interaction):
        estado = carregar_estado()
        estado["ativado"] = False
        salvar_estado(estado)

        await interaction.response.send_message(
            f"Valeu por nos dar férias {interaction.user.mention}, estamos desativando para descansar."
        )

    @app_commands.command(name="status", description="Verifica qual o status do Bot.")
    async def mensagem_status(self, interaction:discord.Interaction):
        estado = carregar_estado()
        
        ativo = estado.get("ativado", False)
        mensagem = (
            f"Aopa {interaction.user.mention}, no momento nós cablocos estamos "
            + ("ativos." if ativo else "desativados.")
        )
        
        await interaction.response.send_message(mensagem)

async def setup(bot):
    await bot.add_cog(AdminCog(bot))