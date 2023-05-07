#include "Deck.h"
#include <ctime>

// Constructors
Deck::Deck() {
    // Initialize the cards in the deck
    createDefaultDeck();
}

// Deck management functions
void Deck::createDefaultDeck() {
    // Clear any existing cards from the deck
    cards_.clear();

    // Create a deck of cards with Ace through King and Spades, Clubs, Hearts, and Diamonds
    std::vector<std::string> ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
    std::vector<std::string> suits = {"Spades", "Hearts", "Clubs", "Diamonds"};

    for (const auto& suit : suits) {
        for (const auto& rank : ranks) {
            Card card(rank, suit);
            cards_.push_back(card);
        }
    }
}

void Deck::createCustomDeck() {
    // Clear any existing cards from the deck
    cards_.clear();

    // Create a deck of cards with user-specified quantities
    std::vector<std::string> ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
    std::vector<std::string> suits = {"Spades", "Clubs", "Hearts", "Diamonds"};

    for (const auto& suit : suits) {
        for (const auto& rank : ranks) {
            int quantity;
            std::cout << "Enter the quantity of " << rank << " of " << suit << ": ";
            std::cin >> quantity;

            for (int i = 0; i < quantity; i++) {
                Card card(rank, suit);
                cards_.push_back(card);
            }
        }
    }
}

void Deck::shuffle() {
    // Shuffle the deck by randomly swapping pairs of cards
    srand(time(NULL));  // Seed the random number generator

    for (int i = 0; i < cards_.size(); i++) {
        int j = rand() % cards_.size();
        std::swap(cards_[i], cards_[j]);
    }
}

void Deck::deal(int numPlayers, int numCards, Player& p1, Player& p2) {
    // Make sure there are enough cards in the deck to deal
    int totalCards = numPlayers * numCards;
    if (cards_.size() < totalCards) {
        std::cerr << "Not enough cards in deck to deal." << std::endl;
        return;
    }

    // Deal cards to the players
    for (int i = 0; i < numCards; i++) {
        for (int j = 0; j < numPlayers; j++) {
            Card card = cards_.back();
            cards_.pop_back();

            if (j == 0) {
                p1.addCard(card);
            } else {
                p2.addCard(card);
            }
        }
    }
}

// Accessors
std::vector<Card> Deck::getCards() const {
    return cards_;
}

int Deck::getNumCards() const {
    return cards_.size();
}

// Output operator
std::ostream& operator<<(std::ostream& os, const Deck& deck) {
    for (const auto& card : deck.cards_) {
        os << card << std::endl;
    }
    return os;
}
