import js2py
import discord
from redbot.core import commands, checks, Config

class eval(commands.Cog):
    """Evals code in JS."""

    @commands.command(aliases=['ev'])
    @checks.is_owner()
    async def eval(self, ctx, *, eArg):
        eval = js2py.eval_js(eArg)
        type = js2py.eval_js('typeof '+eArg)
        embed = discord.Embed(title="Eval", color=await ctx.embed_color())
        await ctx.embed_color()
        embed.add_field(name="Output", value=eval, inline=False)
        embed.add_field(name="Type", value=type, inline=False)
        embed.set_footer(text="Eval done by {}".format(ctx.message.author))
        await ctx.send(embed=embed)
