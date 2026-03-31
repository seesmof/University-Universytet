import javax.sound.sampled.Port;
import javax.swing.*;
import java.awt.*;
import java.io.*;

public class Main extends JFrame {
    private JTextArea codeInput;
    private JTextArea consoleOutput;
    private JTree astTree;

    public Main() {
        setTitle("Rust IDE");
        setSize(1000,800);
        setLayout(new BorderLayout());

        codeInput = new JTextArea();
        codeInput.setFont(new Font("Consolas", Font.PLAIN, 14));
        JScrollPane codeScroll = new JScrollPane(codeInput);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(()->new Main().setVisible(true));
    }
}