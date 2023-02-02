import sys

"""
El archivo debe correrse de la siguiente manera:

python check_output.py correc_output.txt student_output.txt

"""


def get_score(ground_truth, student_output):
    ground_truth_stream = open(ground_truth, "r")
    student_output_stream = open(student_output, "r")

    ground_truth_lines = ground_truth_stream.readlines()
    student_output_lines = student_output_stream.readlines()

    total_lines = len(ground_truth_lines)
    student_output_len = len(student_output_lines)
    correct_lines = 0

    for i in range(min(total_lines, student_output_len)):
        student_output_set = map(int, student_output_lines[i].split())
        ground_truth_set = map(int, ground_truth_lines[i].split())

        if set(student_output_set) == set(ground_truth_set):
            correct_lines += 1

    return correct_lines / total_lines


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    score = get_score(input_file, output_file)
    print(f"Score: {score*100}%")
