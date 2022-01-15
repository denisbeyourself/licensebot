import discord
import random
import sqlite3
import asyncio
import traceback
import json
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.cooldowns import BucketType

#MySQL Calls
conn = sqlite3.connect('keys.db')
c = conn.cursor()

#Discord Command
prefix = "$"
TOKEN = "PUT TOKE HERE"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

#Calls
bot_developer = 'cracked.to/Kojixus'

#color
color = 0x8317FF

#Admin List - Insert the user id of the person here 
admin_list = [put your user id here]

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n------\nMy current prefix is: / \n-----")
    c.execute('UPDATE redeemed_keys SET duration = duration+1 WHERE duration>0')
    conn.commit()
    print("added")
    await bot.change_presence(activity=discord.Game(name=f"Approving Keys {bot.user.name}.\nUse / to interacte with me!"))

#MySQL
def create_key_database():
    conn = sqlite3.connect('keys.db')
    c.execute('CREATE TABLE IF NOT EXISTS key(keys TEXT, duration_start VALUE)')
def create_table_redeemedkeys():
    c.execute('CREATE TABLE IF NOT EXISTS redeemed_keys(discord_id TEXT, key TEXT, duration VALUE)')
create_key_database()
create_table_redeemedkeys()

@bot.command()
async def info(ctx):
    c.execute("SELECT count(*) from redeemed_keys")
    ctx.users = c.fetchall()
    guild = bot.get_guild(ctx.message.guild.id)
    members = len(guild.members)
    role = guild.get_role(member role id here)
    size = len(role.members)
    embed=discord.Embed(title="Buyer Info",color=color,inline=True)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="Buyers:",value=size,inline=True)
    embed.add_field(name="Members:",value=f"{members}",inline=True)
    embed.add_field(name="Developer",value=f"{bot_developer}",inline=True)
    embed.set_footer(text='List of Staff Commands')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role("PUR YOUR STAFF ROLE HERE")
async def staffhelp(ctx):
    await ctx.send(f"{ctx.author.mention},sending you a the list of commands")
    embed = discord.Embed(title='List of Staff commands',description='The list of simple commands',color=color)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="$generatekey days",value="Generates a key with a chosen amount of days",inline=False)
    embed.add_field(name="$generatekey days userid",value="DM's user with license key",inline=False)
    embed.add_field(name="$removesubscription @user",value="Remove a subscription from someone using their discord ID",inline=False)
    embed.add_field(name="$adddayall",value="Adds a day to everyones license, used on special occassions ;)",inline=False)
    embed.add_field(name="$add_day @user amount",value="Adds a certain amount of days to a user",inline=False)
    embed.set_footer(text='List of Staff Commands')
    await ctx.author.send(embed=embed)

@bot.command()
async def help(ctx):
    await ctx.send(f"{ctx.author.mention}, I have sent you a DM showing my commands!")
    embed = discord.Embed(title = 'Help Commands',description = 'Here are some helpful commands to use',color=color)
    embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="$redeem",value="Allows you to redeem a key",inline=False)
    embed.add_field(name="$subscription",value="Check how long you have remaining on your subscription",inline=False)
    embed.add_field(name="$info",value="Information about the server and bot",inline=False)
    embed.set_footer(text='Help commands')
    await ctx.author.send(embed=embed)

