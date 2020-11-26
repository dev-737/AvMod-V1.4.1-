import discord
import os
import random
import aiohttp
from PIL import Image, ImageFont,ImageDraw
from discord.ext import commands

class images(commands.Cog, name='images'):

  def __init__(self, bot):
            self.bot = bot

  @commands.command()
  async def cat(self, ctx):

        """Random picture of a meow"""
        
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow")
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="meow!")

                    await ctx.send(embed=embed)      

  @commands.command()
  async def dog(self, ctx):

      """Random picture of a woof"""

      async with ctx.channel.typing():
          async with aiohttp.ClientSession() as cs:
              async with cs.get("https://random.dog/woof.json") as r:
                  data = await r.json()

                  embed = discord.Embed(title="Woof")
                  embed.set_image(url=data['url'])
                  embed.set_footer(text="Here is a doggo for you!")

                  await ctx.send(embed=embed)

  @commands.command()
  async def drake(self, ctx,*, message):

    """Makes a simple drake meme."""

    text , text2 =message.split(",")
    img = Image.open('drake.png')

          
    Draw = ImageDraw.Draw(img)
    Font = ImageFont.truetype("arial.ttf",32)

    Draw.text((245,10),text,(0,0,0),font = Font)
    Draw.text((244,229),text2,(0,0,0),font = Font)

    img.save("Drakey.png")
    await ctx.send(file = discord.File("Drakey.png"))
    os.remove("Drakey.png")

  @commands.command()
  async def hug(self, ctx, user: discord.Member):

    """Give some huggies to your friends!!"""

    gifs = ["https://cdn.weeb.sh/images/H1ui__XDW.gif", "https://cdn.weeb.sh/images/B11CDkhqM.gif", "https://cdn.weeb.sh/images/rJv2H5adf.gif", "https://cdn.weeb.sh/images/SywetdQvZ.gif", "https://cdn.weeb.sh/images/BJCCd_7Pb.gif"]
    embed = discord.Embed(title="Hug", description=f" {ctx.author.mention} hugs you {user.mention}  ...", color=discord.Color.blue())
    embed.set_image(url=f"{random.choice(gifs)}")
    await ctx.send(embed=embed)

  @commands.command()
  async def stickroll(self, ctx):

    """Oh go on try it out :wink:"""

    await ctx.send("https://tenor.com/view/stick-bug-rick-roll-lol-gif-18118062")


  @commands.command()
  async def changemymind(self, ctx,*, message):

    """Makes a simple drake meme."""

    img = Image.open('cmm.png')

          
    Draw = ImageDraw.Draw(img)
    Font = ImageFont.truetype("arial.ttf",32)


    Draw.text((244,229),message,(0,0,0),font = Font)

    img.save("cmmdun.png")
    await ctx.send(file = discord.File("cmmdun.png"))
    os.remove("Drakey.png")

def setup(bot):
    bot.add_cog(images(bot))