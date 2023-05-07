#ifndef CARD_H
#define CARD_H

#include <iostream>
#include <string>

class Card {
public:
    // Constructors
    Card();
    Card(const std::string& rank, const std::string& suit);

    // Accessors
    std::string getRank() const;
    std::string getSuit() const;

    // Output operator
    friend std::ostream& operator<<(std::ostream& os, const Card& card);

private:
    std::string rank_;
    std::string suit_;
};

#endif
