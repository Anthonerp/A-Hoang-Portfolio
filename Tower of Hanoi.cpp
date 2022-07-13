/*
Author: Anthony Hoang
Date: 2022-04-19
Pseudocode:
create class for creation of peg objects and the block objects on those pegs
function for transfering between pegs
display pegs to the user
*/

#include <iostream>
#include <string>
#include <vector> 

using namespace std;

//All the function protoypes I've had to declare

class peg { //Class for the three pegs used in puzzle

   public: 

      class block { //Nested class because blocks are inherent to pegs, they do not exist without the peg to hold them

         public: 

            int length; 
            int width; 

            block(int x) { //Constructor to create blocks on pegs, should only be called on initialization

               length = x; 
               width = 2; 

            }

      };

      vector<block> blocks; //All pegs are justa series of blocks on top of each other
      int initialLongestLength; //Used for spacing purposes, shouldn't change after initialization
      int initialLength; 

      peg(int blocksOnPeg) { //Initial creation of blocks onto peg, creates stack

         for(int i = 0; i < blocksOnPeg; i++) {

            blocks.push_back(block(((blocksOnPeg * 2) + 1) - (2 * i))); //Each block two less than the last, end with 3

         }

      }

      peg(int blocksOnPeg, bool isPeg1) { //special constructor for peg 1, because for some reason initialLongest Length breaks the others

         for(int i = 0; i < blocksOnPeg; i++) {

            blocks.push_back(block(((blocksOnPeg * 2) + 1) - (2 * i))); 

         }

         initialLongestLength = blocks[0].length; //The longest box should always be the initial box of the bottom of peg 1, space around that
         initialLength = blocksOnPeg;

      }

      peg(){}
      
}; 

peg peg1; //3 pegs are at the core of this program, they're global for convenience tbh.
peg peg2;
peg peg3; 

int moveCount; //I need a lot of different programs to modify the moveCount

/* BROKEN ALGORITHM PLEASE IGNORE, just to make me feel better about having conquered this algorithm

      void moveBlock(vector<block>& targetPeg) {

         if ((blocks[blocks.end()].length) < (targetPeg[targetPeg.end()].length)) { //If the block you're adding is smaller than the one below, it can go there

            targetPeg.push_back(blocks[blocks.end()]);
            blocks.erase(blocks.end()); 

         } else { //If not, program doesn't let the user do that

            cout << "You are unable to make this movement, as the block is larger than the one it sits on." << endl; 

         }

      }

*/

void moveBlock(peg &initialPeg, peg &targetPeg) { //Honest to god, these four lines of code took up my whole night

   if (targetPeg.blocks.size() > 0) {

      if (initialPeg.blocks.back().length < targetPeg.blocks.back().length) {

         targetPeg.blocks.push_back(initialPeg.blocks.back());
         initialPeg.blocks.erase(initialPeg.blocks.end() - 1);

      } else {

         cout << "Invalid move! Try a different move." << endl; 
         system("pause"); 

      } 

   } else {

         targetPeg.blocks.push_back(initialPeg.blocks.back());
         initialPeg.blocks.erase(initialPeg.blocks.end() - 1);

   }

}

void createPegs(int blockAmount) { //Sets up the first peg

   peg1 = peg(blockAmount,true);
   peg2 = peg(0);
   peg3 = peg(0); 

}

void loopSpace(int len) { //function to put a specific amount of spaces to align blocks on peg for AESTHETIC
	
	for (int i = 0; i < len; i++) {
		
		cout << " ";
		
	}
	
}

void loopX(int len) { //Print a character a specific amount of times

   for (int i = 0; i < len; i++) {

      cout << "X"; 

   }

}

void loopChar(int len, char character) { //Just prints out a specified amount of any character

   for (int i = 0; i < len; i++) {

      cout << character;

   }

}

void printRow(int length[], int initialSpace[], int betweenSpace, int nullValue) {

   for (int h = 0; h < 2; h++) { //Copys two rows of identical spacing, cause each block is three blocks wide

      for (int i = 0; i < 3; i++) { //Sets of three because there are three pegs

         loopSpace(initialSpace[i]); //Basically, equal spacing on both sides of a block, and then spaces before next block

         if (length[i] == nullValue)
            loopSpace(nullValue * 2);
         else
            loopX(length[i] * 2); //Prints out twice as many x's to emphasize difference

         loopSpace(initialSpace[i]);
         loopSpace(betweenSpace);

      }

      cout << "\n"; 

   }

}

