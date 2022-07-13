/*
Author: Anthony Hoang
Date: 3/8/2022
Course: COP 1000
Summary: DEDUCE MATHMATICAL RELATIONSHIP BETWEEN COMPARISON COUNT OF REFINED SORT AND BASIC SORT, ALSO MODEL TIME SAVING JUST FOR FUN
Errors:
Pseudocode:

function to create random array of specified length
copy random array to two other arrays
function to calculate comparisons sorting array created with function using basic sort
function to calculator comparisons sorting array created with function using refined sort

subtract basic count - refined sort to calculate difference

print out table of calculations

afterwards use time framework in Carats vs. asterisk to calculate the time difference.

*/

#include <iostream>
#include <vector>
#include <numeric> 
#include <chrono>
#include <sys/time.h>
#include <ctime>
#include <cmath>
#include <string>
#include <stdlib.h>
#include <cstdlib>
#include <string> 

using namespace std;
using std::chrono::duration_cast; //All of these are for time measuring
using std::chrono::milliseconds;
using std::chrono::seconds;
using std::chrono::system_clock;

class List { //Class for list objects, unsorted initially but the sorted via both methods
	
	public:
		
		int length;
		int basicCount=0; 
		int refinedCount=0; 
		int comparisonDifference = 0; 
		int useless; //Variable for constructor used for time calculation		
		
		vector<int> basicList; 
		vector<int> refinedList;
		vector<int> unsortedList; 
		
		vector<int> arrayCreator() { //Creates a pointer to an array with random elements of specified amount
				
			for (int i = 0; i < length; i++) { //loop to create array of specified element count
		
				unsortedList.push_back(rand() % 1001); //Creates array with a random integer for each slot
				
			}
	
			return unsortedList; 
	
		}

		vector<int> basicSort() { //Return sorted list while also adding comparison count to vector of amounts
	
			for (int i = 0; i < length; i++) { //loop to copy unsortedList onto basicList, to maintain unsortedList for presentation
				
				int pushValue = unsortedList[i];
				basicList.push_back(pushValue);
				
			}
			
			int innerIndex = 0, outerIndex = 0; 
			int comparisons = length - 1; 
			int temp; 
			int comparisonCount = 0; 
	
			while (outerIndex < comparisons) { //Actual comparison loop we did in class
		
				innerIndex = 0;
		
				while (innerIndex < comparisons) {
			
					if (basicList[innerIndex] > basicList[innerIndex + 1]) {
			
						temp = basicList[innerIndex + 1];
						basicList[innerIndex + 1] = basicList[innerIndex];
						basicList[innerIndex] = temp; 
			
					}
		
				innerIndex++;
				basicCount++;	
			
				}
	
			outerIndex++;
		
			}
	
			return basicList; 
	
		}

		vector<int> refinedSort() { //Calculate total comparison count for refined bubble sort, return vector of values
	
			for (int i = 0; i < length; i++) {
				
				int pushValue = unsortedList[i];
				refinedList.push_back(pushValue);
				
			}
			
			int innerIndex = 0, outerIndex = 0; 
			int comparisons = length - 1; 
			int pairsToCompare = comparisons; 
			int temp; 
			int comparisonCount = 0; 

			while (outerIndex < comparisons) {
		
				innerIndex = 0;
		
				while (innerIndex < pairsToCompare) {
			
					if (refinedList[innerIndex] > refinedList[innerIndex+1]) {
			
						temp = refinedList[innerIndex+1];
						refinedList[innerIndex+1] = refinedList[innerIndex];
						refinedList[innerIndex] = temp; 
			
					}
		
					innerIndex++;
					refinedCount++;
			
				}
	
				outerIndex++;
				pairsToCompare--;

			}
	
			return refinedList; 
			
		}
		
		int calcDifference() { //Simply calculates difference between basic comparison count and refined comparison count
		
			comparisonDifference = basicCount - refinedCount; 
			
			return comparisonDifference; 
		
		}
		
		int getBasicCount(int num) { //Formula for calculating any amount of basic comparisons, formula I generated using online website
			
			int totalCount = 0;
			totalCount = (num * num) - (2 * num) + 1; 
			
			return totalCount;
			
		}
		
		int getRefinedCount(int num) { //Same thing but for refined
			
			int totalCount = 0; 
			totalCount = ((num * num) - num) / 2;
			
			return totalCount; 
			
		}
		
