from pyscript import document

def print_grade(event=None):
    
    firstname = document.getElementById("firstname").value
    lastname = document.getElementById("lastname").value

    
    sci = document.getElementById("sci").value
    math = document.getElementById("math").value
    eng = document.getElementById("eng").value
    fil = document.getElementById("fil").value
    tle = document.getElementById("tle").value
    pe = document.getElementById("pe").value

    
    try:
        sci = float(sci) if sci else 0
        math = float(math) if math else 0
        eng = float(eng) if eng else 0
        fil = float(fil) if fil else 0
        tle = float(tle) if tle else 0
        pe = float(pe) if pe else 0
    except:
        return

   
    grades_list = [sci, math, eng, fil, tle, pe]
    average = sum(grades_list) / len(grades_list)

   
    document.getElementById("name").innerHTML = f"Student: <b>{firstname} {lastname}</b>"

    document.getElementById("grades").innerHTML = (
        f"Science: {sci}<br>"
        f"Math: {math}<br>"
        f"English: {eng}<br>"
        f"Filipino: {fil}<br>"
        f"TLE: {tle}<br>"
        f"PE: {pe}"
    )

    document.getElementById("average").innerHTML = f"General Average: <b>{average:.2f}</b>"
