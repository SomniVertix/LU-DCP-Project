import xlrd
import xlsxwriter
import os 
from os import walk
from collections import OrderedDict
Title = ['Bachelor of ', 'Associate of ']

# Bold & underlined words
class_maincategories = [
    'CORE COMPETENCY REQUIREMENTS', 'MAJOR', 
    'Christian Life and Thought', 'CHRISTIAN LIFE AND THOUGHT', 'Christian Life & Thought', 'CHRISTIAN LIFE & THOUGHT',
    'Directed Courses', 'DIRECTED COURSES', 
    'Free Electives', 'FREE ELECTIVES', 
    'LIBERAL ARTS FOCUS']

# Underlined words
class_subcategories = {
    'Communication','Mathematics, Science, & Technology', 'Math, Science and Technology', 'Math, Science & Technology',
    'Information Literacy', 'INFORMATION LITERACY', 'Critical Thinking', 'CRITICAL THINKING', 
    'Quantitative Studies', 'QUANTITATIVE STUDIES', 'Core', 'Cognate', 'Concentration'
    }

# Class Abbreviations
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

# Class Electives
## History, Technical and Technology Electives not found in LU Listing
class_electives = [
    'Communications', 'Math', 'Natural Science', 
    'Composition','Information Literacy', 'Literature', 'Philosophy',
    'Social Science', 'Cultural Studies','Non-Religion Majors', 'Religion Majors',
    'Technology', 'Tech.', 'Tech. ', 'Language', 'Early American', 'Modern American',
    'Early American', 'Early Europe', 'General Education', 'World History', 'Modern Europe',
    'History'
    ] #12

def ExcelLookup(write_doc, degreeTitle, index, rowCount, most_recent_maincat,most_recent_subcat):
    excel_filename = "Lookup.xlsx"
    os.chdir('D:/Python Projects/Automate PDFs')
    book = xlrd.open_workbook(excel_filename)
    sheet = book.sheet_by_index(1)
    if (class_electives[index] in sheet.col_values(0,0)):
        sheet = book.sheet_by_index(0)
        for i in range(1, sheet.nrows):
            if (class_electives[index] in sheet.cell(i, 1).value):
                write_doc.write(rowCount, 0, degreeTitle)
                write_doc.write(rowCount, 1, sheet.cell(i, 2).value)
                write_doc.write(rowCount, 2, sheet.cell(i, 3).value)
                write_doc.write(rowCount, 3, most_recent_maincat)
                write_doc.write(rowCount, 4, most_recent_subcat)
                write_doc.write(rowCount, 5, 1)
                write_doc.write(rowCount, 7, class_electives[index])
                rowCount = rowCount + 1
        sheet = book.sheet_by_index(1)    
    os.chdir(r'Output/')
    return rowCount

# Preliminary file setup
def PreliminarySetup():
    filenames = []
    for dirpath, dirname, filename in walk('Output/'):
        filenames.extend(filename)
        break
    # Excel file setup
    excel_filename = "2015-2016 DCPsA"
    workbook = xlsxwriter.Workbook(excel_filename + ".xlsx")
    worksheet = workbook.add_worksheet(excel_filename)
    # Headers
    worksheet.write(0,0, 'Degree')
    worksheet.write(0,1, 'ClassAbbr')
    worksheet.write(0,2, 'ClassNum')
    worksheet.write(0,3, 'Class Notes')
    worksheet.write(0,4, 'Main Category')
    worksheet.write(0,5, 'Main Category Notes')
    worksheet.write(0,6, 'Sub Category')
    worksheet.write(0,7, 'Sub Category Notes')
    worksheet.write(0,8, 'Alternative')
    worksheet.write(0,9, 'Electives')
    return filenames, filename, workbook, worksheet, excel_filename

def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

