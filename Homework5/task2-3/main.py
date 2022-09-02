from ui import ConsoleUI
from candies import *
from tictactoe import *

# Функция выбора и настройки игры
def get_game(ui: UI) -> Game:
    game_number = ui.output_menu(['Конфеты', 'Крестики-Нолики'])
    vs_player = ui.output_menu(['Против бота', 'Против игрока'])
    names = [ui.input_str(f"Укажите имя {f'игрока №{i + 1}' if vs_player else 'игрока' if i == 0 else 'бота'}: ", True) for i in range(2)]

    if game_number == 0:
        game = Candies(CandiesPlayer(names[0], ui), CandiesPlayer(names[1], ui) \
            if vs_player else CandiesBot(names[1], ui), ui, 28, 2021)
    elif game_number == 1:
        game = TicTacToe(TicTacToePlayer(names[0], ui), TicTacToePlayer(names[1], ui) \
            if vs_player else TicTacToeBot(names[1], ui), ui)

    return game

def main():
    ui = ConsoleUI()
    game = None
    repeat = False
    while True:
        if game == None or not repeat:
            game = get_game(ui)
        game.start()
        repeat = ui.output_menu(['Новая игра', 'Повторить'])

if __name__ == '__main__':
    main()
