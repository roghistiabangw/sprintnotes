# === Stage 61: Add performance timing for core list and search operations ===
# Project: SprintNotes
import time


def benchmark_list_operations(items):
    """Benchmark core list and search operations."""
    times = {}

    start = time.perf_counter()
    n = len(items)
    times['append'] = (time.perf_counter() - start) * 1e6
    items.append("benchmark_item")

    start = time.perf_counter()
    idx = items.index("benchmark_item")
    times['index_search'] = (time.perf_counter() - start) * 1e6

    start = time.perf_counter()
    found_any = any(item.startswith("bench") for item in items)
    times['generator_search'] = (time.perf_counter() - start) * 1e6

    start = time.perf_counter()
    sliced = items[0:min(5, len(items))]
    times['slice'] = (time.perf_counter() - start) * 1e6

    return times


if __name__ == "__main__":
    test_data = [f"note_{i}" for i in range(100)]
    results = benchmark_list_operations(test_data)
    for op, ms in results.items():
        print(f"{op}: {ms:.2f} µs")
