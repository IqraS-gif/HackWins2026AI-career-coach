
def calculate_composite_score(completion_rate, avg_assessment, avg_interview, latest_ats):
    # Weights: Progress (30%), Assessment (25%), Interview (25%), ATS (20%)
    score = (completion_rate * 0.30) + (avg_assessment * 0.25) + (avg_interview * 0.25) + (latest_ats * 0.20)
    return round(score, 2)

def test_scoring():
    cases = [
        {"input": (100, 100, 100, 100), "expected": 100.0, "desc": "Perfect scores"},
        {"input": (0, 0, 0, 0), "expected": 0.0, "desc": "Zero scores"},
        {"input": (50, 50, 50, 50), "expected": 50.0, "desc": "Average scores"},
        {"input": (80, 70, 60, 50), "expected": 66.5, "desc": "Varying scores (80*0.3 + 70*0.25 + 60*0.25 + 50*0.2 = 24 + 17.5 + 15 + 10 = 66.5)"},
    ]

    for case in cases:
        actual = calculate_composite_score(*case["input"])
        assert actual == case["expected"], f"Failed {case['desc']}: expected {case['expected']}, got {actual}"
        print(f"PASSED: {case['desc']} -> {actual}")

if __name__ == "__main__":
    test_scoring()
