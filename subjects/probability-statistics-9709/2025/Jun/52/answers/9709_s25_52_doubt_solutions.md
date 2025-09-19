# 9709 S25 Paper 52 - Complete Solutions for Doubt Questions

## Question 4: Road Junction Probability

### Question 4(a): All three vehicles go in different directions

**Problem**: Find the probability that the next three vehicles approaching this junction from Bromley all go in different directions.

**Given**: 30% turn left, 25% turn right, 45% go straight on.

**Solution**:
For three vehicles to go in different directions, we need one vehicle in each direction.

The number of ways to arrange three different directions = 3! = 6

Probability = 0.3 × 0.25 × 0.45 × 6 = 0.2025

**Answer**: 0.2025 or 81/400

---

### Question 4(b): 1st vehicle to go left is before the 9th vehicle

**Problem**: Find the probability that, from the vehicles approaching this junction from Bromley today, the 1st vehicle to go left is before the 9th vehicle.

**Solution**:
This is equivalent to finding the probability that at least one of the first 8 vehicles turns left.

P(1st vehicle to go left is before 9th) = 1 - P(none of first 8 vehicles go left)
= 1 - (0.7)^8
= 1 - 0.05764801
= 0.942

**Answer**: 0.942

---

### Question 4(c): 2nd vehicle to go left is the 7th vehicle

**Problem**: Find the probability that, from the vehicles approaching this junction from Bromley today, the 2nd vehicle to go left is the 7th vehicle.

**Solution**:
For the 2nd vehicle to go left to be the 7th vehicle:
- Exactly one of the first 6 vehicles must go left
- The 7th vehicle must go left

Using negative binomial distribution:
P(2nd left on 7th vehicle) = C(6,1) × (0.3)^2 × (0.7)^5
= 6 × 0.09 × 0.16807
= 0.0908

**Answer**: 0.0908

---

## Question 5: Travel Times to College

### Question 5(a): Cumulative frequency graph

**Solution**: 
Plot the following points and draw a smooth curve:
- (10, 34)
- (20, 86) 
- (30, 142)
- (40, 208)
- (60, 265)
- (90, 300)

The curve should start at (0,0) and be smooth, not linear segments.

---

### Question 5(b): Find k where 120 students take more than k minutes

**Solution**:
If 120 students take more than k minutes, then 300 - 120 = 180 students take k minutes or less.

From the cumulative frequency graph, read across from 180 on the y-axis to meet the curve, then read down to find k.

**Answer**: k = 35 minutes

---

### Question 5(c): Calculate mean and standard deviation

**Solution**:

**Step 1: Find frequencies**
- 0 ≤ t < 10: 34
- 10 ≤ t < 20: 86 - 34 = 52
- 20 ≤ t < 30: 142 - 86 = 56  
- 30 ≤ t < 40: 208 - 142 = 66
- 40 ≤ t < 60: 265 - 208 = 57
- 60 ≤ t < 90: 300 - 265 = 35

**Step 2: Find midpoints**
- 5, 15, 25, 35, 50, 75

**Step 3: Calculate mean**
Mean = (34×5 + 52×15 + 56×25 + 66×35 + 57×50 + 35×75) ÷ 300
= (170 + 780 + 1400 + 2310 + 2850 + 2625) ÷ 300
= 10135 ÷ 300
= 33.8 minutes

**Step 4: Calculate variance**
Variance = [(34×5² + 52×15² + 56×25² + 66×35² + 57×50² + 35×75²) ÷ 300] - (33.8)²
= (34×25 + 52×225 + 56×625 + 66×1225 + 57×2500 + 35×5625) ÷ 300 - 1142.44
= 467775 ÷ 300 - 1142.44
= 1559.25 - 1142.44
= 416.81

Standard deviation = √416.81 = 20.4 minutes

**Answer**: Mean = 33.8 minutes, Standard deviation = 20.4 minutes

---

## Question 6: AMALGAMATE Letter Arrangements

### Question 6(a): M at beginning and end, no As together

**Problem**: Find arrangements with M at beginning, M at end, and no As together.

**Given**: AMALGAMATE has letters A, M, A, L, G, A, M, A, T, E
- 4 As, 2 Ms, 1 each of L, G, T, E

**Solution**:
With Ms fixed at both ends: M _ _ _ _ _ _ _ _ M

Remaining letters: A, A, A, A, L, G, T, E (8 letters with 4 As)

Method: Arrange non-A letters first, then insert As in gaps.

Non-A letters: L, G, T, E → 4! = 24 arrangements
This creates 5 gaps: _L_G_T_E_

Choose 4 gaps from 5 for the As: C(5,4) = 5

Total arrangements = 24 × 5 = 120

**Answer**: 120

---

### Question 6(b): Exactly 3 letters between the two Ms

**Problem**: Find arrangements with exactly 3 letters between the two Ms.

**Solution**:
Pattern: M _ _ _ M _ _ _ _ _

The 8 remaining letters (4 As, L, G, T, E) need to be arranged in 8 positions.

Total arrangements = 8! ÷ 4! = 1680
Ways to choose positions for the Ms with 3 letters between = 6

Total = (8! ÷ 4!) × 6 = 1680 × 6 = 10080

**Answer**: 10080

---

### Question 6(c): Select 5 letters with at least one M and at least two As

**Problem**: From AMALGAMATE, select 5 letters including at least one M and at least two As.

**Solution**:
Available letters: 4 As, 2 Ms, 4 others (L, G, T, E)

Cases for selecting 5 letters with ≥1 M and ≥2 As:

**Case 1: 1M, 2A, 2 others**
- Choose 1M from 2: C(2,1) = 2
- Choose 2A from 4: C(4,2) = 6  
- Choose 2 from 4 others: C(4,2) = 6
- Total: 2 × 6 × 6 = 72... Wait, this doesn't match the mark scheme.

Let me recalculate using the mark scheme approach:

**Case 1: MMAAA** → 1 way
**Case 2: MMAA + 1 other** → C(4,1) = 4 ways
**Case 3: MAA + 2 others** → C(4,2) = 6 ways  
**Case 4: MAAA + 1 other** → C(4,1) = 4 ways
**Case 5: MAAAA** → 1 way

Total = 1 + 4 + 6 + 4 + 1 = 16

**Answer**: 16

---

## Mark Scheme Alignment

These solutions follow the mark scheme exactly, showing:
- Complete working with clear steps
- Correct mathematical notation
- Final answers that match the mark scheme requirements
- Alternative methods where applicable

All answers are given to appropriate accuracy (3 significant figures for non-exact answers).
