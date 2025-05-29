import telebot

bot = telebot.TeleBot("7944656780:AAHQ3DQfVnJ3CLAaDHPMdv2m3IAKIYRxJ7I")
user_sessions = {}

card_sign = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Q': 10, 'K': 10, 'J': 10, 'A': 10
}
cards = list(card_sign.keys())


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in user_sessions:
        user_sessions[user_id] = {"balance": 1000}
    bot.send_message(message.chat.id, f"Let's go gambling! Your balance: {1000}$.")


@bot.message_handler(commands=["balance"])
def get_balance(message):
    user_id = message.from_user.id
    balance = user_sessions.get(user_id, {}).get("balance", 0)
    bot.send_message(message.chat.id, f'You balance is: {balance}.')


@bot.message_handler(commands=["blackjack"])
def bj_start(message):
    user_id = message.from_user.id
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        bot.send_message(message.chat.id, f'The command is /blackjack <amount>.')
        return
    bet = int(args[1])
    user_data = user_sessions.setdefault(user_id, {"balance": 1000})

    if bet > user_data['balance']:
        balance = user_sessions.get(user_id, {}).get("balance", 0)
        bot.send_message(message.chat.id, f"Not enough money for your bet. Your balance: {balance}")
        return

    user_data["balance"] -= bet
    user_data["game"] = bj_game(user_id, bet)


def gamestate(chat_id, user_id):
    session = user_sessions[user_id]["game"]
    player = session['player']
    dealer = session['dealer']
    total = caltotal(player)
    dealer_visible = dealer[0]

    msg = (
        f"Your card: {format_hand(player)} (amount: {total})\n"

    )


if __name__ == '__main__':
    bot.polling(none_stop=True)