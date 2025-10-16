
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

MAIN_MENU = [
    [KeyboardButton("Гражданское право"), KeyboardButton("Уголовное право")],
    [KeyboardButton("Административное право"), KeyboardButton("Трудовое право")],
    [KeyboardButton("Налоговое право"), KeyboardButton("Семейное право")]
]

def back_menu():
    return ReplyKeyboardMarkup([[KeyboardButton("Назад")]], resize_keyboard=True)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать в юридический справочник! Выберите раздел:",
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Гражданское право":
        await update.message.reply_text(
            "Гражданское право регулирует имущественные и личные неимущественные отношения. "
            "Примеры: договоры, наследство, аренда.",
            reply_markup=back_menu()
        )
    elif text == "Уголовное право":
        await update.message.reply_text(
            "Уголовное право определяет ответственность за преступления. "
            "Примеры: кража, мошенничество, хулиганство.",
            reply_markup=back_menu()
        )
    elif text == "Административное право":
        await update.message.reply_text(
            "Административное право регулирует отношения с органами власти. "
            "Примеры: штрафы, лицензии, нарушения ПДД.",
            reply_markup=back_menu()
        )
    elif text == "Трудовое право":
        await update.message.reply_text(
            "Трудовое право регулирует отношения между работниками и работодателями. "
            "Примеры: трудовые договоры, отпуска, увольнения.",
            reply_markup=back_menu()
        )
    elif text == "Налоговое право":
        await update.message.reply_text(
            "Налоговое право регулирует уплату налогов и сборов. "
            "Примеры: НДФЛ, налог на прибыль, налоговые льготы.",
            reply_markup=back_menu()
        )
    elif text == "Семейное право":
        await update.message.reply_text(
            "Семейное право регулирует брачные и семейные отношения. "
            "Примеры: разводы, алименты, усыновление.",
            reply_markup=back_menu()
        )
    elif text == "Назад":
        await update.message.reply_text(
            "Вернулись в главное меню. Выберите раздел:",
            reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
        )
    else:
        await update.message.reply_text(
            "Пожалуйста, выберите раздел из меню.",
            reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
        )

def main():
    TOKEN = "8388557917:AAEm9-BDb2jLKPaDBrretUrnqPJGPfLnglY"

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()