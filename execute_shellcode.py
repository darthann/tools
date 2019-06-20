import pexpect

temp_file_name = "run.c"

script = """#include <stdio.h>
#include <string.h>
 
unsigned char shellcode[] = \"""" + str(shellcode) + """\";

int main()
{
    int (*ret)() = (int(*)())shellcode;
    ret();
}"""

open(temp_file_name, "w").write(script)


compile_cmd = "gcc -z execstack " + temp_file_name + " -o shellcode"
exec_cmd = "./shellcode"

p = pexpect.spawn(compile_cmd)
p.expect(pexpect.EOF)
p = pexpect.spawn(exec_cmd)
p.expect(pexpect.EOF)

result = str(p.before).strip()

print(result)

p = pexpect.spawn("rm shellcode")
