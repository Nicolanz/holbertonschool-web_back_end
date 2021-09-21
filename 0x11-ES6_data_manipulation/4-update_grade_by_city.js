export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const newList = getListStudents.filter((obj) => obj.location === city).map((newObj) => {
    const myObj = newObj;
    const grade = newGrades.filter((studentGrade) => studentGrade.studentId === newObj.id).map(
      (e) => e.grade,
    );
    if (grade.length === 0) {
      myObj.grade = 'N/A';
    } else {
      const [a] = grade;
      myObj.grade = a;
    }
    return myObj;
  });
  return newList;
}
