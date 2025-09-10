# Examiner Tips – Probability & Statistics 9709/52 (March 2020)
**Paper 5: Probability & Statistics 1**

---

## Question 1 – Combinations
- ✅ **Key insight**: Recognize that Ranuf and Saed's positions are fixed, reducing the problem.
- ✅ **Method**: Use C(38, 34) = C(38, 4) for easier calculation.
- ⚠️ **Common mistake**: Trying to arrange all 40 members without considering the constraints.
- ⚠️ **Calculation error**: Forgetting to use the symmetry property of combinations.

---

## Question 2 – Geometric and Binomial Distributions

### Part (a) – Geometric Distribution
- ✅ **Setup**: Clearly identify p = 1/3 (success) and q = 2/3 (failure).
- ✅ **Formula**: P(X = r) = q^(r-1) × p for geometric distribution.
- ⚠️ **Common mistake**: Using binomial instead of geometric distribution.
- ⚠️ **Calculation error**: Incorrect powers when computing (2/3)^n.

### Part (b) – Probability Distribution Table
- ✅ **Recognition**: Identify X ~ B(3, 1/3) immediately.
- ✅ **Table format**: Include x values, probabilities, and calculations.
- ⚠️ **Common mistake**: Not showing the binomial coefficient calculations.
- ⚠️ **Verification**: Probabilities should sum to 1.

### Part (c) – Expected Value
- ✅ **Formula**: For binomial distribution, E(X) = np.
- ✅ **Quick calculation**: 3 × (1/3) = 1.
- ⚠️ **Common mistake**: Using the long method E(X) = Σx·P(X=x) unnecessarily.

---

## Question 3 – Normal Distribution

### Part (a) – Finding Standard Deviation
- ✅ **Setup**: P(X > 87) = 0.22, so P(X ≤ 87) = 0.78.
- ✅ **Standardization**: Use Z = (X - μ)/σ correctly.
- ✅ **Tables**: Find Φ^(-1)(0.78) ≈ 0.772 from inverse normal tables.
- ⚠️ **Common mistake**: Using 0.22 directly instead of 0.78.
- ⚠️ **Table error**: Misreading normal tables or using wrong direction.

### Part (b) – Probability Calculation
- ✅ **Interpretation**: |X - 82| < 4 means 78 < X < 86.
- ✅ **Symmetry**: Use 2Φ(z) - 1 for symmetric intervals around the mean.
- ⚠️ **Common mistake**: Forgetting to use the calculated σ from part (a).
- ⚠️ **Calculation error**: Incorrect standardization or table lookup.

---

## Question 4 – Permutations with Restrictions

### Part (a) – Fixed Positions
- ✅ **Strategy**: Fix red candles at ends, arrange remaining candles.
- ✅ **Formula**: Use multinomial coefficient 9!/(3!×6!).
- ⚠️ **Common mistake**: Trying to place red candles in different ways.

### Part (b) – Multiple Constraints
- ✅ **Method**: Use inclusion-exclusion principle.
- ✅ **Step 1**: Treat blue candles as one unit.
- ✅ **Step 2**: Calculate arrangements where red candles are together.
- ✅ **Step 3**: Subtract unwanted arrangements.
- ⚠️ **Common mistake**: Not considering all constraint combinations.
- ⚠️ **Logic error**: Incorrect application of inclusion-exclusion.

---

## Question 5 – Binomial and Normal Approximation

### Part (a) – Binomial Probability
- ✅ **Setup**: X ~ B(8, 0.7), find P(X < 6) = P(X ≤ 5).
- ✅ **Strategy**: Use complement: 1 - P(X ≥ 6).
- ✅ **Calculation**: Show all binomial probability calculations clearly.
- ⚠️ **Common mistake**: Confusing "less than 6" with "at most 6".
- ⚠️ **Calculation error**: Errors in binomial coefficient or probability calculations.

### Part (b) – Normal Approximation
- ✅ **Conditions**: Check np > 5 and n(1-p) > 5 for validity.
- ✅ **Parameters**: μ = np = 84, σ² = np(1-p) = 25.2.
- ✅ **Continuity correction**: P(X > 75) becomes P(Y > 75.5).
- ⚠️ **Common mistake**: Forgetting continuity correction.
- ⚠️ **Setup error**: Using wrong direction for inequality after standardization.

---

## Question 6 – Conditional Probability and Tree Diagrams

### Part (a) – Tree Diagram
- ✅ **Initial probabilities**: P(Red from A) = 7/8, P(Blue from A) = 1/8.
- ✅ **Conditional probabilities**: Consider how Box B composition changes.
- ⚠️ **Common mistake**: Not updating Box B probabilities based on transfer.

### Part (b) – Different Colors
- ✅ **Method**: P(Red,Blue) + P(Blue,Red).
- ✅ **Calculation**: Use tree diagram probabilities.
- ⚠️ **Common mistake**: Only considering one case of different colors.

### Part (c) – Bayes' Theorem
- ✅ **Formula**: P(A|B) = P(A∩B)/P(B).
- ✅ **Total probability**: Calculate P(Blue from B) using all paths.
- ⚠️ **Common mistake**: Confusing conditional probability direction.
- ⚠️ **Calculation error**: Errors in fraction arithmetic.

---

## Question 7 – Statistics and Cumulative Frequency

### Part (a) – Cumulative Frequency Graph
- ✅ **Points**: Plot at upper class boundaries (9.5, 14.5, 19.5, 30.5).
- ✅ **Curve**: Draw smooth curve through points.
- ⚠️ **Common mistake**: Plotting at class midpoints instead of boundaries.

### Part (b) – Percentiles
- ✅ **Understanding**: 40% have length d or more means 60% have length less than d.
- ✅ **Reading**: Find where cumulative frequency = 90.
- ⚠️ **Common mistake**: Using 40% directly instead of 60%.

### Part (c) – Variance Calculation
- ✅ **Formula**: Var(X) = (Σfx²/n) - x̄².
- ✅ **Midpoints**: Use class midpoints for calculations.
- ✅ **Method**: Show Σfx² calculation clearly.
- ⚠️ **Common mistake**: Using class boundaries instead of midpoints.
- ⚠️ **Calculation error**: Arithmetic errors in large calculations.

---

## General Exam Strategy

### Time Management
- **Question 1-2**: Should take ~15 minutes total
- **Question 3**: Allow 10-12 minutes
- **Question 4**: Allow 8-10 minutes  
- **Question 5**: Allow 12-15 minutes
- **Question 6**: Allow 12-15 minutes
- **Question 7**: Allow 12-15 minutes

### Common Pitfalls
- ⚠️ **Units**: Always include appropriate units in final answers
- ⚠️ **Rounding**: Follow the 3 significant figures rule unless stated otherwise
- ⚠️ **Working**: Show all steps clearly - no marks for calculator-only answers
- ⚠️ **Notation**: Use correct mathematical notation (e.g., P(X = x), not P(x))

### Assessment Objectives
- **AO1 (Knowledge)**: Define terms, state formulae, recall facts
- **AO2 (Application)**: Apply methods to given contexts
- **AO3 (Analysis)**: Perform calculations, manipulate expressions
- **AO4 (Evaluation)**: Interpret results, make conclusions

### Success Tips
- ✅ **Read carefully**: Understand what the question is asking
- ✅ **Show working**: Even if you use a calculator, show the setup
- ✅ **Check answers**: Do quick sense-checks on your results
- ✅ **Use diagrams**: Tree diagrams and sketches can clarify thinking
- ✅ **State assumptions**: When using approximations, state conditions
