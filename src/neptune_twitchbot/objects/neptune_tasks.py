# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import datetime

# Athena Packages
from AthenaTwitchLib.irc.logic import TaskLogic, TaskData
from AthenaTwitchLib.string_formatting import twitch_irc_output_format


# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class NeptuneTasks(TaskLogic):

    @TaskLogic.task(TaskData(interval=datetime.timedelta(seconds=5)))
    async def task_0(self, transport:asyncio.Transport):
        transport.write(twitch_irc_output_format(f"PRIVMSG #directiveathena :seconds 5"))

    @TaskLogic.task(TaskData(at=datetime.timedelta(minutes=5)))
    async def task_1(self, transport:asyncio.Transport):
        transport.write(twitch_irc_output_format(f"PRIVMSG #directiveathena :every five minutes, on the 5 minutev mark"))