//Cursed function incoming
void presentPegs(int blockAmount) { //Creates the peg representation for the user using multidimensional array

   int arrayHeight = blockAmount - 1; //Height of board array
   int arrayLength = 3; //Length of board array

   int nullValue = peg1.initialLongestLength + 2; 
   int board[blockAmount][arrayLength]; //Spreadsheet representation of what to present on screen
   int copyBoard[arrayLength]; //Copy of the board for the print row function
   int spaceBoard[arrayLength]; //Holds spacing information
   int betweenSpace = 10; //Spaces inbetween pegs

   system("cls"); //Clears screen before presenting pegs

   //Step one: Convert contents of pegs into spreadsheet model storing lengths of block in a "cell"
   for (int i = arrayHeight; i >= 0; i--) { //Starts at bottom left for my sanity

      for (int j = 0; j < arrayLength; j++) {

         switch(j) {

            case 0: //First column will always be first peg
               if (((i * -1) + arrayHeight)  >= peg1.blocks.size()) //Starting to think that starting at bottom left was a bad idea
                  board[i][j] = nullValue;
               else
                  board[i][j] = peg1.blocks[(-1 * i) + arrayHeight].length; //Reverses relationship between vector index and i
               break; 

            case 1: //second column will always use second peg, to ensure proper display
               if (((i * -1) + arrayHeight)  >= peg2.blocks.size()) 
                  board[i][j] = nullValue;
               else
                  board[i][j] = peg2.blocks[(-1 * i) + arrayHeight].length; 
               break;                

            case 2: //Third column will always use third peg, by this point probably should've defined a function
               if (((i * -1) + arrayHeight)  >= peg3.blocks.size()) 
                  board[i][j] = nullValue;
               else
                  board[i][j] = peg3.blocks[(-1 * i) + arrayHeight].length; 
               break; 

         }

      }

   }

   //Step two: Convert spreadsheet into something the user can look at
   cout << "Move count: " << moveCount << endl; 
   cout << "---------------" << endl;
   cout << endl; 

   for (int i = 0; i < blockAmount; i++) { //Start top left 

      for (int j = 0; j < arrayLength; j++) {

         copyBoard[j] = board[i][j]; //Copyboard always holds a particular row of board
         spaceBoard[j] = ((nullValue * 2) - (copyBoard[j] * 2)) / 2; //Every block will be spaced in the middle of a nullValue box

      }

      printRow(copyBoard, spaceBoard, betweenSpace, nullValue); //Displays the row of blocks

   }

   for (int i = 0; i < 3; i++) {

      if (i < 2) {

         loopChar(nullValue * 2, 'O');
         loopSpace(betweenSpace);

      } else {

         loopChar(nullValue * 2,'O'); 

      } 
         
   }

   cout << endl; 
   loopChar((((nullValue * 2) + betweenSpace) * 3) - betweenSpace, '-');
   cout << endl; 

}

void commandLine(int blockAmount) { //Creates screen with line for all user commands

   char input; 
   int target;  

   presentPegs(blockAmount); 

   cout << endl << "Please enter a command. type \"h\" for a list of available commands: "; 
   cin >> input;
   cout << endl; 

   switch(input) {

      case 'h':
         system("cls");
         cout << "Help" << endl;
         cout << "______" << endl; 
         cout << "1" << endl; 
         cout << "- Will move a block from peg 1 to another. Will prompt for which peg." << endl; 
         cout << endl << "2" << endl; 
         cout << "- Will move a block from peg 2 to another. Will prompt for which peg" << endl; 
         cout << endl << "3" << endl; 
         cout << "- Will move a block from peg 3 to another. Will prompt for which peg" << endl; 
         cout << endl << "e" << endl; 
         cout << "- Terminate the program" << endl; 
         system("pause");
         commandLine(blockAmount); 
         break; 

      case '1':

         cout << "Which peg do you want to move the block to? (2 or 3)" << endl; 
         cin >> target; 

         if (target == 2) 
            moveBlock(peg1, peg2);
         else if (target == 3)
            moveBlock(peg1, peg3); 

         moveCount++;

         break; 

      case '2':

         cout << "Which peg do you want to move the block to? (1 or 3)" << endl; 
         cin >> target; 

         if (target == 1)
            moveBlock(peg2, peg1); 
         else if (target == 3)
            moveBlock(peg2, peg3); 

         moveCount++;

         break; 

      case '3':

         cout << "Which peg do you want to move the block to? (1 or 2)" << endl; 
         cin >> target; 

         if (target == 1)
            moveBlock(peg3, peg1); 
         else if (target == 2)
            moveBlock(peg3, peg2); 

         moveCount++; 

         break; 

      case 'e':
         exit(0);
         break;

   }

}

int main() {

   int blockAmount;
   bool complete = false; 
   char yesNo;

   cout << "Welcome to Anthony's Tower of Hanoi, extra legitimate because my family is from Vietnam." << endl; 
   cout << "Not quite sure why it's called Tower of Hanoi though....." << endl; 

   cout << "How many blocks will be involved here? ";
   cin >> blockAmount; 

   createPegs(blockAmount);

   while (complete == false) {

      commandLine(blockAmount);

      if (peg3.blocks.size() == peg1.initialLength) {

         presentPegs(blockAmount);
         cout << "Congratulations! You solved the puzzle! Do you want to do it again? (y or n)" << endl; 
         cin >> yesNo; 

         if (yesNo == 'y') {

            cout << "How many blocks will be involved here? ";
            cin >> blockAmount;
            moveCount = 0; 
            createPegs(blockAmount);

         }
         else 
            complete = true; 

      }

   }

   return 0; 

}