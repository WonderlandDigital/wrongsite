import discord, os, colorama, asyncio, random, ctypes, datetime, time, json, re
from discord import app_commands
from discord.ext import commands, tasks
from colorama import Fore
from datetime import datetime
from itertools import cycle
from asyncio import sleep
import openai

with open(
    'config.json'
) as f:  #This is where MadHatter reads your configuration, you can add more.
  config = json.load(f)
  token = config['token']
  prefix = config['prefix']
  update = config['version']
  logchannel = config['logchannelID']
  sleepseconds = config['Sleep Seconds']
  custompingmsg = config['Ping Message']

MadHatter = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
clear = lambda: os.system('cls')
statuscycle = cycle(["Slash commands!", "Hello Earth!", "I am brand new to discord", "How are you?", ":<"])  #-- Change the bot's playing status.

custom_role_name = {}
strikes = {}
openai.api_key = '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'


@tasks.loop(seconds=2)
async def change_status():
  await MadHatter.change_presence(activity=discord.Game(next(statuscycle)))


@MadHatter.event
async def on_ready():
  clear()
  await change_status()
  print(f"""{Fore.MAGENTA}
           .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
      `-._   ````    _.-'
          ``-------''
{Fore.WHITE}Logged in as: {Fore.GREEN}{MadHatter.user}
          """)
  try:
    synced = await MadHatter.tree.sync(
    )  #---- This is where all of your slash commands get synced.
    print(f"{Fore.GREEN}Synced{Fore.WHITE} {len(synced)} command(s)")
  except Exception as e:
    print(e)


#All goes to LOG CHANNEL


@MadHatter.listen("on_message")
async def pingReplier(message):
  sleep_seconds = sleepseconds
  message_to_reply = custompingmsg
  if f'<@{1106995171280814091}>' in str(message.content):
    async with message.channel.typing():
      await asyncio.sleep(0.1)
      msg = await message.reply(message_to_reply, delete_after=2)


@MadHatter.listen("on_message")
async def pingReplier(message):
  if f'game' in str(message.content):
    async with message.channel.typing():
      await asyncio.sleep(0.1)
      msg = await message.reply("Can I join in?", delete_after=2)


@MadHatter.listen("on_message")
async def pingReplier(message):
  if f'help' in str(message.content):
    async with message.channel.typing():
      await asyncio.sleep(0.1)
      msg = await message.reply(
        "Use my prefix ***/*** to see all commands silly!", delete_after=5)


