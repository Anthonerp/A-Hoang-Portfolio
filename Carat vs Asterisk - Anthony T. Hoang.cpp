/*
Author: Anthony Hoang
Date:
Course: COP 1000
Summary: Compare the speeds of using * vs ^ in calculations by taking the time, running the calculation, finding the time difference, and then averaging that over x amount of trials. 
Errors:
Pseudocode:

start
	
	Vector Num asteriskTimes 
	Vector Num caratTimes
	Constant Num power = 3
	Num totalRuns
	Num i
	Num base
	Num asteriskValue
	Num caratValue
	Num asteriskInitial
	Num asteriskPost
	Num caratInitial
	Num caratPost
	Num asteriskChange
	Num caratChange
	Num asteriskAverage
	Num caratAverage
	
	input base
	input totalRuns
	
	for i = 0 to totalRuns
		asteriskInitial = time
		asteriskValue = base * base * base
		asteriskPost = time
		asteriskChange = asteriskPost - asteriskInitial
		add asteriskChange to asteriskTimes
	
	for i = 0 to totalRuns
		caratInitial = time
		caratValue = base^3
		caratPost = time
		caratChange = caratPost - caratInitial
		add caratChange to asteriskTimes 
		
	asteriskAverage = all values in asteriskTimes added together / totalRuns
	caratAverage = all values in caratTimes added together / totalRuns
		
	if asteriskAverage > caratAverage then
		output asterisks are faster than carats by (asteriskAverage - caratAverage) milliseconds on average on this device
	
	if caratAverage > asteriskAverage then
		output carats are faster than asterisks by (caratAverage - asteriskAverage) milliseconds on average on this device
		
	else then
		output something has probably gone wrong
end

*/

#include <iostream>
#include <vector>
#include <numeric> 
#include <chrono>
#include <sys/time.h>
#include <ctime>
#include <cmath>

using namespace std;
using std::chrono::duration_cast; 
using std::chrono::milliseconds;
using std::chrono::seconds;
using std::chrono::system_clock;


int main () {

	vector<int> asteriskTimes; //vectors for creating a list of time differences
	vector<int> caratTimes;
	int totalRuns;
	int base;
	int asteriskValue;
	int caratValue;
	int asteriskChange;
	int caratChange;
	int asteriskTotal;
	int caratTotal;
	float asteriskAverage;
	float caratAverage;
	float percentDifference;
	
	cout << "What will be the base number for this trial? (Keep in mind that that power is 3) "; //inputting what the number being multiplied and the total runs are for averaging
	cin >> base;
	cout << endl << "What will be the trial length (run-throughs)? ";
	cin >> totalRuns;
	cout << "Calculating...";

	for (int i = 0; i < totalRuns - 1; i++) { //loop to calculate asterisk calculation times
		
		auto asteriskInitial = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count(); //code snippet from delftstack.com that basically takes the system clock, asks how long its been since the epoch, and then turns that into a tick count
		
		for (int i = 0; i < 200000000; i++) { //loop to calculate the number 200000000 times, because it kept rounding to zero otherwise
		
			asteriskValue = base * base * base; 
			base += 1; //Added to hopefully make calculations take longer	
		
		}
			
		auto asteriskPost = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
		asteriskChange = asteriskPost - asteriskInitial;	
		
		asteriskTimes.push_back(asteriskChange); //appends time difference to vector

	} 	
	
	for (int i = 0; i < totalRuns - 1; i++) { //loop to calculate carat calculation times
	
		auto caratInitial = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
		
		for (int i = 0; i < 200000000; i++) {
		
			caratValue = pow(base, 3);
			base += 1; 
		
		}		
		
		auto caratPost = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
		caratChange = caratPost - caratInitial;	
		
		caratTimes.push_back(caratChange);
		
	}
	
	asteriskTotal = accumulate(asteriskTimes.begin(), asteriskTimes.end(), 0);
	asteriskAverage = static_cast<float>(asteriskTotal) / static_cast<float>(totalRuns);
	
	caratTotal = accumulate(caratTimes.begin(), caratTimes.end(), 0);
	caratAverage = static_cast<float>(caratTotal) / static_cast<float>(totalRuns); 
	
	percentDifference = (caratAverage - asteriskAverage) / asteriskAverage * 100;
	
	system("cls"); //Displaying the results
	cout << "Results after calculating " << base << " to the 3rd power 200000000 times for " << totalRuns << " runs using asterisks or carats:" << endl;
	cout << "Asterisk average time to calculate: " << asteriskAverage << " milliseconds" << endl;
	cout << "Carat average time to calculate: " << caratAverage << " milliseconds" << endl;
	
	if (asteriskAverage < caratAverage) { //Conditionals for either side being faster
		cout << "Asterisks win! Asterisks are faster than carats by: *** " << caratAverage - asteriskAverage << " milliseconds ***" << endl;
		cout << "Percent Difference: Carats are faster by " << percentDifference << " percent";
	} else if (caratAverage < asteriskAverage) {
		cout << "Carats win! Carats are faster than asterisks by: ^^^ " << asteriskAverage - caratAverage << " millseconds ^^^" << endl;
		cout << "Percent Difference: Carats are faster by " << percentDifference << " percent";
	} else {
		cout << "Something has probably gone wrong, the times are the same";
	}

}

