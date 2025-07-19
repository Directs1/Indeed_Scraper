import logging
import asyncio
from telegram import Bot
from telegram.error import TelegramError
from config import Config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class JobNotificationBot:
    def __init__(self):
        self.bot = Bot(Config.TELEGRAM_BOT_TOKEN)
        self.chat_id = Config.TELEGRAM_CHAT_ID
    
    async def send_message(self, message):
        """Send a message to Telegram"""
        try:
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode='Markdown'
            )
            logger.info("Message sent successfully")
        except TelegramError as e:
            logger.error(f"Failed to send message: {e}")
    
    async def test_connection(self):
        """Test if bot can send messages"""
        await self.send_message("🤖 Job Bot is online!")

if __name__ == "__main__":
    bot = JobNotificationBot()
    asyncio.run(bot.test_connection())