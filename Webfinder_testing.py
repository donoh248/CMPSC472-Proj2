import difflib
import webbrowser
import websites

# Define drug lists
drug_lists = {
    "Weed": ["Weed", "Pot", "Grass", "Herb", "Mary Jane", "Marijuana"],
    "Cocaine": ["Cocaine", "Coke", "Blow", "Snow", "Crack"],
    "Heroin": ["Heroin", "Smack", "Junk", "Brown sugar", "Horse", "H"],
    "Methamphetamine": ["Meth", "Methamphetamine", "Crystal", "Ice", "Glass"]
}

# Define purposes and subjects
purposes = ["Educational", "Personal", "Legal"]
subjects = {
    "Educational": ["General Info", "History", "Health Effects"],
    "Personal": ["Treatment", "Intervention", "Coping"],
    "Legal": ["Legal Consequences", "Rehabilitation", "State Law"]
}

# Function to find drug type
def find_drug():
    while True:
        inpt = input("Enter a drug name to continue: ")
        for drug_name, drug_list in drug_lists.items():
            matches = difflib.get_close_matches(inpt, drug_list)
            if matches:
                confirm = input(f"Did you mean {matches[0]} for {drug_name}? (Y/N): ").lower()
                if confirm == "y":
                    return drug_name
        print("Invalid input. Please try again.")

# Function to find purpose
def find_purpose():
    while True:
        print("Purposes for information are:")
        for purpose in purposes:
            print(purpose)
        inpt = input("What is the purpose of the research you are looking for: ")
        matches = difflib.get_close_matches(inpt, purposes)
        if matches:
            confirm = input(f"Did you mean {matches[0]}? (Y/N): ").lower()
            if confirm == "y":
                return matches[0]
        print("Invalid input. Please try again.")

# Function to find subject
def find_subject(subj_list):
    while True:
        print("Subjects are:")
        for subject in subj_list:
            print(subject)
        inpt = input("Enter one of the following subjects you are looking for info on: ")
        matches = difflib.get_close_matches(inpt, subj_list)
        if matches:
            confirm = input(f"Did you mean {matches[0]}? (Y/N): ").lower()
            if confirm == "y":
                return matches[0]
        print("Invalid input. Please try again.")

# Function to find website
def find_site(drug, info):
    website_mapping = {
        "Weed": {
            "General Info": websites.WeedE1,
            "History": websites.WeedE2,
            "Health Effects": websites.WeedE3,
            "Treatment": websites.WeedP1,
            "Intervention": websites.WeedP2,
            "Coping": websites.WeedP3,
            "Legal Consequences": websites.WeedL1,
            "Rehabilitation": websites.WeedL2,
            "State Law": websites.WeedL3
        },
        "Cocaine": {
            "General Info": websites.CocaineE1,
            "History": websites.CocaineE2,
            "Health Effects": websites.CocaineE3,
            "Treatment": websites.CocaineP1,
            "Intervention": websites.CocaineP2,
            "Coping": websites.CocaineP3,
            "Legal Consequences": websites.CocaineL1,
            "Rehabilitation": websites.CocaineL2,
            "State Law": websites.CocaineL3
        },
        "Heroin": {
            "General Info": websites.HeroinE1,
            "History": websites.HeroinE2,
            "Health Effects": websites.HeroinE3,
            "Treatment": websites.HeroinP1,
            "Intervention": websites.HeroinP2,
            "Coping": websites.HeroinP3,
            "Legal Consequences": websites.HeroinL1,
            "Rehabilitation": websites.HeroinL2,
            "State Law": websites.HeroinL3
        },
        "Methamphetamine": {
            "General Info": websites.MethE1,
            "History": websites.MethE2,
            "Health Effects": websites.MethE3,
            "Treatment": websites.MethP1,
            "Intervention": websites.MethP2,
            "Coping": websites.MethP3,
            "Legal Consequences": websites.MethL1,
            "Rehabilitation": websites.MethL2,
            "State Law": websites.MethL3
        }
    }
    
    if drug in website_mapping and info in website_mapping[drug]:
        return website_mapping[drug][info]

# Main program
drug_type = find_drug()
drug_purpose = find_purpose()
drug_subject = find_subject(subjects[drug_purpose])

print("You are looking for", drug_subject, "information on", drug_type)
url = find_site(drug_type, drug_subject)
if url:
    webbrowser.open(url)
else:
    print("Website not found for the specified drug and subject.")