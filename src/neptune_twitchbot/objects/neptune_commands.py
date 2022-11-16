# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Athena Packages
from AthenaTwitchBot.irc.logic import CommandLogic, CommandData
from AthenaTwitchBot.irc.message_context import MessageCommandContext
from AthenaTwitchBot.irc.data.enums import BotEvent

# Local Imports
from neptune_twitchbot.data.git import GIT_TEXT

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class NeptuneCommands(CommandLogic):

    @CommandLogic.command(CommandData("discord"))
    async def cmd_discord(self, context: MessageCommandContext):
        await context.reply(
            "Want to keep up to date with when Andreas goes live, or are you interested in more background related stuff? Then join our discord! https://discord.gg/RJMHvtvBtp"
        )

    @CommandLogic.command_broadcaster(CommandData("broad_test"))
    async def cmd_broad_test(self, context: MessageCommandContext):
        await context.reply(
            "I should only reply to Andreas"
        )

    @CommandLogic.command(CommandData(["git", "github"]))
    async def cmd_git(self, context:MessageCommandContext):
        await context.reply(
            GIT_TEXT.get(
                context.args[0] if context.args else "",
                GIT_TEXT[""]
            )
        )

    @CommandLogic.command_moderator(CommandData(["restart"]))
    async def cmd_restart(self, context:MessageCommandContext):
        context.bot_event_future.set_result(BotEvent.RESTART)

    @CommandLogic.command_broadcaster(CommandData(["exit"]))
    async def cmd_exit(self, context:MessageCommandContext):
        context.bot_event_future.set_result(BotEvent.EXIT)