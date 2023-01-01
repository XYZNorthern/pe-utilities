import hikari
import crescent
import flare
import time
import datetime
from typing import Annotated as Atd

@flare.button(label="Click here.", style=hikari.ButtonStyle.PRIMARY)
async def btn(ctx: flare.MessageContext) -> None:
    date_time = datetime.datetime.now()
    await plugin.app.rest.create_message(channel=1058355587609526294, content=f"{ctx.user.id} at <t:{int(time.mktime(date_time.timetuple()))}> will be attending.")
    await ctx.respond(content=":white_check_mark: | Your attendance has been submitted.", flags=hikari.MessageFlag.EPHEMERAL)

plugin = crescent.Plugin()

@plugin.include
@crescent.command(name="ktpsession", description="Announce a KTP session.")
async def ktpsession(ctx: crescent.Context, date: Atd[str, int, "When you want the event to be."], driver_supervisors: Atd[int, 'How many Driver Supervisors you want.'], platform_supervisors: Atd[int, "How many Platform Supervisors you want."], network_supervisors: Atd[int, "How many Network Supervisors you want."], managers: Atd[int, "How many Managers you want."]):
    embed = hikari.Embed(title="[" + date+ "]" + " KTP Session", description=f"**Participants required:** \n  > ``{driver_supervisors}`` Driver Supervisors <:SV:1058365271708008458> \n  > ``{platform_supervisors}`` Platform Supervisors <:SV:1058365271708008458> \n > ``{network_supervisors}`` Network Supervisors <:SV:1058365271708008458> \n > ``{managers}`` Manager <:LMA:1058365328171745350> <:MA:1058365329300017153>\n \n Please click the button to show interest.", color="#1a2c23", timestamp=datetime.datetime.now().astimezone())
    row = await flare.Row(btn())
    await ctx.respond(":white_check_mark: | Session announcement has been sent", flags=hikari.MessageFlag.EPHEMERAL)
    await ctx.respond(embed=embed, component=row)