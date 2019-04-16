import yaml;
import bot.JollyBot as JB;

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

    client = JB.JollyBot(command_prefix = "!");

    cogs = [
        Data(bot, host=host, user=user, password=password, db=database)
    ];

    client.start_bot(cogs, TOKEN);

run();