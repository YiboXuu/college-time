import java.sql.*;
import java.io.*;
import java.util.ArrayList;

public class Lab4 {

    private static final String NOT_AVAILABLE_VALUE = "N/A";

    public static void main(String args[]){

        // connect to the SQL Server
        Connection connection = connectToSQL();

        if (connection != null) {

            // 	read in and parse the activity file in XML format
            try {
                Lab4_xml showXML = new Lab4_xml();
                showXML.readXML ("data.xml");
                ArrayList<BorrowedBy> borrowedByList = showXML.getBorrowedByArrayList();

                for (BorrowedBy bb : borrowedByList) {
                    // 	If the transaction is a checkin, simply update the corresponding record appropriately
                    //System.out.println(("Check in date value: " + bb.getCheckin_date()));
                    if (!bb.getCheckin_date().equals("N/A")) {
                        System.out.println(("Checking in book."));
                        checkInBook(connection, bb);
                    } else {
                        //  If the transaction is a checkout, a new record is created
                        System.out.println(("Checking out book."));
                        checkOutBook(connection, bb);
                    }
                }

            }catch( Exception e ) {
                e.printStackTrace();
            }

        } else {
            System.out.println(("USAGE: No connection found. Exiting program."));
            System.exit(1);
        }
    }

    private static Connection connectToSQL() {
        Connection con = null;

        try {
            // Register the JDBC driver for MySQL.
            Class.forName("com.mysql.jdbc.Driver");

            // Define URL of database server for
            // database named 'user' on the faure.
            String url =
                    "jdbc:mysql://faure/yiboxu?useTimezone=true&serverTimezone=UTC";

            // Get a connection to the database for a
            // user named 'user' with the password
            // 123456789.
            con = DriverManager.getConnection(
                    url, "yiboxu", "831673550");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return con;
    }

    // executes check in SQL statements that inserts data into the appropriate relation tables
    private static void checkInBook(Connection connection, BorrowedBy borrowedBy){
        try {
               	Statement stmt;
               	ResultSet rs;
            	stmt = connection.createStatement();
            	rs = stmt.executeQuery("SELECT ISBN FROM BorrowedBy WHERE CheckinDate IS Null AND ISBN = '" + borrowedBy.getIsbn() + "';");
				if(rs.next()){
				
                stmt = connection.createStatement();
                stmt.executeUpdate("UPDATE BorrowedBy SET CheckinDate = '" + borrowedBy.getCheckin_date() + "' WHERE ISBN = '" + borrowedBy.getIsbn() + "' AND MemberId = '" + borrowedBy.getMember_id() + "' AND Library ='"+borrowedBy.getLibrary() +"' AND CheckinDate IS NULL;");

                System.out.println("The book with the ISBN " + borrowedBy.getIsbn() + " is now checked in.");
                }else{
                System.out.println("ERROR: Nobody borrowed this book, the ISBN is "+borrowedBy.getIsbn()+".");
                }
            
				System.out.println();
        } catch( Exception e ) {
            e.printStackTrace();
        }
    }

    // executes check in SQL statements that inserts data into the appropriate relation tables
    private static void checkOutBook(Connection connection, BorrowedBy borrowedBy) {
        try {
             Statement stmt;
             ResultSet rs;
            stmt = connection.createStatement();
            rs = stmt.executeQuery("SELECT ISBN,LibraryName FROM Book B natural join LocatedAt A WHERE B.ISBN = '" + borrowedBy.getIsbn() + "' AND A.LibraryName ='"+borrowedBy.getLibrary()+"';");
			if(rs.next()){
             stmt = connection.createStatement();
             stmt.executeUpdate("INSERT INTO BorrowedBy VALUES ('" + borrowedBy.getMember_id() + "', '" + borrowedBy.getIsbn() + "', '" + borrowedBy.getLibrary() + "', '" + borrowedBy.getCheckout_date() + "', Null);");
            
			
            System.out.println("The book with the ISBN " + borrowedBy.getIsbn() + " is now checked out");
            }else{
            System.out.println("ERROR, No this book checked out information, this book ISBN is"+ borrowedBy.getIsbn()+ "." );
            }
			System.out.println();
        } catch( Exception e ) {
            e.printStackTrace();
        }
    }

}


