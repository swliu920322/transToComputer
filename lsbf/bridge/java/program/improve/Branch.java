/**
 * Represents a branch in a company, containing a list of employees and warehouses.
 */
public class Branch {
    // List of employees belonging to this branch
    private List<Employee> employees;
    // List of warehouses belonging to this branch
    private List<Warehouse> warehouses;
    
    /**
     * Adds an employee to the branch if the employee's branch ID matches the branch's ID.
     * 
     * @param employee The employee to be added.
     */
    public void addEmployee(Employee employee) {
        // Check if the employee's branch ID matches the branch's ID
        if (employee.getBId().equals(this.getBId())) {
            // Add the employee to the list if the IDs match
            employees.add(employee);
        }
    }
}
