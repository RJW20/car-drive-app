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

## Tracks
There are three methods to make Tracks. Two of these allow a user to build a track themselves, placing control points around the plane and a Track being generated around/through them, and the other generates them procedurally. All programs use the same syntax for instantiation <code>poetry run *method* *plane_width* *plane_height* *track_name*</code> where the methods are described below.

### Creator_1
When running method `creator_1`, you will be able to drag around the points and the track will always bend around them. The radius of the curve of the track about the points can be adjusted by selecting a point and using the `UP` and `DOWN` arrow keys. The orientation (if one ends up with a loop around it then change this) can be changed similarly by using the `LEFT` or `RIGHT` arrow keys. More points can be added with `SPACE`, and once happy with the design press the `ENTER` key and then click on the Track where you want the start/finish line to be.

Below are a few examples made using this method:

![c1t1](https://github.com/RJW20/car-drive-app/assets/99192767/d3f431f2-2c90-4d83-a6db-1acb131196f8)
![c1t2](https://github.com/RJW20/car-drive-app/assets/99192767/28924922-37ea-4f62-88a3-4764c93960c4)
![c1t3](https://github.com/RJW20/car-drive-app/assets/99192767/24121e95-8154-4273-9fc2-1905ff58ac2e)

### Creator_2
When running method `creator_2`, you will be able to drag around the points and the track will always traverse through them. Between the points a curve will be constructed using [Catmull-Rom interpolation](https://en.wikipedia.org/wiki/Centripetal_Catmull%E2%80%93Rom_spline). More points can be added with `SPACE`, and once happy with the design press the `ENTER` key and then click on the Track where you want the start/finish line to be.

Below are a few examples made using this method:

![c2t1](https://github.com/RJW20/car-drive-app/assets/99192767/e0affaa2-30a1-4642-bc2e-f902f3e678ab)
![c2t2](https://github.com/RJW20/car-drive-app/assets/99192767/e8b982d9-9b76-4e6a-beaa-83f30ecee043)
![c2t3](https://github.com/RJW20/car-drive-app/assets/99192767/4f33c73a-12fa-4c2d-a45a-ad032544996a)

### Generator
The generator works very similarly to what is described [here](https://www.gamedeveloper.com/programming/generating-procedural-racetracks). The outline is:
- Generate random points.
- Find the convex hull of the points.
- For consecutive points that are far enough apart add another point between that is randomly displaced from the midpoint.
- Repeatedly move points to prevent turns being too tight (<90&deg;) and points being too close.
- Generate the Catmull-Rom interpolation between the points to make up the rest of the Track.

Below are a few examples generated using this method:

![gt1](https://github.com/RJW20/car-drive-app/assets/99192767/2d4633ac-1cda-4cfb-9e3a-435c85a6bdff)
![gt2](https://github.com/RJW20/car-drive-app/assets/99192767/d3479227-2818-4e6b-a7ab-0cbe5280d7a4)
![gt3](https://github.com/RJW20/car-drive-app/assets/99192767/107d86ca-f44f-40a2-8de5-116ce205d7ff)

## Note
I created this so that I could then get AI to learn to drive around the Tracks. See [here](https://github.com/RJW20/car-drive-ai-NEAT).
