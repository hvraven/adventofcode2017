#!/usr/bin/env python3

import numpy as np
import attr

@attr.s
class TuringMachine(object):
    tape = attr.ib(default=np.zeros(256, dtype=bool))
    pos = attr.ib(default=0)

    @property
    def current(self):
        return self.tape[self.pos]

    @current.setter
    def current(self, value):
        self.tape[self.pos] = value

    def left(self):
        if self.pos == 0:
            length = self.tape.shape[0]
            ntape = np.zeros(length * 2, dtype=self.tape.dtype)
            ntape[length:] = self.tape
            self.tape = ntape
            self.pos += length
        self.pos -= 1

    def right(self):
        length = self.tape.shape[0]
        if self.pos == length - 1:
            ntape = np.zeros(length * 2, dtype=self.tape.dtype)
            ntape[:length] = self.tape
            self.tape = ntape
        self.pos += 1

    def diagnostic_checksum(self):
        return np.sum(self.tape)

def state_A(machine):
    if not machine.current:
        machine.current = 1
        machine.right()
        return state_B
    else:
        machine.current = 0
        machine.left()
        return state_C

def state_B(machine):
    if not machine.current:
        machine.current = 1
        machine.left()
        return state_A
    else:
        machine.current = 1
        machine.right()
        return state_D

def state_C(machine):
    if not machine.current:
        machine.current = 1
        machine.right()
        return state_A
    else:
        machine.current = 0
        machine.left()
        return state_E

def state_D(machine):
    if not machine.current:
        machine.current = 1
        machine.right()
        return state_A
    else:
        machine.current = 0
        machine.right()
        return state_B

def state_E(machine):
    if not machine.current:
        machine.current = 1
        machine.left()
        return state_F
    else:
        machine.current = 1
        machine.left()
        return state_C

def state_F(machine):
    if not machine.current:
        machine.current = 1
        machine.right()
        return state_D
    else:
        machine.current = 1
        machine.right()
        return state_A

def run(cycles = 12919244):
    machine = TuringMachine()
    state = state_A
    for i in range(cycles):
        if i % 100000 == 0:
            print(str(i) + ' ' + str(machine.pos) + ' ' + str(machine.tape.shape))
        state = state(machine)
    return machine.diagnostic_checksum()

print(run())