		int getDifference(int num) { //Same thing but for the difference
			
			int totalCount = 0;
			totalCount = ((num * num) - (3 * num) + 2) / 2;
			
		}
	
		List(int num) { //Constructor to invoke when generating table
			
			length = num; 
			unsortedList = arrayCreator();
			basicList = basicSort();
			refinedList = refinedSort();
			comparisonDifference = calcDifference();
			
		}
		
		List(int num, int dummy) { //Constructor to invoke for calculating time difference, just produces unsorted list
			
			useless = dummy;
			length = num; 
			unsortedList = arrayCreator();
			basicList; 
			refinedList;
			
		}
	
};

void dynamicSpace(int len, int total) { //function to left align values, kinda proud of this one
	
	int temp; 
	temp = to_string(len).length();
	
	for (int i = 0; i < (total - temp); i++) {
		
		cout << " ";
		
	}
	
}

vector<List> unsortedHolder; //Top three global vectors hold actual timing data per sort of 50000 lists, bottom three hold per listLength sorting averages and millisecond difference
vector<int> basicTimes;
vector<int> refinedTimes; 
vector<int> basicAverages;
vector<int> refinedAverages; 
vector<int> integerDifferences; 
vector<int> percentDifferences; 

void calculateUnsorted(int listLength, int listAmount) { //Generates unsorted list for use for timed sorting
	
	for (int i = 0; i < listAmount; i++) {
		
		List temp(listLength,0);
		unsortedHolder.push_back(temp);
		
	}	
	
}

void calculateBasicTime() { //Calculates average basic time to sort 

	int basicChange;
	int basicTotal;
	
	auto basicInitial = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();	//This line performs voodoo by converting the sysem UNIX time into exact milliseconds
		
	for (int i = 0; i < unsortedHolder.size(); i++) { //Sorts everything that's in unsortedHolder
		
		unsortedHolder[i].basicSort(); 
		
	}
	
	auto basicPost = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count(); 
	basicChange = basicPost - basicInitial; //Compares the time difference and saves it to a list of differences
	basicTimes.push_back(basicChange);
	
}

void calculateRefinedTime() { //Does the same thign as the function above, except for the refined algorithm

	int refinedChange;
	int refinedTotal;
		
	auto refinedInitial = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();		
		
	for (int i = 0; i < unsortedHolder.size(); i++) {
		
		unsortedHolder[i].refinedSort(); 
		
	}
	
	auto refinedPost = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
	refinedChange = refinedPost - refinedInitial; 
	refinedTimes.push_back(refinedChange);
	
}

void allTogether(int trials, int listLength) { //Combines the two functions above and prints out the results for each trial 
	
	for (int i = 0; i < trials; i++) {
		
		calculateUnsorted(listLength,50000);
		calculateBasicTime();
		calculateRefinedTime();
		
		cout << "Trial " << (i + 1) << endl; //This is for actually creating a presentable table
		cout << "__________________________________________________________________" << endl; 
		cout << endl; 
		cout << "Basic time: " << basicTimes[i] << "               refined time: " << refinedTimes[i] << endl; 
		cout << endl; 
		
		unsortedHolder.clear();
		
	}
	
}

void calcAverage(int listCount) { //Calculates average time per sort type, also displays min and max elements per list. 
	
	float basicAverage; 
	int basicTotal;
	float refinedAverage;
	int refinedTotal; 
	float percentDifference;
	int integerDifference; 
	
	basicTotal = accumulate(basicTimes.begin(), basicTimes.end(), 0); //These lines calculate the average
	basicAverage = (static_cast<float>(basicTotal)) / (static_cast<float>(basicTimes.size())); 
	
	refinedTotal = accumulate(refinedTimes.begin(), refinedTimes.end(), 0); 
	refinedAverage = static_cast<float>(refinedTotal) / (static_cast<float>(refinedTimes.size())); 
	
	if (refinedAverage > basicAverage) { //Calculates the percent difference between times
	
		cout << "Anthony, you've probably done somethign wrong!" << endl; //Basic Average should always be larger than refined average; outputs a message if that's not the case for troubleshooting
		integerDifference = refinedAverage - basicAverage;
		percentDifference = (integerDifference / basicAverage) * 100;
	
	} else if (basicAverage > refinedAverage) {
		
		integerDifference = basicAverage - refinedAverage;
		percentDifference = (integerDifference / refinedAverage) * 100; 
		
	}
	
	basicAverages.push_back(basicAverage);
	refinedAverages.push_back(refinedAverage);
	integerDifferences.push_back(integerDifference);
	percentDifferences.push_back(percentDifference);
	
	cout << "-------------------------------------------------------------------" << endl; //Presents the average for each list length after trials
	cout << "BASIC AVERAGE: " << basicAverages[listCount] << "            REFINED AVERAGE: " << refinedAverages[listCount] << endl; 
	cout << "ABSOLUTE DIFFERENCE: " << integerDifferences[listCount] << endl; 
	cout << "-------------------------------------------------------------------" << endl; 
	cout << endl;
	
	basicTimes.clear();
	refinedTimes.clear();
	
}

