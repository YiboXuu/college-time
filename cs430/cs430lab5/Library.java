import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

public class Library {

	public static final String ANSI_RED = "\u001B[31m";
	public static final String ANSI_RESET = "\u001B[0m";
	private Connection con;

	public Library() {
		try {

			//            Class.forName("com.mysql.jdbc.Driver");

//			String url =
//					"jdbc:mysql://192.168.1.126/library";
            String url =
                   "jdbc:mysql://faure/yiboxu?useTimezone=true&serverTimezone=UTC";
           

			con = DriverManager.getConnection(
					url,"yiboxu", "831673550");
			

		}catch( Exception e ) {
			e.printStackTrace();

		}
	}

	public String addNewMember(String firstName, String lastName, String dob, String gender) {
		Statement stmt;

		String query;
		int memberID = -1;
		try{
			memberID = getNextMemberID();
			query = String.format("INSERT INTO Member VALUES\n (%d, '%s', '%s', '%s', '%s');", memberID, firstName, lastName, this.getSQLDateFormat(dob), gender );
			System.out.println(query);
			stmt = con.createStatement();
			stmt.executeUpdate(query);



		}catch( SQLException e ) {
			e.printStackTrace();

		}


		return "" + memberID;

	}

	public boolean bookAvailable(String isbn) {
		String totalCheckedOutQuery = String.format("select count(MemberID) totalCheckedOut\r\n" + 
				"FROM Book Natural Join BorrowedBy\r\n" + 
				"where ISBN = '%s' and CheckinDate is null;", isbn);

		String totalCopiesQuery = String.format("SELECT sum(TotalCopies) as totalCopies\r\n" + 
				"FROM LocatedAt\r\n" + 
				"WHERE ISBN = '%s';", isbn);
		ResultSet totalCheckedOutRs = executeQuery(totalCheckedOutQuery);
		ResultSet totalCopies = executeQuery(totalCopiesQuery);
		try {
			totalCheckedOutRs.first();
			int totalCheckedOut = totalCheckedOutRs.getInt("totalCheckedOut");
			totalCopies.first();
			int totalCopiesAvailable = totalCopies.getInt("totalCopies");
			return (totalCopiesAvailable - totalCheckedOut ) > 0;

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}


		return false;
	}

	public String memberIDExists(String MemberID) {
		ResultSet result = executeQuery("Select * FROM Member Where MemberID = " + MemberID +";");


		try {
			result.first();
			return result.getString("FirstName");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			return null;
		}
	}

	public ArrayList<HashMap<String, String>> searchByAuthor(String authorName){
		return null;

	}

	public String[][] searchByISBN(String isbn){
		String query = String.format("SELECT ISBN, Book.Title, GROUP_CONCAT(Author.FirstName, ' ',Author.LastName) as Authors\r\n" + 
				"FROM (Book NATURAL JOIN WrittenBy NATURAL JOIN Author)\r\n" + 
				"WHERE ISBN = '%s'\n" +
				"Group by  Book.Title;", isbn);
		System.out.println(query);
		ResultSet rs = executeQuery(query);
		try {
			rs.last();
			int numResults = rs.getRow();
			rs.beforeFirst();
			String[][] resultTable = new String[numResults][3];
			int rowIndex = 0;
			while(rs.next()) {
				resultTable[rowIndex][0] = rs.getString("ISBN");
				resultTable[rowIndex][1] = rs.getString("Title");
				resultTable[rowIndex][2] = rs.getString("Authors");
				rowIndex++;

			}
			return resultTable;
		} catch (SQLException e) {


		}

		return null;
	}

	public String [][] getBookLocation(String isbn) {
		String query = String.format("SELECT ISBN, Book.Title, LibraryName, Shelf\r\n" + 
				"FROM LocatedAt NATURAL JOIN Book\r\n" + 
				"WHERE ISBN = '%s';", isbn);
		ResultSet rs = this.executeQuery(query);
		return this.organizeReturnData(rs, new String [] {"ISBN", "Title", "LibraryName", "Shelf"});
	}
	
	public String[][] searchByTitle(String title){
		String query = String.format("SELECT ISBN, Book.Title, GROUP_CONCAT(Author.FirstName, ' ',Author.LastName) as Authors\r\n" + 
				"FROM (Book NATURAL JOIN WrittenBy NATURAL JOIN Author)\r\n" + 
				"WHERE Book.Title LIKE '%%%s%%'\r\n" + 
				"Group by  Book.Title;", title);

		ResultSet rs = this.executeQuery(query);
		return this.organizeReturnData(rs, new String [] {"ISBN", "Title", "Authors"});
	}
	
	public String [][] searchByAuthor(String firstName, String lastName){
		String query = String.format("SELECT ISBN, Book.Title, GROUP_CONCAT(Author.FirstName, ' ',Author.LastName) as Authors\r\n" + 
				"FROM (Book NATURAL JOIN WrittenBy NATURAL JOIN Author)\r\n" + 
				"WHERE ISBN in (\r\n" + 
				"    select ISBN\r\n" + 
				"    FROM WrittenBy NATURAL JOIN Author\r\n" + 
				"    WHERE Author.FirstName = '%s' and Author.LastName = '%s'\r\n" + 
				"    )\r\n" + 
				"Group by  Book.Title;", firstName, lastName);
		ResultSet rs = this.executeQuery(query);
		return this.organizeReturnData(rs, new String [] {"ISBN", "Title", "Authors"});
	}
	
	private String[][] organizeReturnData(ResultSet rs, String [] columnNames){
		try {
			rs.last();
			int numResults = rs.getRow();
			rs.beforeFirst();
			String[][] resultTable = new String[numResults][columnNames.length];
			int rowIndex = 0;
			while(rs.next()) {
				for (int i = 0; i < columnNames.length; i++) {
					resultTable[rowIndex][i] = rs.getString(columnNames[i]);
				}
				rowIndex++;

			}
			return resultTable;
		} catch (SQLException e) {


		}

		return null;
	}
	
	private String getSQLDateFormat(String dateString) {
		SimpleDateFormat inFormatter = new SimpleDateFormat("mm/dd/yyyy");
		Date date;
		try {
			date = inFormatter.parse(dateString);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			date=null;
		}
		SimpleDateFormat outFormatter = new SimpleDateFormat("yyyy-m-d");
		return outFormatter.format(date);
	}
	
	private ResultSet executeQuery(String query){
		System.out.println(query);
		Statement stmt;

		try{

			stmt = con.createStatement();

			try{
				stmt.executeQuery(query);
				return stmt.getResultSet();

			}catch(Exception e){
				System.out.print(ANSI_RED);
				System.out.println("ERROR: The Following Operation Failed:");
				System.out.print("\tERROR MESSAGE: ");
				System.out.println(e.getMessage());
				System.out.print(ANSI_RESET);

			} 
		}catch( Exception e ) {
			e.printStackTrace();

		}
		return null;


	}

	private int getNextMemberID() throws SQLException {
		String query = "SELECT max(MemberID) as MemberID FROM Member;";
		ResultSet result = this.executeQuery(query);
		result.first();
		return Integer.parseInt(result.getString("MemberID")) + 1;
	}
}