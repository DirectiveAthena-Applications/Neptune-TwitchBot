# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import asyncio
import tracemalloc

# Athena Packages
from AthenaLib.parsers.dot_env import DotEnv as AthenaDotEnv

from AthenaTwitchBot.bot_constuctor import BotConstructor
from AthenaTwitchBot.bot_settings import BotSettings

# Local Imports
from neptune_twitchbot.objects.twitch_bot import Neptune_TwitchBot

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
async def main():
    tracemalloc.start()

    # Load up secrets to environment
    AthenaDotEnv(filepath="secrets/secrets.env", auto_run=True)

    # Assemble the bot settings
    #   Doesn't do anything, but preload some values
    bot_settings = BotSettings(
        bot_name=os.getenv("TWITCH_BOT_NAME"),
        bot_oath_token=os.getenv("TWITCH_BOT_OATH"),
        bot_join_channel=["directiveathena"],
        bot_capability_tags=True,
        bot_capability_commands=True,
        bot_capability_membership=True,
    )

    # Run constructor,
    #   Which starts the connections
    #   create the task in a loop that runs forever
    await BotConstructor(
        settings=bot_settings,
        logic_bot=Neptune_TwitchBot(),
        logging_enabled=True,
        restart_attempts=-1
    ).construct()

if __name__ == '__main__':
    asyncio.run(main())