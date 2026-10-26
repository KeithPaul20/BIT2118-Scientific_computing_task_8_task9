# Task 8: Iterative Methods for Linear Systems

## A. Input values and mathematical operation
- **Input:**  
  - Coefficient matrix **A** (represents either heat balance equations for a rod or resistor coefficients for an electrical network).  
  - Vector **b** (boundary conditions for temperatures, or current injections for the resistor network).  
- **Operation:**  
  - Jacobi and Gauss-Seidel iterative methods are applied to solve the linear system **Ax = b**.  
  - Both methods repeatedly update estimates of the solution until the error between successive iterations is below a tolerance.

---

## B. Parameter change
- Changing the **tolerance** from `1e-8` to `1e-4` makes the algorithm stop earlier.  
  - Result: Faster runtime but less accurate solution.  
- Changing the **boundary condition** (e.g., left boundary from 100 °C to 80 °C, or current injection from 5 A to 3 A) shifts the final solution values.  
  - Result: All interior point values adjust accordingly.

---

## C. Meaning of the output
The program produces three sets of results:

1. **Jacobi Temperatures / Node Voltages**  
   - These are the approximate values computed using the Jacobi method.  
   - Each unknown is updated using only the previous iteration’s estimates.  
   - Convergence is slower, so the values approach the exact solution gradually.  
   - Example output (resistor network):  
     ```
     Jacobi node voltages: [ 0.48879837  0.04276985 -0.19755602]
     ```

2. **Gauss-Seidel Temperatures / Node Voltages**  
   - These are the approximate values computed using the Gauss-Seidel method.  
   - Each unknown is updated immediately within the same iteration, using the most recent estimates.  
   - This makes convergence faster, so the values reach the exact solution in fewer iterations.  
   - Example output (resistor network):  
     ```
     Gauss-Seidel node voltages: [ 0.48879837  0.04276986 -0.19755601]
     ```

3. **Direct Solution**  
   - This is the exact solution obtained by solving **Ax = b** directly with `np.linalg.solve`.  
   - It serves as the benchmark to check accuracy of both iterative methods.  
   - Example output (resistor network):  
     ```
     Direct solution (exact voltages): [ 0.48879837  0.04276986 -0.19755601]
     ```

---

## D. Graph interpretation
- The error vs. iteration plot (logarithmic scale) shows convergence speed.  
- **Jacobi method:** Converges steadily but slower.  
- **Gauss-Seidel method:** Converges faster because it uses updated values immediately within each iteration.  
- The downward slope of the curves indicates that both methods are approaching the exact solution.

---

## E. Modified real-world case
- **Case:** Electrical resistor network solved with Jacobi and Gauss-Seidel.  
- **Assumptions:** Each node follows Kirchhoff’s Current Law, forming linear equations similar to the heat balance system.  
- **Input data:**  
  - Matrix **A** from resistor coefficients.  
  - Vector **b** from current injections at nodes.  
- **Output:** Node voltages across the network.  
- **Interpretation:**  
  - Iterative methods approximate voltages at each node.  
  - The convergence graph shows how quickly each method stabilizes to the correct voltages.  
  - Gauss-Seidel again converges faster than Jacobi.

---

## F. Files in this task
- `Task_08_iterative_linear.py` → Original heat conduction example.  
- `Task_08_resistor_network.py` → Modified electrical network case.  
- `README.md` → Documentation with answers, explanations, and graph interpretations.
