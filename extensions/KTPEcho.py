import hikari
import crescent
from typing import Annotated as Atd

plugin = crescent.Plugin()

@plugin.include
@crescent.command(name="ktpecho", description="Says the message you put in a channel.")
async def ktpecho(ctx: crescent.Context, channel: Atd[str, int, "The channel id you want to send the message in."] ,text: Atd[str, int, "The text to send."]):
    await plugin.app.rest.create_message(channel=channel, content=text)
    await ctx.respond(":white_check_mark: | Your message has been sent", flags=hikari.MessageFlag.EPHEMERAL)