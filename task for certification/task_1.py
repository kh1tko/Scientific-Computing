def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    second_operands = []
    lines = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Each problem must have two operands and one operator.'

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        result = None
        if operator == '+':
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)

        width = max(len(operand1), len(operand2)) + 2
        first_operands.append(operand1.rjust(width))
        second_operands.append(operator + operand2.rjust(width - 1))
        lines.append('-' * width)
        results.append(str(result).rjust(width))

    arranged_problems = '    '.join(first_operands) + '\n'
    arranged_problems += '    '.join(second_operands) + '\n'
    arranged_problems += '    '.join(lines)
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems


print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
