class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq_students = Counter(students)

        for s in sandwiches:
            if freq_students[s] == 0:
                break
            
            freq_students[s] -= 1

        return sum(freq_students.values())
