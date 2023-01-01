import hikari
import crescent
from songbird import ytdl
from songbird.hikari import Voicebox
import flare

@flare.button(label="click", style=hikari.ButtonStyle.SECONDARY)
async def btntest(ctx: flare.MessageContext):

    await ctx.respond("hi")

bot = crescent.Bot('MTA1ODA2NTIzOTQ0ODQ4NjAxOA.GwGY69.FGbvCSpre61amHjdRD497_M_gWYtmGcOsM-hQY')
flare.install(bot)

@bot.include
@crescent.command
async def btntest1(ctx):
    row = await flare.Row(btntest())

    await ctx.respond("a", component=row)



bot.plugins.load("extensions.KTPShiftAssignment")
bot.plugins.load("extensions.KTPMeetings")
bot.plugins.load("extensions.KTPEcho")

bot.run()