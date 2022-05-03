import asyncio

import discord
from discord.ext import commands
from Config import rip_mod_role_id, sea_mod_role_id, time


class MessageSystem(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def sendMsg(self, ctx, channel: discord.TextChannel):
        rip_mod_role = ctx.guild.get_role(rip_mod_role_id)
        sea_mod_role = ctx.guild.get_role(sea_mod_role_id)
        if rip_mod_role not in ctx.author.roles and sea_mod_role not in ctx.author.roles and ctx.author.id != 672768917885681678:
            return

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        answer = ""

        try:
            await ctx.send("What should be the content of the message?")
            msg = await self.client.wait_for('message', timeout=time, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f"The process was canceled, since you didn't answer within {time} seconds. Please answer "
                           "faster next time!")
            return
        else:
            answer = msg.content

        if answer.lower() == "cancel":
            await ctx.send("The process was canceled successfully!")
            return

        await channel.send(answer)

    @commands.command()
    async def editMsg(self, ctx, channel: discord.TextChannel, msg_id: int):
        rip_mod_role = ctx.guild.get_role(rip_mod_role_id)
        sea_mod_role = ctx.guild.get_role(sea_mod_role_id)
        if rip_mod_role not in ctx.author.roles and sea_mod_role not in ctx.author.roles and ctx.author.id != 672768917885681678:
            return
        msg = await channel.fetch_message(msg_id)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        answer = ""

        try:
            await ctx.send("What should be the new content of the message?")
            content_msg = await self.client.wait_for('message', timeout=time, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f"The process was canceled, since you didn't answer within {time} seconds. Please answer "
                           "faster next time!")
            return
        else:
            answer = content_msg.content

        if answer.lower() == "cancel":
            await ctx.send("The process was canceled successfully!")
            return

        await msg.edit(answer)

    @commands.command()
    async def archive(self, ctx, channel: discord.TextChannel):
        rip_mod_role = ctx.guild.get_role(rip_mod_role_id)
        sea_mod_role = ctx.guild.get_role(sea_mod_role_id)
        if rip_mod_role not in ctx.author.roles and sea_mod_role not in ctx.author.roles and ctx.author.id != 672768917885681678:
            return

        questions = ["Please enter the title:", "Please enter the contributor(s):", "Please enter a brief description:",
                     "Please enter the resource you want to be archived:"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:

            try:
                await ctx.send(i)
                msg = await self.client.wait_for('message', timeout=time, check=check)
            except asyncio.TimeoutError:
                await ctx.send(
                    f"The process was canceled, since you didn't answer within {time} seconds. Please answer "
                    "faster next time!")
                return
            else:
                if msg.content.lower() == "cancel":
                    await ctx.send("The process was canceled successfully!")
                    return
                answers.append(msg.content)

        title = answers[0]
        contributors = answers[1]
        description = answers[2]
        resource = answers[3]

        await channel.send(f"**{title}:**\r\n"
                           f"`Contributor(s):` {contributors}\r\n"
                           f"`Brief Description:` {description}\r\n"
                           "\r\n"
                           f"{resource}")


def setup(bot):
    bot.add_cog(MessageSystem(bot))
