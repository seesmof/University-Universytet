import gen.MainLexer;
import gen.MainParser;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.Trees;

import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import java.awt.*;

public class Main extends JFrame {
    private JTextArea codeArea;
    private JTree astTree;
    private JTextArea errorConsole;

    public Main() {
        setTitle("Rust Simple IDE (ANTLR4)");
        setSize(1000,700);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        codeArea = new JTextArea();
        codeArea.setFont(new Font("Consolas", Font.PLAIN, 14));
        JScrollPane codeScroll = new JScrollPane(codeArea);
        codeScroll.setBorder(BorderFactory.createTitledBorder("Rust Source Code"));

        astTree = new JTree(new DefaultMutableTreeNode("AST Root"));
        JScrollPane treeScroll = new JScrollPane(astTree);
        treeScroll.setBorder(BorderFactory.createTitledBorder("Abstract Syntax Tree"));

        errorConsole = new JTextArea(8, 0);
        errorConsole.setEditable(false);
        errorConsole.setForeground(Color.RED);
        JScrollPane errorScroll = new JScrollPane(errorConsole);
        errorScroll.setBorder(BorderFactory.createTitledBorder("Error Console"));

        JSplitPane mainSplit = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, codeScroll, treeScroll);
        mainSplit.setDividerLocation(500);
        add(mainSplit, BorderLayout.CENTER);
        add(errorScroll, BorderLayout.SOUTH);

        JButton runBtn = new JButton("Analyze Code");
        runBtn.addActionListener(event -> runAnalysis());
        add(runBtn, BorderLayout.NORTH);
    }

    private void runAnalysis() {
        String code = codeArea.getText();
        errorConsole.setText("");

        try {
            CodePointCharStream input = CharStreams.fromString(code);
            MainLexer lexer = new MainLexer(input);
            CommonTokenStream tokens = new CommonTokenStream(lexer);
            MainParser parser = new MainParser(tokens);

            parser.removeErrorListeners();
            parser.addErrorListener(new BaseErrorListener() {
                @Override
                public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol, int line,
                                        int charPositionInLine, String msg, RecognitionException e) {
                    errorConsole.append("Error at line " + line + ":" + charPositionInLine + " - "+msg+"\n");
                }
            });

            ParseTree tree = parser.program();

            DefaultMutableTreeNode root = buildJTree(tree, parser);
            astTree.setModel(new DefaultTreeModel(root));

            if (errorConsole.getText().isEmpty()) {
                errorConsole.setBackground(new Color(0,207,0));
                errorConsole.setForeground(Color.black);
                errorConsole.setText("Analysis successful! No errors found.");
            } else {
                errorConsole.setBackground(new Color(207, 0, 0));
                errorConsole.setForeground(Color.RED);
            }
        } catch (Exception e) {
            errorConsole.append("System error: "+e.getMessage());
        }
    }

    private DefaultMutableTreeNode buildJTree(ParseTree antlrTree, MainParser parser) {
        String text = Trees.getNodeText(antlrTree, parser);
        DefaultMutableTreeNode node = new DefaultMutableTreeNode(text);
        for (int i = 0; i < antlrTree.getChildCount(); i++) {
            node.add(buildJTree(antlrTree.getChild(i), parser));
        }
        return node;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(()->new Main().setVisible(true));
    }
}