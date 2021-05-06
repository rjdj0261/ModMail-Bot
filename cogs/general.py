import logging
import platform
import time

import discord
import psutil

from discord.ext import commands

from utils.paginator import Paginator

log = logging.getLogger(__name__)


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        psutil.cpu_percent()

    @commands.bot_has_permissions(add_reactions=True)
    @commands.command(
        description="Shows the help menu or information for a specific command when specified.",
        usage="help [command]",
        aliases=["h", "commands"],
    )
    async def help(self, ctx, *, command: str = None):
        if command:
            command = self.bot.get_command(command.lower())
            if not command:
                await ctx.send(
                    embed=discord.Embed(
                        description=f"That command does not exist. Use `{ctx.prefix}help` to see all the commands.",
                        colour=self.bot.primary_colour,
                    )
                )
                return
            embed = discord.Embed(title=command.name, description=command.description, colour=self.bot.primary_colour)
            usage = "\n".join([ctx.prefix + x.strip() for x in command.usage.split("\n")])
            embed.add_field(name="Usage", value=f"```{usage}```", inline=False)
            if len(command.aliases) > 1:
                embed.add_field(name="Aliases", value=f"`{'`, `'.join(command.aliases)}`")
            elif len(command.aliases) > 0:
                embed.add_field(name="Alias", value=f"`{command.aliases[0]}`")
            await ctx.send(embed=embed)
            return
        all_pages = []
        page = discord.Embed(
            title=f"{self.bot.user.name} Help Menu",
            description="Thank you for using ModMail! Please direct message me if you wish to contact staff. You can "
            "also invite me to your server with the link below, or join our support server if you need further help."
            f"\n\nDon't forget to check out our partners with the `{ctx.prefix}partners` command!",
            colour=self.bot.primary_colour,
        )
        page.set_thumbnail(url=self.bot.user.avatar_url)
        page.set_footer(text="Use the reactions to flip pages.")
        page.add_field(name="Invite", value="https://dsc.gg/modmail-bot", inline=False)
        page.add_field(name="Support Server", value="https://dsc.gg/modmail-support", inline=False)
        all_pages.append(page)
        page = discord.Embed(title=f"{self.bot.user.name} Help Menu", colour=self.bot.primary_colour)
        page.set_thumbnail(url=self.bot.user.avatar_url)
        page.set_footer(text="Use the reactions to flip pages.")
        page.add_field(
            name="About ModMail",
            value="ModMail is a feature-rich Discord bot designed to enable your server members to contact staff "
            "easily. A new channel is created whenever a user messages the bot, and the channel will serve as a shared "
            "inbox for seamless communication between staff and the user.",
            inline=False,
        )
        page.add_field(
            name="Getting Started",
            value="Follow these steps to get the bot all ready to serve your server!\n1. Invite the bot with "
            f"[this link](https://dsc.gg/modmail-bot)\n2. Run `{ctx.prefix}setup`, there will be an interactive guide."
            f"\n3. All done! For a full list of commands, see `{ctx.prefix}help`.",
            inline=False,
        )
        all_pages.append(page)
        for _, cog_name in enumerate(self.bot.cogs):
            if cog_name in ["Owner", "Admin"]:
                continue
            cog = self.bot.get_cog(cog_name)
            cog_commands = cog.get_commands()
            if len(cog_commands) == 0:
                continue
            page = discord.Embed(
                title=cog_name,
                description=f"My prefix is `{ctx.prefix}`. Use `{ctx.prefix}"
                "help <command>` for more information on a command.",
                colour=self.bot.primary_colour,
            )
            page.set_author(name=f"{self.bot.user.name} Help Menu", icon_url=self.bot.user.avatar_url)
            page.set_thumbnail(url=self.bot.user.avatar_url)
            page.set_footer(text="Use the reactions to flip pages.")
            for cmd in cog_commands:
                if cmd.hidden is False:
                    page.add_field(name=cmd.name, value=cmd.description, inline=False)
            all_pages.append(page)
        paginator = Paginator(length=1, entries=all_pages, use_defaults=True, embed=True, timeout=120)
        await paginator.start(ctx)

    @commands.command(description="Pong! Get my latency.", usage="ping")
    async def ping(self, ctx):
        start = time.time()
        msg = await ctx.send(embed=discord.Embed(description="Checking latency...", colour=self.bot.primary_colour))
        await msg.edit(
            embed=discord.Embed(
                title="Pong!",
                description=f"Gateway latency: {round(self.bot.latency * 1000, 2)}ms.\n"
                f"HTTP API latency: {round((time.time() - start) * 1000, 2)}ms.",
                colour=self.bot.primary_colour,
            )
        )

    def get_bot_uptime(self, *, brief=False):
        hours, remainder = divmod(int(self.bot.uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if not brief:
            if days:
                fmt = "{d} days, {h} hours, {m} minutes, and {s} seconds"
            else:
                fmt = "{h} hours, {m} minutes, and {s} seconds"
        else:
            fmt = "{h}h {m}m {s}s"
            if days:
                fmt = "{d}d " + fmt
        return fmt.format(d=days, h=hours, m=minutes, s=seconds)

    @commands.command(
        description="See some super cool statistics about me.",
        usage="stats",
        aliases=["statistics", "info"],
    )
    async def stats(self, ctx):
        guilds = sum(await self.bot.comm.handler("guild_count", self.bot.cluster_count))
        channels = sum(await self.bot.comm.handler("channel_count", self.bot.cluster_count))
        users = sum(await self.bot.comm.handler("user_count", self.bot.cluster_count))

        embed = discord.Embed(title=f"{self.bot.user.name} Statistics", colour=self.bot.primary_colour)
        embed.add_field(name="Owner", value="Spartan#1124")
        embed.add_field(name="Bot Version", value=self.bot.version)
        embed.add_field(name="Uptime", value=self.get_bot_uptime(brief=True))
        embed.add_field(name="Clusters", value=f"{self.bot.cluster}/{self.bot.cluster_count}")
        if ctx.guild:
            embed.add_field(name="Shards", value=f"{ctx.guild.shard_id + 1}/{self.bot.shard_count}")
        else:
            embed.add_field(name="Shards", value=f"{self.bot.shard_count}")
        embed.add_field(name="Servers", value=str(guilds))
        embed.add_field(name="Channels", value=str(channels))
        embed.add_field(name="Users", value=str(users))
        embed.add_field(name="CPU Usage", value=f"{psutil.cpu_percent(interval=None)}%")
        embed.add_field(name="RAM Usage", value=f"{psutil.virtual_memory().percent}%")
        embed.add_field(name="Python Version", value=platform.python_version())
        embed.add_field(name="discord.py Version", value=discord.__version__)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(
            text="Made with ❤ using discord.py",
            icon_url="https://www.python.org/static/opengraph-icon-200x200.png",
        )
        await ctx.send(embed=embed)

    @commands.command(description="Get a link to invite me.", usage="invite")
    async def invite(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Invite Link",
                description="https://dsc.gg/modmail-bot",
                colour=self.bot.primary_colour,
            )
        )

    @commands.command(description="Get a link to my support server.", usage="support", aliases=["server"])
    async def support(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Support Server",
                description="https://dsc.gg/modmail-support",
                colour=self.bot.primary_colour,
            )
        )

    @commands.command(description="Get the link to ModMail's GitHub repository.", usage="source", aliases=["github"])
    async def source(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="GitHub Repository",
                description="https://github.com/ReyBotDev/ModMail-Bot",
                colour=self.bot.primary_colour,
            )
        )


def setup(bot):
    bot.add_cog(General(bot))
