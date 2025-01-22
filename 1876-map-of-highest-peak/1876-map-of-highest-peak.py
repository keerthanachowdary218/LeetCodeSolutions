class Solution:
    def highestPeak(self, is_water):
        dx = [0, 0, 1, -1]  # Horizontal movement: right, left, down, up
        dy = [1, -1, 0, 0]  # Vertical movement corresponding to dx

        rows = len(is_water)
        columns = len(is_water[0])
        cell_heights = [[-1 for _ in range(columns)] for _ in range(rows)]
        cell_queue = deque()
        for x in range(rows):
            for y in range(columns):
                if is_water[x][y] == 1:
                    cell_queue.append((x, y))
                    cell_heights[x][y] = 0
        height_of_next_layer = 1

        # Perform BFS
        while cell_queue:
            layer_size = len(cell_queue)
            for _ in range(layer_size):
                current_cell = cell_queue.popleft()
                for d in range(4):
                    neighbor_x = current_cell[0] + dx[d]
                    neighbor_y = current_cell[1] + dy[d]
                    if (self._is_valid_cell(neighbor_x, neighbor_y, rows, columns) and cell_heights[neighbor_x][neighbor_y] == -1):
                        cell_heights[neighbor_x][neighbor_y] = height_of_next_layer
                        cell_queue.append((neighbor_x, neighbor_y))
            height_of_next_layer += 1  # Increment height for the next layer
        return cell_heights

    def _is_valid_cell(self, x, y, rows, columns):
        return 0 <= x < rows and 0 <= y < columns