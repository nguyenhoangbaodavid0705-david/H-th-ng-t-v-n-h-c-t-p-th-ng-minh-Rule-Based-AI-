def analyze_student(gpa,study_hours,weak_subjects,effort):
    if gpa <2.5 and study_hours<10:
        return "Yeu","Thieu thoi gian hoc ","Nen hoc lai kien thuc co ban"
    if gpa >=3.7 and study_hours>=20 and effort>=4:
        return "Gioi","Co gang duy trinh","Y thuc hoc tap tot","Nen hoc nang cao va lam project"
    if gpa>=3.2 and effort>=3:
        return "Kha ","chua toi uu cach hoc","Can tang gio hoc va on tap"
    return "Trung binh","Chua toi uu cach hoc ","can tang gio hoc va on tap"