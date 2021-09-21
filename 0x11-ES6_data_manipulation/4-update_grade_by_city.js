export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const newList = [];

  if (Array.isArray(getListStudents) === false || Array.isArray(newGrades) === false) {
    return newList;
  }

  getListStudents.filter((obj) => obj.location === city).map((x) => {
    const newObj = x;
    newGrades.map((i) => {
      if (newObj.id === i.studentId) {
        newObj.grade = i.grade;
        newList.push(newObj);
      } else if (newGrades.at(-1) === i && newObj.grade === undefined) {
        newObj.grade = 'N/A';
        newList.push(newObj);
      }
      return i.studentId;
    });
    return newObj;
  });
  return newList;
}
