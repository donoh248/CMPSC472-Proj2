import difflib
import webbrowser

import websites

drug_type = ""
drug_subject = ""
drug_purpose = ""
urgent = True
inpt = ""

weed = ["Weed", "Pot", "Grass", "Herb", "Mary Jane", "Marijuana"]
cocaine = ["Cocaine", "Coke", "Blow", "Snow", "Crack"]
heroin = ["Heroin", "Smack", "Junk", "Brown sugar", "Horse", "H"]
methamphetamine = ["Meth","Methamphetamine", "Crystal", "Ice", "Glass"]
drug_lists = {"Weed": weed, "Cocaine": cocaine, "Heroin": heroin, "Methamphetamine": methamphetamine}
purposes = ["Educational", "Personal", "Legal"]
subjectsE = ["General Info", "History", "Health Effects" ]
subjectsP = ["Treatment", "Intervention", "Coping"]
subjectsL = ["Legal Consequences", "Rehabilitation", "State Law"]


def find_drug():
  drug_lists = {
    "Weed": weed,
    "Cocaine": cocaine,
    "Heroin": heroin,
    "Methamphetamine": methamphetamine
    }

  confirm = False
  while not confirm:
    inpt = input("Enter the drug name: ")
    match_found = False

    for drug_name, drug_list in drug_lists.items():
      matches = difflib.get_close_matches(inpt, drug_list)
      if matches:
        match_found = True
        print(f"Did you mean {matches[0]} for {drug_name}? (Y/N):")
        CF = input("")
        if CF.lower() == "Y".lower():
          return drug_name
    if not match_found:
      print("Invalid input. Please try again.") #Finds drug type

def find_purpose():
  confirm = False
  while not confirm:
    print("purposes for information are:\nEducational\nPersonal\nLegal")
    inpt = input("What is the purpose of the research you are looking for: ")
    match_found = False
    for purpose in purposes:
      matches = difflib.get_close_matches(inpt, purposes)
      if matches:
        match_found = True
        print("Did you mean", matches[0], "(Y/N):")
        CF = input("")
        if CF.lower() == "Y".lower():
          if matches[0] == "Educational":
            return find_subject(subjectsE)
          elif matches[0] == "Personal":
            return find_subject(subjectsP)
          elif matches[0] == "Legal":
            return find_subject(subjectsL)
    if not match_found:
      print("Invalid input. Please try again.") #finds purpose of research
      
def find_subject(subj_list):
  confirm = False
  while not confirm:
    print("Subjects are:")
    for subject in subj_list:
      print(subject)
    inpt = input("Enter one of the following subjects you are looking for info on: ")
    match_found = False
    for subject in subj_list:
      matches = difflib.get_close_matches(inpt, subj_list)
      if matches and matches[0] == subject:
        match_found = True
        print("Did you mean", matches[0], "(Y/N):")
        CF = input("")
        if CF.lower() == "Y".lower():
          return subject
    if not match_found:
      print("Invalid input. Please try again.") #Finds subject based on purpose

def find_site(drug,info):
  if drug == "Weed":
    if info == "General":
      return websites.WeedE1
    if info == "History":
      return websites.WeedE2
    if info == "Health Effects":
      return websites.WeedE3
    if info == "Treatment":
      return websites.WeedP1
    if info == "Intervention":
      return websites.WeedP2
    if info == "Coping":
      return websites.WeedP3
    if info == "Legal Consequences":
      return websites.WeedL1
    if info == "Rehabilitation":
      return websites.WeedL2
    if info == "State Law":
      return websites.WeedL3
  elif drug == "Cocaine":
    if info == "General":
      return websites.CocaineE1
    if info == "History":
      return websites.CocaineE2
    if info == "Health Effects":
      return websites.CocaineE3
    if info == "Treatment":
      return websites.CocaineP1
    if info == "Intervention":
      return websites.CocaineP2
    if info == "Coping":
      return websites.CocaineP3
    if info == "Legal Consequences":
      return websites.CocaineL1
    if info == "Rehabilitation":
      return websites.CocaineL2
    if info == "State Law":
      return websites.CocaineL3
  elif drug == "Heroin":
    if info == "General":
      return websites.HeroinE1
    if info == "History":
      return websites.HeroinE2
    if info == "Health Effects":
      return websites.HeroinE3
    if info == "Treatment":
      return websites.HeroinP1
    if info == "Intervention":
      return websites.HeroinP2
    if info == "Coping":
      return websites.HeroinP3
    if info == "Legal Consequences":
      return websites.HeroinL1
    if info == "Rehabilitation":
      return websites.HeroinL2
    if info == "State Law":
      return websites.HeroinL3
  elif drug == "Methamphetamine":
    if info == "General":
      return websites.MethE1
    if info == "History":
      return websites.MethE2
    if info == "Health Effects":
      return websites.MethE3
    if info == "Treatment":
      return websites.MethP1
    if info == "Intervention":
      return websites.MethP2
    if info == "Coping":
      return websites.MethP3
    if info == "Legal Consequences":
      return websites.MethL1
    if info == "Rehabilitation":
      return websites.MethL2
    if info == "State Law":
      return websites.MethL3 #Finds website based on user inputs of drug and subject

drug_type = find_drug()
drug_info = find_purpose()

print("So you are looking for", drug_info, "on", drug_type)
url = find_site(drug_type, drug_info)
webbrowser.open(url) #Make sure any website open by this program is closed before running!
