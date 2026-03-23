import gen.MainLexer;
import gen.MainParser;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.Trees;

import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import java.awt.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main extends JFrame {
    private JTextArea codeArea;
    private JTree astTree;
    private JTextArea console;

    public Main() {
        setTitle("Rust IDE with Compiler Backend");
        setSize(1000,750);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        codeArea = new JTextArea();
        codeArea.setFont(new Font("Consolas", Font.PLAIN, 14));
        codeArea.setTabSize(4);
        JScrollPane codeScroll = new JScrollPane(codeArea);
        codeScroll.setBorder(BorderFactory.createTitledBorder("Rust Source Code"));

        astTree = new JTree(new DefaultMutableTreeNode("AST Root"));
        JScrollPane treeScroll = new JScrollPane(astTree);
        treeScroll.setBorder(BorderFactory.createTitledBorder("Abstract Syntax Tree"));

        console = new JTextArea(10,0);
        console.setEditable(false);
        console.setFont(new Font("Monospaced", Font.PLAIN, 12));
        console.setBackground(new Color(30,30,30));
        console.setForeground(Color.WHITE);
        JScrollPane consoleScroll = new JScrollPane(console);
        consoleScroll.setBorder(BorderFactory.createTitledBorder("Console Output"));

        JSplitPane mainSplit = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, codeScroll, treeScroll);
        mainSplit.setDividerLocation(600);
        add(mainSplit, BorderLayout.CENTER);
        add(consoleScroll, BorderLayout.SOUTH);

        JPanel toolBar = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JButton analyzeButton = new JButton("Analyze Only");
        JButton buildAndRunButton = new JButton("Build & Run");

        buildAndRunButton.setBackground(new Color(0,120,215));
        buildAndRunButton.setForeground(Color.WHITE);

        toolBar.add(analyzeButton);
        toolBar.add(buildAndRunButton);
        add(toolBar,BorderLayout.NORTH);

        analyzeButton.addActionListener(e-> runAnalysis(false));
        buildAndRunButton.addActionListener(e->runAnalysis(true));
    }

    private void runAnalysis(boolean shouldBuild) {
        String code = codeArea.getText();
        console.setText("");
        console.setForeground(Color.WHITE);

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
                    console.setForeground(Color.RED);
                    console.append("[Syntax Error] line "+line+":"+charPositionInLine+" - "+msg+"\n");
                }
            });

            ParseTree tree = parser.program();

            DefaultMutableTreeNode root = buildJTree(tree, parser);
            astTree.setModel(new DefaultTreeModel(root));

            if (console.getText().isEmpty()) {
                console.append("[Info] Syntax analysis successful.\n");

                if (shouldBuild) { executeBuildPipeline(tree); }
            }
        } catch (Exception e) {
            console.setForeground(Color.RED);
            console.append("[System Error] "+e.getMessage()+"\n");
        }
    }

    private void executeBuildPipeline(ParseTree tree) {
        try {
            console.append("[Build] Starting generation of intermediate representation...\n");

            CodeGenerator gen = new CodeGenerator();
            gen.visit(tree);

            String asmFile = "output.s";
            String exeFile = "app.out";

            Backend.generateAssembly(gen.getInstructions(), asmFile);
            console.append("[Build] Assembly code generated in "+asmFile+"\n");

            boolean success = Backend.compileWithGcc(asmFile, exeFile);

            if (success) {
                console.append("[Build] Compilation successful! Running executable...\n");
                console.append("--------------------------------------------------\n");
                runExecutable(exeFile);
            } else {
                console.setForeground(Color.RED);
                console.append("[Build] GCC compilation failed. Make sure GCC is installed.\n");
            }
        } catch (Exception e) {
            console.append("[Build Error] "+e.getMessage()+"\n");
        }
    }

    private void runExecutable(String path) {
        try {
            Process p = Runtime.getRuntime().exec(path);
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while ((line=reader.readLine()) != null) {
                console.append(line+"\n");
            }
            p.waitFor();
            console.append("--------------------------------------------------\n");
            console.append("[Info] Process finished with exit code "+p.exitValue()+"\n");
        } catch (Exception e) {
            console.append("[Runtime Error] "+e.getMessage()+"\n");
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