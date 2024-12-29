// Define a Java class
public class ANIMAL {
    // Data attributes
    private String AName;
    private String AID;
    private String Description;

    //  Constructor
    public ANIMAL(String AName, String AID, String Description) {
        this.AName = AName;
        this.AID = AID;
        this.Description = Description;
    }
    // Create THREE ANIMAL objects
    public static void main(String[] args) {
        ANIMAL giraffe = new ANIMAL("Giraffe", "G001",
                "A tall female giraffe with distinctive spotted pattern, height 5.5m");

        ANIMAL penguin = new ANIMAL("Emperor Penguin", "P001",
                "A playful penguin that loves swimming and sliding on ice");

        ANIMAL monkey = new ANIMAL("Capuchin Monkey", "M001",
                "An intelligent monkey that can use tools and loves to interact with visitors");

        System.out.println("\n=== FunWorld Zoo Animals ===\n");
        giraffe.displayInfo();
        System.out.println();
        penguin.displayInfo();
        System.out.println();
        monkey.displayInfo();
    }

    public void displayInfo() {
        System.out.println("════════════════════════════════════════");
        System.out.println("Animal Information");
        System.out.println("Name: " + AName);
        System.out.println("ID: " + AID);
        System.out.println("Description: " + Description);
        System.out.println("════════════════════════════════════════");
    }
}