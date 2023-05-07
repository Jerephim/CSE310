#include "Card.h"

// Constructors
Card::Card() {}
Card::Card(const std::string& rank, const std::string& suit) : rank_(rank), suit_(suit) {}

// Accessors
std::string Card::getRank() const {
    return rank_;
}

std::string Card::getSuit() const {
    return suit_;
}

std::ostream& operator<<(std::ostream& os, const Card& card) {
    os << card.rank_ << " of " << card.suit_;
    return os;
}
