import os 
from os import walk
from collections import OrderedDict

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
        if ('Choose' in line):
            if ('Choose one of the following:' != line.replace('\n','')) and ('Choose from:' not in line):
                print (line.replace('\n',''))
        if notes in line:
            index = i + 1
    if index != 0:
        for i in range(index, len(lines)):
            first_line = lines[i].rstrip('\n')
            if ('MAJOR (' in lines[i]):
                break
            if key < 9:
                if is_int(first_line[0]) and not is_int(first_line[1]) and first_line[1] != ',' and first_line[1] != ' ':
                    key = int(first_line[0])
                    final = first_line[1:]
                else:
                    final = final + first_line
            else:
                if is_int(first_line[0:2]) and not is_int(first_line[3]) and first_line[3] != ',' and first_line[3] != ' ':
                    key = int(first_line[0:2])
                    final = first_line[2:]
                else:
                    final = final + first_line
            if i + 1 < len(lines):
                second_line = lines[i + 1].rstrip('\n')
                if not is_int(second_line[0]):
                    final = (final + ' ' + second_line)
            NOTES[key] = final
    return NOTES

filenames = []
for dirpath, dirname, filename in walk('Output/'):
    filenames.extend(filename)
    break
os.chdir(r'Output/')
f = open("Filtered Notes.txt", "w")
h = open("Unfiltered Notes.txt", "w")
for individual_file in filenames:
    with open(individual_file, "r") as text_file:
        #print ('New DCP: ', individual_file)
        #print ('------------------------------')
        f.write ('New DCP: ' + individual_file + '\n')
        f.write ('------------------------------' + '\n')
        lines = text_file.readlines()
        Notes = get_notes(lines)

        for key, value in Notes.items():
            #print (str(key) + ': ' + value)
            if ("Please refer to the list of Approved General Education and Integrative Courses at" in value):
                f.write( "Case Taken : 1"+ '\n')
            elif ("All students must pass the Computer Assess" in value):
                f.write( "Case Taken : 2"+ '\n')
            elif ("Must be the same language" in value):
                f.write( "Case Taken : 3"+ '\n')
            elif ("Honors Program students may take BIBL 205 and 210 in place of BIBL 105 and 110" in value):
                f.write( "Case Taken : 4"+ '\n')
            elif ("WVW 101 and 102 must be completed" in value):
                f.write( "Case Taken : 5"+ '\n')
            elif ('Crosslisted with' in value):
                f.write( "Case Taken : 6"+ '\n')
            elif ('Choose from' in value):
                f.write( "Case Taken : 7"+ '\n')
            elif ('strongly recommended' in value):
                f.write( "Case Taken : 8"+ '\n')
            elif ('Minimum grade of' in value):
                f.write( "Case Taken : 9"+ '\n')
            elif ("These are approved General Education" in value):
                f.write( "Case Taken : 10"+ '\n')
            elif ("Minors are included" in value):
                f.write( "Case Taken : 11"+ '\n')
            elif (' *Or Approved Instrument' in value):
                f.write( "Case Taken : 12"+ '\n')
            elif ("*Students may choose to take the same ensemble more than once **Students should take one ensemble per semester ***Three credits must be upper-level" in value):
                f.write( "Case Taken : 13"+ '\n')
            elif ('Choose a course not already applying to the major' in value):
                f.write( "Case Taken : 14"+ '\n')
            elif ('GPA of' in value):
                f.write( "Case Taken : 15"+ '\n')
            elif ('is not an approved General Education course' in value):
                f.write( "Case Taken : 16"+ '\n')
            elif ('To be taken in the final semester of study' in value):
                f.write( "Case Taken : 17"+ '\n')
            elif ('Student may select one course for Integrative Studies which contains the same prefix as courses within the major.' in value):
                f.write( "Case Taken : 18"+ '\n')
            elif ('Students with a minimum of' in value):
                f.write( "Case Taken : 19"+ '\n')
            elif ('Refer to www.liberty.edu/uguide for licensure information' in value):
                f.write( "Case Taken : 20"+ '\n')
            elif ('upper-level requirement' in value):
                f.write( "Case Taken : 21"+ '\n')
            elif ('This test must be passed before' in value):
                f.write( "Case Taken : 22"+ '\n')
            elif ('industry standard certification' in value):
                f.write( "Case Taken : 23"+ '\n')
            elif ('cannot be applied to more than one requirement in major' in value):
                f.write( "Case Taken : 24"+ '\n')
            elif ('Must be completed after' in value):
                f.write( "Case Taken : 25"+ '\n')
            elif ('choose according to' in value):
                f.write( "Case Taken : 26"+ '\n')
            elif ('Choose a' in value):
                f.write( "Case Taken : 27"+ '\n')
            elif ('preferred' in value):
                f.write( "Case Taken : 28"+ '\n')
            elif ('Course may be repeated' in value):
                f.write( "Case Taken : 29"+ '\n')
            elif ('not allowed to apply as a Free Elective' in value):
                f.write( "Case Taken : 30"+ '\n')
            elif ('courses will be delivered at' in value):
                f.write( "Case Taken : 31"+ '\n')
            elif ('May choose' in value) and ('Each Area of Study should' in value):
                f.write( "Case Taken : 32"+ '\n')
            elif ('may apply to clusters with Department Approval' in value):
                f.write( "Case Taken : 33"+ '\n')
            elif ('A minimum' in value) and ('from list of' in value):
                f.write( "Case Taken : 34"+ '\n')
            elif ('Honor' in value) and ('student' in value):
                f.write( "Case Taken : 35"+ '\n')
            elif ('Must be' in value) and ('certified' in value):
                f.write( "Case Taken : 36"+ '\n')
            elif ('Application to Graduate School in' in value):
                f.write( "Case Taken : 37"+ '\n')
            elif ('hours of internship or the equivalent' in value):
                f.write( "Case Taken : 38"+ '\n')
            elif ('Students must choose either the' in value):
                f.write( "Case Taken : 39"+ '\n')
            elif ('Modern Language courses' in value):
                f.write( "Case Taken : 40"+ '\n')
            elif ('average' in value):
                f.write( "Case Taken : 41"+ '\n')
            elif ('cannot apply towards' in value):
                f.write( "Case Taken : 42"+ '\n')
            elif ('After the completion of all Core courses, the student will be required' in value):
                f.write( "Case Taken : 43"+ '\n')
            elif ('Recommended that General Electives be limited to' in value):
                f.write( "Case Taken : 44"+ '\n')
            elif ('Students intending to go to graduate school' in value):
                f.write( "Case Taken : 45"+ '\n')
            elif ('Students preparing to coach in high school' in value):
                f.write( "Case Taken : 46"+ '\n')
            elif ('Students will be required to obtain a double major or approved minor.' in value):
                f.write( "Case Taken : 47"+ '\n')
            elif ('These' in value) and ('courses are approved' in value):
                f.write( "Case Taken : 48"+ '\n')
            elif ('There are approved General Education courses' in value):
                f.write( "Case Taken : 49"+ '\n')
            elif ('Choose four' in value):
                f.write( "Case Taken : 50"+ '\n')
            else:
                h.write(individual_file + ': ' + value + '\n')