import discord
from discord.ext import commands, tasks
import datetime
import os

from dotenv import load_dotenv
from utils.data_handler import carregar_estado

load_dotenv() 
ID_CANAL_DE_TESTES = int(os.getenv("CANAL_AVISOS_ID"))

class SchedulerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.verificador_diario.start()

    def cog_unload(self):
        self.verificador_diario.cancel()

    @tasks.loop(minutes=1)
    async def verificador_diario(self):

        estado = carregar_estado()
        if not estado.get("ativado", False):
            return 
        
        canal = self.bot.get_channel(ID_CANAL_DE_TESTES)

        if canal:
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            await canal.send(f"O loop de teste rodou! Hora: {timestamp}")
        else:
            print(f"ERRO no Agendador: Canal com ID {ID_CANAL_DE_TESTES} não foi encontrado.")

    @verificador_diario.before_loop
    async def antes_do_verificador_diario(self):
        print("Agendador: Aguardando o bot ficar 100% pronto...")
        await self.bot.wait_until_ready()
        print("Agendador: Bot pronto. O loop de verificação vai começar.")

async def setup(bot: commands.Bot):
    await bot.add_cog(SchedulerCog(bot))