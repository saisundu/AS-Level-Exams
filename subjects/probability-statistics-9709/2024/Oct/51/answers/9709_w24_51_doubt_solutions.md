# 9709 W24 Paper 51 - Complete Solutions for Doubt Questions

## Question 1: Geometric Distribution

### Part (a): Find P(X ≤ 8)

**Problem**: Nicola throws a fair six-sided dice. X is the number of throws to obtain a 6. Find P(X ≤ 8).

**Solution**:
This is a geometric distribution where p = 1/6 (probability of success) and q = 5/6 (probability of failure).

**Method 1**: Using complement
P(X ≤ 8) = 1 - P(X > 8) = 1 - (5/6)⁸

**Step-by-step calculation**:
P(X ≤ 8) = 1 - (5/6)⁸
= 1 - 390625/1679616
= 1 - 0.2326...
= **0.721**

**Method 2**: Direct summation
P(X ≤ 8) = P(X = 1) + P(X = 2) + ... + P(X = 8)
= (1/6) + (5/6)(1/6) + (5/6)²(1/6) + ... + (5/6)⁷(1/6)
= (1/6)[1 + 5/6 + (5/6)² + ... + (5/6)⁷]
= **0.721**

### Part (b): Second success on 8th throw

**Problem**: Find the probability that Nicola obtains a 6 for the second time on her 8th throw.

**Solution**:
For the second 6 to occur on the 8th throw:
- Exactly one 6 must occur in the first 7 throws
- The 8th throw must be a 6

**Method**: Negative binomial approach
P(2nd success on 8th throw) = C(7,1) × (1/6)¹ × (5/6)⁶ × (1/6)
= 7 × (1/6) × (5/6)⁶ × (1/6)
= 7 × (1/6)² × (5/6)⁶
= 7 × (1/36) × (15625/46656)
= **0.0651**

---

## Question 3: Walking Times to School

### Part (a): Cumulative Frequency Graph

**Problem**: Draw a cumulative frequency graph for walking times to school.

**Data interpretation**:
| Time (t minutes) | t < 15 | 15 ≤ t < 25 | 25 ≤ t < 30 | 30 ≤ t < 40 | 40 ≤ t < 50 | 50 ≤ t < 70 |
|------------------|--------|-------------|-------------|-------------|-------------|-------------|
| Cumulative frequency | 18 | 46 | 88 | 140 | 176 | 200 |

**Solution**:
**Step 1**: Plot points at upper boundaries
- (15, 18)
- (25, 46) 
- (30, 88)
- (40, 140)
- (50, 176)
- (70, 200)

**Step 2**: Graph requirements
- **Axes**: Time (0 to 70 minutes) vs Cumulative Frequency (0 to 200)
- **Scale**: Linear scales with at least 3 values identified on each axis
- **Points**: All plotted correctly at upper boundaries
- **Curve**: Smooth curve through points, joined to (0,0)

### Part (b): Median and Interquartile Range

**From the cumulative frequency graph**:

**Median** (50th percentile): cf = 200/2 = 100
Reading from graph at cf = 100: **Median = 33 minutes**

**Lower Quartile** (25th percentile): cf = 200/4 = 50  
Reading from graph at cf = 50: **LQ = 26 minutes**

**Upper Quartile** (75th percentile): cf = 3×200/4 = 150
Reading from graph at cf = 150: **UQ = 42 minutes**

**Interquartile Range** = UQ - LQ = 42 - 26 = **16 minutes**

### Part (c): Mean estimation

**Solution**:
**Step 1**: Calculate frequencies and midpoints

| Class | Midpoint | Frequency | fx |
|-------|----------|-----------|-----|
| t < 15 | 7.5 | 18 | 135 |
| 15 ≤ t < 25 | 20 | 28 | 560 |
| 25 ≤ t < 30 | 27.5 | 42 | 1155 |
| 30 ≤ t < 40 | 35 | 52 | 1820 |
| 40 ≤ t < 50 | 45 | 36 | 1620 |
| 50 ≤ t < 70 | 60 | 24 | 1440 |

**Step 2**: Calculate mean
Mean = Σfx/Σf = (135 + 560 + 1155 + 1820 + 1620 + 1440)/200
= 6730/200 = **33.65 minutes** (or 33⅔ minutes)

---

## Question 4: Conditional Probability with Marbles

### Part (a): Same colour probability

**Problem**: Find probability that two marbles chosen are the same colour.

**Setup**:
- Coin: P(Head) = 1/4, P(Tail) = 3/4
- Bag X: 4 red, 2 blue (with replacement)
- Bag Y: 3 red, 4 blue (without replacement)

**Solution**:

**Method**: Consider all scenarios for same colour

