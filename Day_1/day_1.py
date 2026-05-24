import numpy as np
# STEP 1: Generate Random Scores

scores = np.random.randint(0, 100, size=50)
print("Student Scores:\n")
print(scores)

# STEP 2: Basic Statistics

mean_score = np.mean(scores)
median_score = np.median(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)
std_deviation = np.std(scores)

print("\n----- Statistics -----")
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Standard Deviation:", std_deviation)

# STEP 3: Find Failures and Distinctions

fail_students = scores[scores < 40]   # Students scoring below 40

distinction_students = scores[scores > 85]  # Students scoring above 85

print("\n----- Failed Students (<40) -----")
print(fail_students)
print("\n----- Distinction Students (>85) -----")
print(distinction_students)

# STEP 4: Normalize Scores (0 to 1)

normalized_scores = scores / 100

print("\n----- Normalized Scores -----")
print(normalized_scores)

# STEP 5: Reshape into 5 x 10 Matrix

reshaped_scores = scores.reshape(5, 10)
print("\n----- Reshaped Scores (5x10) -----")
print(reshaped_scores)

# STEP 6: Row-wise Average

row_averages = np.mean(reshaped_scores, axis=1) # Average of each row
print("\n----- Row-wise Averages -----")
print(row_averages)

# BONUS CHALLENGE
# Weighted Score Calculation
# Generate theory and practical marks
theory = np.random.randint(0, 100, size=50)
practical = np.random.randint(0, 100, size=50)

# Weighted formula:
# 40% Theory + 60% Practical
final_scores = (0.4 * theory) + (0.6 * practical)
print("\n----- Theory Marks -----")
print(theory)
print("\n----- Practical Marks -----")
print(practical)
print("\n----- Weighted Final Scores -----")
print(final_scores)