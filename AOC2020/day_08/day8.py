from __future__ import annotations
from abc import abstractmethod
from enum import Enum, unique

from AOC2020.helpers import GIT_DIR


def open_input() -> list[tuple[int, str]]:
    _TEST = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    # lines = [line.split(' ') for line in _TEST.split('\n')]
    # lines = [(opcode, int(arg)) for (opcode, arg) in lines]
    # return lines
    with open(f'{GIT_DIR}/day_08/input.txt', 'r') as fh:
        lines = [line.strip().split(' ') for line in fh.read().split('\n')]
        lines = [(opcode, int(arg)) for (opcode, arg) in lines[:-1]]
        return lines


class Operation:
    opcode = None

    def __call__(self, *args, **kwargs):
        ret = self._func(*args, **kwargs)
        return ret

    @abstractmethod
    def _func(self):
        pass


class Nop(Operation):
    opcode: str = 'nop'

    def _func(self) -> None:
        return


class Accumulator(Operation):
    opcode: str = 'acc'

    def _func(self, arg: int) -> int:
        return arg


class Jump(Operation):
    opcode: str = 'jmp'

    def _func(self, arg: int) -> int:
        return arg


OPS = {
    insttype.opcode: insttype for insttype in [Nop, Accumulator, Jump]
}


class Instruction:
    def __init__(self, op: Operation, arg: int):
        self.op = op
        self.arg = arg
        self.has_run = False

    def __call__(self):
        self.has_run = True
        return self.op(self.arg)

    def run(self):
        return self.__call__()

    def __str__(self):
        return f'{self.op.opcode=}\t{self.arg=}\t{self.index=}'

    @classmethod
    def from_tuple(cls, tup: tuple[str, int]) -> Instruction:
        return cls(
            op=OPS[tup[0]](),
            arg=tup[1],
        )


class InstructionSet:
    def __init__(self, instructions: list[Instruction]):
        self._op_idx = 0
        self._instrcts = instructions
        self.accumulated_value = 0
        self._exit_line = len(instructions)
        self._handling_rules = {
            Nop: self._handle_nop,
            Jump: self._handle_jmp,
            Accumulator: self._handle_acc,
        }

    def _handle_nop(self, inst: Nop, *args, **kwargs):
        self._op_idx += 1

    def _handle_jmp(self, inst: Nop, *args, **kwargs):
        self._op_idx += inst()

    def _handle_acc(self, inst: Accumulator, *args, **kwargs):
        newval = inst()
        self.accumulated_value += newval
        self._op_idx += 1

    def run_next_instruction(self):
        if not 0 <= self._op_idx < len(self._instrcts):
            raise IndexError('op_idx invalid')
        next_inst = self._instrcts[self._op_idx]
        self._handling_rules[type(next_inst.op)](next_inst)

    def run_until_repeat(self):
        while not self._instrcts[self._op_idx].has_run:
            self.run_next_instruction()

    def run_until_done(self):
        opstot = 0
        while not self._op_idx == self._exit_line:
            self.run_next_instruction()
            opstot += 1
            if opstot > self._exit_line:
                print('No good')
                return
        print(f'Fixed accumulator value: {self.accumulated_value}')

    def find_op_to_change(self):
        fixed = False
        self._ops_run = set()
        og_ins = self._instrcts.copy()
        for idx, instruct in enumerate(og_ins):
            self.reset(og_ins.copy())
            if isinstance(instruct.op, Accumulator):
                continue
            elif isinstance(instruct.op, Nop):
                self._instrcts[idx] = Instruction.from_tuple(('jmp', instruct.arg))
            elif isinstance(instruct.op, Jump):
                self._instrcts[idx] = Instruction.from_tuple(('nop', instruct.arg))
            self.run_until_done()

    def reset(self, og: list[Instruction]):
        self.accumulated_value = 0
        for ins in self._instrcts:
            ins.has_run = False
        self._instrcts = og.copy()
        self._op_idx = 0


if __name__ == '__main__':
    data = open_input()
    iss = InstructionSet(
        [Instruction.from_tuple(line) for line in data]
    )
    iss.find_op_to_change()
