# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Athena Packages
from AthenaTwitchLib.irc.logic import CommandLogic, CommandData
from AthenaTwitchLib.irc.message_context import MessageCommandContext
from AthenaTwitchLib.irc.data.enums import BotEvent

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

    @CommandLogic.command_broadcaster(CommandData("broadcaster_test"))
    async def cmd_broad_test(self, context: MessageCommandContext):
        await context.reply(
            "I should only reply to Andreas"
        )

    @CommandLogic.command(CommandData(["git", "github"]))
    async def cmd_git(self, context:MessageCommandContext):
        await context.reply(
            GIT_TEXT.GET(context.args[0] if context.args else "", GIT_TEXT[""])
        )

    @CommandLogic.command_moderator(CommandData(["restart"]))
    async def cmd_restart(self, context:MessageCommandContext):
        context.bot_event_future.set_result(BotEvent.RESTART)

    @CommandLogic.command_broadcaster(CommandData(["exit"]))
    async def cmd_exit(self, context:MessageCommandContext):
        context.bot_event_future.set_result(BotEvent.EXIT)

    @CommandLogic.command_moderator(CommandData(["so"]))
    async def cmd_shout_out(self, context:MessageCommandContext):
        await context.write(
            f"Shout out to: @{context.args[0]} !!! Follow them on https://www.twitch.tv/{context.args[0]}"
        )