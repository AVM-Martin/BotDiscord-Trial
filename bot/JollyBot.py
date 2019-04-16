import discord;
import discord.ext.commands as BOT;

class JollyBot(BOT.Bot):
    def start_bot(self, cogs, TOKEN):
        for cog in cogs:
            self.add_cog(cog);
        self.run(TOKEN);

    async def on_ready(self):
        # change presence
        await client.change_presence(activity=discord.Game(name="Playing with !help"));
        #
        print("Logged in as {0.name} with {0.id} version {1}".format(client.user));
        print("------------------------------");
