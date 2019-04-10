#Jacy Yang's Part B: Rocket Ship

height = 3

#top of rocket function
def pyramid():
    #determine the total number of rows
    top = height * 2 - 1
    #for every row in pyramid pattern...
    for row in range(0, top):
        line = ""
        #determines total number of left spaces
        leftspace = height - row + 2
        #add a space to the line as many times as leftspace
        for i in range(0, leftspace):
            line = line + " "
        #determine tbe total number of forward slash
        leftdash = row + 1
        #add forward slash as many times as leftdash
        for i in range(0, leftdash):
            line = line + "/"
        #adds astrids to the line
        line = line + "**"
        #determine total amount of back slash
        rightdash = row + 1
        #add as many back slash as righdash
        for i in range(0, rightdash):
            line = line + "\\"
        #print line
        print line
#function for single line pattern
def line():
    #start line with +
    line = "+"
    #determine the frequency of pattern
    pattern = height * 2
    #add =* as many times as pattern
    for i in range(0, pattern):
        line = line + "=*"
    #add + to the line
    line = line + "+"
    #print line
    print line
#function for one part of the rocket body
def top_body():
    #adds vertical line in each row per height
    for row in range(0, height):
        line = "|"
        #determine the frequency of dots
        dots = height - row - 1
        #adds dots to line as many times as dots variable
        for i in range(0, dots):
            line = line + "."
        #determine the total amount of slashes
        slash = row + 1
        #adds double slashes as many times as slash
        for i in range(0, slash):
            line = line + "/\\"
        #determines frequency of dots in the middle
        middle_dots = 2 * dots
        #adds dots as many times as middle_dots
        for i in range(0, middle_dots):
            line = line + "."
        #determines the number of slashes
        slash = row + 1
        #adds double slashes as many times as slashes
        for i in range(0, slash):
            line = line + "/\\"
        #determines total number of dots
        dots = height - row - 1
        #adds dots as many times as dots
        for i in range(0, dots):
            line = line + "."
        #finishes line with vertical line
        line = line + "|"
        #prints line
        print line
#function for other half of the rocket body
def bottom_body():
    #starts lines with vertical line
    for row in range(0, height):
        line = "|"
        #add vertical line as many times as row
        for i in range(0, row):
            line = line + "."
        #determines frequency for upside down triangles
        slash = height - row
        #add as many triangles as slash
        for i in range(0, slash):
            line = line + "\\/"
        #determines dots in the middle
        middle_dots = row * 2
        #adds dots in the middle as many times and middle_dots
        for i in range(0, middle_dots):
            line = line + "."
        #determines the frequency for upside down triangles
        slash = height - row
        #adds triangles as many times as slash
        for i in range(0, slash):
            line = line + "\\/"
        #add dots as many times as rows
        for i in range(0, row):
            line = line + "."
        #finishes line with vertical line
        line = line + "|"
        #print line
        print line

################################################################################
pyramid()
line()
top_body()
bottom_body()
line()
bottom_body()
top_body()
pyramid()
