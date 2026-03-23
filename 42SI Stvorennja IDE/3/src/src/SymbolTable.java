import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

enum Type {I32, F64, BOOL, STRING, VECTOR, VOID, UNKNOWN}
class Symbol {
    String name;
    Type type;
    int line, charPos;
    boolean isUsed = false;
    boolean isFunction = false;
    List<Type> paramTypes = new ArrayList<>();

    public Symbol(String name, Type type, int line, int charPos) {
        this.name = name;
        this.type = type;
        this.line = line;
        this.charPos = charPos;
    }
}

class Scope {
    private Scope parent;
    private Map<String,Symbol> symbols = new HashMap<>();

    public Scope(Scope parent) { this.parent = parent; }

    public void define(Symbol sym) { symbols.put(sym.name, sym); }

    public Symbol resolve(String name) {
        Symbol s = symbols.get(name);
        if (s != null) return s;
        if (parent != null) return parent.resolve(name);
        return null;
    }

    public Symbol resolveLocal(String name) { return symbols.get(name); }
    public Scope getEnclosingScope() { return this.parent; }
    public Map<String, Symbol> getSymbols() { return symbols; }
}