@bot.command()
async def generatekey(ctx,length,id:int = None):
    if ctx.author.id in admin_list:
                if id == None:
                    letters = ["A","B","C","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    letter1 = random.choice(letters)
                    letter2 = random.choice(letters)
                    letter3 = random.choice(letters)
                    letter4 = random.choice(letters)
                    letter5 = random.choice(letters)
                    letter6 = random.choice(letters)
                    letter7 = random.choice(letters)
                    letter8 = random.choice(letters)
                    letter9 = random.choice(letters)
                    letter10 = random.choice(letters)
                    letter11 = random.choice(letters)
                    letter12 = random.choice(letters)
                    letter13 = random.choice(letters)
                    letter14 = random.choice(letters)
                    letter15 = random.choice(letters)
                    code = (letter1+letter2+letter3+letter4+letter5+letter6+letter7+letter8+letter9+letter10+letter11+letter12+letter13+letter14+letter15)
                    duration_start = length
                    embed = discord.Embed(title="Key Generated",description=(f"A key with {duration_start} days was successfully generated: {code}"),color=color)
                    embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                    embed.set_footer(text='Key Generated') 
                    c.execute(f"INSERT INTO key (keys,duration_start) VALUES('{code}', {duration_start})")
                    conn.commit()
                    await ctx.send(embed=embed)
                    embed = discord.Embed(title="Instructions",description=(f"""Here’s your key: **{code}** Please run the command /redeem (key) in the bot commands channel"""),color=color)
                    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                    embed.set_footer(text='Key Sent') 
                    await ctx.send(embed=embed)
                else:
                    letters = ["A","B","C","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    letter1 = random.choice(letters)
                    letter2 = random.choice(letters)
                    letter3 = random.choice(letters)
                    letter4 = random.choice(letters)
                    letter5 = random.choice(letters)
                    letter6 = random.choice(letters)
                    letter7 = random.choice(letters)
                    letter8 = random.choice(letters)
                    letter9 = random.choice(letters)
                    letter10 = random.choice(letters)
                    letter11 = random.choice(letters)
                    letter12 = random.choice(letters)
                    letter13 = random.choice(letters)
                    letter14 = random.choice(letters)
                    letter15 = random.choice(letters)
                    code = (letter1+letter2+letter3+letter4+letter5+letter6+letter7+letter8+letter9+letter10+letter11+letter12+letter13+letter14+letter15)
                    duration_start = length
                    embed = discord.Embed(title="Key Generated",description=(f"A key with {duration_start} days was successfully generated: {code}"),color=color)
                    embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                    embed.set_footer(text='Key Generated') 
                    await ctx.send(embed=embed)
                    try:
                        server = bot.get_guild(server id)
                        user = server.get_member(id)
                        embed=discord.Embed(title="Subscription Key",description=(f"""Here’s your key: **{code}**\nPlease run the command /redeem (key) in the bot commands channel!."""),color=color)
                        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                        embed.set_footer(text='Have fun generating!') 
                        await user.send(embed=embed)
                        c.execute(f"INSERT INTO key (keys,duration_start) VALUES('{code}', {duration_start})")
                        conn.commit()
                        await ctx.send(f"Successfully sent key to user with id {id}")
                    except:
                        embed = discord.Embed(title="Failed Request",description="Could not send a DM to that user",color=color)
                        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                        embed.set_footer(text='Failed to Send')  
                        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Unauthorised access",description=(f"You do not have permission to generate a key"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Unauthorised')  
        await ctx.send(embed=embed)
#key redeem command
@bot.command()
async def redeem(ctx, key):
    c.execute("SELECT * FROM key WHERE keys=?", (key,))
    if not c.fetchone():
        embed = discord.Embed(title="Key is invalid",description=(f"That is not a valid key, please open a ticket!"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Invalid')  
        await ctx.send(embed=embed)
    else:
        c.execute("SELECT * FROM key WHERE keys=?", (key,))
        data = c.fetchall()
        subscription_length = data[0][1]
        discord_user = ctx.message.author.id
        key = data[0][0]
        print(data)
        embed = discord.Embed(title="You found a key!",description=(f"Thank you for your purchase {ctx.author.name}, your key has been redeemed\n**You have {subscription_length} days left on your license**"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Your key has been found')
        guild = ctx.guild
        role = guild.get_role(premium role id here)
        member = ctx.author
        await member.add_roles(role)
        await ctx.send(embed=embed)
        c.execute(f'DELETE from key WHERE keys=?', (key,))
        conn.commit()
        embed = discord.Embed(title="Key successfully redeemed",description = (f"Thank you for purchasing access to our Premium Account Generator\nYou are able to generate an account every one minute due to the cooldown in the #generator channel\nIf you encounter any problems feel free to message a member of staff\nIf the account does not work wait for the cooldown and generate another one!\nHave fun!"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Key has been redeemed')
        await ctx.author.send(embed=embed)
        c.execute(f"INSERT INTO redeemed_keys (discord_id, key, duration) VALUES('{discord_user}','{key}','{subscription_length}')")
        conn.commit()
#add extra day to key command
@bot.command()
async def add_day(ctx, member:discord.Member, amount:int):
    if ctx.message.author.id in admin_list:
        member_id = member.id
        c.execute("SELECT * FROM redeemed_keys WHERE discord_id=?", (member_id,))
        data = c.fetchall()
        current_amount_of_days = (data[0][2])
        c.execute(f'DELETE from redeemed_keys WHERE discord_id=?', (member_id,))
        conn.commit()
        new_days = (current_amount_of_days+amount)
        key = "updated amount"
        c.execute(f"INSERT INTO redeemed_keys (discord_id, key, duration) VALUES('{member_id}','{key}','{new_days}')")
        conn.commit()
        embed=discord.Embed(title="Added a Day Successful",description=f"Added {amount} to {member.name}'s subscription",color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Request Successful')      
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Your Request Failed",description="You do not have permission to add days to a user's subscription",color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Request Failed')  
        await ctx.send(embed=embed)
@bot.command()
@commands.has_role("PUT ROLE HERE")
async def subscription(ctx):
    id = ctx.message.author.id
    c.execute("SELECT * FROM redeemed_keys WHERE discord_id=?", (id,))
    data = c.fetchall()
    print(data)
    subscription_length = data[0][2]
    embed=discord.Embed(title=f"You have {subscription_length} days remaining on your license",color=color)
    embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.set_footer(text='Lenth of Subscription') 
    await ctx.send(embed=embed)
#Tasks Loops - Loops account key expire times - 24 hours
@tasks.loop(hours=24) #In 24 hours keys
async def my_loop():
    await asyncio.sleep(7)
    c.execute('UPDATE redeemed_keys SET duration = duration-1 WHERE duration>0')
    conn.commit()
    print("minused")
#Task loop - loops accounts - in 60 mins
@tasks.loop(minutes=30)
async def check_loop(ctx):
    await bot.wait_until_ready()
    await asyncio.sleep(8)
    duration_end = 0
    c.execute("SELECT * FROM redeemed_keys WHERE duration=?", (duration_end,))
    if not c.fetchone():
        print("No user's subscriptions have ended")
    else:
        try:
            c.execute("SELECT * FROM redeemed_keys WHERE duration=?", (duration_end,))
            data = c.fetchall()
            print(data)
            expired_id = []
            length = (len(data))
            print(f"{length} users have their license expired")
            for i in range(length):
                add = data[i][0]
                expired_id.append(add)
            expired_user = len(expired_id)
            for i in range(expired_user):
                try:
                    user = expired_id[i]
                    user_id = (int(user))
                    print(user)
                    guild = bot.get_guild(server id)
                    member = guild.get_member(user_id)
                    role = guild.get_role(premium role id here)
                    await member.remove_roles(role)
                    embed=discord.Embed(title="Thank you for using us!",description=f"Hey {member.name},\n\nThank you for purchasing our service. Your license has now expired and your role has been removed. If you wish to extend your license, please go to our store and purchase a new one!",color=color)
                    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                    embed.set_footer(text='Thank you!') 
                    await member.send(embed=embed)
                    print(f"dmed {member.name}")
                    c.execute("DELETE FROM redeemed_keys WHERE discord_id=?", (user_id,))
                    conn.commit()
                except:
                    print("Error user is no longer in server")
        except:
            traceback.print_exc()

@bot.command()
async def removesubscription(ctx, member:discord.Member):
    if ctx.message.author.id in admin_list:
        discord_id = member.id
        c.execute("SELECT * FROM redeemed_keys WHERE discord_id=?", (discord_id,))
        if not c.fetchone():
            embed=discord.Embed(title="Your request has failed",description="User does not have a subscription",color=color)
            embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text='Request Failed')         
            await ctx.send(embed=embed)
        else:
            c.execute("DELETE FROM redeemed_keys WHERE discord_id=?", (discord_id,))
            conn.commit()
            embed=discord.Embed(title="Your request was Successful",description=f"Successfully removed {member.name}'s subscription",color=color)
            embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text='Request Successful') 
            await ctx.send(embed=embed)
            guild = bot.get_guild(server id)
            role = guild.get_role(733506154914775102)
            await member.remove_roles(role)
            embed=discord.Embed(title="Subscription had ended",description="Your subscription has been removed, if you wish to know why please go purchase a new one",color=color)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text='RIP YOUR SUBSCRIPTION') 
            await member.send(embed=embed)
    else:
        embed=discord.Embed(title="Your request has failed",description="You do not have permission to remove a subscription from a user",color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Request Failed')
        await ctx.send(embed=embed)
#command to add extra day to all keys command - only used for special events or holidays
@bot.command()
async def adddayall(ctx):
    if ctx.message.author.id in admin_list:
        c.execute('UPDATE redeemed_keys SET duration = duration+1 WHERE duration>0')
        conn.commit()
        embed=discord.Embed(title="Successful",description="One day has been added to everyone's license",color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Request Success')
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Failed",description="You do not have permission to add a day to everyone's license",color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Request Failed')
        await ctx.send(embed=embed)
bot.run(TOKEN)