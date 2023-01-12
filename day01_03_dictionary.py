subjects = {
    "의영": "a+",
    "오래된 미래": "b+",
    "양자역학": "a0",
}
student = "김도훈"
subject = "오래된 미래"
#old style
print("%s 학생의 %s 과목 성적은 %s 입니다." % (student, subject, subjects[subject]))
#modern style(forma함수)
print("{} 학생의 {} 과목 성적은 {} 입니다.".format(student, subject, subjects[subject]))
#ultra modern
print(f"{student} 학생의 {subject} 과목 성적은 {subjects[subject]} 입니다.")
