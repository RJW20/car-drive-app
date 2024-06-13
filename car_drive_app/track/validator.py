from car_drive_app.track.base_track import BaseTrack
from car_drive_app.track.exceptions import TrackOutOfBoundsError


def contained_in_plane(track: BaseTrack) -> bool:
    """Return True if all points in track.center_line are more than track.radius away from the 
    edges of the plane with track.dimensions."""

    for point in track.center_line:

        if point.x + track.radius > track.dimensions.x or point.x - track.radius < 0:
            return False
        
        if point.y + track.radius > track.dimensions.y or point.y - track.radius < 0:
            return False

    return True


def validate(track: BaseException) -> None:
    """Validate the given Track
    
    Raises a TrackOutOfBoundsError if the Track is not contained on the plane.
    ."""

    if not contained_in_plane(track):
        raise TrackOutOfBoundsError('The created Track is not contained in the plane, aborting...')