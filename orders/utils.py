import telegram
from django.conf import settings

async def send_telegram_message(order):
    """Send Telegram notification about new order"""
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    
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

    await bot.send_message(
        chat_id=settings.TELEGRAM_ADMIN_CHAT_ID,
        text=message,
        parse_mode='HTML'
    )

    if order.media:
        try:
            await bot.send_document(
                chat_id=settings.TELEGRAM_ADMIN_CHAT_ID,
                document=open(order.media.path, 'rb'),
                caption=f"Файл к заказу #{order.id}"
            )
        except Exception as e:
            print(f"Error sending file: {e}")