BOT_TOKEN='Enter Token Here'
BOT_PREFIX='Prefix Here!'

import discord
from discord.ext import commands

bot=commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	print('Bot is Online')
	print('--------------')

@bot.command()
@commands.has_permission(Administrator=True)
async def announce(ctx,*,message):
	await ctx.send(f'''@everyone''')
	await ctx.send(message)


@bot.command()
@commands.has_permission(Administrator=True)
async def embed(ctx,*,message):
	await ctx.send(f'''@everyone''')
	embed=discord.Embed(
		
		title=f'''Announcement from {ctx.message.author.mention}''',
		description=message,
		colour=discord.Colour.blue(),
		timestamp=ctx.message.created_at
		)
	await ctx.send(embed=embed)


bot.run(BOT_TOKEN)
