import javax.swing.JFrame;
import javax.swing.JTabbedPane;
import javax.swing.JPanel;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.JButton;
import javax.swing.JRadioButton;
import javax.swing.JTable;
import javax.swing.border.LineBorder;
import java.awt.Color;
import javax.swing.table.DefaultTableModel;
import javax.swing.ButtonGroup;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.SwingConstants;
import javax.swing.JScrollPane;


public class GUI {

	public JFrame frmLibrarySearch;
	private JTextField memberID;
	private JTextField searchField;
	private JTable searchResultTable;
	private JTabbedPane tabbedPane;
	private JLabel idNotFound;
	private JLabel memberGreeting;
	private JPanel newMemberPane;
	private final ButtonGroup buttonGroup = new ButtonGroup();
	@SuppressWarnings("unused")
	private JTextField newMemberFirstName;
	private JTextField newMemberLastName;
	private JTextField newMemberDOB;
	
	Library library;
	@SuppressWarnings("rawtypes")
	private JComboBox newMemberGender;
	private JLabel newMemberID;
	private JPanel newMemberIDPane;
	private JLabel invalidFirstNameMessage;
	private JLabel invalidLastNameMessage;
	private JLabel invalidDOBMessage;
	private JLabel invalidGenderMessage;
	private JLabel searchTermFormatError;
	private static final String isbnFormatErrorMessage = "Error ISBN format must be: ##-#####-#####";
	private static final String authorFormatErrorMessage = "Author format must be firstName lastName";
	private JLabel noBookSelectedErrorMessage;
	private JTable bookLocationTable;
	private JLabel allCopiesCheckedOutMessage;
	private JRadioButton searchByISBN;
	private JLabel noSearchResults;

	/**
	 * Launch the application.
	 */


	/**
	 * Create the application.
	 */
	public GUI() {
		initialize();
		library = new Library();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	@SuppressWarnings("unchecked")
	private void initialize() {
		frmLibrarySearch = new JFrame();
		frmLibrarySearch.setTitle("Library Search");
		frmLibrarySearch.setBounds(100, 100, 581, 383);
		frmLibrarySearch.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmLibrarySearch.getContentPane().setLayout(null);
		
		tabbedPane = new JTabbedPane(JTabbedPane.TOP);
		tabbedPane.setFont(new Font("Tahoma", Font.PLAIN, 15));
		tabbedPane.setBounds(0, 0, 565, 344);
		frmLibrarySearch.getContentPane().add(tabbedPane);
		
		JPanel memberIdTab = new JPanel();
		tabbedPane.addTab("Member ID", null, memberIdTab, null);
		memberIdTab.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Enter Your Member ID");
		lblNewLabel.setBounds(6, 10, 209, 19);
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 15));
		memberIdTab.add(lblNewLabel);
		
		memberID = new JTextField();
		memberID.setBounds(225, 7, 209, 25);
		memberID.setFont(new Font("Tahoma", Font.PLAIN, 15));
		memberIdTab.add(memberID);
		memberID.setColumns(10);
		
