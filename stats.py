import statistics
from collections import defaultdict
import time

class StatsCollector:
    """
    A simple stats collector class that gathers statistics on numerical data.
    It supports adding values under different keys (categories) and computing
    basic stats like mean, median, std dev, min, max, and count.
    
    Example usage:
    collector = StatsCollector()
    collector.add('response_time', 0.5)
    collector.add('response_time', 0.7)
    stats = collector.get_stats('response_time')
    print(stats)
    """

    def __init__(self):
        self.data = defaultdict(list)
        self.timestamps = defaultdict(list)  # Optional: track when values were added

    def add(self, key, value):
        """
        Add a value to a specific key (category).
        
        :param key: str, the category name
        :param value: float or int, the numerical value to add
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number (int or float)")
        self.data[key].append(value)
        self.timestamps[key].append(time.time())

    def get_stats(self, key):
        """
        Get statistics for a specific key.
        
        :param key: str, the category name
        :return: dict with stats or None if no data
        """
        values = self.data.get(key)
        if not values:
            return None
        
        return {
            'count': len(values),
            'min': min(values),
            'max': max(values),
            'mean': statistics.mean(values),
            'median': statistics.median(values),
            'stdev': statistics.stdev(values) if len(values) > 1 else 0,
            'last_added': self.timestamps[key][-1]
        }

    def get_all_stats(self):
        """
        Get stats for all keys.
        
        :return: dict with keys as categories and values as stats dicts
        """
        return {key: self.get_stats(key) for key in self.data}

    def clear(self, key=None):
        """
        Clear data for a specific key or all keys if none provided.
        
        :param key: str, optional category name
        """
        if key:
            self.data.pop(key, None)
            self.timestamps.pop(key, None)
        else:
            self.data.clear()
            self.timestamps.clear()

# Example usage
if __name__ == "__main__":
    collector = StatsCollector()
    collector.add('cpu_usage', 45.2)
    collector.add('cpu_usage', 50.1)
    collector.add('cpu_usage', 48.7)
    collector.add('memory_usage', 2048)
    collector.add('memory_usage', 2100)
    
    print("Stats for cpu_usage:")
    print(collector.get_stats('cpu_usage'))
    
    print("\nAll stats:")
    print(collector.get_all_stats())
