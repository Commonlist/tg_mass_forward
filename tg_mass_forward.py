import asyncio
from pyrogram import Client, filters
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Замените на ваши API ID и API Hash
api_id = "api_id"
api_hash = "api_hash"
# Замените на ваш действительный логин
my_username = "your_username"

# Создаем клиент Telegram
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# ID исходного чата и логины целевых пользователей
source_chat_id = -100source_chat_id  # Замените на действительный ID исходного чата
target_usernames = [
    "buzz_lightyear", "woody_pride", "mr_potato_head", "rex_the_dinosaur",
    "slinky_dog", "hamm_piggy_bank", "bo_peep", "duke_caboom",
    "gabby_gabby", "forbidden_planet_robot"
]

# Обработчик сообщений из исходного чата
@app.on_message(filters.chat(source_chat_id))
async def forward_message(client, message):
    # Если сообщение переслано
    if message.forward_from is not None:
        for username in target_usernames:
            try:
                # Пересылаем сообщение целевым пользователям
                await client.forward_messages(username, source_chat_id, [message.id])
            except Exception:
                pass
    else:
        # Если сообщение от вас
        if message.from_user.username == my_username:
            for username in target_usernames:
                try:
                    # Отправляем текстовые сообщения
                    if message.text:
                        await client.send_message(username, message.text)
                    # Отправляем фотографии
                    elif message.photo:
                        await client.send_photo(username, message.photo.file_id, caption=message.caption)
                    # Отправляем видео
                    elif message.video:
                        await client.send_video(username, message.video.file_id, caption=message.caption)
                    # Отправляем документы
                    elif message.document:
                        await client.send_document(username, message.document.file_id, caption=message.caption)
                    # Отправляем аудио
                    elif message.audio:
                        await client.send_audio(username, message.audio.file_id, caption=message.caption)
                    # Отправляем голосовые сообщения
                    elif message.voice:
                        await client.send_voice(username, message.voice.file_id, caption=message.caption)
                except Exception:
                    pass
        else:
            # Если сообщение не от вас и не переслано
            for username in target_usernames:
                try:
                    # Пересылаем сообщение целевым пользователям
                    await client.forward_messages(username, source_chat_id, [message.id])
                except Exception:
                    pass

# Запуск клиента
app.run()