import com.sun.tools.jconsole.JConsoleContext;
import gen.MainLexer;
import gen.MainParser;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class RustIDE extends JFrame {
    private JTextArea codeArea = new JTextArea();
    private JTextArea outputArea = new JTextArea();

    public RustIDE() {
        setTitle("Rust Semantic Analyzer IDE");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        JPanel toolBar = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JButton openBtn = new JButton("Open file");
        JButton analyzeBtn = new JButton("Run Semantic Analysis");
        toolBar.add(openBtn);
        toolBar.add(analyzeBtn);

        openBtn.addActionListener(e -> openFile());
        analyzeBtn.addActionListener(e-> analyze());

        codeArea.setFont(new Font("Consolas", Font.PLAIN, 14));

        add(new JScrollPane(codeArea), BorderLayout.CENTER);
        add(new JScrollPane(outputArea), BorderLayout.SOUTH);
        add(toolBar, BorderLayout.NORTH);
        outputArea.setPreferredSize(new Dimension(800, 200));
        outputArea.setEditable(false);
    }

    private void analyze() {
        outputArea.setText("");
        MainLexer lexer = new MainLexer(CharStreams.fromString(codeArea.getText()));
        MainParser parser = new MainParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.program();

        ParseTreeWalker walker = new ParseTreeWalker();
        SemanticAnalyzer analyzer = new SemanticAnalyzer();
        walker.walk(analyzer, tree);

        if (analyzer.errors.isEmpty() && analyzer.warnings.isEmpty()) {
            outputArea.setText("Analysis complete. No issues found.");
        } else {
            for (String err : analyzer.errors) outputArea.append(err + "\n");
            for (String warn : analyzer.warnings) outputArea.append(warn + "\n");
        }
    }

    private void openFile(){
        JFileChooser fileChooser = new JFileChooser();
        int result = fileChooser.showOpenDialog(this);
        if (result==JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            try {
                String content = Files.readString(selectedFile.toPath());
                codeArea.setText(content);
            } catch (IOException e) {
                JOptionPane.showMessageDialog(this, "Error reading file: "+e.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(()-> new RustIDE().setVisible(true));
    }
}
