from telegram.ext import Updater, CommandHandler

def main():
    # Instancia de updater
    updater = Updater(token=open("./bot_token").read(), use_context=True)
    #Añadir manejador al comando /start
    updater.dispatcher.add_Handler(CommandHandler("start", start))

    #Añadir manejador al comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #Añadir manejador al comando /sumar
    updater.dispatcher.add_handler(CommandHandler("sumar", sumar))

    # Pedir notificaciones a telegram
    updater.start_polling()

    # Capturar señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text('Hola, soy un bot!')

def repite(update, context):
    update.message.reply_text(update.message.text)

def sumar(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text('El resultado es: ' + str(resultado))

main()