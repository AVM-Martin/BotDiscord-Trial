import discord.utils;
import discord.ext.commands as BOT;
import cogs.utils.MyDatabase as DB;
import cogs.utils.NIMCheckers as NIMCheckers;

class Data(BOT.Cog):
    def __init__(self, bot):
        self.bot = bot;
        self._db = DB.MyDatabase(host="localhost", user="root", password="", db="avmlearning_db", charset="latin1");

    async def _setGeneralData(self, ctx, data, dataType, func):
        # delete command message
        await ctx.message.delete();
        # push data
        try:
            func(ctx.guild.id, ctx.author.id, data);
            await ctx.send("{0.mention}, your **{1}** is successfully recorded".format(ctx.author, dataType), delete_after=10.0);
        except:
            await ctx.send("An error occured! Please contact the administrator for further assistance");

    async def _getGeneralData(self, ctx, userID, dataType, func):
        user = discord.utils.get(ctx.guild.members, id=int(userID[2:-1]));
        # delete command message
        await ctx.message.delete();
        # bot checking
        if(user.bot == True):
            await ctx.send("{0.mention} is a bot!".format(user), delete_after=10.0);
            return;
        # find result
        try:
            result = func(ctx.guild.id, user.id);
            if(result == None):
                raise;
            await ctx.send("```{0}```".format(result), delete_after=10.0);
        except:
            await ctx.send("{0.mention}, your **{1}** data is incomplete! Please complete your data immediately".format(user, dataType));


    @BOT.command(name="setnim")
    async def _setNIM(self, ctx, *, NIM):
        # delete command message
        await ctx.message.delete();
        # nim checks
        NIM = NIMCheckers.NIM(NIM);
        if(NIM.isValid() == False):
            await ctx.send("Invalid NIM!", delete_after=10.0);
            return;
        # push data
        try:
            self._db.Users.setNIM(ctx.guild.id, ctx.author.id, str(NIM));
            await ctx.send("{0.mention}, your **{1}** is successfully recorded".format(ctx.author, "NIM"), delete_after=10.0);
        except:
            await ctx.send("An error occured! Please contact the administrator for further assistance");

    @BOT.command(name="getnim")
    async def _getNIM(self, ctx, *, userID):
        await self._getGeneralData(ctx, userID, "NIM", self._db.Users.getNIM);

    @BOT.command(name="setphone")
    async def _setPhoneNumber(self, ctx, *, phoneNumber):
        await self._setGeneralData(ctx, phoneNumber, "Phone Number", self._db.Users.setPhoneNumber);
    @BOT.command(name="getphone")
    async def _getPhoneNumber(self, ctx, *, userID):
        await self._getGeneralData(ctx, userID, "Phone Number", self._db.Users.getPhoneNumber);

    @BOT.command(name="setbank")
    async def _setBankAccount(self, ctx, *, bankAccount):
        await self._setGeneralData(ctx, bankAccount, "Bank Account", self._db.Users.setBankAccount);
    @BOT.command(name="getbank")
    async def _getBankAccount(self, ctx, *, userID):
        await self._getGeneralData(ctx, userID, "Bank Account", self._db.Users.getBankAccount);