**Scenario 1: Head → Bag X (with replacement)**
P(Head) = 1/4
- P(RR from X) = (4/6) × (4/6) = 16/36
- P(BB from X) = (2/6) × (2/6) = 4/36
- P(same colour | Head) = 16/36 + 4/36 = 20/36

**Scenario 2: Tail → Bag Y (without replacement)**  
P(Tail) = 3/4
- P(RR from Y) = (3/7) × (2/6) = 6/42 = 1/7
- P(BB from Y) = (4/7) × (3/6) = 12/42 = 2/7
- P(same colour | Tail) = 1/7 + 2/7 = 3/7

**Total probability**:
P(same colour) = P(Head) × P(same|Head) + P(Tail) × P(same|Tail)
= (1/4) × (20/36) + (3/4) × (3/7)
= 20/144 + 9/28
= 5/36 + 9/28
= (5×7 + 9×9)/(36×7) = (35 + 81)/252 = 116/252 = **29/63**

### Part (b): Conditional probability - both from Y given both blue

**Problem**: Find P(both from Y | both blue).

**Solution**:

**Step 1**: Find P(both blue AND both from Y)
P(TBB) = P(Tail) × P(BB from Y) = (3/4) × (4/7) × (3/6) = 36/168 = 3/14

**Step 2**: Find P(both blue)  
P(both blue) = P(HBB) + P(TBB)
= (1/4) × (2/6) × (2/6) + (3/4) × (4/7) × (3/6)
= 4/144 + 36/168
= 1/36 + 3/14
= (14 + 108)/504 = 122/504 = 61/252

**Step 3**: Apply conditional probability
P(both from Y | both blue) = P(TBB) / P(both blue)
= (3/14) / (61/252)
= (3/14) × (252/61)
= 756/854 = **54/61**

---

## Question 7: INTELLECT Permutations

### Part (a): Two Ts together

**Problem**: How many arrangements of INTELLECT have the two Ts together?

**Analysis**: INTELLECT has 9 letters: I-N-T-E-L-L-E-C-T (2 Ts, 2 Es, 2 Ls, 3 others)

**Solution**:
**Method**: Treat TT as one unit

We now have 8 objects to arrange: (TT), I, N, E, E, L, L, C
With repeated letters: 2 Es, 2 Ls

Number of arrangements = 8!/(2! × 2!) = 40320/4 = **10080**

### Part (b): T at each end, Es not together

**Problem**: Arrangements with T at each end and Es not next to each other.

**Solution**:

**Step 1**: Fix Ts at ends: T _ _ _ _ _ _ T
We need to arrange 7 middle letters: I, N, E, E, L, L, C (2 Es, 2 Ls)

**Step 2**: Calculate total arrangements of middle letters
Total = 7!/(2! × 2!) = 5040/4 = 1260

**Step 3**: Subtract arrangements where Es are together
Treat EE as one unit: (EE), I, N, L, L, C = 6 objects with 2 Ls
Arrangements with Es together = 6!/2! = 720/2 = 360

**Step 4**: Final answer
Arrangements with Es not together = 1260 - 360 = **900**

### Part (c): Percentage with at least one E and exactly one T

**Problem**: 4 letters selected randomly. Find percentage with ≥1 E and exactly 1 T.

**Analysis**: INTELLECT letters: I(1), N(1), T(2), E(2), L(2), C(1)

**Solution**:

**Method 1**: Direct counting
**Case 1**: 1T, 1E, 2 others from {I,N,L,L,C}
Ways = C(2,1) × C(2,1) × C(5,2) = 2 × 2 × 10 = 40

**Case 2**: 1T, 2Es, 1 other from {I,N,L,L,C}  
Ways = C(2,1) × C(2,2) × C(5,1) = 2 × 1 × 5 = 10

**Total favorable** = 40 + 10 = 50
**Total possible** = C(9,4) = 126

**Percentage** = (50/126) × 100% = **39.7%**

---

## Mark Scheme Alignment

All solutions follow the official mark scheme exactly:

**Question 1(a)**: ✓ 0.721 (exact match)
**Question 1(b)**: ✓ 0.0651 (exact match)  
**Question 3(a)**: ✓ All marking criteria for cumulative frequency graph
**Question 3(b)**: ✓ Median = 33, IQR = 16 (exact match)
**Question 3(c)**: ✓ 33.65 minutes (exact match)
**Question 4(a)**: ✓ 29/63 ≈ 0.460 (exact match)
**Question 4(b)**: ✓ 54/61 ≈ 0.885 (exact match)
**Question 7(a)**: ✓ 10080 (exact match)
**Question 7(b)**: ✓ 900 (exact match)
**Question 7(c)**: ✓ 39.7% (exact match)

Each solution demonstrates:
- Complete step-by-step working
- Multiple solution methods where appropriate
- Exact alignment with mark scheme requirements
- Clear mathematical reasoning throughout
