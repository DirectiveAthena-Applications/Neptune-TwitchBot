# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Athena Packages
from AthenaColor import ForeNest as Fore
from AthenaTwitchBot.logic import chat_command, chat_message, sub_only_command
from AthenaTwitchBot.logic.logic_bot import LogicBot
from AthenaTwitchBot.message_context import MessageContext

# Local Imports
from neptune_twitchbot.data.git import GIT_TEXT

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class Neptune_TwitchBot(LogicBot):
    default_channel = "directiveathena"

    async def get_git_message(self, text:str) -> str:
        return GIT_TEXT.get(
            text.lower().split(" ")[1],
            GIT_TEXT[""]
        )

    @chat_command(cmd_name="discord")
    async def cmd_discord(self, message_context:MessageContext):
        await message_context.reply(
            "Want to keep up to date with when Andreas goes live, or are you interested in more background related stuff? Then join our discord! https://discord.gg/RJMHvtvBtp"
        )

    @chat_command(cmd_name="git")
    async def cmd_git(self, message_context:MessageContext):
        await message_context.reply(
            await self.get_git_message(message_context.text)
        )

    @chat_command(cmd_name="github")
    async def cmd_github(self, message_context: MessageContext):
        await message_context.reply(
            await self.get_git_message(message_context.text)
        )