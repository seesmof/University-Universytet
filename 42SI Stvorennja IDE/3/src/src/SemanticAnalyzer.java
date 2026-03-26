import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.tree.ParseTreeProperty;

import java.util.ArrayList;
import java.util.List;

import gen.*;

public class SemanticAnalyzer extends MainBaseListener {
    private Scope currentScope = new Scope(null);
    private int loopDepth = 0;
    public List<String> errors = new ArrayList<>();
    public List<String> warnings = new ArrayList<>();
    private ParseTreeProperty<Type> types = new ParseTreeProperty<>();

    private void reportError(Token t, String msg) {
        errors.add("ERROR ["+t.getLine()+":"+t.getCharPositionInLine()+"]: "+msg);
    }

    @Override public void enterBlock(MainParser.BlockContext context) {
        currentScope = new Scope(currentScope);
    }

    @Override public void exitBlock(MainParser.BlockContext context) {
        // Перевірка на невикористані зміннні перед виходом
        for (Symbol s : currentScope.getSymbols().values()) {
            if (!s.isUsed && !s.isFunction) {
                warnings.add("WARNING ["+s.line+":"+s.charPos+"]: Variable '"+s.name+"' is never used.");
            }
        }
        if (currentScope.getEnclosingScope() != null) {
            currentScope = currentScope.getEnclosingScope();
        }
    }

    @Override public void enterLetBinding(MainParser.LetBindingContext context) {
        String name = context.ID().getText();

//        Перевірка повторного оголошення в тій же області
        if (currentScope.resolveLocal(name) != null) {
            reportError(context.ID().getSymbol(), "Identifier '"+name+"' already declared in this scope.");
            return;
        }

        Type t = Type.UNKNOWN;
        if (context.type() != null) {
            try {
                t = Type.valueOf(context.type().getText().toUpperCase());
            } catch (IllegalArgumentException e) {
                t=Type.UNKNOWN;
            }
        }
        currentScope.define(new Symbol(name, t, context.ID().getSymbol().getLine(), context.ID().getSymbol().getCharPositionInLine()));
    }

    @Override public void enterIdExpr(MainParser.IdExprContext context) {
        String name = context.ID().getText();
        Symbol s = currentScope.resolve(name);

        if (s==null) {
            reportError(context.ID().getSymbol(), "Variable '"+name+"' used without declaration");
        } else {
            s.isUsed = true;
            types.put(context, s.type);
        }
    }

    @Override public void enterWhileStatement(MainParser.WhileStatementContext context) { loopDepth++; }
    @Override public void enterLoopStatement(MainParser.LoopStatementContext context) { loopDepth++; }
    @Override public void exitLoopStatement(MainParser.LoopStatementContext context) { loopDepth--; }

    @Override public void enterBreakStmt(MainParser.BreakStmtContext context) {
        if (loopDepth==0) reportError(context.getStart(), "'break' used outside of loop.");
    }

    @Override public void exitIndexExpr(MainParser.IndexExprContext context) {
        Type idxType = types.get(context.expression(1));
        if (idxType != Type.I32) {
            reportError(context.getStart(), "Array index must be an integer (i32).");
        }
    }

    @Override
    public void enterPrintStatement(MainParser.PrintStatementContext context) {
//        1. Отримати текст рядка
        String string = context.STRING().getText();

//        2. Рахувати кількість аргументів у виклику
        int argsCount = context.expression().size();

//        3. Семантична перевірка аргументів (чи всі вони оголошені)
        for (MainParser.ExpressionContext expression : context.expression()) {
            visit(expression);
        }

        if (argsCount == 0 && string.contains("{}")) {
            warnings.add("WARNING ["+context.getStart().getLine()+"]: println! contains placeholder '{}', but no arguments provided.");
        }
    }
}
