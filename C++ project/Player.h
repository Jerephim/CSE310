#ifndef PLAYER_H
#define PLAYER_H

#include <iostream>
#include <vector>
#include "Card.h"

class Player {
public:
    // Constructors
    Player(const std::string& name);

    // Member functions
    void addCard(const Card& card);
    void displayHand() const;
    Card playCard(int index);
    int getNumCards() const;
    std::string getName() const;
    int getHandValue() const;

    // Output operator
    friend std::ostream& operator<<(std::ostream& os, const Player& player);

private:
    std::string name_;
    std::vector<Card> hand_;
};

#endif
