#!/usr/bin/env python3

###############################################################################
# TranslAAAAAAAAAAAAAAAAAtor: sauce metadata finder from nhentai.net for Discord
# Copyright (C) 2019 Lucien "Phundrak" Cartier-Tilet
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""TranslAAAAAAAAAAAAAAAAAtorBot.

Discord bot for nhentai sauce.

Usage:
  saucebot <token>

Options:
  <token>    Bot's Discord API token
  -h --help  Show this screen"""

import asyncio
import re
import os

import discord
from discord.ext import commands

BOT_PREFIX = 'aa!'
BOT_LINK = "https://labs.phundrak.com/phundrak/TranslAAAAAAAAAAAAAAAAAtor",


class TranslAAAAAAAAAAAAAAAAAtorBot:
    def __init__(self):
        """Initialize the bot using the Discord token.

        :param bot_token: Full secret bot token
        """
        self.token = os.getenv('BOT_TOKEN')
        self.bot = commands.Bot(command_prefix=BOT_PREFIX, help_command=None)
        self.setup()

    def setup(self):
        @self.bot.event
        @asyncio.coroutine
        async def on_ready():
            print("Bot online!")
            print("Name: {}".format(self.bot.user.name))
            print("ID: {}".format(self.bot.user.id))
            await self.bot.change_presence(activity=discord.Game(
                name="aa!help"))

        @self.bot.event
        @asyncio.coroutine
        async def on_message(message):
            # ignore self messages
            if message.author.bot:
                return
            if message.content is None:
                print("Empty message received.")
                return
            if message.content.startswith(BOT_PREFIX):
                if message.content.startswith(BOT_PREFIX + "a"):
                    text = message.content[5:]
                    print(text)
                    await message.channel.send(re.sub(r"[^\s]", "A", text))
                else:
                    await self.bot.process_commands(message)
            # else:
            #     await message.channel.trigger_typing()
            #     # await message.channel.send(embed=embed)

        @self.bot.command()
        @asyncio.coroutine
        async def help(ctx):
            embed = discord.Embed(
                title="TranslAAAAAAAAAAAAAAAAAtor help",
                description="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                color=0xeee657)
            embed.add_field(name="`aa!a bbbbb`",
                            value="AAAAA",
                            inline=False)
            embed.add_field(name="AAAAAA AAAA", value=BOT_LINK, inline=False)
            await ctx.send(embed=embed)

        # @self.bot.command()
        # @asyncio.coroutine
        # async def a(ctx, text):
        #     await ctx.channel.trigger_typing()
        #     print(text)
        #     await ctx.send(re.sub(r"[^\s]", "A", text))
        #     # embed = self.translate(text)
        #     # await ctx.send(embed=embed)

    def run(self):
        self.bot.run(self.token)

    def translate(text):
        return


bot = TranslAAAAAAAAAAAAAAAAAtorBot()
bot.run()
