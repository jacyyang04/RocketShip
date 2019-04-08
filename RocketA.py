# Jacy Yang's Part A for Demo Text Art

size = 4

#prints solid scores needed for the head
def outline():
    line = ""
    ot = size*8
    for i in range(0, ot):
        line = line + "_"
    print line
#recieves variable and makes scores on side
def hair(line):
    for i in range(0, size):
        line = line + "_"
    return line
#prints line with spaces only
def second():
    line = ""
    #makes left side scores
    line = hair(line)
    #adding spaces
    middle = size * 6
    for i in range(0, middle):
        line = line + " "
    #makes right side scores
    line = hair(line)
    print line
#recieves variable and makes eyes
def muag(line):
    line = line + "["
    #spaces in eyes
    qhov = size-1
    for i in range(0, qhov):
        line = line + " "
        #finish making left eye
    line = line + "]"
    return line
#prints line with eyes
def eyes():
    #making left facial temple
    line = ""
    #makes left side scores
    line = hair(line)
    for i in range(0, size):
        line = line + " "
    #making of left eye
    line = muag(line)
    #spaces between eyes
    spaces = size + 2
    for i in range(0, spaces):
        line = line + " "
    #making of right eye
    line = muag(line)
    #making right facial temple
    for i in range(0, size):
        line = line + " "
    #makes right side scores
    line = hair(line)
    print line
#prints line with mouth
def mouth():
    line = ""
    #makes left side scores
    line = hair(line)
    #makes spaces to mouth
    spaces = size * 3 - 1
    for i in range(0, spaces):
        line = line + " "
    #adds mouth
    lips = size / 2
    for i in range (0, lips):
        line = line + "_"
    #makes spaces from mouth
    spaces = size * 3 - 1
    for i in range(0, spaces):
        line = line + " "
    #makes right side scores
    line = hair(line)
    print line
################################################################################

outline()
second()
second()
eyes()
mouth()
second()
outline()
