import yaml;
import bot.JollyBot as JB;
import cogs.Data as DATA;

def run():
    # import data from config.yml
    with open("config/config.yml", 'r') as yml_config:
        config = yaml.load(yml_config);

    TOKEN = config["token"];
    host = config["mysql"]["host"];
    user = config["mysql"]["user"];
    password = config["mysql"]["password"];
    database = config["mysql"]["database"];

    # start bot

    bot = JB.JollyBot(command_prefix = "!");

    cogs = [
        DATA.Data(bot, host=host, user=user, password=password, db=database)
    ];

    bot.start_bot(cogs, TOKEN);

run();