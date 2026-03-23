import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public
class Backend {
    public static void generateAssembly(List<IRInstr> instructions, String filename) throws IOException {
        PrintWriter writer = new PrintWriter(new FileWriter(filename));

        writer.println(".section .text");
        writer.println(".globl main");
        writer.println("main:");
        writer.println("    pushq %rbp");
        writer.println("    movq %rsp, %rbp");

        for (IRInstr instr : instructions) {
            if (instr.op.equals("+")) {
                writer.println("    movq $"+instr.arg1+", %rax");
                writer.println("    addq $"+instr.arg2+", %rax");
            }
        }

        writer.println("    movq $0, %rax");
        writer.println("    popq %rbp");
        writer.println("    ret");
        writer.close();
    }

    public static boolean compileWithGcc(String asmFile, String outFile) {
        try {
            Process p = Runtime.getRuntime().exec("gcc "+asmFile+" -o "+outFile);
            int exitCode = p.waitFor();
            return exitCode==0;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}
