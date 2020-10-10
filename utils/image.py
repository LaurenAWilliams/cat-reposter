import numpy
import urllib.request
import cv2

HAAR_CASCADE_LOC = 'utils/files/haarcascade_frontalcatface_extended.xml'


def _get_image_from_url(url):
    with urllib.request.urlopen(url) as resp:
        raw_image = numpy.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(raw_image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def is_cat(image_url):
    image = _get_image_from_url(image_url)
    detector = cv2.CascadeClassifier(HAAR_CASCADE_LOC)
    locations = detector.detectMultiScale(image, scaleFactor=1.2, minNeighbors=3, minSize=(75, 75))
    return len(locations) != 0
