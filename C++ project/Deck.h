#ifndef DECK_H
#define DECK_H

#include <vector>
#include <cstdlib>
#include "Card.h"
#include "Player.h"

class Deck {
public:
    // Constructors
    Deck();

    // Deck management functions
    void createDefaultDeck();
    void createCustomDeck();
    void shuffle();
    void deal(int numPlayers, int numCards, Player& p1, Player& p2);

    // Accessors
    std::vector<Card> getCards() const;
    int getNumCards() const;

    // Output operator
    friend std::ostream& operator<<(std::ostream& os, const Deck& deck);

private:
    std::vector<Card> cards_;
};

#endif
