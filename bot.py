
import discord
import random
from discord.ext import commands
from config import token

class Car:

    def __init__(self, merek, warna,) :
        self.merek = merek
        self.warna = warna

    def info(self) :
        return f"Mobil ini bermerek {self.merek}, Warnanya {self.warna}"


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah login sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ini adalah echo-bot yang dibuat dengan pustaka discord.py!')

@client.command()
async def info(ctx):
    await ctx.send('Bot ini bisa mengikuti pesan yang kamu kirim! ketik "/help_me" untuk menampilkan command list')

@client.command()
async def Coin_flip(ctx):
    N = random.randint(1,10)
    if N <= 5:
        await ctx.send('Head!')

    else:
        await ctx.send('Tail!')

@client.command()
async def car(ctx, merek: str, warna: str):
    mobil = Car(merek, warna)
    await ctx.send(mobil.info())

@client.command()
async def help_me(ctx):
    await ctx.send ('Command yang bisa kamu gunakan :\n '
    '/about dan /info = info tentang bot \n ' 
    '/Coin_flip = lemparan koin\n' 
    '/car <merek> <warna> = buat mobil baru' )



client.run(token)
