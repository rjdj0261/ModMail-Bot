import datetime
import logging
import sys
import traceback

import aiohttp
import aioredis
import asyncpg

from discord.ext import commands

import config

import os

from utils import prometheus, tools

log = logging.getLogger(__name__)


class ModMail(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_time = datetime.datetime.utcnow()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.cluster = kwargs.get("cluster_id")
        self.cluster_count = kwargs.get("cluster_count")
        self.version = kwargs.get("version")
        self.uptime = datetime.datetime.utcnow() - self.start_time
        self.config = config
        self.tools = tools
        self.primary_colour = self.config.primary_colour
        self.user_colour = self.config.user_colour
        self.mod_colour = self.config.mod_colour
        self.error_colour = self.config.error_colour
        self.comm = self.cogs["Communication"]
        self.all_prefix = {}
        self.banned_guilds = []
        self.banned_users = []

    async def get_data(self, guild):
        async with self.pool.acquire() as conn:
            res = await conn.fetchrow("SELECT * FROM data WHERE guild=$1", guild)
            if not res:
                res = await conn.fetchrow(
                    "INSERT INTO data VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11) RETURNING *",
                    guild,
                    None,
                    None,
                    [],
                    None,
                    None,
                    None,
                    False,
                    [],
                    [],
                    False,
                )
        return res

    async def connect_redis(self):
        self.redis = await aioredis.create_pool(self.config.ipc_channel, minsize=5, maxsize=10, loop=self.loop, db=0)
        info = (await self.redis.execute("INFO")).decode()
        for line in info.split("\n"):
            if line.startswith("redis_version"):
                self.redis_version = line.split(":")[1]
                break

    async def connect_postgres(self):
        self.pool = await asyncpg.create_pool(**self.config.database, max_size=50, command_timeout=60)

    async def connect_prometheus(self):
        self.prom = prometheus.Prometheus(self)
        if self.config.testing is False:
            await self.prom.start()

    async def start_bot(self):
        await self.connect_redis()
        await self.connect_postgres()
        await self.connect_prometheus()
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
        await self.start(self.config.token)
