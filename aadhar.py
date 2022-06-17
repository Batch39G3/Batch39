

def aadhar_details(aadhar_no):
    aadhar={"123456789102":["8660072831","bang"],"485820350979":["9482423818","bang"],"784534984054":["8660072831","bang"],"484856567878":["6362287285","dj-halli"]}
    if aadhar_no not in aadhar:
        return "not found","not found"
    else:
        region=aadhar[aadhar_no][1]
        phno=aadhar[aadhar_no][0]
        return phno,region


#a,b=aadhar_details("12345678901")
#print(a)
#print(b)
