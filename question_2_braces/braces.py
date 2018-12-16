import re


REGEX_BRACE_OPENING_VERSIONS = '(\{|\(|\[)'
REGEX_BRACE_CLOSING_VERSIONS = '(\}|\)|\])'


def is_braces_balanced(braces):
    braces_stack = []
    valid = True
    for brace in braces:
        if re.match(REGEX_BRACE_OPENING_VERSIONS, brace):
            braces_stack.append(brace)
        elif re.match(REGEX_BRACE_CLOSING_VERSIONS, brace):
            if len(braces_stack) == 0:
                valid = False
            if brace == '}':
                if len(braces_stack) != 0 and braces_stack.pop() != '{':
                    valid = False
            elif brace == ')':
                if len(braces_stack) != 0 and braces_stack.pop() != '(':
                    valid = False
            elif brace == ']':
                if len(braces_stack) != 0 and braces_stack.pop() != '[':
                    valid = False
    return len(braces_stack) == 0 and valid


def braces(values):
    return ['YES' if is_braces_balanced(braces_input) else 'NO' for braces_input in values]
