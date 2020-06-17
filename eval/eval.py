import js2py
import discord
from redbot.core import commands, checks, Config


class eval(commands.Cog):
    """eval boiiiii"""
	
    @commands.command()
    @checks.is_owner()
    async def eval(self, ctx, *, eArg):
        eval = js2py.eval_js(eArg)
        await ctx.send(eval)

