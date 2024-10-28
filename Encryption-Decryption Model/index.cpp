#include <iostream>
#include <limits>
using namespace std;

// Function to generate permutations
void generatePermutation(char* result, char start, char end, int length, int depth) {
    // Prints the result if depth reaches the length. 
    if (depth == length) {
        result[length] = '\0'; 
        cout << result << endl;
        return;  // Exits the function after printing result
    }

    if (start <= end) {
        // Ascending order if ending letter is greater than starting letter
        for (char c = start; c <= end; c++) {
            result[depth] = c;  // Set the current character in the result
            generatePermutation(result, start, end, length, depth + 1);  // Recursive call to fill the next position
        }
    } else {
        // Descending order if ending letter is less than starting letter
        for (char c = start; c >= end; c--) {
            result[depth] = c;
            generatePermutation(result, start, end, length, depth + 1); 
        }
    }
}

// Function to validate character input
char validateCharInput(const string& prompt) {
    char input;
    while (true) {
        cout << prompt;  // Prompt the user for input
        cin >> input;

        // Validation if the user fails to enter a valid input
        if (cin.fail() || !isalpha(input) || cin.peek() != '\n') {
            cout << "Invalid input. Please enter a single letter." << endl; 
            cin.clear();  // Clear the error flag on cin
            cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Discard invalid input
            continue;  // Restart the loop for valid input
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Clear input buffer after valid input
        return input;  // Return the valid character input
    }
}

// Function to validate integer input
int validateIntInput(const string& prompt) {
    int input;
    while (true) {
        cout << prompt; 
        cin >> input;

        // Validation if the user fails to enter a valid input
        if (cin.fail()) {
            cout << "Invalid input. Please enter a valid integer." << endl; 
            cin.clear(); 
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
            continue;  
        }
        else if(input <= 0 || input > 5) {  // Check if the integer is in the range of 1-5
            cout << "Invalid input. Please enter an integer ranging from 1-5." << endl;
            continue;  // Restarts the loop for valid input
        }
        else {
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
            return input; 
        }
    }
}

// Function to validate that both starting and ending letters are in the same case
bool validateSameCase(char start, char end) {
    return (islower(start) && islower(end)) || (isupper(start) && isupper(end));  // Return true if both characters are in the same case
}

int main() {
    char startingLetter, endingLetter;
    
    // Loop until valid inputs for starting and ending letters are entered
    while (true) {
        startingLetter = validateCharInput("Enter the starting letter: ");  // Get starting letter from user
        endingLetter = validateCharInput("Enter the ending letter: ");  // Get ending letter from user

        // Validate that both letters are in the same case
        if (validateSameCase(startingLetter, endingLetter)) {
            break;  // Exit the loop if the case validation is successful
        } else {
            cout << "Please try again, kindly input a character in the same case (uppercase or lowercase)." << endl;
        }
    }

    int length = validateIntInput("Enter the desired length (1-5): ");  // Get the length from user

    // Dynamically allocate memory for the result array (+ 1 for null terminator)
    char* result = new char[length + 1]; 

    // Call the recursive function to generate permutations
    generatePermutation(result, startingLetter, endingLetter, length, 0);

    // Free the dynamically allocated memory to prevent memory leaks
    delete[] result;

    return 0;
}