def get_notes(lines):
    NOTES = OrderedDict()
    notes = 'NOTES'
    index = 0
    key = 0
    for i, line in enumerate(lines):
        if notes in line:
            index = i + 1
    if index != 0:
        for i in range(index, len(lines)):
            first_line = lines[i].rstrip('\n')
            if key < 9:
                if is_int(first_line[0]):
                    key = int(first_line[0])
                    final = first_line[1:]
            else:
                if is_int(first_line[0:2]):
                    key = int(first_line[0:2])
                    final = first_line[2:]
            if i + 1 < len(lines):
                second_line = lines[i + 1].rstrip('\n')
                if not is_int(second_line[0]):
                    final = (final + ' ' + second_line)
            NOTES[key] = final
    return NOTES

filenames, filename, workbook, worksheet, excel_filename = PreliminarySetup()
os.chdir(r'Output/')
rowCount = 1
columnCount = 1
maincatNotes = ""
subcatNotes = ""
classNotes = ""
for individual_file in filenames:
    with open(individual_file, "r") as text_file:
        print ('New DCP: ', individual_file)
        print ('------------------------------')
        
        lines = text_file.readlines()
        Notes = get_notes(lines)

        for i, line in enumerate(lines):
            # Look for Degree Name
            if any(mainTitle in line for mainTitle in Title ) and (i < 4 ): 
                degreeTitle = line.replace('\n', '')
                if ('Cognate' in lines[i + 1]) or ('Concentration'in lines[i + 1]) :
                    degreeTitle = degreeTitle + " " + lines[i + 1]

            # Look for class maincategories
            if any(maincat in line for maincat in class_maincategories):
                if (')' in line):
                    maincatNotes = ""
                    subcatNotes = ""
                    most_recent_subcat = ""
                    line = line.replace('\n', '')
                    most_recent_maincat = line
                    mainWords = line.split('(')
                    for key, value in reversed(list(Notes.items())):
                        if (str(key) in mainWords[0]):
                            maincatNotes = maincatNotes + " " +  str(key) + ";"
                            most_recent_maincat = mainWords[0].replace(str(key), '')
                            mainWords[0] = mainWords[0].replace(str(key), '')
                    if (("(" + mainWords[1]) not in most_recent_maincat):
                        most_recent_maincat = most_recent_maincat + "(" + mainWords[1]

            # Look for class subcategories
            if any(subcat in line for subcat in class_subcategories) or (' hours)' in line and not any(maincat in line for maincat in class_maincategories)):
                if (')' in line):
                    subcatNotes = ""
                    line = line.replace('\n', '')
                    most_recent_subcat = line
                    subWords = line.split('(')
                    for key, value in reversed(list(Notes.items())):
                        if (str(key) in subWords[0]):
                            subcatNotes = subcatNotes + " " +  str(key) + ";"
                            most_recent_subcat = subWords[0].replace(str(key), '')
                            subWords[0] = subWords[0].replace(str(key), '')
                    if (("(" + subWords[1]) not in most_recent_subcat):
                        most_recent_subcat = most_recent_subcat + "(" + subWords[1]

            # Look for class
            if any(abbr in line for abbr in class_abbrs):                
                if (len(line) <=10):
                    if (' ' in line) and ('.' not in line):
                        line = line.replace('\n', '')
                        course = line.split(' ')
                        for key, value in reversed(list(Notes.items())):
                            if (str(key) in lines[i + 1].replace('\n', '')):
                                classNotes = classNotes + " " +  str(key) + " " + value + ";"
                                lines[i + 1] = lines[i + 1].replace(str(key), '')
                        worksheet.write(rowCount, 0, degreeTitle)
                        worksheet.write(rowCount, 1, course[0])
                        if (course[1] != ''):
                            worksheet.write(rowCount, 2, int(course[1]))
                        else:
                            worksheet.write(rowCount, 2, course[1])
                        worksheet.write(rowCount, 3, classNotes)
                        worksheet.write(rowCount, 4, most_recent_maincat)
                        worksheet.write(rowCount, 5, maincatNotes)
                        worksheet.write(rowCount, 6, most_recent_subcat)
                        worksheet.write(rowCount, 7, subcatNotes)
                        worksheet.write(rowCount, 8, 0)
                        rowCount = rowCount + 1
                        classNotes = ""
                    else:
                        for key, value in reversed(list(Notes.items())):
                            if (str(key) in lines[i + 1].replace('\n', '')):
                                classNotes = classNotes + " " +  str(key) + " " + value + ";"
                        worksheet.write(rowCount, 0, degreeTitle)
                        worksheet.write(rowCount, 1, line)
                        worksheet.write(rowCount, 3, classNotes)
                        worksheet.write(rowCount, 4, most_recent_maincat)
                        worksheet.write(rowCount, 5, maincatNotes)
                        worksheet.write(rowCount, 6, most_recent_subcat)
                        worksheet.write(rowCount, 7, subcatNotes)
                        worksheet.write(rowCount, 8, 0)
                        rowCount = rowCount + 1
                        classNotes = ""

            # Look for 'or' followed by a class
            if ('or ' in line and any(abbr in line for abbr in class_abbrs)):
                if(len(line) <= 21) and ('.' not in line):
                    line = line.replace('\n', '')
                    line = line.replace('or ','')
                    segments = line.split(' ')
                    worksheet.write(rowCount - 1, 8, 1)
                    worksheet.write(rowCount, 0, degreeTitle)
                    worksheet.write(rowCount, 1, segments[0])
                    worksheet.write(rowCount, 2, int(segments[1]))
                    worksheet.write(rowCount, 3, classNotes)
                    worksheet.write(rowCount, 4, most_recent_maincat)
                    worksheet.write(rowCount, 5, maincatNotes)
                    worksheet.write(rowCount, 6, most_recent_subcat)
                    worksheet.write(rowCount, 7, subcatNotes)
                    worksheet.write(rowCount, 8, 1)
                    rowCount = rowCount + 1

            ### Case for 'OR' 

            # Look for Class Electives
            if (('Elective' or 'ELECTIVE' or 'Competency') in line):
                if (')' not in line):
                    if (any(elec in line for elec in class_electives) or (len(line.replace('Elective', '')) <=25)):
                        
                        line = line.replace('\n', '')
                        if (', ' in line):
                            line = line.replace(' or', '')
                            electives = line.split(',')
                            for elective in electives:
                                text = ""
                                if (elective[0] == " "):
                                    elective = elective[1:]
                                elective = elective.replace(' Elective', '')
                                for i in elective:
                                    if not i.isdigit():
                                        text = text + i
                                elective = text
                                if elective != '' and (class_electives.index(elective) == 12 or class_electives.index(elective) == 13) :
                                    worksheet.write(rowCount, 0, degreeTitle)
                                    worksheet.write(rowCount, 3, classNotes)
                                    worksheet.write(rowCount, 4, most_recent_maincat)
                                    worksheet.write(rowCount, 5, maincatNotes)
                                    worksheet.write(rowCount, 6, most_recent_subcat)
                                    worksheet.write(rowCount, 7, subcatNotes)
                                    worksheet.write(rowCount, 8, 0)
                                    worksheet.write(rowCount, 9, class_electives[11])
                                    rowCount = rowCount + 1
                                else:
                                    worksheet.write(rowCount, 0, degreeTitle)
                                    worksheet.write(rowCount, 3, classNotes)
                                    worksheet.write(rowCount, 4, most_recent_maincat)
                                    worksheet.write(rowCount, 5, maincatNotes)
                                    worksheet.write(rowCount, 6, most_recent_subcat)
                                    worksheet.write(rowCount, 7, subcatNotes)
                                    worksheet.write(rowCount, 8, 0)
                                    worksheet.write(rowCount, 9, elective)
                                    rowCount = rowCount + 1
                        else:
                            line = line.replace('\n','')
                            line = line.replace(' Elective','')
                            worksheet.write(rowCount, 0, degreeTitle)
                            worksheet.write(rowCount, 3, classNotes)
                            worksheet.write(rowCount, 4, most_recent_maincat)
                            worksheet.write(rowCount, 5, maincatNotes)
                            worksheet.write(rowCount, 6, most_recent_subcat)
                            worksheet.write(rowCount, 7, subcatNotes)
                            worksheet.write(rowCount, 8, 0)
                            worksheet.write(rowCount, 9, line)
                            rowCount = rowCount + 1
                    
workbook.close()