students = {
"ali":{
    "age":"40",
    "gender":"male",
    "length":"200",
    "weight":"90"
},
"salma":{
    "age":"20",
    "gender":"female",
    "length":"160",
    "weight":"50"
}
}
for student in students: 
    print (student)
    for spec in students[student] :
        print(f"{spec} ==> {students[student][spec]}")