import hikari
import crescent
import flare
import datetime
import time
from typing import Annotated as Atd

@flare.button(label="Click to submit attendance", style=hikari.ButtonStyle.SUCCESS)
async def meetingsbtn(ctx: flare.MessageContext):
    date_time = datetime.datetime.now()
    await plugin.app.rest.create_message(channel=CHANNEL_ID, content=f"{ctx.user.id} at <t:{int(time.mktime(date_time.timetuple()))}> will be attending.")
    await ctx.respond(content=":white_check_mark: | Your attendance has been submitted.", flags=hikari.MessageFlag.EPHEMERAL)

plugin = crescent.Plugin()

@plugin.include
@crescent.command(name="ktpmeeting", description="Announce meetings.")
async def ktpmeeting(ctx: crescent.Context, date: Atd[str, int, "The date when the meeting will happen."], time: Atd[str, int, "The time the meeting will happen."]):
    embed = hikari.Embed(title=f'[{date}] KTP Meeting', description="A meeting will be occurring soon. Please click the button to confirm your attendance.", colour="#1a2c23")
    row = await flare.Row(meetingsbtn())
    await ctx.respond(embed=embed, component=row)