void displayTime() { //Display all the times calculated

	int runs; //Variables for user inputer to control loop length
	int startLength;
	int endLength;
	int interval;
	int q = 0; //Dummy variables used for custom length loops
	int r = 0;
	
	cout << "What will be the trial length/# of run throughs? (bigger = more accurate)" << endl; 
	cin >> runs;
	cout << endl << "What length of list do you want to start with?" << endl;
	cin >> startLength;
	cout << endl << "What will be the maximum list length? (Table might not include max, depending on interval)" << endl; 
	cin >> endLength;
	cout << endl << "What will be the interval between list lengths?" << endl; 
	cin >> interval;
	cout << endl; 
	system("cls"); 
	
	cout << "*UNITS IN MILLSECONDS*" << endl;
	cout << endl; 
	
	for (int i = startLength; i <= endLength; i += interval) {
		
		cout << "List size " << i << ": " << endl;
		cout << endl;
		allTogether(runs, i);
		calcAverage(q);
		q += 1; 
		
	}

		
	cout << endl; 	
	
	cout << endl; 
	system("pause");
	
	cout << "Okay, the results have been calculated before your eyes. What the computer did was create 50,000 lists of each list length you defined,"  << endl;
	cout << "and timed how long it took to sort using each algorithm. Here's a summary of those times: " << endl; 
	cout << endl; 
	
	for (int i = startLength; i <= endLength; i += interval) { //This loop presents end results for whatever parameters the user set earlier
		
		cout << "Stats for list length " << i << ": " << endl; 
		cout << "------------------------------" << endl;
		cout << "Average basic sort time: " << basicAverages[r] << " milliseconds" << endl;
		cout << "Average refined sort time: " << refinedAverages[r] << " milliseconds" << endl;
		cout << "Refined sort time was faster by: " << integerDifferences[r] << " milliseconds" << endl;
		cout << "That results in refined sort being faster by: " << percentDifferences[r] << " percent" << endl; 
		cout << endl;
		r++;
		
	}
	
	cout << "Thank you for using this super cool feature!" << endl;
	system("pause");
	
	basicAverages.clear();
	refinedAverages.clear();
	integerDifferences.clear();
	percentDifferences.clear();
	
}

vector<List> listHolder; //Holds list for the table

void createSort(int runs) { //Cool display of all the lists being sorted initially
	
	system("cls");
	
	for (int i = 2; i <= (runs + 2); i++) {
		
		List temp(i);
		cout << "List length: " << i << endl; 
	
		for (int q = 0; q < temp.basicList.size(); q++) {
		
			dynamicSpace(0,28);
			cout << temp.unsortedList[q];
			dynamicSpace(temp.unsortedList[q], 28);
			cout << temp.basicList[q];
			dynamicSpace(temp.basicList[q], 28);
			cout << temp.refinedList[q];
			cout << endl; 
			
		}
		
		cout << endl; 
		listHolder.push_back(temp);	
		
	}
	
	system("pause");
	system("cls");
	
}

void showFormulas() { //Simple function to display formulas of comparison calculation
	
	cout << "x = Number of Array Elements" << endl; 
	cout << "FORMULA FOR BASIC COMPARISON COUNT: (x^2) - 2x + 1" << endl; 
	cout << "FORMULA FOR REFINED COMPARISON COUNT: ((x^2) - x) / 2" << endl; 
	cout << "FORMULA FOR COMPARISON DIFFERENCE COUNT: ((x^2) - 3x + 2) / 2" << endl;
	
}

