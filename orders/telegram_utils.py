import telegram
from django.conf import settings
from datetime import datetime
import asyncio

async def send_telegram_message(message, file_path=None):
    """
    Send message and optionally a file to Telegram admin
    """
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    
    # Send text message
    await bot.send_message(
        chat_id=settings.TELEGRAM_ADMIN_CHAT_ID,
        text=message,
        parse_mode='HTML'
    )
    
    # If file exists, send it
    if file_path:
        await bot.send_document(
            chat_id=settings.TELEGRAM_ADMIN_CHAT_ID,
            document=open(file_path, 'rb'),
            caption="Прикрепленный файл"
        )

async def send_order_notification(order):
    """
    Send order notification to Telegram admin
    """
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    
    # Format message
    message = f"""
🆕 Новый заказ #{order.id}

👤 Пользователь: {order.user.username}
📧 Email: {order.user.email}
📱 Telegram: {order.user.telegram_username}

📑 Название: {order.name}
📝 Описание: {order.description}
⏰ Дедлайн: {order.deadline.strftime('%d.%m.%Y')}
📊 Статус: {order.get_status_display()}
"""

    # Send text message
    await bot.send_message(
        chat_id=settings.TELEGRAM_ADMIN_CHAT_ID,
        text=message,
        parse_mode='HTML'
    )

    # Send file if attached
    if order.media:
        try:
            await bot.send_document(
                chat_id=settings.TELEGRAM_ADMIN_CHAT_ID,
                document=open(order.media.path, 'rb'),
                caption=f"Файл к заказу #{order.id}"
            )
        except Exception as e:
            print(f"Error sending file: {e}")