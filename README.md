# Car Drive App
Simple Python game for driving a car around a track.

![screenshot](https://github.com/RJW20/car-drive-app/assets/99192767/6fe5c8a1-d8f0-4067-b743-3173827fc2f8)

A small amount of drifting is possible due to having different sideways friction coefficents for the front and back wheels:

![drift](https://github.com/RJW20/car-drive-app/assets/99192767/3399600c-3f2b-4585-9e61-aadb5f726c37)

## Basic Requirements
1. [Python](https://www.python.org/downloads/).
2. [Poetry](https://python-poetry.org/docs/) for ease of installing the dependencies.
3. A switch pro controller (or possibly others, none tested) since we need to be able to map a continuous input to the steering angle of the car, and pressing left and right arrow keys don't allow fast enough turning from e.g. hard left to hard right.

## Getting Started
1. Clone or download the repo `git clone https://github.com/RJW20/car-drive-app.git`.
2. Set up the virtual environment with `poetry install`.
3. Run the game with <code>poetry run main *track_name*</code> where track_name is the name of a track saved using any of the methods below.
4. Turn the car with the left joystick, accelerate with `A` and brake with `B` and try and get around the Track without hitting the offroad.

## Tracks
There are three methods to make Tracks. Two of these allow a user to build a track themselves, placing control points around the plane and a Track being generated around/through them, and the other generates them procedurally. All programs use the same syntax for instantiation <code>poetry run *method* *plane_width* *plane_height* *track_name*</code> where the methods are described below.

### Creator_1
When running method `creator_1`, you will be able to drag around the points and the track will always bend around them. The radius of the curve of the track about the points can be adjusted by selecting a point and using the `UP` and `DOWN` arrow keys. The orientation (if one ends up with a loop around it then change this) can be changed similarly by using the `LEFT` or `RIGHT` arrow keys. More points can be added with `SPACE`, and once happy with the design press the `ENTER` key and then click on the Track where you want the start/finish line to be.

Below are a few examples made using this method:

![c1t1](https://github.com/RJW20/car-drive-app/assets/99192767/1f607d26-6778-4604-93e2-6fa631a01138)
![c1t2](https://github.com/RJW20/car-drive-app/assets/99192767/90f00c8c-4864-48b0-92fc-68f48df87c91)
![c1t3](https://github.com/RJW20/car-drive-app/assets/99192767/4cf8c6a9-5c11-45e4-8a94-63e19804ce53)

### Creator_2
When running method `creator_2`, you will be able to drag around the points and the track will always traverse through them. Between the points a curve will be constructed using [Catmull-Rom interpolation](https://en.wikipedia.org/wiki/Centripetal_Catmull%E2%80%93Rom_spline). More points can be added with `SPACE`, and once happy with the design press the `ENTER` key and then click on the Track where you want the start/finish line to be.

Below are a few examples made using this method:

![c2t1](https://github.com/RJW20/car-drive-app/assets/99192767/80e694d7-6171-4bed-9d9b-60d368bee357)
![c2t2](https://github.com/RJW20/car-drive-app/assets/99192767/dbac67c1-11fc-44d1-a7e2-1721bedcbe56)
![c2t3](https://github.com/RJW20/car-drive-app/assets/99192767/79a95d45-d7ad-4b94-a14b-b153464fa658)

### Generator
The generator works very similarly to what is described [here](https://www.gamedeveloper.com/programming/generating-procedural-racetracks). The outline is:
- Generate random points.
- Find the convex hull of the points.
- For consecutive points that are far enough apart add another point between that is randomly displaced from the midpoint.
- Repeatedly move points to prevent turns being too tight (<90&deg;) and points being too close.
- Generate the Catmull-Rom interpolation between the points to make up the rest of the Track.

Below are a few examples generated using this method:

![gt1](https://github.com/RJW20/car-drive-app/assets/99192767/4934be00-d1f9-4a91-aad7-896d916ecee8)
![gt2](https://github.com/RJW20/car-drive-app/assets/99192767/a8453e31-bf71-4d2a-93d9-0a0f0b7999df)
![gt3](https://github.com/RJW20/car-drive-app/assets/99192767/4ae3d676-77ba-43a6-bcd3-7ffdc22b4c2c)

## Note
I created this so that I could then get AI to learn to drive around the Tracks. See [here](https://github.com/RJW20/car-drive-ai-NEAT).