		JButton loginWithMemberID = new JButton("Submit");
		loginWithMemberID.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				login();
			}
		});
		loginWithMemberID.setBounds(444, 6, 92, 27);
		loginWithMemberID.setFont(new Font("Tahoma", Font.PLAIN, 15));
		memberIdTab.add(loginWithMemberID);
		
		idNotFound = new JLabel("Member ID Not Found");
		idNotFound.setFont(new Font("Tahoma", Font.PLAIN, 20));
		idNotFound.setBounds(162, 43, 209, 25);
		idNotFound.setVisible(false);
		memberIdTab.add(idNotFound);
		
		newMemberPane = new JPanel();
		newMemberPane.setVisible(false);
		newMemberPane.setBounds(6, 79, 554, 170);
		memberIdTab.add(newMemberPane);
		newMemberPane.setLayout(null);
		
		newMemberFirstName = new JTextField();
		newMemberFirstName.setBounds(110, 38, 118, 20);
		newMemberFirstName.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberPane.add(newMemberFirstName);
		newMemberFirstName.setColumns(10);
		
		JLabel lblNewLabel_3 = new JLabel("First Name");
		lblNewLabel_3.setBounds(0, 41, 96, 14);
		lblNewLabel_3.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberPane.add(lblNewLabel_3);
		
		JLabel lblNewLabel_4 = new JLabel("Last Name");
		lblNewLabel_4.setBounds(268, 41, 86, 14);
		lblNewLabel_4.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberPane.add(lblNewLabel_4);
		
		newMemberLastName = new JTextField();
		newMemberLastName.setBounds(378, 38, 118, 20);
		newMemberLastName.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberPane.add(newMemberLastName);
		newMemberLastName.setColumns(10);
		
		JLabel lblNewLabel_5 = new JLabel("Birthday (m/d/yyyy)");
		lblNewLabel_5.setBounds(0, 85, 156, 17);
		lblNewLabel_5.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberPane.add(lblNewLabel_5);
		
		newMemberDOB = new JTextField();
		newMemberDOB.setBounds(142, 83, 102, 20);
		newMemberDOB.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberPane.add(newMemberDOB);
		newMemberDOB.setColumns(10);
		
		JLabel lblNewLabel_6 = new JLabel("Gender");
		lblNewLabel_6.setBounds(300, 86, 54, 14);
		lblNewLabel_6.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberPane.add(lblNewLabel_6);
		
		newMemberGender = new JComboBox<Object>();
		newMemberGender.setBounds(380, 82, 54, 22);
		newMemberGender.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberGender.setModel(new DefaultComboBoxModel<Object>(new String[] {"", "M", "F"}));
		newMemberPane.add(newMemberGender);
		
		JButton createNewMember = new JButton("Submit");
		createNewMember.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				addNewMember();
			}
		});
		createNewMember.setBounds(0, 126, 89, 23);
		newMemberPane.add(createNewMember);
		
		JLabel lblNewLabel_7 = new JLabel("Create new membership using form below");
		lblNewLabel_7.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_7.setBounds(111, 0, 323, 14);
		newMemberPane.add(lblNewLabel_7);
		
		invalidFirstNameMessage = new JLabel("Error: cannot be blank or contain non letter characters");
		invalidFirstNameMessage.setFont(new Font("Tahoma", Font.PLAIN, 9));
		invalidFirstNameMessage.setForeground(Color.RED);
		invalidFirstNameMessage.setBounds(0, 57, 306, 14);
		invalidFirstNameMessage.setVisible(false);
		newMemberPane.add(invalidFirstNameMessage);
		
		invalidLastNameMessage = new JLabel("Error: cannot blank or contain non letter characters");
		invalidLastNameMessage.setFont(new Font("Tahoma", Font.PLAIN, 9));
		invalidLastNameMessage.setForeground(Color.RED);
		invalidLastNameMessage.setBounds(268, 57, 276, 14);
		invalidLastNameMessage.setVisible(false);
		newMemberPane.add(invalidLastNameMessage);
		
		invalidDOBMessage = new JLabel("Error: Date must be in form m/d/yyyy");
		invalidDOBMessage.setFont(new Font("Tahoma", Font.PLAIN, 9));
		invalidDOBMessage.setForeground(Color.RED);
		invalidDOBMessage.setBounds(0, 105, 228, 14);
		invalidDOBMessage.setVisible(false);
		newMemberPane.add(invalidDOBMessage);
		
		invalidGenderMessage = new JLabel("Error: Must choose an option");
		invalidGenderMessage.setForeground(Color.RED);
		invalidGenderMessage.setFont(new Font("Tahoma", Font.PLAIN, 9));
		invalidGenderMessage.setBounds(300, 105, 134, 14);
		invalidGenderMessage.setVisible(false);
		newMemberPane.add(invalidGenderMessage);
		
		JButton noThanks = new JButton("No Thanks");
		noThanks.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				reset();
			}
		});
		noThanks.setBounds(110, 126, 134, 23);
		newMemberPane.add(noThanks);
		
		newMemberIDPane = new JPanel();
		newMemberIDPane.setBounds(6, 260, 554, 40);
		memberIdTab.add(newMemberIDPane);
		newMemberIDPane.setVisible(false);
		newMemberIDPane.setLayout(null);
		
		JLabel lblNewLabel_8 = new JLabel("Membership Creation Succesfull, Your Member ID is: ");
		lblNewLabel_8.setBounds(0, 2, 390, 40);
		lblNewLabel_8.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberIDPane.add(lblNewLabel_8);
		
		newMemberID = new JLabel("New label");
		newMemberID.setFont(new Font("Tahoma", Font.PLAIN, 15));
		newMemberID.setBounds(400, 15, 115, 14);
		newMemberIDPane.add(newMemberID);
		
		JPanel bookSearchTab = new JPanel();
		tabbedPane.addTab("Book Search", null, bookSearchTab, null);
		tabbedPane.setEnabledAt(1, false);
		bookSearchTab.setLayout(null);
		
		noSearchResults = new JLabel("Library does not have any books matching your search terms");
		noSearchResults.setVisible(false);
		noSearchResults.setHorizontalAlignment(SwingConstants.CENTER);
		noSearchResults.setFont(new Font("Tahoma", Font.PLAIN, 15));
		noSearchResults.setBounds(10, 125, 540, 129);
		bookSearchTab.add(noSearchResults);
		
		JPanel panel = new JPanel();
		panel.setBounds(0, 34, 550, 41);
		bookSearchTab.add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel_1 = new JLabel("Search By: ");
		lblNewLabel_1.setBounds(6, 10, 76, 19);
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 15));
		panel.add(lblNewLabel_1);
		
		searchByISBN = new JRadioButton("ISBN");
		searchByISBN.setActionCommand("ISBN");
		searchByISBN.setSelected(true);
		buttonGroup.add(searchByISBN);
		searchByISBN.setBounds(88, 6, 59, 27);
		searchByISBN.setFont(new Font("Tahoma", Font.PLAIN, 15));
		panel.add(searchByISBN);
		
		JRadioButton searchByTitle = new JRadioButton("Title Contains");
		searchByTitle.setActionCommand("Title");
		buttonGroup.add(searchByTitle);
		searchByTitle.setBounds(153, 6, 130, 27);
		searchByTitle.setFont(new Font("Tahoma", Font.PLAIN, 15));
		panel.add(searchByTitle);
		
		JRadioButton searchByAuthor = new JRadioButton("Author (FirstName LastName)");
		searchByAuthor.setActionCommand("Author");
		buttonGroup.add(searchByAuthor);
		searchByAuthor.setBounds(280, 6, 264, 27);
		searchByAuthor.setFont(new Font("Tahoma", Font.PLAIN, 15));
		panel.add(searchByAuthor);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBounds(0, 85, 550, 41);
		bookSearchTab.add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel_2 = new JLabel("Search Term");
		lblNewLabel_2.setBounds(6, 8, 112, 19);
		lblNewLabel_2.setFont(new Font("Tahoma", Font.PLAIN, 15));
		panel_1.add(lblNewLabel_2);
		
		searchField = new JTextField();
		searchField.setBounds(128, 7, 317, 20);
		panel_1.add(searchField);
		searchField.setColumns(10);
		
		JButton searchButton = new JButton("Search");
		searchButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				search();
			}
		});
		searchButton.setBounds(455, 4, 85, 23);
		panel_1.add(searchButton);
		
		searchTermFormatError = new JLabel("Error: ISBN Format needs to be ##-#####-#####");
		searchTermFormatError.setForeground(Color.RED);
		searchTermFormatError.setFont(new Font("Tahoma", Font.PLAIN, 9));
		searchTermFormatError.setBounds(128, 27, 236, 14);
		searchTermFormatError.setVisible(false);
		panel_1.add(searchTermFormatError);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(10, 137, 540, 125);
		bookSearchTab.add(scrollPane);
		
		searchResultTable = new JTable();
		searchResultTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		scrollPane.setViewportView(searchResultTable);
		searchResultTable.setBorder(new LineBorder(new Color(0, 0, 0)));
		searchResultTable.setModel(new DefaultTableModel(
			new Object[][] {
			},
			new String[] {
				"ISBN", "Title", "Authors"
			}
		));
		
		JScrollPane scrollPane_1 = new JScrollPane();
		scrollPane.setColumnHeaderView(scrollPane_1);
		searchResultTable.getColumnModel().getColumn(0).setResizable(false);
		
		
		JPanel panel_2 = new JPanel();
		panel_2.setBounds(0, 0, 550, 41);
		bookSearchTab.add(panel_2);
		panel_2.setLayout(null);
		
		memberGreeting = new JLabel("Hello User!");
		memberGreeting.setBounds(10, 6, 208, 19);
		memberGreeting.setFont(new Font("Tahoma", Font.PLAIN, 15));
		panel_2.add(memberGreeting);
		
		JButton logOutButton = new JButton("Log Out");
		logOutButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				reset();
			}
		});
		logOutButton.setBounds(420, 6, 120, 23);
		panel_2.add(logOutButton);
		
		JButton slectBook = new JButton("Select Book");
		slectBook.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int rowSelected = searchResultTable.getSelectedRow();
				findBookSelected(rowSelected);
			}
		});
		slectBook.setBounds(229, 265, 132, 23);
		bookSearchTab.add(slectBook);
		
		noBookSelectedErrorMessage = new JLabel("Please select a book from the table above");
		noBookSelectedErrorMessage.setVisible(false);
		noBookSelectedErrorMessage.setFont(new Font("Tahoma", Font.PLAIN, 9));
		noBookSelectedErrorMessage.setForeground(Color.RED);
		noBookSelectedErrorMessage.setBounds(209, 286, 287, 14);
		bookSearchTab.add(noBookSelectedErrorMessage);
		
		allCopiesCheckedOutMessage = new JLabel("All copies of that book are checked out");
		allCopiesCheckedOutMessage.setVisible(false);
		allCopiesCheckedOutMessage.setFont(new Font("Tahoma", Font.PLAIN, 13));
		allCopiesCheckedOutMessage.setBounds(158, 286, 282, 14);
		bookSearchTab.add(allCopiesCheckedOutMessage);
		
		JPanel resultsTab = new JPanel();
		tabbedPane.addTab("Search Results", null, resultsTab, null);
		resultsTab.setLayout(null);
		
		JPanel panel_3 = new JPanel();
		panel_3.setBounds(25, 43, 504, 198);
		resultsTab.add(panel_3);
		panel_3.setLayout(null);
		
		JScrollPane scrollPane_2 = new JScrollPane();
		scrollPane_2.setBounds(0, 0, 504, 198);
		panel_3.add(scrollPane_2);
		
		bookLocationTable = new JTable();
		bookLocationTable.setRowSelectionAllowed(false);
		scrollPane_2.setViewportView(bookLocationTable);
		bookLocationTable.setModel(new DefaultTableModel(
			new Object[][] {
			},
			new String[] {
				"ISBN", "Title", "Library", "Shelf"
			}
		));
		
		JLabel lblNewLabel_9 = new JLabel("You can find the book here:");
		lblNewLabel_9.setFont(new Font("Tahoma", Font.PLAIN, 15));
		lblNewLabel_9.setBounds(26, 11, 380, 14);
		resultsTab.add(lblNewLabel_9);
		
		JButton btnNewButton = new JButton("Log Out");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				reset();
			}
		});
		btnNewButton.setBounds(214, 261, 119, 23);
		resultsTab.add(btnNewButton);
		tabbedPane.setEnabledAt(2, false);
	}
	


	protected void reset() {
		// TODO Auto-generated method stub
		this.hideErrorMessages();
		this.tabbedPane.setSelectedIndex(0);
		clearTableResults(this.bookLocationTable);
		clearTableResults(this.searchResultTable);
		this.searchField.setText("");
		this.searchByISBN.setSelected(true);
		this.memberID.setText("");
		this.newMemberDOB.setText("");
		this.newMemberFirstName.setText("");
		this.newMemberLastName.setText("");
		this.newMemberGender.setSelectedIndex(0);
		this.newMemberIDPane.setVisible(false);
		this.newMemberPane.setVisible(false);
		tabbedPane.setEnabledAt(1, false);
		tabbedPane.setEnabledAt(2, false);
		this.idNotFound.setVisible(false);
		
		
		
		
	}

	protected void findBookSelected(int rowSelected) {
		// TODO Auto-generated method stub
		this.hideErrorMessages();
		this.clearTableResults(this.bookLocationTable);
		if (rowSelected < 0) {
			this.noBookSelectedErrorMessage.setVisible(true);
			return;
		}
		String bookIsbn = (String) this.searchResultTable.getValueAt(rowSelected, 0);
		
		
		if(library.bookAvailable(bookIsbn)) {
			this.tabbedPane.setEnabledAt(2, true);
			tabbedPane.setSelectedIndex(2);
			this.updateSearchResultsTable(library.getBookLocation(bookIsbn), this.bookLocationTable);
		}
		else {
			this.allCopiesCheckedOutMessage.setVisible(true);
		}
		
	}

	
	
	public void search() {
		String action = buttonGroup.getSelection().getActionCommand();
		clearTableResults(this.searchResultTable);
		this.hideErrorMessages();
		System.out.println(action);
		switch(action) {
		case "ISBN":
			searchByISBN();
			break;
		case "Title":
			searchByTitle();
			break;
		case "Author":
			searchByAuthor();
			break;
		}
	}

	private void searchByAuthor() {
		System.out.println("Search by Author");
		if(!this.searchField.getText().trim().matches("[A-Za-z]+ [A-Za-z]+")) {
			this.searchTermFormatError.setText(authorFormatErrorMessage);
			this.searchTermFormatError.setVisible(true);
			return;
		}
		String[] author = this.searchField.getText().trim().split(" ");
		
		this.updateSearchResultsTable(library.searchByAuthor(author[0], author[1]), searchResultTable);
		
	}

	private void searchByTitle() {
		// TODO Auto-generated method stub
		System.out.println("Search by Title");
		this.updateSearchResultsTable(library.searchByTitle(this.searchField.getText().trim()), searchResultTable);
		
	}

	private void searchByISBN() {
		// TODO Auto-generated method stub
		
		System.out.println("Search by ISBN");
		String isbn = this.searchField.getText().trim();
		if(!validateISBNFormat(isbn)) {
			this.searchTermFormatError.setText(this.isbnFormatErrorMessage);
			this.searchTermFormatError.setVisible(true);
			return;
		}
		
		String[][] searchResults = library.searchByISBN(isbn);
		this.updateSearchResultsTable(searchResults, searchResultTable);
		
		
		
		
	}
	
	private void updateSearchResultsTable(String[][] newRows, JTable table ) {
		if(newRows.length == 0) {
			this.noSearchResults.setVisible(true);
		}
		DefaultTableModel tableModel = (DefaultTableModel) table.getModel();
		for (int i = 0 ; i < newRows.length; i++)
			tableModel.addRow(newRows[i]);
	}
	
	private void clearTableResults(JTable table) {
		// TODO Auto-generated method stub
		DefaultTableModel tableModel = (DefaultTableModel) table.getModel();
		tableModel.setRowCount(0);
		
		
	}

	private boolean validateISBNFormat(String isbn) {
		// TODO Auto-generated method stub
		return isbn.matches("[0-9]{2}-[0-9]{5}-[0-9]{5}");
	}

	protected void login() {
		// TODO Auto-generated method stub
		System.out.println("Login");
		System.out.println("Member ID = " + memberID.getText());
		if(memberID.getText().trim().isEmpty()) {
			idNotFound.setVisible(true);
			newMemberPane.setVisible(true);
			return;
		}
		String memberName = library.memberIDExists(memberID.getText().trim());
		if(memberName != null) {
			System.out.println("Member Exists");
			tabbedPane.setEnabledAt(1, true);
			tabbedPane.setSelectedIndex(1);
			this.memberGreeting.setText("Hello " + memberName + "!");
		}
		else {
			System.out.println("Member Does Not Exists");
			idNotFound.setVisible(true);
			newMemberPane.setVisible(true);
			
		}
		
	}
	
	private void addNewMember() {
		this.hideErrorMessages();
		boolean validEntries = true;
		if(!validateName(this.newMemberFirstName.getText().trim())) {
			validEntries = false;
			this.invalidFirstNameMessage.setVisible(true);
		}
		if(!validateName(this.newMemberLastName.getText().trim())) {
			validEntries = false;
			this.invalidLastNameMessage.setVisible(true);
		}
		if(!this.validateDateFormat(this.newMemberDOB.getText().trim())) {
			validEntries = false;
			this.invalidDOBMessage.setVisible(true);
		}
		if(((String)this.newMemberGender.getSelectedItem()).trim().isEmpty()) {
			this.invalidGenderMessage.setVisible(true);
			validEntries = false;
		}
		
		if(!validEntries) {
			return;
		}
		String memberID = library.addNewMember(this.newMemberFirstName.getText().trim(), this.newMemberLastName.getText().trim(), this.newMemberDOB.getText().trim(), (String)this.newMemberGender.getSelectedItem());
		this.newMemberID.setText(memberID);
		this.memberID.setText(memberID);
		this.newMemberIDPane.setVisible(true);
		
		
	}
	
	private boolean validateDateFormat(String dateString) {
		SimpleDateFormat inFormatter = new SimpleDateFormat("mm/dd/yyyy");
        try {
			Date date = inFormatter.parse(dateString);
			if (date != null) {
				return true;
			}
			
		} catch (ParseException e) {
		}
		return false;
	}
	
	private boolean validateName(String name) {
		if(name.isEmpty()) {
			return false;
		}
		
		if(!name.matches("[A-Za-z]+")) {
			return false;
		}
		return true;
		
	}
	
	private void hideErrorMessages() {
		this.invalidDOBMessage.setVisible(false);
		this.invalidLastNameMessage.setVisible(false);
		this.invalidFirstNameMessage.setVisible(false);
		this.invalidGenderMessage.setVisible(false);
		this.searchTermFormatError.setVisible(false);
		noBookSelectedErrorMessage.setVisible(false);
		allCopiesCheckedOutMessage.setVisible(false);
		noSearchResults.setVisible(false);
		
	}
}