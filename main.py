# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import asyncio
import tracemalloc

# Athena Packages
from AthenaLib.parsers.dot_env import DotEnv

from AthenaTwitchBot.bot_constuctor import bot_constructor
from AthenaTwitchBot.bot_settings import BotSettings

# Local Imports
from neptune_twitchbot.objects.twitch_bot import Neptune_TwitchBot

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    tracemalloc.start()

    # Load up secrets to environment
    DotEnv(filepath="secrets/secrets.env", auto_run=True)

    # Run constructor,
    #   Which starts the connections
    #   create the task in a loop that runs forever
    loop = asyncio.new_event_loop()

    loop.create_task(bot_constructor(settings=BotSettings(
        bot_name=os.getenv("TWITCH_BOT_NAME"),
        bot_oath_token=os.getenv("TWITCH_BOT_OATH"),
        bot_join_channel=["directiveathena"],
        bot_capability_tags=True,
        bot_capability_commands=True,
        bot_capability_membership=True,
        bot_join_message="Hello there everyone! I am alive direct112Ducky"
    ), logic_bot=Neptune_TwitchBot()))

    loop.run_forever()

if __name__ == '__main__':
    main()