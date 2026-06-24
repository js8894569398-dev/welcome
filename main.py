import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

CHANNEL_ID = 1364819822948519957
AUTO_ROLE_ID = 1356635989862514688 

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
    embed.set_footer(text="HSL & CORPORATION • Official Community")

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
    embed.set_footer(text="HSL & CORPORATION • Official Community")

    await channel.send(embed=embed)


# Commands

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency * 1000)}ms")


@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author

    embed = discord.Embed(
        title=f"{member.name}'s Avatar",
        color=0x8A2BE2
    )

    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)


@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild

    embed = discord.Embed(
        title="🏠 Server Info",
        color=0x8A2BE2
    )

    embed.add_field(name="Server", value=guild.name, inline=False)
    embed.add_field(name="Members", value=guild.member_count, inline=False)

    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)

    await ctx.send(embed=embed)


bot.run(TOKEN)