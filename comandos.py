import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print("El bot esta activo")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if str(message.author.name) == "tipunquillo":
		if str(message.content).lower() == "guenas":
			await message.channel.send("wenas mijo ")
	if str(message.content).lower() == "mariachiloco":
		await message.add_reaction("\U0001F44B")

@client.event
async def on_reaction_add(reaction, user):
	await reaction.message.channel.send(str(user) + " reacciono con: " + reaction.emoji)

@client.event
async def on_message_edit(before, after):
    await before.channel.send(str(before.author) + "edito el mensaje \nAntes: " + before.content + "\nDespués: " + after.content)

client.run('')
