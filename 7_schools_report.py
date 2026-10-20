import json
"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:
Oklahoma State University-Main Campus
Purdue University-Main Campus
Rutgers University-New Brunswick
Southern Methodist University
Temple University
Texas A & M University-College Station
Texas Christian University
Texas Tech University
The Pennsylvania State University
The University of Alabama
The University of Tennessee-Knoxville
The University of Texas at Austin
Tulane University of Louisiana
United States Naval Academy
University of Arkansas
University of Central Florida
University of Cincinnati-Main Campus
University of Florida
University of Florida-Online
University of Georgia
University of Houston
University of Illinois Urbana-Champaign
University of Iowa
University of Kansas
University of Kentucky
University of Maryland-College Park
University of Memphis
University of Michigan-Ann Arbor
University of Minnesota-Twin Cities
University of Mississippi
University of Missouri-Columbia
University of Nebraska-Lincoln
University of Oklahoma-Norman Campus
University of South Carolina-Columbia
University of South Florida
University of Wisconsin-Madison
Vanderbilt University
West Virginia University

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"

"""
#Display report for all universities that have a graduation rate for Women over 75%
with open("school_data.json", "r") as file:
    schools = json.load(file)

for school in schools:
    name = school["instnm"]
    women = school["Percent of total enrollment that are women (DRVEF2020)"]

    if women > 75:
        print(name)

print()
print()
#Display report for all universities that have a total price for in-state students living off campus over $60,000
for school in schools:
    name = school["instnm"]
    price = int(school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])

    if price > 60000:
        print(name)






conference_codes = [372,108,107,130]

for school in schools:
    name = school["instnm"]
    conference = school["NCAA"]["NAIA conference number football (IC2020)"]

    if conference in conference_codes:
        print(name)