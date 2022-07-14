import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from discord import Embed
import datetime
intents = discord.Intents.default()
intents.members = True
intents.bans = True



keep_alive()
bot = commands.Bot(command_prefix = "+", intents = intents)
bot.deleted_messages = {}


@bot.event
async def on_ready():
    print("Looggy Ready!")
    await bot.change_presence(status=discord.Status.dnd,activity=discord.Game(name="Eating a Watermelon"))
@bot.event
async def on_message_delete(message: discord.Message):
  guild = message.guild
  channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='capybara')
  
  image = None
    
  if message.attachments:
      image = await message.attachments[-1].to_file(use_cached=True)
  
  bot.deleted_messages[message.channel.id] = (message.content, message.author, message.channel.name, message.created_at, image)

  

  embed = discord.Embed(description=message.content, color=discord.Color.orange(), timestamp=message.created_at)
    
  if image:
        
      embed.set_image(url=f"attachment://{image.filename}")
  embed.set_author(name=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
  embed.set_footer(text=f"Deleted in : #{message.channel.name}")

  await channel.send(embed=embed, file=image)





  

  
@bot.event
async def on_message_edit(message_before, message_after,):
  
  guild = message_before.guild
  channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='capybara')
  
  embed = Embed(
             color=0xE6F139
        ).set_author(name=message_before.author, url=Embed.Empty, icon_url=message_before.author.avatar_url)

  embed.add_field(name=message_before.content, value="Before",
                    inline=True)
  embed.add_field(name=message_after.content, value="After",
                    inline=True)
  embed.timestamp = message_before.created_at
  embed.set_footer(text=f"Edited in : #{message_before.channel.name}")
  
  await channel.send(embed=embed)


@bot.event
async def on_member_join(member):
  #channel=bot.get_channel(878441637901115424)
  guild = member.guild
  channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='capybara')
  embed = Embed(
             color=0x2EDD4D
        ).set_author(name="Member Join", url=Embed.Empty, icon_url=member.avatar_url)
  embed.add_field(name=member.name + "#" + member.discriminator,  value=member.mention,
                    inline=True)
  
  embed.timestamp = datetime.datetime.utcnow()
  
  
  await channel.send(embed=embed)

@bot.event
async def on_member_ban(guild,member):
  channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='capybara')
  embed = Embed(
             color=0xFF0000
        ).set_author(name="Member Banned", url=Embed.Empty, icon_url=member.avatar_url)
  embed.add_field(name=member.name + "#" + member.discriminator, value=member.mention,
                    inline=True)
  
  embed.timestamp = datetime.datetime.utcnow()
  
  
  await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
  guild = member.guild
  channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='capybara')
  embed = Embed(
             color=0xBE1DDE
        ).set_author(name="Member Leave", url=Embed.Empty, icon_url=member.avatar_url)
  embed.add_field(name=member.name + "#" + member.discriminator, value=member.mention,
                    inline=True)
  
  embed.timestamp = datetime.datetime.utcnow()
  
  
  await channel.send(embed=embed)



@bot.event
async def on_member_kick(member):
  guild = member.guild
  channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='capybara')
  embed = Embed(
             color=0xF17439
        ).set_author(name="Member Kicked", url=Embed.Empty, icon_url=member.avatar_url)
  embed.add_field(name=member.name + "#" + member.discriminator, value=member.mention,
                    inline=True)
  
  embed.timestamp = datetime.datetime.utcnow()
  
  
  await channel.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
  guild = ctx.message.guild
  overwrites = {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    guild.default_role: discord.PermissionOverwrite(view_channel=False),
    guild.me: discord.PermissionOverwrite(read_messages=True)
}

  await guild.create_text_channel('capybara', overwrites=overwrites)

@bot.event
async def on_member_update(before, after):
  if before.nick != after.nick:
    guild = before.guild
    channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='capybara')
  
    embed = Embed(
             color=0x5bf0e6
        ).set_author(name=before, url=Embed.Empty, icon_url=before.avatar_url)


    embed.add_field(name=before.nick, value="Before",
                    inline=True)
    embed.add_field(name=after.nick, value="After",
                    inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Nickname Update")
  
    await channel.send(embed=embed)
  
 
  



#@bot.event
#async def on_member_join(self, member):
   # for channel in member.guild.channels:
        
     #       embed = discord.Embed(color=0x4a3d9a)
  #3        embed.add_field(name="Member Joined", value=f"{member.name}", inline=False)
     #       embed.set_image(url=member.avatar_url)
     #       channel = bot.get_channel(878441637901115424)
    #        await channel.send(embed=embed)

bot.run(os.getenv('TOKEN'))
