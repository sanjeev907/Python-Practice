def result(marks):
    for i in marks:
        if i>=33:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")
    
    result([50,60,85,100])