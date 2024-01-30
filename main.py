import discord, os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print("El bot esta encendido")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if str(message.author.name) == "oskh0s":
    if str(message.content).lower() == "buenas":
      await message.channel.send("wenas")
  if str(message.content).lower() == "lagartijo":
    await message.add_reaction("🦎")

@client.event
async def on_reaction_add(reaction, user):
  await reaction.message.channel.send(
      str(user) + " te dejo puesto un: " + reaction.emoji)

token = os.getenv('TOKEN') 
client.run(token)
