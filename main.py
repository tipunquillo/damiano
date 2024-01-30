import discord, os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print("El bot esta encendido")

token = os.getenv('TOKEN') 
client.run(token)
