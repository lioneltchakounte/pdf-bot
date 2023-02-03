import telebot
from reportlab.pdfgen import canvas

bot = telebot.TeleBot('6023203871:AAGTxpd5EM70BOYKvzuLHr1QXW5M9utsVso')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm ChatSonic. I can turn any text into a PDF format. Just send me the text and I will convert it for you.")

@bot.message_handler(func=lambda message: True)
def pdf_bot(message):
    # Generate PDF file
    c = canvas.Canvas(message.from_user.id+'.pdf')
    c.drawString(100,100, message.text)
    c.save()
    # Send generated PDF file
    doc = open(message.from_user.id+'.pdf', 'rb')
    bot.send_document(message.chat.id, doc)
    doc.close()

bot.polling()