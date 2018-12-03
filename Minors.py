import xlrd
import xlsxwriter
import os 
from os import walk
from collections import OrderedDict

minor_titles = ['Accounting', 'Aeronautics', 'Airline Flight Attendant', 'American Sign Language', 
    'Apologetics and Cultural Engagement', 'Biblical Greek', 'Biblical Languages', 'Biblical Studies', 
    'Biology', 'Biomedical Sciences', 'Business', 'Camp and Outdoor Adventure Leadership', 'Chemistry', 
    'Chinese', 'Cinematic Arts', 'Coaching', 'Computer Science', 'Creative Writing', 'Criminal Justice', 
    'Digital Media - Audio', 'Digital Media - Editing', 'Digital Media - Performance', 'Digital Media - Video', 
    'Digital Media - Writing for Digital Media', 'English', 'Expositional Preaching', 'French', 'German', 
    'Global Studies', 'Government', 'Graphic Design', 'Health Promotion', 'History', 'Information Security', 
    'Information Systems', 'International Relations**', 'International Studies', 'Journalism', 'Kinesiology', 
    'Linguistics', 'Mathematics', 'Military History', 'Military Leadership*', 'Music- Brass, Woodwind or Percussion**', 
    'Music- Liberal Arts**', 'Old Testament', 
    'Pastoral Leadership', 'Philosophy', 'Photography', 'Politics and Policy **', 'Psychology', 'Sociology', 'Spanish', 
    'Special Education**', 'Sport Management', 'Sport Outreach', 'Strategic and Intelligence Studies', 'Studio Art', 
    'Technical Studies', 'Theatre Arts', 'Theology', 'Western Legal Traditions**', 'Women\'s Leadership', 'Writing', 
    'Youth Ministries']

class_abbrs = {
    'ACCT', 'AIRS', 'AMOA', 'APOL', 'ARTS', 'ASLI', 'ATHL', 'ATTR', 'AVIA', 'AVMT',
    'AVMX', 'BCHM', 'BIBL', 'BIOL', 'BUSI', 'BWVW', 'CARA', 'CARP', 'CCOU', 'CESL',
    'CFRE', 'CGRM', 'CHEM', 'CHHI', 'CHIN', 'CHMN', 'CHND', 'CINE', 'CJUS', 'CLED',
    'CLST', 'COAL', 'COMS', 'COSP', 'CRFT', 'CRIS', 'CRST', 'CSIS', 'CSMA', 'CSPA',
    'CSTU', 'DBFA', 'DBMF', 'DBPC', 'DIGI', 'DMCA', 'ECON', 'EDSP', 'EDUC', 'ELIL',
    'ELIO', 'ELTC', 'ENGC', 'ENGE', 'ENGI', 'ENGL', 'ENGM', 'ENGR', 'ENVR', 'ESLP',
    'ESOL', 'ETHC', 'ETHM', 'EVAN', 'EXSC', 'FACS', 'FIRE', 'FNLT', 'FREN', 'FRSM',
    'GBST', 'GEED', 'GEOG', 'GLST', 'GOVT', 'GREK', 'GRMN', 'HBRW', 'HIEU', 'HIST',
    'HIUS', 'HIWD', 'HLTH', 'HONR', 'HSER', 'HVAC', 'INDS', 'INFO', 'INFT', 'INQR',
    'JOUR', 'KINE', 'LIFC', 'LING', 'MATH', 'MENT', 'MILT', 'MISC', 'MLAN', 'MUSC',
    'NASC', 'NURS', 'PADM', 'PHED', 'PHIL', 'PHSC', 'PHYS', 'PLED', 'PLMB', 'PLST',
    'PRTH', 'PSYC', 'RLGN', 'RLST', 'RSCH', 'RUSS', 'SCOM', 'SMGT', 'SOCI', 'SOWK',
    'SPAN', 'STCO', 'STEM', 'TESL', 'THEA', 'THEO', 'UNIV', 'WELD', 'WLED', 'WMUS',
    'WRIT', 'WRSP', 'YOUT'
    }
def is_int(value):
    try:
        int(value)
        return True
    except:
        return False


minor = []
creditsForMinor = ""
creditsForClass = ""
bitOperator = 0
with open("Untitled.txt", "r") as text_file:
    lines = text_file.readlines()
    for i, line in enumerate(lines):
        # Look for class
        if any(abbr in line for abbr in class_abbrs) and not ('or ' in line):                
            course = line[0:8]
            if (len(lines) >(i + 2)):
                creditsForClass = lines[i + 2]
            #print (course)
        # Look for 'or' followed by a class
        elif ('or ' in line and any(abbr in line for abbr in class_abbrs)):
            bitOperator = 1
        elif ('Choose' in line)and ('level' in line):
            bitOperator = 1
            line = line.replace('\n', '')
            print ( line)
        elif any(titles in line for titles in minor_titles) and ('level)' not in line):
            line = line.replace('\n', '')
            if(line in minor_titles):
                minor_titles.remove(line)
                minor = line
                creditsForMinor = lines[i + 1]
                #print (minor)
                #print ('--------------------')             