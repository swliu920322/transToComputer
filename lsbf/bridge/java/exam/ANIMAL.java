/**
 * This class represents an Animal in the FunWorld Zoo system
 * It stores basic information about zoo animals including name, ID and description
 */
public class ANIMAL {
    // Data attributes - Store the basic information of an animal
    private String AName;      // Stores the name of the animal
    private String AID;        // Stores the unique identifier of the animal
    private String Description; // Stores the detailed description of the animal

    /**
     * Constructor to initialize a new Animal object
     * @param AName The name of the animal
     * @param AID The unique identifier of the animal
     * @param Description A detailed description of the animal
     */
    public ANIMAL(String AName, String AID, String Description) {
        this.AName = AName;
        this.AID = AID;
        this.Description = Description;
    }

    /**
     * Main method to demonstrate the creation and display of animal objects
     * Creates three different animals and displays their information
     */
    public static void main(String[] args) {
        // Create a giraffe object with its specific details
        ANIMAL giraffe = new ANIMAL("Giraffe", "G001",
                "A tall female giraffe with distinctive spotted pattern, height 5.5m");

        // Create a penguin object with its specific details
        ANIMAL penguin = new ANIMAL("Emperor Penguin", "P001",
                "A playful penguin that loves swimming and sliding on ice");

        // Create a monkey object with its specific details
        ANIMAL monkey = new ANIMAL("Capuchin Monkey", "M001",
                "An intelligent monkey that can use tools and loves to interact with visitors");

        // Display header for the zoo animals list
        System.out.println("\n=== FunWorld Zoo Animals ===\n");
        // Display information for each animal with spacing between them
        giraffe.displayInfo();
        System.out.println();
        penguin.displayInfo();
        System.out.println();
        monkey.displayInfo();
    }

    /**
     * Method to display the information of an animal
     * Prints the animal's details in a formatted manner with decorative borders
     */
    public void displayInfo() {
        System.out.println("════════════════════════════════════════");
        System.out.println("Animal Information");
        System.out.println("Name: " + AName);
        System.out.println("ID: " + AID);
        System.out.println("Description: " + Description);
        System.out.println("════════════════════════════════════════");
    }
}