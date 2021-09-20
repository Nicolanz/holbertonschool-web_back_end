import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(getListStudents) {
  const reducer = (prev, current) => prev + current;
  const studentList = getListStudentIds(getListStudents);
  return studentList.reduce(reducer);
}
