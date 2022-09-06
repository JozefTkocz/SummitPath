from typing import List, Tuple
import pandas as pd
from src.models import Coordinate, MapGrid
from src.heuristic import Heuristic
from src.a_star import a_star_search


class RoutePlanner:
    def __init__(self,
                 heightmap: MapGrid,
                 heuristic: Heuristic,
                 waypoints: pd.DataFrame):
        self.heightmap = heightmap
        self.waypoints = waypoints
        self.heuristic = heuristic

    def construct_directed_graph(self, waypoints: List[str]) -> pd.DataFrame:
        waypoint_pair_combinations = pair_combinations(waypoints)

        leg_data = []
        for idx, leg in enumerate(waypoint_pair_combinations):
            start = get_summit_coordinate(leg[0], self.waypoints)
            end = get_summit_coordinate(leg[1], self.waypoints)
            route, distance = a_star_search(map_grid=self.heightmap,
                                            start_grid_position=self.heightmap.coordinate_to_grid_position(start),
                                            end_grid_position=self.heightmap.coordinate_to_grid_position(end),
                                            heuristic=self.heuristic)

            leg_data.append(pd.DataFrame({'Start': [leg[0]],
                                          'Stop': [leg[1]],
                                          'Time': [distance],
                                          'Route Index': [idx]}))
        return pd.concat(leg_data, ignore_index=True)


def pair_combinations(input_list: List) -> Tuple[Tuple]:
    list_indices = list(range(len(input_list)))
    result = []
    for idx in list_indices:
        list_item = input_list[idx]
        remaining_items = [item for item in list_indices if item != idx]
        for pair_idx in remaining_items:
            paired_item = input_list[pair_idx]
            result.append(tuple([list_item, paired_item]))

    return tuple(result)


def get_summit_coordinate(summit_name: str, database: pd.DataFrame) -> Coordinate:
    x = database.loc[database['Name'] == summit_name, 'Xcoord'].values[0]
    y = database.loc[database['Name'] == summit_name, 'Ycoord'].values[0]
    return Coordinate(x=x, y=y)
