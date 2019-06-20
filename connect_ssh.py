import pexpect

cmd = "ssh sudoku@challenges.ringzer0team.com -p 10143"

child = pexpect.spawn (cmd)
# Server is going to ask for password
child.expect("password")
child.sendline("dg43zz6R0E")

# Read content (Example with sudoku challenge)
child.expect("Solve this sudoku")
# child.before contains output of the server

# To get last ouput of console
child.expect(pexpect.EOF)
print(child.before)
