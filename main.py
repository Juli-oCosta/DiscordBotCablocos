import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class Cabloco(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents = intents
        )
        
    async def setup_hook(self):
        print("Iniciando o hook de configuração...")
        
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f"-> Módulo '{filename[:-3]}' carregado com sucesso.")
                except Exception as e:
                    print(f"Falha ao carregar o módulo '{filename[:-3]}'. Erro: {e}")

        try:
            synced = await self.tree.sync()
            print(f"-> {len(synced)} comandos de barra sincronizados com o Discord.")
        except Exception as e:
            print(f"Falha ao sincronizar comandos: {e}")

    async def on_ready(self):
        print("-" * 40)
        print(f"Os {self.user} estão atentos e online!")
        print(f"ID do Bot: {self.user.id}")
        print("-" * 40)

if __name__ == "__main__":
    bot = Cabloco()
    bot.run(TOKEN)
