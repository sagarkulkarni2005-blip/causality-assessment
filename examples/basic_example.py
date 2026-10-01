"""
Basic example of using the Causality Assessment framework.
"""

import pandas as pd

from causality_assessment import CausalityAssessor


def main():
    """Run a basic causality assessment example."""
    # Create sample data
    data = pd.DataFrame({
        'treatment': [0, 1, 0, 1, 0, 1, 0, 1],
        'outcome': [10, 15, 11, 16, 9, 14, 12, 17],
        'confounder': [1, 2, 1, 2, 1, 2, 1, 2],
    })

    # Initialize assessor
    assessor = CausalityAssessor(name="Example Assessment")

    # Load data
    assessor.load_data(data)
    print("Data loaded successfully")
    print(f"Shape: {data.shape}")
    print()

    # Perform assessment
    results = assessor.assess()
    print("Assessment Results:")
    print(results)


if __name__ == "__main__":
    main()
