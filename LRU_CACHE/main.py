class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        self.latest_hit_key = -1

    def get(self, key: int) -> int:
        if key not in (self.cache_map).keys():
            return -1
        self.latest_hit_key = key
        return self.cache_map[key]

    def put(self, key: int, value: int) -> None:
        # reach the maximum limitation
        if len(self.cache_map.keys()) + 1 > self.capacity:
            if len(self.cache_map.keys()) == 1:
                 self.cache_map.clear()
            # means there is no `get` before, then will pop the 1st insert into the map
            for  _key in self.cache_map.keys():
                if self.latest_hit_key == _key:
                    continue
                # only pop the earliest not used item
                self.cache_map.pop(_key)
                self.latest_hit_key = -1
                break

        self.cache_map[key] = value
        self.latest_hit_key = key
                    
lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(2, 2)
lRUCache.get(2)
lRUCache.put(1, 1)
lRUCache.put(4, 1)
lRUCache.get(2)  
    