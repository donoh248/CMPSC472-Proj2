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

As you can see, based on the information inputted by the user, a specific link is given to them from the program. When running this program normally the link would open up on the user's browser in another tab. Since the main thing being tested is the code, a minor change was added to show which link was being open from the program

## Discussion and Conclusions
This project exemplifies the practical application of operating system concepts within a computer science context, showcasing the integration of processes, data management, and resource allocation. Through techniques like input parsing and similarity matching, the code efficiently navigates through a complex array of drug-related information, echoing the challenges faced in operating system design regarding process handling and resource management. By organizing the code into modular functions and utilizing dictionaries for data storage, it not only enhances readability and scalability but also reflects the structured architecture inherent in operating systems. These principles, such as modularity, abstraction, and resource management, are pivotal in simplifying complexities and providing users with a straightforward interface to access drug information.

The project's integration of web scraping underscores the interconnected nature of modern computing environments and the importance of inter-process communication in distributed systems. By retrieving information from external sources, it highlights the reliance on diverse resources for information retrieval and processing, mirroring the real-world challenges of data aggregation and dissemination. The use of different types of websites showcases the versatility of the script in retrieving diverse information. This approach not only demonstrates the project's adaptability but also emphasizes the interdisciplinary nature of computer science, where knowledge from operating systems intersects with web technologies to create robust solutions for information retrieval and decision-making processes.

To further enhance the project's utility, considerations for scalability and extensibility in the design are imperative. Refactoring the code to support dynamic updates to drug lists and website mappings, as well as implementing modular design patterns, would facilitate easier maintenance and future expansions. Additionally, conducting thorough testing across various input scenarios and edge cases would help identify and address any unforeseen issues, ensuring the program's reliability and robustness in diverse usage scenarios. By continually refining the project based on these principles, it can serve as a model for the practical application of operating system concepts, facilitating efficient information retrieval and decision-making processes while adapting to evolving needs in the field of computer science.
