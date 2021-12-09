from typing import List, Tuple

def decks_from_file(filepath: str):
    """
    Reads input from a given file and returns the cards,
    as defined in https://adventofcode.com/2020/day/22.
    """
    decks = []
    with open(filepath, "r") as file:
        cards = []
        for line in file.readlines():
            line = line.strip()
            if line == "Player 1:" or line == "":
                pass
            elif line == "Player 2:":
                decks.append(cards)
                cards = []
            else:
                cards.append(int(line))
        decks.append(cards)
    return decks

saved_games = {}
played_games = 0
rounds = {}

def play_recursive_combat(p1deck: List[int], p2deck: List[int]) -> Tuple[int, List[int]]:
    global saved_games, rounds, played_games
    game = played_games + 1
    played_games += 1
    rounds[game] = 1
    saved_games.setdefault(game, {})
    #print(f"=== Game {game} ===")
    while p1deck and p2deck:
        rounds[game] += 1
        #print(f"\n-- Round {rounds[game]} (Game {game}) --")

        game_key = (tuple(p1deck), tuple(p2deck))
        if game_key in saved_games[game]:
            return 1, p1deck
        else:
            saved_games[game][game_key] = True
        #print("Player 1's deck:", ", ".join(list(map(str, p1deck))))
        #print("Player 2's deck:", ", ".join(list(map(str, p2deck))))
        card1 = p1deck.pop(0)
        card2 = p2deck.pop(0)
        #print(f"Player 1 plays: {card1}")
        #print(f"Player 2 plays: {card2}")
        if len(p1deck) >= card1 and len(p2deck) >= card2:
            #print("Playing a sub-game to determine the winner...\n")
            winner, _ = play_recursive_combat(list(p1deck)[:card1], list(p2deck)[:card2])
            #print(f"...anyway, back to game {game}.")
            if winner == 1:
                winnerdeck = p1deck
            else:
                winnerdeck = p2deck
        else:
            if card1 > card2:
                winner = 1
                winnerdeck = p1deck
            else:
                winnerdeck = p2deck
                winner = 2
        #print(f"Player {winner} wins round {rounds[game]} of game {game}!")
        winnerdeck.append(card1 if winner == 1 else card2)
        winnerdeck.append(card2 if winner == 1 else card1)
    #print(f"The winner of game {game} is player {winner}!")
    return (winner, winnerdeck)

def main(file: str):
    p1deck, p2deck = decks_from_file(file)
    # Part 1 simulation
    while not any([len(deck) == 0 for deck in [p1deck, p2deck]]):
        card1 = p1deck.pop(0)
        card2 = p2deck.pop(0)
        if card1 > card2:
            winnerdeck = p1deck
        else:
            winnerdeck = p2deck
        winnerdeck.append(card1 if card1 > card2 else card2)
        winnerdeck.append(card1 if card1 < card2 else card2)
    print(sum([i * winnerdeck[len(winnerdeck)-i] for i in range(1, len(winnerdeck) + 1)]))
    # Part 2 simulation
    p1deck, p2deck = decks_from_file(file)
    _, winnerdeck = play_recursive_combat(p1deck, p2deck)
    print(sum([i * winnerdeck[len(winnerdeck)-i] for i in range(1, len(winnerdeck) + 1)]))


if __name__ == "__main__":
    print("-- test --")
    main("test.txt")
    print("-- input --")
    main("input.txt")
