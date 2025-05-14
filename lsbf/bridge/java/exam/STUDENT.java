/**
 * This class represents a Student entity
 * It stores basic information about a student including name, student ID and contact details
 */
public class STUDENT {
    // Data attributes - Store the basic information of a student
    private String Name;    // Stores the full name of the student
    private String SID;     // Stores the unique student identification number
    private String Contact; // Stores the contact information (phone number)

    /**
     * Constructor to initialize a new Student object
     * @param Name The full name of the student
     * @param SID The student's identification number
     * @param Contact The student's contact information
     */
    public STUDENT(String Name, String SID, String Contact) {
        this.Name = Name;
        this.SID = SID;
        this.Contact = Contact;
    }

    /**
     * Main method to demonstrate the creation of a student object
     * Creates a student object with personal information and prints the name
     */
    public static void main(String[] args) {
        // Create a new student object with specific details
        STUDENT student = new STUDENT("Suntao", "S1038988", "wechat:xxxxxx");
        // Print out the student's name
        System.out.println(student.Name);
    }
}