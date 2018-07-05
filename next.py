from disco.bot import Bot, Plugin
from disco.types.message import MessageEmbed


class NextPlugin(Plugin):
    def load(self, ctx):
        self.streamers = {'Warths': Schedule('/home/bot/PhantomBot_Warths/addons/next.txt', '/home/bot/PhantomBot_Warths/addons/hour.txt'),
                          'ValentinStream': Schedule('/home/bot/PhantomBot_Valentin/addons/next.txt', '/home/bot/PhantomBot_Valentin/addons/hour.txt'),
                          'Air_ONE29': Schedule('/home/bot/PhantomBot_AirOne/addons/next.txt', '', phantom_bot=True)}

    @Plugin.command('next', '[pseudo:str...]')
    def on_next_command(self, event, pseudo=None):
        chan = str(event.channel)
        if chan != "#bot":
            return
        if pseudo:
            for streamer in self.streamers:
                if pseudo.lower() == streamer.lower():
                    embed = MessageEmbed()
                    embed.add_field(name=streamer, value=(self.streamers[streamer].get_next().capitalize()), inline=True)
                    embed.description = 'Prochain stream  de %s' % streamer
                    embed.color = '10038562'
                    event.msg.reply(embed=embed)
        else:
            embed = MessageEmbed()

            for streamer in self.streamers:
                embed.add_field(name=streamer, value=(self.streamers[streamer].get_next().capitalize()), inline=True)
            embed.description = 'Les infos sur les prochains steams'
            embed.color = '10038562'
            event.msg.reply(embed=embed)

class Schedule:
    def __init__(self, day_path, hour_path, phantom_bot=False):
        self.phantom_bot = phantom_bot
        self.day_path = day_path
        self.hour_path = hour_path

    def get_next(self):
        if self.phantom_bot:
            with open(self.day_path, 'r') as response:
                response = response.readline().split(' ')
                try:
                    return '%s Ã  %s' % (response[0], response[2])
                except IndexError:
                    return 'ERROR'
        with open(self.day_path, 'r') as day:
            day = day.readline().replace('\n', '')
        with open(self.hour_path, 'r') as hour:
            hour = hour.readline().replace('\n', '')
        return '%s Ã  %s' % (day, hour)
