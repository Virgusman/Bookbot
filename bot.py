import asyncio


from aiogram import Bot, Dispatcher
from config_data.config import TOKEN


from handlers import other_handlers, user_handlers
#from handlers.other_handlers import register_echo_handler
#from handlers.user_handlers import register_user_handlers
from keyboards.main_menu import set_main_menu


# Фнукция для регистрации всех хэндлеров
#def register_all_handlers(dp: Dispatcher) -> None:
#    register_user_handlers(dp)
#    register_echo_handler(dp)


# Функция конфигурирования и запуска бота
async def main():
    bot: Bot = Bot(token=TOKEN)
    dp: Dispatcher = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем все хэндлеры
    #register_all_handlers(dp)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    # Запускаем polling
    #try:
    #    await dp.start_polling()
    #finally:
    #    await bot.close()


if __name__ == '__main__':
    try:
        # Запускаем функцию main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        print('Bot stopped!')