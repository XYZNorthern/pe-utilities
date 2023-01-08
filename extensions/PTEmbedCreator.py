import hikari
import crescent

plugin = crescent.Plugin()

@plugin.include
@crescent.command(name="ptembedbuilder", description="Creates an embed.")
class EmbedBuilder:
    embed_title = crescent.option(str, "The title of the embed")
    embed_description = crescent.option(str, "The description of the embed")
    embed_colour = crescent.option(str, "The colour of the embed.")
    channel = crescent.option(str, "The channel where to send it to.")
    text = crescent.option(str, "The text you want to put in the embed.", default=None)
    embed_set_footer_text = crescent.option(str, "The footer text of the embed", default=None)
    embed_set_footer_icon = crescent.option(hikari.Attachment, "The icon of the embed footer", default=None)
    embed_set_image = crescent.option(hikari.Attachment, "The image of the embed", default=None)
    embed_set_thumbnail = crescent.option(hikari.Attachment, "The thumbnail for the embed", default=None)

    async def callback(self, ctx: crescent.Context) -> None:
        embed = hikari.Embed(title=self.embed_title, description=self.embed_description, color=self.embed_colour)
        embed.set_footer(text=self.embed_set_footer_text, icon=self.embed_set_footer_icon)
        embed.set_image(self.embed_set_image)
        embed.set_thumbnail(self.embed_set_thumbnail)
        await ctx.respond("> :white_check_mark: | I have sent the embed.", flags=hikari.MessageFlag.EPHEMERAL)
        await plugin.app.rest.create_message(channel=self.channel, content=self.text + embed)

class myError(Exception):
    pass

@plugin.include
@crescent.catch_command(myError)
async def on_err(exc: myError, ctx: crescent.Context):
    await ctx.respond("An error occurred while running this command. Check if you have made a typo.", flags=hikari.MessageFlag.EPHEMERAL)
    raise myError()