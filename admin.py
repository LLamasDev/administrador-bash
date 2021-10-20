#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import subprocess
from data import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

proceso_seleccionado = '' # Variable global con la que gestionaremos los procesos
proceso_seleccionado_completo = '' # Variable global con el nombre completo del proceso

def main_menu_keyboard(): # Menu inicial
    keyboard = [[InlineKeyboardButton('Supercell', callback_data='supercell')], [InlineKeyboardButton('Clash Royale', callback_data='clashroyale')], [InlineKeyboardButton('Clash of Clans', callback_data='clashofclans')]]

    return InlineKeyboardMarkup(keyboard)

def main_menu_keyboard_all(): # Menu del proceso
    keyboard = [[InlineKeyboardButton('Menú principal', callback_data='menu_principal')], [InlineKeyboardButton('Estado', callback_data='menu_estado')], [InlineKeyboardButton('Arrancar', callback_data='menu_arrancar'), InlineKeyboardButton('Parar', callback_data='menu_parada')]]

    return InlineKeyboardMarkup(keyboard)

def main():
    updater = Updater(TOKEN, use_context=True)
    ud = updater.dispatcher
    ud.add_handler(CommandHandler('start', start))
    ud.add_handler(CallbackQueryHandler(menu_bot_cambio, pattern='supercell'))
    ud.add_handler(CallbackQueryHandler(menu_bot_cambio, pattern='clashroyale'))
    ud.add_handler(CallbackQueryHandler(menu_bot_cambio, pattern='clashofclans'))
    ud.add_handler(CallbackQueryHandler(menu_bot_principal, pattern='menu_principal'))
    ud.add_handler(CallbackQueryHandler(menu_bot_estado, pattern='menu_estado'))
    ud.add_handler(CallbackQueryHandler(menu_bot_arranque, pattern='menu_arrancar'))
    ud.add_handler(CallbackQueryHandler(menu_bot_parada, pattern='menu_parada'))
    updater.start_polling()
    updater.idle()

def start(update, context):
    chatId = update.message.from_user.id

    if chatId == miID: # Si el ID no es el mio no hago nada
        update.message.reply_text('Todos los bots:', reply_markup=main_menu_keyboard())

def menu_bot_cambio(update, context): # Cambio las variables globales
    query = update.callback_query
    query.answer # Saco lo pulsado en el boton
    global proceso_seleccionado, proceso_seleccionado_completo
    proceso_seleccionado = query.data # Cambio la variable global a lo pulsado en el boton que es el proceso que quiero tocar

    if proceso_seleccionado == 'supercell':
        proceso_seleccionado_completo = 'Supercell'
    elif proceso_seleccionado == 'clashroyale':
        proceso_seleccionado_completo = 'Clash Royale'
    elif proceso_seleccionado == 'clashofclans':
        proceso_seleccionado_completo = 'Clash of Clans'

    menu_bot_estado(update, context)

def menu_bot_principal(update, context):
    query = update.callback_query

    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text='Todos los bots:', reply_markup=main_menu_keyboard())

def menu_bot_estado(update, context):
    query = update.callback_query
    global proceso_seleccionado, proceso_seleccionado_completo
    proceso_seleccionado_estado = './procesos.sh ' + proceso_seleccionado
    texto_cr = subprocess.check_output([proceso_seleccionado_estado], universal_newlines=True, shell=True) #texto_cr = subprocess.run(['ls', '-a'], capture_output=True, text=True)

    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text=proceso_seleccionado_completo + ':\n' + texto_cr, reply_markup=main_menu_keyboard_all())

def menu_bot_arranque(update, context):
    query = update.callback_query
    global proceso_seleccionado, proceso_seleccionado_completo
    proceso_seleccionado_arranque = './start.sh ' + proceso_seleccionado
    texto_cr = subprocess.check_output([proceso_seleccionado_arranque], universal_newlines=True, shell=True)

    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text=proceso_seleccionado_completo + ':\n' + texto_cr, reply_markup=main_menu_keyboard_all())

def menu_bot_parada(update, context):
    query = update.callback_query
    global proceso_seleccionado, proceso_seleccionado_completo
    proceso_seleccionado_parada = './stop.sh ' + proceso_seleccionado
    texto_cr = subprocess.check_output([proceso_seleccionado_parada], universal_newlines=True, shell=True)

    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text=proceso_seleccionado_completo + ':\n' + texto_cr, reply_markup=main_menu_keyboard_all())

if __name__ == '__main__':
    main()
