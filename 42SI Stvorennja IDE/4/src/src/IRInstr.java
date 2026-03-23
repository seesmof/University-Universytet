public class IRInstr {
    String op, res, arg1, arg2;
    public IRInstr(String op, String res, String arg1, String arg2) {
        this.op=op;
        this.res=res;
        this.arg1=arg1;
        this.arg2=arg2;
    }
    @Override
    public String toString() {
        return String.format("%s %s = %s, %s", op, res, arg1, arg2);
    }
}
