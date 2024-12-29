// Define a Java class
public class STUDENT {
    // Data attributes
    private String Name;
    private String SID;
    private String Contact;

    // Constructor
    public STUDENT(String Name, String SID, String Contact) {
        this.Name = Name;
        this.SID = SID;
        this.Contact = Contact;
    }
    // Create an object using my name, my student id and contact
    public static void main(String[] args) {
        STUDENT student = new STUDENT("LIU SHENGWEI", "S1037766", "(+86)15312610071");
        System.out.println(student.Name);
    }
}