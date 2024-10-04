import discord
import asyncio
from discord.ext import commands

# Inisialisasi bot
intents = discord.Intents.default()
intents.typing = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Token bot dari Discord Developer Portal
TOKEN = 'MTI5MTgyNDYwMjA1NzgwNTk4Nw.GMDp6q.AH8D5h4587v_3q6k7Be1vXVrNQB-7yqfFeAhJo'

# Channel list dan custom teks untuk dikirim
channels_to_type_in = {
    1291823404281888770: "Sell at Xiry \nGhost Charm 31<:WL:880251447470596157> \nGhost Be Gone 14<:WL:880251447470596157> \nNeutron Power Gun 34<:WL:880251447470596157> \nDark Spirit Board 22<:WL:880251447470596157> \nEctobone 5<:WL:880251447470596157> \nSet Ghost 3<:WL:880251447470596157>",  # Ganti dengan ID channel dan teks
    #987654321098765432: "Another message for a different channel!",
}

# Waktu delay antar pesan (dalam detik)
typing_delay = 10  # Ubah sesuai kebutuhanmu


# Fungsi untuk mengetik dan mengirim pesan di beberapa channel
async def auto_typer():
    await bot.wait_until_ready()
    
    while not bot.is_closed():
        for channel_id, text in channels_to_type_in.items():
            channel = bot.get_channel(channel_id)
            
            if channel:
                try:
                    # Mulai mengetik di channel
                    async with channel.typing():
                        await asyncio.sleep(typing_delay)  # Simulasi waktu mengetik
                        
                    # Kirim pesan kustom setelah mengetik
                    await channel.send(text)
                    print(f"Sent message to {channel.name}")
                    
                except Exception as e:
                    print(f"Error typing in {channel_id}: {e}")
        
        # Menunggu sebelum mulai siklus berikutnya
        await asyncio.sleep(typing_delay)


# Override setup_hook untuk memulai auto_typer saat bot siap
class MyBot(commands.Bot):
    async def setup_hook(self):
        # Menjalankan fungsi auto_typer sebagai task
        self.loop.create_task(auto_typer())

# Inisialisasi bot menggunakan subclass MyBot
bot = MyBot(command_prefix="!", intents=intents)

# Event ketika bot sudah siap
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Menjalankan bot
bot.run(TOKEN)
