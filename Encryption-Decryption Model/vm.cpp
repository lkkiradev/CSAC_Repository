#include <iostream>

using namespace std;

struct Book {
    string title;
    int price;
};

void displayBooks(Book books[], int numBooks) {
    cout << "Available Books:\n";
    for (int i = 0; i < numBooks; ++i) {
        cout << i + 1 << ". " << books[i].title << " - Php " << books[i].price << endl;
    }
}

void calculate_change(int payment) {
    int denominations[] = {1000, 500, 200, 100, 50, 20, 10, 5, 1};
    int num_denominations = sizeof(denominations) / sizeof(denominations[0]);

    cout << "Change:" << endl;

    for (int i = 0; i < num_denominations; ++i) {
        int denomination = denominations[i];
        int count = payment / denomination;
        if (count > 0) {
            cout << count << " x " << denomination << endl;
            payment %= denomination;
        }
    }
}

int main() {
    Book books[] = {
        {"The Art of Rock n Roll", 1100},
        {"Coding 101", 1430},
        {"Awaken your Psychic Abilities", 1640},
        {"How to be an Intel Agent", 1575},
        {"The Dichotomy of Self", 1125},
        {"Maritime Strategy", 991}
    };
    int numBooks = sizeof(books) / sizeof(books[0]);

    displayBooks(books, numBooks);

    int choice;
    cout << "Enter the number of the book you want to purchase: ";
    cin >> choice;

    if (choice >= 1 && choice <= numBooks) {
        int quantity;
        cout << "Enter the quantity: ";
        cin >> quantity;

        int totalCost = books[choice - 1].price * quantity;
        cout << "Total cost: Php " << totalCost << endl;

        int payment;
        cout << "Enter the payment amount: ";
        cin >> payment;

        if (payment >= totalCost) {
            int change = payment - totalCost;
            cout << "Total Change: Php " << change << endl;
            calculate_change(change);
        } else {
            cout << "Insufficient payment.\n";
        }
    } else {
        cout << "Invalid choice.\n";
    }

    return 0;
}
