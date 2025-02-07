class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        '''
        #so dont use set, memory limit exceeded., use hashmap
        colors=[0]*(limit+1)
        ans=[]
        for query in queries:
            colors[query[0]]=query[1]
            if 0 in set(colors):
                ans.append(len(set(colors))-1)
            else:
                ans.append(len(set(colors)))
        return ans
        '''
        n = len(queries)
        result = []
        color_map = {}
        ball_map = {}
        for i in range(n):
            ball, color = queries[i]
            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1

                # If there are no balls with previous color left, remove color from color map
                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            # Set color of ball to the new color
            ball_map[ball] = color

            # Increment the count of the new color
            color_map[color] = color_map.get(color, 0) + 1

            result.append(len(color_map))

        return result