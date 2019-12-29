from typing import Union
from collections import defaultdict


class IntCode:
    def __init__(self, mem, input=None, i=-1):
        self.i = i
        self.mem = defaultdict(int, enumerate(map(int, mem)))
        self.rb = 0
        self.ip = 0
        self.op = -1
        self.modes = []
        self.reads = []
        self.writes = []
        self.input = input
        self.halted = False
        self.paused = False

    def _get_inst(self) -> None:
        mem = str(self.mem[self.ip]).zfill(5)
        self.op = int(mem[-2:])
        self.modes = [int(c) for c in mem[:-2][::-1]]

    def _get_args(self, size: int) -> None:
        args = [self.mem[self.ip + i] for i in range(1, size)]
        self.reads = [(self.mem[x], x, self.mem[x + self.rb])[m]
                      for x, m in zip(args, self.modes)]
        self.writes = [(x, None, x + self.rb)[m]
                       for x, m in zip(args, self.modes)]

    def run_all(self):
        """Run until HALT"""
        ans = []
        while True:
            val = self.run()
            if val is None:
                return ans
            ans.append(val)

    def run(self, inp=None) -> Union[None, int]:
        """Returns next output"""
        while True:
            self._get_inst()
            if self.op == 99:  # Halt
                self.halted = True
                return None

            size = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2][self.op]
            self._get_args(size)

            self.ip += size
            if self.op == 1:  # Add
                self.mem[self.writes[2]] = self.reads[0] + self.reads[1]

            elif self.op == 2:  # Multiply
                self.mem[self.writes[2]] = self.reads[0] * self.reads[1]

            elif self.op == 3:  # Input
                if inp is None or len(inp) == 0:
                    if self.i == -1:
                        inp = self.input()
                    else:
                        inp = self.input(self.i)
                if type(inp) == int:
                    inp = [inp]
                self.mem[self.writes[0]] = inp.pop(0)

            elif self.op == 4:  # Output
                return int(self.reads[0])

            elif self.op == 5:  # Jump if Not Zero
                if self.reads[0]:
                    self.ip = self.reads[1]

            elif self.op == 6:  # Jump if Zero
                if not self.reads[0]:
                    self.ip = self.reads[1]

            elif self.op == 7:  # Less Than
                self.mem[self.writes[2]] = (self.reads[0] < self.reads[1])

            elif self.op == 8:  # Equals
                self.mem[self.writes[2]] = (self.reads[0] == self.reads[1])

            elif self.op == 9:  # Relative Base
                self.rb += self.reads[0]

            else:
                print(
                    f'Unhandled error on code: {self.op}\nip = {self.ip}\nmem = {self.mem}')
                assert False
