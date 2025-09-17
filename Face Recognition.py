import cv2
import face_recognition as fr


def load_and_convert_image(path: str):
    image = fr.load_image_file(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def get_face_encoding(image):
    locations = fr.face_locations(image)
    if len(locations) == 0:
        raise ValueError("No face detected")
    encoding = fr.face_encodings(image, known_face_locations=locations)[0]
    return locations[0], encoding


def draw_rectangle(image, location, color=(0, 255, 0)):
    top, right, bottom, left = location
    cv2.rectangle(image, (left, top), (right, bottom), color, 2)
    return image


def compare_faces(encoding_ref, encoding_test):
    result = fr.compare_faces([encoding_ref], encoding_test)[0]
    distance = fr.face_distance([encoding_ref], encoding_test)[0]
    return result, distance


def resize_for_display(image, size=(390, 480)):
    return cv2.resize(image, size)


def show_images(images: dict):
    for title, img in images.items():
        cv2.imshow(title, resize_for_display(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # Img URLs
    control_path = input("Insert control image path: ")
    test_path = input("Insert test image path: ")
    another_test_path = input("Insert another test image path: ")

    # Load imgs
    control_img = load_and_convert_image(control_path)
    test_img = load_and_convert_image(test_path)
    another_test_img = load_and_convert_image(another_test_path)

    # Encodings
    face_A_loc, face_A_enc = get_face_encoding(control_img)
    face_B_loc, face_B_enc = get_face_encoding(test_img)
    face_C_loc, face_C_enc = get_face_encoding(another_test_img)

    draw_rectangle(control_img, face_A_loc)
    draw_rectangle(test_img, face_B_loc)
    draw_rectangle(another_test_img, face_C_loc)

    # Comparations
    result_AB, dist_AB = compare_faces(face_A_enc, face_B_enc)
    result_AC, dist_AC = compare_faces(face_A_enc, face_C_enc)

    print(f"A vs B → Match: {result_AB}, Distance: {dist_AB:.4f}")
    print(f"A vs C → Match: {result_AC}, Distance: {dist_AC:.4f}")

    if result_AB:
        print("Picture A and B match!")
    else:
        print("Picture A and B don’t match.")

    if result_AC:
        print("Picture A and C match!")
    else:
        print("Picture A and C don’t match.")

    show_images({
        "Control picture": control_img,
        "Test picture": test_img,
        "Another test picture": another_test_img
    })


if __name__ == "__main__":
    main()
