# CMPSC472-Proj2
CMPSC472 Project 2 for Spring 2024 by Zachary Whitaker and Donovan Biedermann

## Project goals
The main goal of this project is to create a program using material we learned in class to address drug abuse. We aim to make the user more aware of the medical facts of each major abusive drug and how to effects someone so that in the future, symptoms of addiction or abuse can be easier to identify and treatment can be administered faster.

## Significance of the project
The significance of this project is the access to a collective knowledgebase to quickly identify and learn about various drugs. This application has compiled a substantial list of websites on drug information for the user to search and educate themselves on.

## Installation and usage instructions
- To install this code, simply type in the terminal: <code>git clone https://github.com/donoh248/CMPSC472-Proj2.git</code>
- To run this CLI application, type in the terminal: <code>python Webfinder.py</code> and the application will open.

## Code structure
### Structure of Code:
<code>
CMPSC472-PROJ2
 ∟ Webfinder.py
 ∟ websites.py
</code>

- Webfinder.py is the main program logic for the application.
- websites.py contains the list of sources for drug information. This is used as a dependency for Webfinder.py

## List of functionalities and test results
The program contains 4 functions:
- **find_drugs**- Asks what type of drug you are looking for info on. The input scans a dictionary of drugs, which in turn contains lists of different names of the drugs. The scan runs through the dictionary and uses get_close_matches to find the closest match to the input. When the user confirms it it stores that string as the drug_type to be used for later
- **find_purpose**- Asks about the purpose of the research: Educational, Personal, or Legal. Follows a similar pattern of using get_close_matches to find and confirm the user's choice. The program then takes the purpose and the appropriate list (i.e. educational purpose uses the list of educational subjects) and runs it through the find_subject function
- **find_subject**- Asks what type of information you are looking for based on your subject. After confirming what subject the user is looking for, it return the subject and stores it as drug_info
- **find_site**- Function uses drug_type and drug_info from previous functions and finds the required website based on the strings given. The websites used are stored into websites.py. It then stores the website as a string called url. This url is then used in a webbrowser.open() code to open the url and give the user the information they are looking for.

### Test result images
**Test 1 running the code in a basic standard case, having all inputs spelled correctly**
![Test 1](https://github.com/donoh248/CMPSC472-Proj2/blob/main/CMPSC472%20Project2%20Image1.png)

**Test 2 running the code and demonstratiting how the program scans for all possible matches the are close to the user's input. Also shows how the input does not need to be fully inputted as seen when asking for the purpose**
![Test 2](https://github.com/donoh248/CMPSC472-Proj2/blob/main/CMPSC472%20Project2%20Image2.png)

**Test 3 running the code and denying a choice that demonstrates the loop until a definite answer has been inputted. Just like Test 2 shows how the input does not need to be fully complete**
![Test 3](https://github.com/donoh248/CMPSC472-Proj2/blob/main/CMPSC472%20Project2%20Image3.png)

## Discussion and Conclusions

