import java.awt.EventQueue;

public class Lab5 {
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GUI window = new GUI();
					window.frmLibrarySearch.setVisible(true);
					window.frmLibrarySearch.setResizable(false);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

}