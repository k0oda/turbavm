import os

COMMAND_CODES = {
    'mov': '0001',
    'add': '0010',
    'sub': '0011',
    'mult': '0100',
    'div': '0101',
    'out': '0110',
    'wait': '0111',
}


def compile(source_path : str, save_path : str):
    data = open(source_path, 'r')
    compiled = open(save_path, 'w')
    lines = data.readlines()
    line_counter = 0
    for line in lines:
        line = line.strip()
        parts = line.split(' ')
        command = parts[0]
        args = parts[1:]
        if command in COMMAND_CODES:
            command_code = COMMAND_CODES[command]
        else:
            print(f"Invalid Command on line: {line_counter} ({command})")
            return None
        compiled.write(command_code)
        for arg in args:
            compiled.write('-' + arg)
        compiled.write('/')
        line_counter += 1
    return True

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    compile(os.path.join(base, 'code.txt'), os.path.join(base, 'code.run'))
