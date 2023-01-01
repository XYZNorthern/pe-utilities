import hikari
import crescent
import flare

bot = crescent.Bot('YOUR TOKEN')
flare.install(bot)

bot.plugins.load("extensions.KTPShiftAssignment")
bot.plugins.load("extensions.KTPMeetings")
bot.plugins.load("extensions.KTPEcho")

bot.run()
