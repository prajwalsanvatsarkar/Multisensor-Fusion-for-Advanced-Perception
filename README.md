# Multisensor-Fusion-for-Advanced-Perception

The goal of this project is to build a system that can estimate how far away vehicles are, by combining camera images with LiDAR and Radar data. YOLO is used to detect vehicles in the images, and then point cloud data from the sensors is projected onto the same image. From there, only the points that fall inside each detected vehicle are kept, and the average distance is calculated. By fusing LiDAR and Radar, the system takes advantage of the strengths of both sensors. Finally, the accuracy of the distance estimates is checked using metrics like Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) to make sure the results are consistent and trustworthy.


# Step 1: Object Detection with YOLO
- YOLOv5 is used on the front-camera images to detect vehicles like cars, buses, and trucks.  
- For each image, the detected vehicles are shown with green boxes and confidence scores, and the results are saved for the next steps.
  <img width="685" height="252" alt="image" src="https://github.com/user-attachments/assets/a66213a0-7260-4b4a-a97f-84d95f283aff" />


# Step 2: Project the point cloud on Image
- LiDAR and Radar points are transformed from their own sensor frames into the camera reference frame using the extrinsic calibration (rotation + translation).  
- The camera intrinsic matrix is then applied to project these 3D points into 2D pixel coordinates.  
- Finally, the projected points are overlaid on the camera image, so we can visually confirm that LiDAR and Radar align correctly with the detected vehicles. 
<img width="698" height="257" alt="image" src="https://github.com/user-attachments/assets/bd2a006d-cdad-4168-9f84-b1547bcf443e" />
<img width="678" height="267" alt="image" src="https://github.com/user-attachments/assets/6e2cbbdf-1ade-4b29-b770-ebdeb8e55cba" />
<img width="1214" height="400" alt="image" src="https://github.com/user-attachments/assets/c65ed909-e44b-49d8-89e2-248f5a8d1c87" />

# Step 3: Filter the Points in Bounding Boxes
- After projecting LiDAR and Radar points into the image, only those points that fall inside each YOLO bounding box are kept.  
- This ensures we only work with sensor points that truly belong to the detected vehicles, ignoring the rest of the scene.
<img width="683" height="266" alt="image" src="https://github.com/user-attachments/assets/40eb0c25-fe17-412e-8bca-f0a64864fd9b" />
<img width="678" height="266" alt="image" src="https://github.com/user-attachments/assets/b6fb60c8-6a0d-49c2-b592-3f35ccaa0211" />

# Step 4: Estimate the Distance
- For every detected vehicle, we looked at the LiDAR and Radar points that fall inside its bounding box.  
- From those points, we calculated the average distance to the vehicle for LiDAR and for Radar separately.
<img width="721" height="273" alt="image" src="https://github.com/user-attachments/assets/87922eb1-ca01-4e75-ab0c-434d719ca7e6" />

# Step 5: Calculate Fused Distance
- After getting LiDAR and Radar distances, we combined them into one fused value.  
- We gave LiDAR a higher weight (0.7) and Radar a lower weight (0.3), since LiDAR is usually more precise.  
- The fused distance was calculated using this formula:
- Fused distance: d_fused = 0.7 * d_LiDAR + 0.3 * d_Radar

<img width="711" height="258" alt="image" src="https://github.com/user-attachments/assets/da3bc0db-db3a-46ce-ae79-cbd00fdabe51" />

# Step 6: Estimate Mean Absolute Error and Root Mean Squared Error
In the final step we checked how accurate the distance estimates were using two metrics: Mean Absolute Error (MAE) and Root Mean Square Error (RMSE). Both came out to about 1.13 meters. This means that, on average, our distance estimates were only about a meter off from the actual values. Since MAE and RMSE are almost the same, it also shows there were no big mistakes or outliers. Overall, the system gave very accurate results for estimating vehicle distances.

<img width="1403" height="452" alt="image" src="https://github.com/user-attachments/assets/a408f3e5-4f6d-4ce9-803c-a16944bc0bef" />
