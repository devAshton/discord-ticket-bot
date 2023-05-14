import nextcord 
from nextcord.ext import commands, tasks
from nextcord.ui import View, Button

bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

ticket_message = # change_to_your_message_id
ticket_category = # change_to_your_category
ticket_channel = # change_to_your_ticket_channel
reactemoji = "🎟️"

@bot.event
async def on_ready():
    message = await bot.get_channel(ticket_channel).fetch_message(ticket_message)
    if reactemoji not in [reaction.emoji for reaction in message.reactions]:
        await message.add_reaction(reactemoji)

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)

    if payload.message_id == ticket_message and str(payload.emoji) == reactemoji and not user.bot:
        message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        if reactemoji not in [reaction.emoji for reaction in message.reactions]:
            await message.add_reaction
        else:
            await message.remove_reaction(payload.emoji, user)
        category = bot.get_channel(ticket_category)
        channel_name = f"{user.name}-ticket"

        for channel in category.text_channels:
            if channel.name.lower() == channel_name.lower():
                print(f"Ticket Already Open - {user.name}#{user.discriminator} ({user.id})")
                return
        overwrites = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
            user: nextcord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True)
        }

        channel = await category.create_text_channel(name=channel_name, overwrites=overwrites)
        embed = nextcord.Embed(
            title="Ticket Created!",
            description="Please describe what you need support with and we will be with you shortly.",
            color=0x2b2d31
        )
        embed.set_author(name=user.name+"#"+user.discriminator, icon_url=str(user.avatar.url))
        message = await channel.send(user.mention,embed=embed)
        print(f"Ticket created - {user.name}#{user.discriminator} ({user.id})")
 

bot.run("your_bot_token")
