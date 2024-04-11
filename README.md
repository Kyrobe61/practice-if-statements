# practice-if-statements

Introduction									
The aim of this workout assignment is to practice decision making (conditional if statements). The use of if statements are due to the nature of the problem; that is, you cannot finish this workout assignment without using them.

Description

In this workout assignment exam, you are going to implement a citizenship inquiry system. States grant citizenship through various mechanisms (e.g., birth, marriage and naturalization) with varying details. Your system will be only based on the applicant’s birth conditions. Write a Python program for only two countries, "USA" and "Switzerland", in which an applicant will answer a set of "yes"/"no" questions to find out if they are granted citizenship or not.

For the US, the rules are simple. If the applicant was born in the US or was born abroad to U.S. citizen parent(s). Unlike the US, Switzerland does not grant a child citizenship for being born on Swiss soil. A person is automatically Swiss, if he or she is the child of married parents, at least one of whom is Swiss. The child of an unmarried Swiss woman is also automatically Swiss. If an unmarried father is Swiss (and the mother is a foreigner), the child can have Swiss citizenship as long as the father acknowledges paternity before the child turns legal age.

The program should first ask for the country information. It can be either the "USA" or "Switzerland". Any other entry (even "usa" is invalid) should cause the program to terminate with the appropriate error message ("Invalid entry! Terminating the program."). If the user enters "USA", then your program should first ask the applicant if they were born in the USA or not. If the answer is "yes", then print the appropriate affirmative message ("The applicant is a U.S. citizen."). If the answer is "no", then ask for their parents’ citizenship. If at least one of their parents is a US citizen (i.e. answer is "yes"), then you should print the appropriate affirmative message. Otherwise, print the negative message ("The applicant is not a U.S. citizen.").

If the user enters "Switzerland", then your program should ask whether the applicant’s parents are married. If the answer is "yes", then it should ask whether at least one of the parents is Swiss. If one of the married parents is Swiss (i.e. answer is "yes"), then the applicant will be a Swiss citizen (print "The applicant is a Swiss citizen."). If both married parents are foreign (i.e. answer is "no"), then the applicant will not be a Swiss citizen (print "The applicant is not a Swiss citizen."). If the father and mother are not married, then you should ask whether the unmarried mother is a Swiss citizen. If the answer is "yes", then the applicant will be Swiss. But if the answer is "no", then you should ask whether the unmarried father is Swiss. If the unmarried father is not Swiss like the unmarried mother (if the answer is "no"), then the applicant cannot be a Swiss citizen. However, if the unmarried father is Swiss (if the answer is "yes"), then you should ask whether the unmarried father acknowledges paternity before the applicant turns legal age. If the answer is "yes", then the applicant becomes a Swiss citizen, but if the answer is "no", the applicant will not be a Swiss citizen. Surely, if none of unmarried parents are Swiss, then the applicant will not be a Swiss citizen.

For every answer (except for the country input), your program must validate that the given answer is either "yes" or "no". Any other entry should cause the program to terminate with the appropriate error message (see sample runs). Please note that your inputs should be case insensitive for yes-no answers only, which means that "yes" and "Yes" are the same ("Yes", "YES", "YeS", "yes"  is a valid answer).


Sample Runs
Below, we provide some sample runs of the program that you will develop. The italic and bold phrases are inputs taken from the user. You have to display the required information in the same order and with the same words and characters as below. 


Sample Run 1 
Please enter the country for citizenship inquiry: China
Invalid entry! Terminating the program.

Sample Run 2
Please enter the country for citizenship inquiry: USA
Was the applicant born in the United States or a territory of the United States? no
Was at least one of the applicant's parents a U.S. citizen? yess
Invalid entry! Terminating the program.



Sample Run 3
Please enter the country for citizenship inquiry: USA
Was the applicant born in the United States or a territory of the United States? No
Was at least one of the applicant's parents a U.S. citizen? yes
The applicant is a U.S. citizen.


Sample Run 4
Please enter the country for citizenship inquiry: USA
Was the applicant born in the United States or a territory of the United States? nO
Was at least one of the applicant's parents a U.S. citizen? YES
The applicant is a U.S. citizen.

Sample Run 5
Please enter the country for citizenship inquiry: USA
Was the applicant born in the United States or a territory of the United States? no
Was at least one of the applicant's parents a U.S. citizen? yes
The applicant is a U.S. citizen.

Sample Run 6
Please enter the country for citizenship inquiry: Switzerland
Are the applicant's parents married? no
Is unmarried mother a Swiss citizen? no
Is unmarried father a Swiss citizen? yes
Does unmarried father acknowledge paternity? yes
The applicant is a Swiss citizen.

Sample Run 7
Please enter the country for citizenship inquiry: Switzerland
Are the applicant's parents married? yes
Is one of the parents a Swiss citizen? yes
The applicant is a Swiss citizen.

Sample Run 8
Please enter the country for citizenship inquiry: Switzerland
Are the applicant's parents married? no
Is unmarried mother a Swiss citizen? yea
Invalid entry! Terminating the program.



Sample Run 9 
Please enter the country for citizenship inquiry: usa
Invalid entry! Terminating the program.

Sample Run 10 
Please enter the country for citizenship inquiry: USA
Was the applicant born in the United States or a territory of the United States? no
Was at least one of the applicant's parents a U.S. citizen? no
The applicant is not a U.S. citizen.

Sample Run 11 
Please enter the country for citizenship inquiry: Switzerland
Are the applicant's parents married? yes
Is one of the parents a Swiss citizen? no
The applicant is not a Swiss citizen.

Sample Run 12
Please enter the country for citizenship inquiry: Swiss
Invalid entry! Terminating the program.
