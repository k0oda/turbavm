from machine import Machine
import os


def main():
    machine = Machine(100, 500)
    machine.run()

    base = os.path.dirname(os.path.abspath(__file__))
    executable = open(os.path.join(base, 'code.run'), 'r')
    commands = executable.readline().split('/')[:-1]
    for command in commands:
        parts = command.split('-')
        machine.send_command(*parts)
    machine.stop()

if __name__ == "__main__":
    main()
