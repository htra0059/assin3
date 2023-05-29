from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0


class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.our_adt = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        new_adt = MaxHeap(len(hive_list))
        for hive in hive_list: # O(M)
            new_adt.add(hive)
        self.our_adt = new_adt


    
    def add_beehive(self, hive: Beehive):
        self.our_adt.add(hive)
    
    def harvest_best_beehive(self):
        popped_hive = self.our_adt.get_max()
        harvested_value = min(popped_hive.capacity, popped_hive.volume)*popped_hive.nutrient_factor
        popped_hive.volume = max(0, popped_hive.volume - popped_hive.capacity)
        self.our_adt.add(popped_hive)
        return harvested_value
