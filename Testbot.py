import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import random
import aiohttp

ALLOWED_ROLES = [1408434403247390821, 222222222222222222] # Rollen die erlaubt sind die cmd zu benutzen FÜR ALLES
ALLOWED_USERS = [1, ] # Leute die erlaubt sind die cmd zu benutzen FÜR ALLES
ALLOWED_USERS_split_or_steal = [1408434403247390821]  # nur diese User dürfen Command 1
ALLOWED_ROLES_split_or_steal = [1408434403247390821, 1408430847585161317] # Beu _CMD1 muss der name hin

ALLOWED_ROLES_Owner = [1408434403247390821,] # Beu _CMD1 muss der name hin

ALLOWED_ROLES_Mod = [1, 1] # Beu _CMD1 muss der name hin

ALLOWED_ROLES_Helper = [1408430847585161317, 1] # Beu _CMD1 muss der name hin






load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
print("TOKEN:", TOKEN)  # Testausgabe

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)






# 1408434403247390821 = Owner
# 1408430847585161317 = Mod




def check_permissions(allowed_roles, allowed_users):
    async def predicate(interaction: discord.Interaction):
        # Hole alle Rollen-IDs des Users
        user_roles = [role.id for role in interaction.user.roles]
        
        # Check: User ist erlaubt, oder hat erlaubte Rolle
        if interaction.user.id in allowed_users or any(r in allowed_roles for r in user_roles):
            return True

        # Wenn nicht berechtigt → CheckFailure werfen
        raise app_commands.CheckFailure("❌ You are not allowed to use this command!")
    
    return app_commands.check(predicate)












GUILD_ID = discord.Object(id=1384944992027545713) # Nur wenn man den Command auf 1 Server benutzt und nicht Global

class Client(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        


        async def setup_hook(self):
          self.tree.command(sayHello, guild=GUILD_ID)



    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.tree.sync(guild=GUILD_ID)

    async def on_message(self, message): # terminal
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


# Profilbild

AVATAR_URL = "https://th.bing.com/th/id/OIP.eQOwLqNOrTy6rPCiC9QvJAHaFj?w=219&h=180&c=7&r=0&o=7&pid=1.7&rm=3"  # hier die URL deines Bildes

@client.event
async def on_ready():
    

    async with aiohttp.ClientSession() as session:
        async with session.get(AVATAR_URL) as resp:
            if resp.status != 200:
                print("Fehler beim Laden des Avatars!")
                return
            avatar_bytes = await resp.read()

    await client.user.edit(avatar=avatar_bytes)
    print("Avatar erfolgreich gesetzt!")




@client.tree.command(name="hello", description="Say Hello", guild=GUILD_ID)
@check_permissions(ALLOWED_ROLES, ALLOWED_USERS)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hi there!")


# Ban cmd

@client.tree.command(name="ban", description="Bannt einen Nutzer", guild=GUILD_ID)
@app_commands.describe(user="Wer soll gebannt werden?", reason="Warum?")
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str = "Kein Grund angegeben"):
    try:
        await user.ban(reason=reason)
        await interaction.response.send_message(f"{user.mention} wurde gebannt. Grund: {reason}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Fehler: {e}", ephemeral=True)



# Kick cmd

@client.tree.command(name="kick", description="Kick einen User.", guild=GUILD_ID)
@app_commands.describe(user="Wer soll gekickt werden", reason="Warum")
@check_permissions(ALLOWED_ROLES, ALLOWED_USERS)
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str):
    try:
        await user.kick(reason=reason)
        await interaction.response.send_message(f"User wurde erfolgreich gekickt. Grund: {reason}")
    except Exception as e:
        await interaction.response.send_message(f'Fehler: {e}') 



@client.tree.command(name="rules", description="Prints the rules", guild=GUILD_ID)
async def rules(interaction: discord.Interaction):
    await interaction.response.send_message(f"📜Regeln: \n"
                                             "Respektvoll sein \n"
                                             "Nicht Beleidigen \n")
    



@client.tree.command(name="embed", description="sends embed", guild=GUILD_ID)
async def snedsembed(interaction: discord.Interaction):
    embed=discord.Embed(title="I am title", url="https://th.bing.com/th/id/OIP.eBeEAU77g_2zdhPpyaiPnQHaIp?w=143&h=180&c=7&r=0&o=7&pid=1.7&rm=3", description="Description", color=discord.Color.red())
    embed.set_thumbnail(url="https://th.bing.com/th/id/OIP.eBeEAU77g_2zdhPpyaiPnQHaIp?w=143&h=180&c=7&r=0&o=7&pid=1.7&rm=3")
    embed.add_field(name="Zeile 1", value="Beschreibung von feld 1", inline=False) # Die Value (von der zeile) ist einfach nur ein Text darunter / Beschreibung
    embed.add_field(name="Feld 2", value="ka", inline=True) # Wenn "inline=true" sind die felder nebeneinander wenn "inline=false" sind die Felder untereinander
    embed.add_field(name="Feld 2", value="ka", inline=True) # Wenn 2 Felder nebeneinander sein sollen müssen beide true danach wenns wieder runter gehen soll wieder auf False machen
    embed.set_footer(text="Notiz") # Kleiner Text / Notiz
    embed.set_author(name="Gemacht von Tim😮‍💨", url="https://th.bing.com/th/id/OIP.eQOwLqNOrTy6rPCiC9QvJAHaFj?w=219&h=180&c=7&r=0&o=7&pid=1.7&rm=3", icon_url="https://th.bing.com/th/id/OIP.eQOwLqNOrTy6rPCiC9QvJAHaFj?w=219&h=180&c=7&r=0&o=7&pid=1.7&rm=3")
    # "Icon_url" ist ein kleines Icon neben dem author Text
    await interaction.response.send_message(embed=embed)








