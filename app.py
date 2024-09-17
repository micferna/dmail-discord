import discord
from discord.ext import commands
from config import TOKEN
from message import MESSAGE

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} est connecté et prêt !')

@bot.command()
@commands.has_permissions(administrator=True)
async def envoyer_mp(ctx):
    total_members = len(ctx.guild.members)
    success_count = 0
    fail_count = 0

    for member in ctx.guild.members:
        try:
            await member.send(MESSAGE)
            print(f"Message envoyé à {member.name}")
            success_count += 1
        except discord.Forbidden:
            print(f"Impossible d'envoyer un message à {member.name}")
            fail_count += 1

    await ctx.send(f"Messages privés envoyés :\n"
                   f"✅ Réussis : {success_count}\n"
                   f"❌ Échoués : {fail_count}\n"
                   f"📊 Total des membres : {total_members}")

bot.run(TOKEN)
