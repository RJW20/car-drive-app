from car_drive_app.cartesians import Vector


def interpolation_point(t: float, points: list[Vector], time_intervals: list[float]) -> Vector:
    """Return the point with parameter value t between points[1] and points[2]."""

    A = [((time_intervals[i+1]-t) * points[i] + (t-time_intervals[i]) * points[i+1]) / (time_intervals[i+1] - time_intervals[i]) for i in range(3)]
    B = [((time_intervals[i+2]-t) * A[i] + (t-time_intervals[i]) * A[i+1]) / (time_intervals[i+2] - time_intervals[i]) for i in range(2)]
    C = ((time_intervals[2]-t) * B[0] + (t-time_intervals[1]) * B[1]) / (time_intervals[2] - time_intervals[1])
    return C


def interpolate(points: list[Vector], points_per_segment: int) -> list[Vector]:
    """Return the points that make up the Catmull-Rom interpolation between points[1] and points[2].
    
    points[0] and points[3] are the control points.
    points_per_segment is the integer number of equally spaced points to place along each curve.
    points[1] is included in the interpolation but points[2] is not.
    """

    # Prepare the t_i values
    time_intervals = [0]
    for i in range(3):
        dx = points[i+1].x - points[i].x
        dy = points[i+1].y - points[i].y
        time_intervals.append(time_intervals[i] + (dx**2 + dy**2) ** 0.5)   # Chordal: alpha = 1 (=2*0.5)
    t_start = time_intervals[1]
    t_end = time_intervals[2]
    dt = (t_end - t_start)/points_per_segment

    # Create the points
    interpolation = [points[1]]
    for i in range(1, points_per_segment):
        t = t_start + i * dt
        interpolation.append(interpolation_point(t, points, time_intervals))
    
    return interpolation
    

def catmull_rom(points: list[Vector], points_per_segment: int) -> list[Vector]:
    """Return the list of Vectors that make up the Catmull-Rom interpolation curve of the 
    given points.
    
    points should form a closed loop, with the last and first points being the same.
    points_per_segment is the integer number of equally spaced points to place along each curve.
    The actual distance between each point will depend on the spacing between the control points.
    """

    curve = []
    
    # First segment has second last point as P0
    curve.extend(interpolate([points[-2], points[0], points[1], points[2]], points_per_segment))

    N = len(points)
    for i in range(0, N - 3):
        curve.extend(interpolate(points[i:i+4], points_per_segment))

    # Last segment has second point as P3
    curve.extend(interpolate([points[N-3], points[N-2], points[N-1], points[1]], points_per_segment))

    return curve