# Split or Steal Command!






class Versuch(discord.ui.View):
    def __init__(self, allowed_users: list[int], interaction: discord.Interaction):
        super().__init__(timeout=None)
        self.allowed_users = allowed_users
        self.clicked_users: set[int] = set()
        self.choices: dict[int, str] = {}
        self.interaction = interaction

    async def handle_click(self, interaction: discord.Interaction, choice: str):
        user_id = interaction.user.id

        if user_id not in self.allowed_users:
            await interaction.response.send_message(
                "Du bist nicht berechtigt, hier zu klicken.", ephemeral=True
            )
            return False

        if user_id in self.clicked_users:
            await interaction.response.send_message(
                "Du hast bereits gewählt!", ephemeral=True
            )
            return False

        # Wahl speichern
        self.clicked_users.add(user_id)
        self.choices[user_id] = choice
        await interaction.response.send_message(
            f"Du hast **{choice.capitalize()}** gewählt!", ephemeral=True
        )
        return True

    @discord.ui.button(label="Split", style=discord.ButtonStyle.green, emoji="🤝")
    async def split(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_click(interaction, "split")

    @discord.ui.button(label="Steal", style=discord.ButtonStyle.red, emoji="💀")
    async def steal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_click(interaction, "steal")

    # ⏰ Timer läuft parallel und wertet nach 10s aus
    async def timer(self):
        print("Timer wurde gestartet")
        await asyncio.sleep(10)

        # Auswertung
        if len(self.clicked_users) == 0:
            await self.interaction.followup.send("No one chose, no one wins!")
            return

        if len(self.clicked_users) == 1:
            user_id = next(iter(self.clicked_users))
            user = await self.interaction.client.fetch_user(user_id)
            await self.interaction.followup.send(
                f"{user.mention} Was the only one who chose and wins! 🎉"
            )
            return

        # len == 2 → echte Split-or-Steal-Logik
        user_ids = list(self.clicked_users)
        u1, u2 = user_ids[0], user_ids[1]
        c1, c2 = self.choices[u1], self.choices[u2]
        user1 = await self.interaction.client.fetch_user(u1)
        user2 = await self.interaction.client.fetch_user(u2)

        if c1 == "split" and c2 == "split":
            await self.interaction.followup.send("Both did **Split** and both are won.")
        elif c1 == "steal" and c2 == "steal":
            await self.interaction.followup.send("Both chosed **Steal** and No one wins.")
        elif c1 == "steal" and c2 == "split":
            await self.interaction.followup.send(f"{user1.mention} **Stole** and gets Everything 🎉")
        elif c2 == "steal" and c1 == "split":
            await self.interaction.followup.send(f"{user2.mention} **Stole** and gets Everything 🎉")


@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.CheckFailure):
        await interaction.response.send_message(str(error), ephemeral=True)







# Slash-Command: Embed + View senden und Timer starten
@client.tree.command(name="split_or_steal", description="split or steal", guild=GUILD_ID)
@check_permissions(ALLOWED_ROLES_Owner, ALLOWED_USERS)
@app_commands.describe(user1="Winner1", user2="Winner2")
async def snedsembed(interaction: discord.Interaction, user1: discord.User, user2: discord.User):
    embed = discord.Embed(
        title="Split or Steal",
        description=f"{user1.mention}, {user2.mention}, Please Choose **Split** or **Steal**.",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://th.bing.com/th/id/OIP.eQOwLqNOrTy6rPCiC9QvJAHaFj?w=219&h=180&c=7&r=0&o=7&pid=1.7&rm=3")
    embed.add_field(name="Split", value="If you decide to Split the money both get half of it.", inline=False)
    embed.add_field(name="Steal", value="If you decide to Steal the money you will get all, but if both steal NO ONE gets it.", inline=False)
    embed.set_author(name="Made by Tim😮‍💨", icon_url="https://th.bing.com/th/id/OIP.eQOwLqNOrTy6rPCiC9QvJAHaFj?w=219&h=180&c=7&r=0&o=7&pid=1.7&rm=3")
    embed.set_footer(text="Make sure to Invite your friends!")
    view = Versuch(allowed_users=[user1.id, user2.id], interaction=interaction)
    await interaction.response.send_message(embed=embed, view=view)

    asyncio.create_task(view.timer())






    
    








   











# Name des Commands muss Klein sein 1384944992027545713


















client.run(TOKEN)

