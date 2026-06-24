
import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1412434814891720759
AUTO_ROLE_ID = 1517579923865342252

BANNER_GIF = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3RqemR3c3A0MHl3NWw1NHE4a2FjdWVkdDdqdXppaXdxdHhobGF5ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iBILBPeCHDVuELjOND/giphy.gif"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    # Auto Role
    role = member.guild.get_role(AUTO_ROLE_ID)
    if role:
        try:
            await member.add_roles(role)
        except Exception as e:
            print(f"Role Error: {e}")

    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title="👑 Welcome to HSL & CORPORATION",
        description=(
            f"Welcome {member.mention}!\n\n"
            "🎉 We're glad to have you join our community.\n\n"
            "💬 Join the conversations\n"
            "🎮 Enjoy your stay\n"
            "🎁 Participate in events\n\n"
            f"👥 Member #{member.guild.member_count}\n\n"
            "🔥 Together We Rise."
        ),
        color=0x8A2BE2
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.set_image(url=BANNER_GIF)

    embed.set_footer(
        text="HSL & CORPORATION • Official Community"
    )

    await channel.send(
        content=f"🎉 Welcome {member.mention}!",
        embed=embed
    )


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title="👋 Goodbye",
        description=(
            f"**{member.name}** has left HSL & CORPORATION.\n\n"
            f"👥 Members Remaining: {member.guild.member_count}\n\n"
            "🔥 Once HSL, Always HSL."
        ),
        color=0xFF5555
    )

    embed.set_thumbnail(url=member.display_avatar.url)
    
    embed.set_image(url=BANNER_GIF)

    embed.set_footer(
        text="HSL & CORPORATION"
    )

    await channel.send(embed=embed)



import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1412434814891720759
AUTO_ROLE_ID = 1517579923865342252

BANNER_GIF = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3RqemR3c3A0MHl3NWw1NHE4a2FjdWVkdDdqdXppaXdxdHhobGF5ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iBILBPeCHDVuELjOND/giphy.gif"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    # Auto Role
    role = member.guild.get_role(AUTO_ROLE_ID)
    if role:
        try:
            await member.add_roles(role)
        except Exception as e:
            print(f"Role Error: {e}")

    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title="👑 Welcome to HSL & CORPORATION",
        description=(
            f"Welcome {member.mention}!\n\n"
            "🎉 We're glad to have you join our community.\n\n"
            "💬 Join the conversations\n"
            "🎮 Enjoy your stay\n"
            "🎁 Participate in events\n\n"
            f"👥 Member #{member.guild.member_count}\n\n"
            "🔥 Together We Rise."
        ),
        color=0x8A2BE2
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.set_image(url=BANNER_GIF)

    embed.set_footer(
        text="HSL & CORPORATION • Official Community"
    )

    await channel.send(
        content=f"🎉 Welcome {member.mention}!",
        embed=embed
    )


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title="👋 Goodbye",
        description=(
            f"**{member.name}** has left HSL & CORPORATION.\n\n"
            f"👥 Members Remaining: {member.guild.member_count}\n\n"
            "🔥 Once HSL, Always HSL."
        ),
        color=0xFF5555
    )

    embed.set_thumbnail(url=member.display_avatar.url)
    
    embed.set_image(url=BANNER_GIF)

    embed.set_footer(
        text="HSL & CORPORATION"
    )

    await channel.send(embed=embed)


bot.run(TOKEN)