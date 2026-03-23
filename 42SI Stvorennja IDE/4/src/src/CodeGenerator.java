import gen.MainBaseVisitor;
import gen.MainParser;

import java.util.ArrayList;
import java.util.List;

public class CodeGenerator extends MainBaseVisitor<String> {
    private List<IRInstr> irInstructions = new ArrayList<>();
    private int tempCount = 0;
    private String newTemp() { return "t" + (tempCount++); }
    @Override
    public String visitBinaryExpr(MainParser.BinaryExprContext context) {
        String left = visit(context.expression(0));
        String right = visit(context.expression(1));
        String op = context.op.getText();

        try {
            int lvalue = Integer.parseInt(left);
            int rvalue = Integer.parseInt(right);
            if (op.equals("+")) return String.valueOf(lvalue+rvalue);
            if (op.equals("*")) return String.valueOf(lvalue*rvalue);
        } catch (NumberFormatException e) { }

        String target = newTemp();
        irInstructions.add(new IRInstr(op, target, left, right));
        return target;
    }

    @Override
    public
    String visitiIntLiteral(MainParser.IntLiteralContext context) {
        return context.getText();
    }

    @Override
    public
    String vistiIdExpr(MainParser.IdExprContext context) {
        return context.ID().getText();
    }

    public List<IRInstr> getInstructions() { return irInstructions; }
}
