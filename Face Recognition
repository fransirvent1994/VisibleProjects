import cv2
import face_recognition as fr

# Load images
control_picture = fr.load_image_file("insertimage.jpg")
test_picture = fr.load_image_file("insertimage.jpg")
another_test_picture = fr.load_image_file("insertimage.jpg")

# Images to RGB
control_picture = cv2.cvtColor(control_picture, cv2.COLOR_BGR2RGB)
test_picture = cv2.cvtColor(test_picture, cv2.COLOR_BGR2RGB)
another_test_picture = cv2.cvtColor(another_test_picture, cv2.COLOR_BGR2RGB)

# Locate face
face_A_location = fr.face_locations(control_picture)[0]
coded_face_A = fr.face_encodings(control_picture)[0]

face_B_location = fr.face_locations(test_picture)[0]
coded_face_B = fr.face_encodings(test_picture)[0]

face_C_location = fr.face_locations(another_test_picture)[0]
coded_face_C = fr.face_encodings(another_test_picture)[0]

# Show rectangle
cv2.rectangle(control_picture,
              (face_A_location[3], face_A_location[0]),
              (face_A_location[1], face_A_location[2]),
              (0, 255, 0),
              2)

cv2.rectangle(test_picture,
              (face_B_location[3], face_B_location[0]),
              (face_B_location[1], face_B_location[2]),
              (0, 255, 0),
              2)

cv2.rectangle(another_test_picture,
              (face_C_location[3], face_C_location[0]),
              (face_C_location[1], face_C_location[2]),
              (0, 255, 0),
              2)

# Compare
result_AB = fr.compare_faces([coded_face_A], coded_face_B)
result_AC = fr.compare_faces([coded_face_A], coded_face_C)

print(result_AB)
print(result_AC)

# Show images
control_picture_resize = cv2.resize(control_picture, (390, 480))
test_picture_resize = cv2.resize(test_picture, (390, 480))
another_test_picture_resize = cv2.resize(another_test_picture, (390, 480))
cv2.imshow("Control picture", control_picture_resize)
cv2.imshow("Test picture", test_picture_resize)
cv2.imshow("Picture 3", another_test_picture_resize)

# Count the distance
distanceAB = fr.face_distance([coded_face_A], coded_face_B)
distanceAC = fr.face_distance([coded_face_A], coded_face_C)
print(distanceAB)
print(distanceAC)

if result_AB == [True]:
    print("Picture A and B match!")
else:
    print("Picture A and B don´t match")

if result_AC == [True]:
    print("Picture A and C match!")
else:
    print("Picture A and C not match")

# Keep the program open
cv2.waitKey(0)
