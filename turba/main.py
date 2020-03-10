from machine import Machine
import os


def main():
    machine = Machine(100, 500)
    machine.run()

    base = os.path.dirname(os.path.abspath(__file__))
    code_file = open(os.path.join(base, 'code.txt'), 'r')
    lines = code_file.readlines()
    for line in lines:
        line = line.strip()
        parts = line.split(' ')
        command = parts[0]
        parts = parts[1:]
        machine.send_command(command, *parts)
    machine.stop()

if __name__ == "__main__":
    main()
