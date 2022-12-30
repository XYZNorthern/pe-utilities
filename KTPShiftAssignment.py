import hikari
import crescent
import flare
import time
import datetime

@flare.button(label="Click here.", style=hikari.ButtonStyle.PRIMARY)
async def btn(ctx: flare.MessageContext) -> None:
    await ctx.respond(content=ctx.user.id)

plugin = crescent.Plugin()

@plugin.include
@crescent.command(name="ktpsession", description="Announce a KTP session.")
async def ktpsession(ctx: crescent.Context):
    embed = hikari.Embed(title="[" + time.strftime('%d/%m/%y') + "]" + " KTP Session", description="**Participants required:** \n ``x2`` Driver Supervisors :KTP_DSV: \n ``x2`` Platform Supervisros :KTP_PSV: \n ``x1`` Network Supervisors :KTP_NSV: \n ``x1`` Manager :KTP_HOP: :KTP_HCM: :KTP_HNO: :KTP_HPO: :KTP_HDO: \n \n Please click the button to show interest.", color="#1a2c23", timestamp=datetime.datetime.now().astimezone())
    row = await flare.Row(btn())
    await ctx.respond(embed=embed, component=row)
