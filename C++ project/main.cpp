#include <iostream>
#include <string>
#include "Card.h"
#include "Deck.h"
#include "Player.h"

using namespace std;

int main() {
    cout << "\t--Welcome to 2 player cards. This is a basic\n\t  program that takes 2 players, deals them random\n\t  cards, and then compares their totals\n\t  to see who has the most points--\n";
    // Create the deck of cards and shuffle it
    Deck deck;
    deck.createDefaultDeck();
    deck.shuffle();

    // Get the number of players and the number of cards per hand
    int numPlayers, numCards;
    numPlayers = 2;
    cout << "Enter the number of cards per hand: ";
    cin >> numCards;

    // Create the players
    vector<Player> players;
    for (int i = 1; i <= numPlayers; i++) {
        string name;
        cout << "Enter the name of Player " << i << ": ";
        cin >> name;
        Player player(name);
        players.push_back(player);
    }

    // Play the game
    bool continuePlaying = true;
    while (continuePlaying) {
        // Deal the cards to the players
        deck.deal(numPlayers, numCards, players[0], players[1]);

        // Display the players' hands
        for (const auto& player : players) {
            player.displayHand();
            cout << endl;
        }

        // Determine the winner
        Player winner = players[0];
        for (const auto& player : players) {
            if (player.getHandValue() > winner.getHandValue()) {
                winner = player;
            }
        }
        cout << "The winner is " << winner.getName() << "!" << endl;

        // Ask the user if they want to play another round
        char playAgain;
        
        playAgain = 'N';
        continuePlaying = (playAgain == 'y' || playAgain == 'Y');
    }

    return 0;
}
