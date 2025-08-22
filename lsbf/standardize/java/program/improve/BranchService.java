/**
 * This class provides services related to the Branch entity.
 * It manages a list of branches and offers methods to add new branches.
 */
public class BranchService {
    // List to store all branches
    private List<Branch> branches;

    /**
     * Adds a new branch to the list.
     * Performs business logic validation to ensure that the branch does not already exist.
     * 
     * @param branch The branch to be added.
     * @throws BusinessException if the branch with the same ID already exists.
     */
    public void addBranch(Branch branch) {
        // Validate business logic: check if the branch already exists
        if (isBranchExists(branch.getBId())) {
            throw new BusinessException("Branch already exists");
        }
        // Add the branch to the list
        branches.add(branch);
    }

    // You may need to initialize the 'branches' list in the constructor
    public BranchService() {
        this.branches = new ArrayList<>();
    }

    /**
     * Checks if a branch with the given ID already exists in the list.
     * 
     * @param branchId The ID of the branch to check.
     * @return true if the branch exists, false otherwise.
     */
    private boolean isBranchExists(String branchId) {
        for (Branch b : branches) {
            if (b.getBId().equals(branchId)) {
                return true;
            }
        }
        return false;
    }
}