@MadHatter.event
async def on_user_update(before, after):
  channel = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(
    title="User changed profile!",
    description=
    f"Username Before: {before.name}\nUsername After: {after.name}\nDiscrim Before: {before.discriminator}\nDiscrim After: {after.discriminator}",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  await channel.send(embed=embed)


@MadHatter.event
async def on_member_unban(guild, user):
  channel = MadHatter.get_channel(1094688186493566986)
  embed123 = discord.Embed(
    title="Unbanned!",
    description=
    f"**{user}** has been unbanned successfully.\nInside **{guild}**",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  await channel.send(embed=embed123)


@MadHatter.event
async def on_member_update(before, after):
  if not before.premium_since and after.premium_since:  # User started boosting the server
    guild = after.guild
    role_name = "Picture Perms"  # Name of the role to assign
    role = discord.utils.get(guild.roles, name=role_name)
    if role:
      await after.add_roles(role)
      print(f'Assigned the role "{role_name}" to {after.name}.')


@MadHatter.event
async def on_member_join(member):
  channel = MadHatter.get_channel(916847542682153060)
  embed = discord.Embed(
    title=
    f'Welcome to {member.guild.name} <a:6_floatingheart:963808375840337990> \n',
    color=0x9208ea)
  embed.add_field(name="\n𝐌𝐞𝐦𝐛𝐞𝐫", value=f"{member.mention}", inline=False)
  embed.set_thumbnail(url=member.avatar.url)
  embed.add_field(name="\n𝗜𝗗", value=member.id, inline=False)
  embed.add_field(name="\n𝗖𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲",
                  value=member.created_at,
                  inline=False)
  embed.set_footer(
    text=f'{member.guild.name}',
    icon_url=
    "https://i.pinimg.com/736x/6c/45/b2/6c45b24e8ffc0bc3a1a8d70e8f6c725f.jpg")
  await channel.send(embed=embed)  #Sends a welcome message to #Welcome Channel
  await member.send(
    f"I am Mad Hatter, and welcome {member.mention} to **{member.guild.name}.**\nRemember to use the <#963487085594042368> channel to gain access to the whole server.\nEnjoy your stay at **{member.guild.name}**! <a:6_floatingheart:963808375840337990>"
  )  #DM the member upon arrival to the server.
  await member.send(
    f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _https://media.tenor.com/XPvqU-vtvpsAAAAC/alice-in-wonderland-mad-hatter.gif"
  )


@MadHatter.event
async def on_message_delete(message):  #Checking if any messages get deleted.
  channelaudit = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(
    title=f"{message.author}'s Message was deleted.",
    description=
    f"Deleted Message: {message.content}\nAuthor: {message.author.mention}\nLocation: {message.channel.mention}",
    timestamp=datetime.now(),
    color=discord.Colour.red())
  embed.set_author(name=message.author.name,
                   icon_url=message.author.display_avatar)
  await channelaudit.send(embed=embed)


@MadHatter.event
async def on_message_edit(before,
                          after):  #Checking if any messages are edited.
  try:
    channelaudit = MadHatter.get_channel(1094688186493566986)
    embed = discord.Embed(
      title=f"{before.author} Edited their nessage",
      description=
      f"Before: {before.content}\nAfter: {after.content}\nAuthor: {before.author.mention}\nLocation: {before.channel.mention}",
      timestamp=datetime.now(),
      color=discord.Colour.blue())
    embed.set_author(name=after.author.name,
                     icon_url=after.author.display_avatar)
    await channelaudit.send(embed=embed)
  except:
    pass


@MadHatter.event
async def on_guild_channel_create(
    channel):  #Checking if any new channels are created.
  channelaudit = MadHatter.get_channel(1094688186493566986)


@MadHatter.event
async def on_guild_channel_delete(
    channel):  #Checking if any channel's get deleted.
  channelaudit = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(title=f"Channel {channel.name} was deleted",
                        timestamp=datetime.now(),
                        color=discord.Colour.red())
  await channelaudit.send(embed=embed)


@MadHatter.event
async def on_member_update(before, after):
  channelaudit = MadHatter.get_channel(1094688186493566986)
  if len(before.roles) > len(
      after.roles):  #Checking if a role has been removed.
    role = next(role for role in before.roles if role not in after.roles)
    embed = discord.Embed(
      title=f"{before}'s Role has Been Removed",
      description=f"{role.name} was removed from {before.mention}.",
      timestamp=datetime.now(),
      color=discord.Colour.red())
  elif len(after.roles) > len(
      before.roles):  #Checking if a role has been added.
    role = next(role for role in after.roles if role not in before.roles)
    embed = discord.Embed(
      title=f"{before} Got a New Role",
      description=f"{role.name} was added to {before.mention}.",
      timestamp=datetime.now(),
      color=discord.Colour.green())
  elif before.nick != after.nick:  #Checking if a user's nickname has been changed.
    embed = discord.Embed(
      title=f"{before}'s Nickname Changed",
      description=f"Before: {before.nick}\nAfter: {after.nick}",
      timestamp=datetime.now(),
      color=discord.Colour.blue())
  else:
    return
  embed.set_author(name=after.name, icon_url=after.display_avatar)
  await channelaudit.send(embed=embed)


# Utility Commands
@MadHatter.tree.command(description="To see if I am active, use this command!"
                        )  # To see if the bot is active.
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Hello {interaction.user.mention} I am a new bot in development.",
    ephemeral=True)


@MadHatter.tree.command(name="ping",
                        description="Pings Mad Hatter to see if he is online.")
async def ping(interaction: discord.Interaction):
  embed = discord.Embed(
    title="Pong🏓",
    description=
    f"On some shit... Mad Hatter's ping is: **{round(MadHatter.latency * 1000)}ms**",
    color=discord.Colour.green())
  embed.set_image(
    url=
    "https://ultimatedisneymoviemarathon.files.wordpress.com/2013/10/images-alice-wonderland-g1.jpg"
  )
  embed.set_footer(text=f"Requested by {interaction.user}",
                   icon_url=interaction.user.avatar.url)
  await interaction.response.send_message(embed=embed, ephemeral=True)


@MadHatter.tree.command(
  name='sync',
  description='Sync all of new commands to discords api - Owner only'
)  #To resync all commands to discord's api.
async def sync(interaction: discord.Interaction):
  if interaction.user.id == 176217706440294400:
    synced = await MadHatter.tree.sync()
    await interaction.response.send_message(
      f"Synced {len(synced)} command(s)! {interaction.user.mention}")
  else:
    await interaction.response.send_message(
      'You must be the owner to use this command!', ephemeral=True)


@MadHatter.tree.command(
  description="A command to restart Mad Hatter Discord bot.")
async def restart(interaction: discord.Interaction):
  if interaction.user.id == (176217706440294400):
    await interaction.response.send_message("I will be restarting now.",
                                            ephemeral=True)
    os.startfile('start.bat')
    os._exit(1)
  else:
    await interaction.response.send_message(
      "You need to be my developer to run this command.", ephemeral=True)


@MadHatter.tree.command(name="members",
                        description="Displays the member count.")
async def members(interaction: discord.Interaction):
  await interaction.response.send_message(
    f'Currently there are, `{interaction.guild.member_count}` members within **{interaction.guild.name}**.',
    ephemeral=True)


@MadHatter.tree.command(
  description="A command to purge 'x' amount of messages.")
async def purge(interaction: discord.Interaction, amount: str):
  msg = await interaction.response.send_message(f"Purged {amount} messages.",
                                                ephemeral=True)
  await interaction.channel.purge(limit=int(amount) + 1)
  await asyncio.sleep(0.2)


@MadHatter.tree.command(name="nuke",
                        description="A command to nuke a text channel.")
async def nuke(interaction: discord.Interaction):
  await interaction.channel.purge(limit=int(1000) + 1)
  await interaction.channel.send(
    f"{interaction.channel.mention} `Nuked by {interaction.user}`")


@MadHatter.tree.command(name="lookup",
                        description="Lookup another user's information.")
async def lookup(interaction: discord.Interaction,
                 user: discord.Member = None):
  if user == None:
    user = interaction.user
  rlist = []
  for role in user.roles:
    if role.name != "@everyone":
      rlist.append(role.mention)

    b = ", ".join(rlist)

  embed = discord.Embed(colour=user.color)
  embed.set_author(name=f"Information about - {user}"),
  embed.set_thumbnail(url=user.avatar.url)
  embed.add_field(name='Username:', value=user.display_name, inline=False)
  embed.add_field(name='Discord ID:', value=user.id, inline=False)
  embed.add_field(name='Account creation:',
                  value=user.created_at,
                  inline=False)
  embed.add_field(name='Joined server:', value=user.joined_at, inline=False)
  embed.add_field(name="Bot", value=user.bot, inline=False)
  await interaction.response.send_message(embed=embed, ephemeral=True)


@MadHatter.tree.command(
  name="avatar",
  description="A command to get a specified users avatar, or yourself.")
async def avatar(interaction: discord.Interaction,
                 username: discord.Member = None):
  if username == None:
    embed = discord.Embed(
      title="Mad Hatter! [ERROR] ❌",
      description="Please specify a member to get their avatar",
      color=0xe74c3c)
    embed.set_image(url=interaction.user.avatar.url)
    embed.add_field(name=f"\n{interaction.user}'s Avatar", value="")
    embed.set_footer(
      text=f"{interaction.guild.name} | Requested by {interaction.user} ")
    await interaction.response.send_message(embed=embed, ephemeral=True)
  else:
    userAvatarURL = username.avatar.url
    embed = discord.Embed(title='{}\'s Avatar'.format(username.name),
                          color=0x9208ea)
    embed.set_image(url='{}'.format(userAvatarURL))
    embed.set_footer(
      text=f"{interaction.guild.name} | Requested by {interaction.user} ")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@MadHatter.tree.command(name="changenick",
                        description="A command to change a users nickname.")
async def change(interaction: discord.Interaction, member: discord.Member,
                 nick: str):
  await member.edit(nick=nick)
  await interaction.response.send_message(
    f"Successfully nicknamed {member} to {nick}", ephemeral=True)


@MadHatter.tree.command(
  name="version",
  description="A command to check Mad Hatter's current update.")
async def version(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"I am currently using patch, {update}.")


@MadHatter.tree.command(
  name="circus", description="A command to upload clips to my discord server.")
async def circus(interaction: discord.Interaction, game: str, clipname: str,
                 link: str):
  clipchannel = MadHatter.get_channel(1001905092225675356)
  embed = discord.Embed(color=0x9208ea, timestamp=datetime.now())
  embed.set_author(
    name=f"Successfully clipped, {game}!",
    icon_url="https://media4.giphy.com/media/xT1XGSMV4l7QU3sAzC/giphy.gif")
  embed.set_footer(text=f"Uploader: {interaction.user}")
  await clipchannel.send(
    f"**{clipname}**||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _{link}"
  )
  await clipchannel.send(embed=embed)
  await interaction.response.send_message(
    f"Successfully uploaded a clip!\nGame: **{game}**\nClip Title: **{clipname}**\nUploaded to: **{clipchannel.mention}**",
    ephemeral=True)


@MadHatter.tree.command(name="addrole",
                        description="Add a role to another user.")
async def addrole(interaction: discord.Interaction, member: discord.Member,
                  role: discord.Role):
  await member.add_roles(role)
  channel = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(
    title="Added a Role!",
    description=f"{member.mention} **was given:** {role.mention}",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed.set_footer(text="Wonderland Digital")
  await interaction.response.send_message(embed=embed)
  await channel.send(embed=embed)


@MadHatter.tree.command(name="removerole",
                        description="Remove a role to another user.")
async def addrole(interaction: discord.Interaction, member: discord.Member,
                  role: discord.Role):
  await member.remove_roles(role)
  channel = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(
    title="Removed a Role!",
    description=f"{member.mention} **lost the role:** {role.mention}",
    timestamp=datetime.now(),
    color=discord.Colour.red())
  embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed.set_footer(text="Wonderland Digital")
  await interaction.response.send_message(embed=embed)
  await channel.send(embed=embed)


@MadHatter.tree.command(name="ban",
                        description="A command to ban another user.")
async def ban(interaction: discord.Interaction, member: discord.Member,
              reason: str, duration: str):
  await member.send(
    f"Do not direct message <@176217706440294400> for a ban appeal, cry your heart out to his moderators so you get pity."
  )
  embed = discord.Embed(
    title="Banned!",
    description=
    f"**User:** {member.mention}\n**Reason:** {reason}\n**Duration:** {duration}",
    timestamp=datetime.now(),
    color=discord.Colour.red())
  embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed.set_footer(text="Wonderland Digital")
  await interaction.response.send_message(embed=embed)
  embed = discord.Embed(
    title="You have been banned!",
    description=
    f"***Reason:*** ```{reason}```\n***Guild:*** ```{interaction.guild.name}```\n***Banned by:*** ```{interaction.user}```\n***Duration:*** ```{duration}```",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  embed.set_author(name=f"You have violated our TOS.",
                   icon_url=interaction.user.avatar.url)
  await member.send(embed=embed)
  await interaction.guild.ban(member, reason=f"{reason}")


@MadHatter.tree.command(name="coinflip",
                        description="A command to flip a coin.")
async def coinflip(interaction: discord.Interaction):
  n = random.randint(0, 1)
  embed = discord.Embed(title="Coinflip", color=0x9208ea)
  embed.add_field(name="`What shall it be?`", value="", inline=False)
  embed.set_thumbnail(
    url="https://media.tenor.com/bd3puNXKLwUAAAAC/coin-toss.gif")
  embed.set_footer(text=f"Wonderland | Requested by {interaction.user}")
  await interaction.response.send_message(embed=embed)
  await interaction.channel.send(f"**Heads**" if n == 1 else "**Tails**")


@MadHatter.tree.command(
  name="unban", description="A command to unban another user (use their ID)")
async def unban(interaction: discord.Interaction, userid: str, reason: str):
  guild = interaction.guild
  user = discord.Object(id=userid)
  await guild.unban(user=user, reason=reason)
  unbanembed = discord.Embed(
    title=f"Unbanned!",
    description=f"**User:** <@{userid}>\n**Reason:** {reason}",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  unbanembed.set_author(name=interaction.user,
                        icon_url=interaction.user.avatar.url)
  unbanembed.set_footer(text="Wonderland Digital")
  await interaction.response.send_message(embed=unbanembed)


@MadHatter.tree.command(
  name="blunt", description="A command to pass a blunt to another user.")
async def blunt(interaction: discord.Interaction, user: discord.Member = None):
  if user is None:
    embed = discord.Embed(
      title="The Blunt Rotation",
      description="You got no friends? or are you a lone wolf.",
      color=0x2ecc71,
      timestamp=datetime.now())
    embed.add_field(name=f"There is no one to pass to...",
                    value="Maybe, you should take another hit.")
    embed.set_image(
      url="https://i.kym-cdn.com/photos/images/facebook/002/410/683/01d.jpg")
    embed.set_footer(text=f"Wonderland Digital")
    await interaction.response.send_message(embed=embed)
  else:
    embed = discord.Embed(title=f"The Blunt Rotation",
                          description="",
                          color=0x2ecc71,
                          timestamp=datetime.now())
    embed.add_field(name=f"{interaction.user} Passed to:",
                    value=f"{user.mention} It's your turn to take a toke.")
    embed.set_image(
      url=
      "https://media.tenor.com/DWU1rRs2tZ8AAAAd/pass-the-joint-wiz-khalifa.gif"
    )
    embed.set_footer(text=f"Wonderland Digital")
    await interaction.response.send_message(embed=embed)


@MadHatter.tree.command(
  name="customrole",
  description="A command for boosters to create a custom role.")
async def customrole(interaction: discord.Interaction, rolename: str,
                     rolecolor: str):
  booster_id = interaction.user.id
  if booster_id in custom_role_name:
    await interaction.response.send_message(
      'You have already created a custom role.')
  else:
    guild = interaction.guild
    existing_role = discord.utils.get(guild.roles, name=rolename)
  if existing_role:
    await interaction.response.send_message(
      'A role with that name already exists.')
  else:
    new_role = await guild.create_role(name=rolename,
                                       color=discord.Color(int(rolecolor, 16)))
    await interaction.user.add_roles(new_role)
    custom_role_name[booster_id] = rolename
    await interaction.response.send_message(
      f'Created and assigned the role {new_role.mention} to {interaction.user.mention}.'
    )


snipe_message_content = None
snipe_message_author = None


@MadHatter.listen("on_message_delete")
async def on_message_delete(message):
  global snipe_message_content
  global snipe_message_author

  snipe_message_content = message.content
  snipe_message_author = message.author.mention


@MadHatter.tree.command(
  name="snipe", description="A command to snipe a recently deleted message.")
async def snipe(interaction: discord.Interaction):
  if snipe_message_content == None:
    await interaction.response.send_message(
      "There is no deleted messages to snipe.")
  else:
    embed = discord.Embed(title="Mad Hatter Sniped!",
                          description=f"**Message**:\n{snipe_message_content}",
                          color=0x9208ea,
                          timestamp=datetime.now())
    embed.set_image(
      url="https://media.tenor.com/KtfhXv5J1UEAAAAM/kill-boys-kill.gif")
    embed.add_field(name=f"Sent by:\n", value=f"{snipe_message_author}")
    embed.set_footer(text=f"Wonderland Digital")
    embed.set_author(name=interaction.user,
                     icon_url=interaction.user.avatar.url)
    await interaction.response.send_message(embed=embed)


#Non Slash Admin commands

@MadHatter.event
async def on_message(message):
  if message.author == MadHatter.user:
    return
  if message.content.startswith(prefix + 'ask'):
    question = message.content[len(prefix + 'ask'):].strip()
    response = generate_response(question)
    await message.channel.send(response)

def generate_response(question):
  response = openai.Completion.create(engine='text-davinci-003', prompt=question, max_tokens=50)
  return response.choices[0].text.strip()
    


MadHatter.run(token)
