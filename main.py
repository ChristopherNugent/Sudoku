from Sudoku import SudokuTable

#s = SudokuTable("800000000003600000070090200050007000000045700000100030001000068008500010090000400")
s = SudokuTable("030700900a020f000f0003720be05ad000e000000508070b50bac00800710040000c0a8b500004000b00d0e080g906150000060c00b090004d05001g00000300003000001800d0f700080900b0300000b140g8070d0a00c00060000a7490g0000g007e00200bf80180d020a000000c000c960540de8000a0001080600c00e070")
#s = SudokuTable(4)

s.print()

print()
print()

#t = s.copy()
#t.findAllFreebies()
t = SudokuTable.guessSolve(s)

t.print()
