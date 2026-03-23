import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Test {
    private JFrame mainFrame;
    private JLabel headerLabel;
    private JLabel statusLabel;
    private JPanel controlPanel;
    private JLabel msgLabel;

    public Test() {
        prepareGUI();
    }
    public static void main(String[] args) {
        Test layout= new Test();
        layout.showBorderLayout();
    }
    private void prepareGUI() {
        mainFrame = new JFrame("Java SWING Examples");
        mainFrame.setSize(400,400);
        mainFrame.setLayout(new GridLayout(3,1));

        headerLabel= new JLabel("", JLabel.CENTER);
        statusLabel=new JLabel("",JLabel.CENTER);
        statusLabel.setSize(350,100);

        mainFrame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent windowEvent) {
                System.exit(0);
            }
        });
        controlPanel = new JPanel();
        controlPanel.setLayout(new FlowLayout());

        mainFrame.add(headerLabel);
        mainFrame.add(controlPanel);
        mainFrame.add(statusLabel);
        mainFrame.setVisible(true);
    }
    private void showBorderLayout() {
        headerLabel.setText("Layout in action: BorderLayout");

        JPanel panel = new JPanel();
        panel.setBackground(Color.darkGray);
        panel.setSize(300,300);
        BorderLayout layout = new BorderLayout();
        layout.setHgap(10);
        layout.setVgap(10);

        panel.setLayout(layout);
        panel.add(new Button("Center"),BorderLayout.CENTER);
        panel.add(new JButton("Line Start"), BorderLayout.LINE_START);
        panel.add(new JButton("Line End"), BorderLayout.LINE_END);
    }
}
