from selenium import webdriver
import xlsxwriter

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

excel_filename = "Class Listing"
workbook = xlsxwriter.Workbook( excel_filename + ".xlsx")
worksheet = workbook.add_worksheet(excel_filename)
# Headers
worksheet.write(0,0, 'Course ID')
worksheet.write(0,1, 'Class Abbr')
worksheet.write(0,2, 'Class Number')
worksheet.write(0,3, 'Course Title')
worksheet.write(0,4, 'Description')
worksheet.write(0,5, 'Prereqs/Coreqs')
worksheet.write(0,6, 'Credits')
worksheet.write(0,7, 'Notes')
worksheet.write(0,8, 'Is Online')
worksheet.write(0,9, 'Is Residential')


driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
driver.get('https://www.liberty.edu/index.cfm?PID=19959&CatID=31&action=search')
element = driver.find_element_by_name('prefix')
all_options = element.find_elements_by_tag_name("option")
courseID = 1
for i in range(1, len(all_options)):
    if (i <= 5):
        # Choose Prefix
        driver.implicitly_wait(5)
        all_options[i].click()
        # Assign and click Submit
        submit_button = driver.find_element_by_name("submit")
        submit_button.click()
        # Find all <li> elements
        listing = driver.find_elements_by_tag_name("li")
        for indiv_list in listing:
            text = indiv_list.text 
            # Find all <li> elements that have a class abbreviation in them
            if any(abbr in text for abbr in class_abbrs):
                # Open up the link and wait for the javascript to open the div underneath
                indiv_list.click()
                driver.implicitly_wait(5)
                # Use the ID in the <li> to find the corresponding Div
                detailNumber = indiv_list.get_property("id")
                classInfoDiv = driver.find_element_by_id("detail" + detailNumber)
                # In that Div, find all <p> inside
                classInfoPara = classInfoDiv.find_elements_by_tag_name("p")
                driver.implicitly_wait(5)

                # Printing: CourseID, Class Abbr, Class Num, Course Name, Availability (Online & Residential),
                # Description, Prereqs/Coreqs, Credits, and Notes 
                print ('New Class: ',indiv_list.text)
                course = indiv_list.text.split(' - ')
                courseTitle = course[1]
                courseAbbrAndNum = course[0].split(' ')
                IsOnline=IsResidential=False
                Description=PreCoreqs=Credits=Notes = ""
                for para in classInfoPara:
                    if (para.text != "" and para.text != "  "):
                        # Setting Notes
                        if ("Note:" in para.text):
                            Notes = para.text.replace('Note:', '')
                        
                        # Setting Prereqs/Coreqs
                        elif ("Prerequisites:" in para.text or "Corequisites:" in para.text):
                            PreCoreqs = para.text.replace('\n', ' ')
                            ### Set up AND/OR configurations writing to new file
                            ### Set up (Minimum grade of '') and (minimum grade of '') configurations
                            ### Decide on format of excel file
                            PreCoreqs = PreCoreqs.replace('Prerequisites: ', 'P:')
                            PreCoreqs = PreCoreqs.replace('Corequisites: ', 'C:')
                            PreCoreqs = PreCoreqs.replace('P:taken concurrent with ', 'C:') 
                        
                        # Setting Credits
                        elif("Credits:" in para.text):
                            Credits = para.text.replace('\n', '')
                            Credits = Credits.replace('Credits: ', '')
                            Credits = Credits.replace(' to ', '-')

                        # Setting Availability
                        elif(("This course is " in para.text or ("THIS COURSE IS " in para.text)) and 
                            ("online" in para.text or 
                            "ONLINE" in para.text or
                            "residentially" in para.text or 
                            "residential" in para.text) and len(para.text) < 57):
                            if ("online" in para.text or "ONLINE" in para.text):
                                IsOnline = True
                            if ("residential" in para.text or "residentially" in para.text):
                                IsResidential = True

                        # Setting Description
                        elif("View on Separate Page" not in para.text):
                            Description = para.text
                worksheet.write(courseID,0, courseID)
                worksheet.write(courseID,1, courseAbbrAndNum[0])
                worksheet.write(courseID,2, courseAbbrAndNum[1])
                worksheet.write(courseID,3, courseTitle)
                worksheet.write(courseID,4, Description)
                worksheet.write(courseID,5, PreCoreqs)
                worksheet.write(courseID,6, Credits)
                worksheet.write(courseID,7, Notes)
                worksheet.write(courseID,8, IsOnline)
                worksheet.write(courseID,9, IsResidential)
                courseID = courseID + 1
        driver.implicitly_wait(5)
        element = driver.find_element_by_name('prefix')
        all_options = element.find_elements_by_tag_name("option")
workbook.close()
print ("Workbook Complete")

    
