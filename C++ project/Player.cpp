#include "Player.h"

// Constructors
Player::Player(const std::string& name) : name_(name) {}

// Member functions
void Player::addCard(const Card& card) {
    hand_.push_back(card);
}

void Player::displayHand() const {
    std::cout << name_ << "'s hand:" << std::endl;
    for (const auto& card : hand_) {
        std::cout << card << std::endl;
    }
}

Card Player::playCard(int index) {
    Card card = hand_[index];
    hand_.erase(hand_.begin() + index);
    return card;
}

int Player::getNumCards() const {
    return hand_.size();
}

std::string Player::getName() const {
    return name_;
}

int Player::getHandValue() const {
    int handValue = 0;
    int numAces = 0;

    // Calculate the value of the hand
    for (const auto& card : hand_) {
        if (card.getRank() == "Ace") {
            numAces++;
            handValue += 11;
        } else if (card.getRank() == "King" || card.getRank() == "Queen" || card.getRank() == "Jack") {
            handValue += 10;
        } else {
            handValue += stoi(card.getRank());
        }
    }

    // Adjust for Aces
    while (handValue > 21 && numAces > 0) {
        handValue -= 10;
        numAces--;
    }

    return handValue;
}

std::ostream& operator<<(std::ostream& os, const Player& player) {
    os << player.name_ << "'s hand:" << std::endl;
    for (const auto& card : player.hand_) {
        os << card << std::endl;
    }
    return os;
}
