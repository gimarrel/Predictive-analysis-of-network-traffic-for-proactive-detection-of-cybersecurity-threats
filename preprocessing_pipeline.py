# Evidence of Chronological Partitioning
print(f"Full Dataset Date Range: {df['Timestamp'].min()} to {df['Timestamp'].max()}")

# Training set: Monday - Wednesday
# Test set: Thursday - Friday
print(f"Training Range: {train_df['Timestamp'].min()} to {train_df['Timestamp'].max()}")
print(f"Test Range: {test_df['Timestamp'].min()} to {test_df['Timestamp'].max()}")

# Asserting that no overlap exists (Leakage Check)
assert train_df['Timestamp'].max() < test_df['Timestamp'].min()
