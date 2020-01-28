import time

BENCHMARK_RESULT = 123


def some_function(duration=0.000001):
    time.sleep(duration)
    return BENCHMARK_RESULT


def test_benchmark(benchmark):
    result = benchmark(some_function)
    assert result == BENCHMARK_RESULT
        
