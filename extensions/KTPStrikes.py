import hikari
import crescent
from typing import Annotated as Atd
import sqlite3
import datetime

plugin = crescent.Plugin()


connect = sqlite3.connect("KTPStrikes.sqlite")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS ktpdatabase(case_number INTEGER, user_id INTEGER, reason TEXT)""")
connect.commit()

@plugin.include
@crescent.command(name="ktpstrikeadd", description="Add a strike to a staff member.")
async def add(ctx: crescent.Context, the_member: Atd[hikari.User, "The user who you are giving a strike"], reason: Atd[str, int, "The reason as to why you are warning."]):
    connect = sqlite3.connect("KTPStrikes.sqlite")
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO ktpdatabase(case_number, user_id, reason) VALUES (0, {the_member.id}, '{reason}')""")
    cursor.execute("""UPDATE ktpdatabase SET case_number = case_number + 1""")
    connect.commit()

    user = ctx.member
    embed = hikari.Embed(title="", description=f":necktie: You have been issued with a __**strike**__ by {ctx.user} for `{reason}`. This strike will expire in **a year's time** in the event that you do not recieve any further infractions. \n \n :helmet_with_cross: If you feel any of these actions are wrong please DM a member of the directorial team or founders.", color="#1a2c23", timestamp=datetime.datetime.now().astimezone())
    await ctx.respond(f"> :white_check_mark: | {the_member} has received a strike.", flags=hikari.MessageFlag.EPHEMERAL)
    await plugin.app.rest.create_message(channel=1042496469212614686, content=f"> :x: | {ctx.member} has given a strike to {the_member.id} for {reason}")
    await the_member.send(embed=embed)

@plugin.include
@crescent.command(name="ktpstrikesview", description="View strikes from a staff member.")
async def view(ctx: crescent.Context, user: Atd[hikari.User, "The user who you want to view warnings on."]):
    connection = sqlite3.connect("KTPStrikes.sqlite")
    cursor = connect.cursor()

    user_id = user.id
    cursor.execute(f"""SELECT case_number, {user_id}, reason FROM ktpdatabase ORDER BY case_number ASC""")
    connection.commit()
    infractions = cursor.fetchall()
    for row in infractions:
        print(row[0], row[1], row[2])
        embed = hikari.Embed(title=f"{user}'s strikes", description=f"``#{row[0]}`` **STRIKE** | {row[2]}", color="#1a2c23", timestamp=datetime.datetime.now().astimezone())
        await ctx.respond(embed=embed)

@plugin.include
@crescent.command(name="ktpstrikesremove", description="Remove a strike from a staff member.")
async def remove(ctx: crescent.Context, user: Atd[hikari.User, "The user who you want to remove the strike from"], case_number: Atd[int, "The case number of the staff member who you are removing the strike."]):
    con = sqlite3.connect("KTPStrikes.sqlite")
    cursor = con.cursor()

    user_id = user.id
    cursor.execute(f"DELETE FROM ktpdatabase WHERE case_number={case_number}")
    cursor.execute(f"""SELECT case_number FROM ktpdatabase WHERE case_number = ?""", (case_number,))
    con.commit()
    remove = cursor.fetchall()
    for row1 in remove:
        print(row1[0])
        embed = hikari.Embed(title="", description=f":necktie: The strike you have been issued with the case number ``#{row1[0]}`` has been removed from your account. \n \n We apologise for the inconvinience.", color="#1a2c23", timestamp=datetime.datetime.now().astimezone())
        await user.send(embed=embed)
        await ctx.respond(f":white_check_mark: | {user}'s strike has been removed.", flags=hikari.MessageFlag.EPHEMERAL)
        await plugin.app.rest.create_message(channel=1042496469212614686, content=f"> :x: | {ctx.member} has removed a strike from {user_id} with case number {row1[0]}") 