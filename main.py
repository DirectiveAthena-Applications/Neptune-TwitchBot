# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import asyncio
import sys
import tracemalloc

# Athena Packages
from AthenaLib.parsers.dot_env import AthenaDotEnv

from AthenaTwitchLib.irc.irc_connection import IrcConnection
from AthenaTwitchLib.irc.bot import Bot
from AthenaTwitchLib.logger import IrcLogger,ApiLogger
from AthenaTwitchLib.irc.logic.commands_sqlite import CommandLogicSqlite

# Local Imports
from neptune_twitchbot.objects.neptune_commands import NeptuneCommands
from neptune_twitchbot.objects.neptune_tasks import NeptuneTasks

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
async def main():
    # Because of Asyncio errors
    tracemalloc.start()

    # Load up secrets to environment
    AthenaDotEnv(filepath="secrets/secrets.env", auto_run=True)

    # Define the logger as soon as possible,
    #   As it is called by a lot of different systems
    #   Will create tables if need be
    with IrcLogger, ApiLogger:

        # Run constructor,
        #   Which starts the connections
        #   create the task in a loop that runs forever
        await IrcConnection(

            # Assemble the bare BOT
            bot_obj=Bot(
                name=os.getenv("TWITCH_BOT_NAME"),
                oath_token=os.getenv("TWITCH_BOT_OATH"),
                join_channel=["directiveathena"],
                capability_tags=True,
                capability_commands=True,
                capability_membership=True,
                # command_logic=NeptuneCommands(),
                command_logic=CommandLogicSqlite(path="data/logic.sqlite"),
                # task_logic=NeptuneTasks()
            ),

            # Define restart attempts
            #   -1 is infinite restarts
            restart_attempts=-1

        ).construct()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        raise
        # sys.exit(e)