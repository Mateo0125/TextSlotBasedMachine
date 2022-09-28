import random

ROWS = 3
COLS = 3

# It's a constant variable and this is how it's written
MAX_LINES = 5
MIN_LINES = 3
MAX_BET = 50
MIN_BET = 10

symbol_count = {
    "a": 2,
    "b": 4,
    "c": 6,
    "d": 8
}

symbol_value = {
    "a": 5,
    "b": 4,
    "c": 3,
    "d": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])

        print()


def deposit():
    while True:
        amount = input(f"Deposit the amount of money: $")
        # checking if this amount is a positive number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Amount most be greater than 0.")
        else:
            print(f"Please enter a number")
    return amount


def get_bet_lines():
    while True:
        print("")
        bet_lines = input(
            f"Select a number of lines between {MIN_LINES} and {MAX_LINES} that you'd like to bet: ")
        if bet_lines.isdigit():
            bet_lines = int(bet_lines)
            if MIN_LINES <= bet_lines <= MAX_LINES:
                print(f"You picked {bet_lines} bet lines")
                break
            else:
                print(
                    f"The number of bet lines has to be between {MIN_LINES} and {MAX_LINES}")
        else:
            print(f"Write a valid number between {MIN_LINES} and {MAX_LINES}")
    return bet_lines


def get_bet():
    while True:
        print("")
        bet = input(
            f"How much would you like to bet on each line? min ${MIN_BET} max ${MAX_BET}: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(
                    f"You have to bet more than {MIN_BET} and less than {MAX_BET}")
        else:
            print(f"Write a valid bet")
    return bet


def game(balance):
    lines = get_bet_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"The total bet -> {total_bet} is over the balance -> {balance}, so you can't bet.")
        else:
            break

    print(f"\nBalance: ${balance}\n")
    print(
        f"You're betting ${bet} bucks on each {lines} lines. \nThe total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        decision = input(f"Press enter to spin. (q to quit): ")
        if decision == "q":
            break
        balance += game(balance)

    print(f"You left with ${balance}")


main()
