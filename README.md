# AI-report-04
introduction
This lab explores on the implementation of a modified K-Means clustering algorithm using Python. In this task, you must generate a data file containing 100 Cartesian points P(x, y) and 10 initial cluster centers C(x, y). The algorithm should be rewritten to use the Manhattan distance method for calculating distances between points and clusters. Additionally, you are required to create a 2D visualization of the clustered data using a matrix, where each cell represents a coordinate on the plane and displays either a data point or a cluster center using distinct symbols. This visualization must be displayed using only the print() function.
objectives
1. Implement the K-Means algorithm using Manhattan distance for clustering.


2.Generate a dataset consisting of 100 points and 10 initial cluster centers.

3.Create a text-based 2D matrix to visualize the clustering process.

4.Analyze intra-cluster distances and final cluster center positions.
procedure
Step-1:Start.


Step-2:Generate 100 points and 10 centers randomly and save them in data.csv.


Step-3:Read points and centers from the CSV file.


Step-4:Initialize a 50×50 grid filled with zeros.

Step-5:Assign each point to the nearest center using Manhattan distance.


Step-6:Update cluster centers by averaging the coordinates of assigned points.


Step-7:Repeat Steps 5 and 6 until cluster centers do not move (convergence).

Step-8:Fill the grid with cluster numbers for points and 'C' for centers.


Step-9:Calculate intra-cluster distances for each cluster.


Step-10:Print all results and visualize the 2D grid using print()

Step-11:End

output
![image alt]{https://github.com/NADIA623424/AI-report-04/blob/52a035324ad05c784853631c85afa4bcd38406fd/Screenshot%202025-04-26%20211724.png}
!{image alt}{https://github.com/NADIA623424/AI-report-04/blob/6d26de17db89ba9d7675a953435ae9249e7c500d/Screenshot%202025-04-26%20211752.png}
!{https://github.com/NADIA623424/AI-report-04/blob/74891f9393d264aee2b3208b3a44fc9282040049/Screenshot%202025-04-26%20211846.png}

disscussion
 In this lab, we successfully implemented a modified K-Means clustering algorithm using Manhattan distance instead of the traditional Euclidean distance. By generating random data points and initial cluster centers, we simulated a real-world clustering scenario where data points are grouped based on proximity.100 random points and 10 initial centers were generated and clustered based on proximity.Cluster centers were updated until no changes occurred, ensuring convergence.A 2D matrix visualization was created using print(), showing points and centers clearly.The results confirmed that the algorithm grouped points efficiently based on the Manhattan distance.
 conclusion
 The experiment successfully demonstrated the implementation of a modified K-Means clustering algorithm using Manhattan distance in Python.The clustering process effectively grouped the points, and the printed matrix provided a simple yet clear visualization of the results.This technique is especially applicable in urban planning, logistics, and other fields where Manhattan distance offers a more realistic measurement compared to Euclidean distance.Future enhancements may include dynamic visualization or applying the approach to real-world spatial datasets.
