import random
import csv

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class CustomKMeans:
    def __init__(self, total_points, total_clusters):
        self.total_points = total_points
        self.total_clusters = total_clusters
        self.grid = [[0 for _ in range(50)] for _ in range(50)]
        self.nodes = []
        self.cluster_centers = []
        self.load_nodes()
        self.perform_clustering()

    def load_nodes(self):
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for entry in reader:
                if entry['Type'] == 'Point':
                    self.nodes.append(Node(int(entry['X']), int(entry['Y'])))
                elif entry['Type'] == 'Center':
                    self.cluster_centers.append(Node(int(entry['X']), int(entry['Y'])))

    def perform_clustering(self):
        while True:
            for node in self.nodes:
                min_distance = float('inf')
                for idx, center in enumerate(self.cluster_centers):
                    dist = abs(node.x - center.x) + abs(node.y - center.y)
                    if dist < min_distance:
                        min_distance = dist
                        node.cluster = idx

            updated_centers = [Node(center.x, center.y) for center in self.cluster_centers]

            for idx in range(self.total_clusters):
                sum_x = sum_y = count = 0
                for node in self.nodes:
                    if node.cluster == idx:
                        sum_x += node.x
                        sum_y += node.y
                        count += 1
                if count > 0:
                    self.cluster_centers[idx].x = sum_x // count
                    self.cluster_centers[idx].y = sum_y // count

            total_shift = 0
            for i in range(self.total_clusters):
                total_shift += abs(self.cluster_centers[i].x - updated_centers[i].x) + abs(self.cluster_centers[i].y - updated_centers[i].y)

            if total_shift == 0:
                break

        for node in self.nodes:
            self.grid[node.x][node.y] = node.cluster + 1
        for center in self.cluster_centers:
            self.grid[center.x][center.y] = 'C'

        for idx in range(self.total_clusters):
            intra_cluster_distance = sum(
                abs(self.cluster_centers[idx].x - node.x) + abs(self.cluster_centers[idx].y - node.y)
                for node in self.nodes if node.cluster == idx
            )
            print(f"Cluster {idx + 1} Intra-cluster Distance: {intra_cluster_distance}")

        for node in self.nodes:
            print(f"Node ({node.x}, {node.y}) belongs to Cluster {node.cluster + 1}")

        for idx, center in enumerate(self.cluster_centers):
            print(f"Cluster {idx + 1} Center Position: ({center.x}, {center.y})")

        print("\nGrid Layout:\n")
        for i in range(50):
            for j in range(50):
                if self.grid[i][j] == 0:
                    print('.', end=' ')
                elif self.grid[i][j] == 'C':
                    print('C', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print()

def generate_data_file(total_points, total_clusters):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "X", "Y"])
        for _ in range(total_points):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            writer.writerow(["Point", x, y])
        for _ in range(total_clusters):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            writer.writerow(["Center", x, y])

def main():
    total_points = 100
    total_clusters = 10
    generate_data_file(total_points, total_clusters)
    CustomKMeans(total_points, total_clusters)

if __name__ == "__main__":
    main()
