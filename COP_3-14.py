class Machine:
    def __init__(self):
        self.PC = int("0340", 8)
        self.I1 = int("1111", 8)
        self.I2 = int("0256", 8)
    
    def get_addr(self, ins: str) -> int:
        ins_int = int(ins, 8)
        A   = ins_int & 0b111111
        Z_C = (ins_int >> 6) & 0b1
        I2f = (ins_int >> 7) & 0b1
        I1f = (ins_int >> 8) & 0b1
        OP  = (ins_int >> 9) & 0b11
        At  = (ins_int >> 11) & 0b1
        
        # unused variable OP
        _ = OP

        if Z_C == 0:
            base = A
        else:
            pc_page = (self.PC >> 6) & 0b111111
            base = (pc_page << 6) | A
        
        if I1f:
            base += self.I1
        if I2f:
            base += self.I2

        base &= 0xFFF

        if At == 1:
            # there's no regs ouo
            return 0
        
        return base


if __name__ == "__main__":
    m = Machine()
    print("\n".join(f"{m.get_addr(v):04o}Q" for v in ("1046", "2433", "3215", "1111")))