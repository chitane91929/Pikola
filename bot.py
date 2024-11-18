import telebot
import openai

# استبدل TOKEN برمز بوت تيليجرام الخاص بك
TELEGRAM_BOT_TOKEN = "7396397001:AAFV9I1aMqD3mrt2E0-ubOfI59cM-jWqVgo"
# استبدل OPENAI_API_KEY بمفتاح API الخاص بك من OpenAI
OPENAI_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! أنا بوت ChatGPT على تيليجرام. كيف يمكنني مساعدتك؟")

@bot.message_handler(func=lambda message: True)
def chatgpt(message):
    response = openai.Completion.create(
        engine="text-davinci-003",  # أو gpt-3.5-turbo
        prompt=message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.reply_to(message, response.choices[0].text)

bot.polling()
