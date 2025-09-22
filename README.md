# Multisensor-Fusion-for-Advanced-Perception

The goal of this project is to build a system that can estimate how far away vehicles are, by combining camera images with LiDAR and Radar data. YOLO is used to detect vehicles in the images, and then point cloud data from the sensors is projected onto the same image. From there, only the points that fall inside each detected vehicle are kept, and the average distance is calculated. By fusing LiDAR and Radar, the system takes advantage of the strengths of both sensors. Finally, the accuracy of the distance estimates is checked using metrics like Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) to make sure the results are consistent and trustworthy.


# Step 1: Object Detection with YOLO
- YOLOv5 is used on the front-camera images to detect vehicles like cars, buses, and trucks.  
- For each image, the detected vehicles are shown with green boxes and confidence scores, and the results are saved for the next steps.
<img width="1303" height="420" alt="image" src="https://github.com/user-attachments/assets/86771989-ede7-4bd3-9d88-aba05111500c" />


# Step 2: Project the point cloud on Image
- LiDAR and Radar points are transformed from their own sensor frames into the camera reference frame using the extrinsic calibration (rotation + translation).  
- The camera intrinsic matrix is then applied to project these 3D points into 2D pixel coordinates.  
- Finally, the projected points are overlaid on the camera image, so we can visually confirm that LiDAR and Radar align correctly with the detected vehicles. 
<img width="1287" height="427" alt="image" src="https://github.com/user-attachments/assets/503380d9-8510-4a94-9688-f2298e7cb940" />
<img width="1278" height="430" alt="image" src="https://github.com/user-attachments/assets/338c93cd-e29e-41a6-b4df-a7efb2215f7d" />


# Step 3: Filter the Points in Bounding Boxes
- After projecting LiDAR and Radar points into the image, only those points that fall inside each YOLO bounding box are kept.  
- This ensures we only work with sensor points that truly belong to the detected vehicles, ignoring the rest of the scene.
<img width="1298" height="431" alt="image" src="https://github.com/user-attachments/assets/45632091-d87f-4882-8c99-81bb4185d04c" />
<img width="1290" height="433" alt="image" src="https://github.com/user-attachments/assets/0bcbbfd2-37c7-4f11-88c2-a28d0d0c57fc" />

# Step 4: Estimate the Distance
- For every detected vehicle, we looked at the LiDAR and Radar points that fall inside its bounding box.  
- From those points, we calculated the average distance to the vehicle for LiDAR and for Radar separately.
<img width="1303" height="426" alt="image" src="https://github.com/user-attachments/assets/332cb6aa-82f5-4576-a3d0-3530d5ba2da2" />

# Step 5: Calculate Fused Distance
- After getting LiDAR and Radar distances, we combined them into one fused value.  
- We gave LiDAR a higher weight (0.7) and Radar a lower weight (0.3), since LiDAR is usually more precise.  
- The fused distance was calculated using this formula:
- Fused distance: d_fused = 0.7 * d_LiDAR + 0.3 * d_Radar
<img width="1291" height="422" alt="image" src="https://github.com/user-attachments/assets/3020e173-d638-4c00-a91e-8981df920566" />


# Step 6: Conclusion
- In conclusion, this report presented a multisensor fusion approach for estimating vehicle distances in the images.
- The final step evaluates the accuracy using Mean Absolute Error (MAE) and Root Mean Square Error (RMSE), achieving a MAE of 5.49 meters and RMSE of 6.67 meters, indicating good overall accuracy.
- To resolve these errors, in future instead of filtering projected points in specified bounding box, asegmented mask of vehicle can be considered for estimating the actual vehicle boundary.