int calcFormulas() { //Calculates comparison count of any integer, though I really should limit it to unsigned integers
	
	int input;
	int basic;
	int refined;
	int difference;
	
	cout << "Input a number: ";
	cin >> input;
	
	basic = (input * input) - (2 * input) + 1;
	refined = ((input * input) - input) / 2;
	difference = ((input * input) - (3 * input) + 2) / 2;
	
	cout << endl << endl << "BASIC COMPARISON COUNT: " << basic << endl; 
	cout << "REFINED COMPARISON COUNT: " << refined << endl;
	cout << "COMPARISON DIFFERENCE: " << difference << endl;
	cout << endl;
	system("pause");
	system("cls");
	
}

void createTable(int runs) {
	
	char command;  //Wish this was a string but switch statements don't take strings, tragically
	int tableSpaces = 27; //Variable for dynamic space parameter
	
	system("cls");
	
	cout << " AMOUNT OF ARRAY ELEMENTS: | BASIC SORT COMPARISON COUNT: | REFINED SORT COMPARISON COUNT: | COMPARISON DIFFERENCE " << endl; //Header of table
	cout << "___________________________________________________________________________________________________________________" << endl;
	

	
	for (int i = 0; i <= (runs); i++) { //loop for generating table lines
		
		cout << i + 2;
		dynamicSpace(i + 2, tableSpaces);
		cout << "| ";
		cout << listHolder[i].basicCount;
		dynamicSpace(listHolder[i].basicCount, tableSpaces); 
		cout << "  | ";
		cout << listHolder[i].refinedCount; 
		dynamicSpace(listHolder[i].refinedCount, tableSpaces); 
		cout << "    | ";
		cout << listHolder[i].comparisonDifference << endl;
		
	}
	
	cout << endl << "Please enter a command. Type \"h\" (no quotations marks) for a list of available commands" << endl; 
	cin >> command; 
	cout << endl; 
	
	switch (command) { //Switch statement for user commands
		
		case 'h': //Case to list possible commands
			
			system("cls");
			cout << "Commands:" << endl; 
			cout << "_______________" << endl; 
			cout << endl; 
			cout << "t" << endl;
			cout << "- begins process to calculate time difference between basic sort and refined sort. Pretty cool, if I say so myself." << endl; 
			cout << endl << "f" << endl;
			cout << "- Displays the formulas used to calculate basic comparison count, refined comparison count, and comparison difference" << endl; 
			cout << endl << "c" << endl;
			cout << "- brings up request to calculate basic comparison count, refined comparison count, and comparison count difference of any integer" << endl; 
			cout << endl << "r" << endl; 
			cout << "- brings up request to reconfigure new table values for new length" << endl; 
			cout << endl << "e" << endl; 
			cout << "- ends the program" << endl; 
			cout << endl;
			system("pause");
			createTable(runs); 
			break; 
			
		case 't': //Case to bring up time comparison functions
			
			system("cls");
			displayTime();
			createTable(runs);
			break;
			
		case 'f': //Case to present formulas
			
			system("cls");
			showFormulas();
			system("pause");
			createTable(runs);
			break;
			
		case 'c': //Case to use formulas to calculate comparison count and difference
			
			system("cls");
			calcFormulas();
			createTable(runs);
			break;
			
		case 'r': //Case to reformat table to new user input table values
			
			int input;
			cout << "How many table values do you want to reconfigure the table to? ";
			cin >> input;
			listHolder.clear();
			createSort(input);
			createTable(input);
			break;
			
		case 'e': //Case to exit
			
			exit(0);
			break;

	}
	
}

int main () {
	
	char yesNo; 
	int tableRuns;
	
	srand(time(0)); //initalize random seed based off time

	cout << "Hello! I'm here to present to you some data comparing the basic bubble sort to the refined bubble sort." << endl; 
	cout << "Are you ready? (y/n) "; 
	cin >> yesNo; 
	
	if (yesNo == 'y') {
		
		cout << endl << "Sweet! How many many table values do you want to generate? (input an integer)" << endl; 
		cin >> tableRuns;
		cout << endl;
		createSort(tableRuns);
		createTable(tableRuns);
		
	} else { 
	
		system("cls");
		cout << "Why'd you initialize this program then! Come back when you're ready." << endl; 
	
	} 
	
	return 0;

}