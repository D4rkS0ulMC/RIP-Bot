from discord.ext import commands

from .bot import AimBot
from .utils import get_permissions, get_tags, is_valid_thread

__all__ = (
    "AimBot",
    "Cog",
    "get_permissions",
    "get_tags",
    "is_valid_thread"
)


class Cog(commands.Cog):
    """Base class for all cogs"""

    def __init__(self, bot: AimBot) -> None:
        self.bot = bot
